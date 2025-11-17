import network
from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii, machine, dht
from time import sleep, ticks_diff, ticks_ms

# WiFi (Wokwi)
SSID = 'Wokwi-GUEST'
PASSWORD = ''

# MQTT (shiftr.io Cloud)
MQTT_SERVER = 'micropythonproject.cloud.shiftr.io'
MQTT_USER   = 'micropythonproject'
MQTT_PASS   = 'abcd1234efgh5678'
CLIENT_ID = 'esp32'

TOPIC_UMID  = 'esp32/umidade'
TOPIC_TEMP  = 'esp32/temperatura'


# --- CONFIGURAÇÕES DO SISTEMA ---
UMIDADE_BAIXA = 40         # abaixo disso, está "seco"
CONSUMO_POR_REGADA = 10    # quanto a água diminui cada vez que rega
NIVEL_MINIMO = 20          # abaixo disso, não pode regar
nivel_agua = 100           # nível inicial da caixa (0 a 100)
ultimo_clique = 0

# --- FUNÇÕES ---
def wifi_connect():
    conn = network.WLAN(network.STA_IF)
    conn.active(True)
    if not conn.isconnected():
        print('Conectando ao Wi-Fi...')
        conn.connect(SSID, PASSWORD)
        while not conn.isconnected():
            sleep(0.5)
    print('Wi-Fi OK, IP:', conn.ifconfig()[0])

def mqtt_connect():
    c = MQTTClient(CLIENT_ID, MQTT_SERVER, user=MQTT_USER, password=MQTT_PASS)
    c.connect()
    return c


def irq_botao(pin):
    global nivel_agua, ultimo_clique

    agora = ticks_ms()

    # Debounce → 250 ms entre cliques
    if ticks_diff(agora, ultimo_clique) < 250:
        return

    ultimo_clique = agora

    nivel_agua = 100
    print("💧 Caixa d'água reabastecida!")


wifi_connect()
client = mqtt_connect()

# Sensores e atuadores
sensor = dht.DHT22(Pin(4))
rele = Pin(21, Pin.OUT)      # Relé controla o LED vermelho (válvula)
led_nivel = Pin(22, Pin.OUT) # LED azul, nível da água
botao = Pin(23, Pin.IN, Pin.PULL_UP)
botao.irq(trigger=Pin.IRQ_FALLING, handler=irq_botao)

# --- LOOP PRINCIPAL ---
while True:
    sensor.measure()
    umid = sensor.humidity()
    temp = sensor.temperature()

    print("Umidade:", umid, "% | Temperatura:", temp, "°C")
    print("Nível da água:", nivel_agua, "%")

    # Publicar MQTT
    client.publish(TOPIC_UMID, str(umid))
    client.publish(TOPIC_TEMP, str(temp))

    # -------- LÓGICA DE REGAGEM --------
    if nivel_agua <= NIVEL_MINIMO:
        # pouca água → LED azul acende/fica piscando
        led_nivel.value(1)
        rele.value(0)  # impede regar
        print("⚠️ Nível de água baixo! Não é possível regar.")
    
    else:
        led_nivel.value(0)  # nível OK

        if umid < UMIDADE_BAIXA:
            # solo seco → regar
            print("🌱 Solo seco → Regando...")
            rele.value(1)   # liga válvula (LED vermelho acende)
            nivel_agua -= CONSUMO_POR_REGADA  # reduzir nível
            if nivel_agua < 0:
                nivel_agua = 0
            
        else:
            # solo úmido → não regar
            rele.value(0)

    sleep(2)
