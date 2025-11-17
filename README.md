# Sistema Inteligente de Irrigação com ESP32 e Dashboard IoT

Este projeto implementa um sistema integrado de irrigação automática utilizando um microcontrolador ESP32, um sensor de umidade simulado, uma bomba d’água controlada por relé e comunicação via Wi-Fi com um dashboard MQTT no Shiftr.io. O objetivo é monitorar o estado do solo e controlar a irrigação de forma automática, apresentando as informações em tempo real ao usuário.

## **Integrantes**

Gabriel Caldeira, Gustavo Marchiori e João Weslen.

## **Visão Geral do Sistema**

O sistema funciona como um controlador automático de irrigação. Ele monitora:

- Umidade do solo (simulada com sensor DHT22 no Wokwi)

- Nível de água do reservatório (variável interna no firmware)

- Estado da bomba (ativa/desativada)

A lógica principal consiste em:

- Verificar a umidade do solo em ciclos contínuos

- Acionar a bomba caso a umidade esteja abaixo do limite configurado

- Reduzir o nível de água do reservatório a cada ciclo de irrigação

- Bloquear a irrigação quando o nível do reservatório estiver baixo

- Reabastecer o reservatório através de um botão físico

- Enviar todos os dados para visualização em dashboard MQTT no Shiftr.io

## **Objetivos do Projeto**

- Simular um sistema IoT funcional utilizando ESP32 no Wowki.

- Monitorar parâmetros ambientais em tempo real.

- Automatizar a irrigação com regras de controle.

- Implementar comunicação MQTT com dashboard externo.


## **Funcionamento Detalhado**

1. Leitura de Umidade

- O ESP32 realiza leituras periódicas do sensor DHT22 conectado ao pino GPIO4.

- A umidade lida é interpretada como “umidade do solo” para fins de simulação.

2. Lógica de Controle da Bomba

- Se a umidade estiver abaixo do valor configurado (solo seco), o ESP32 ativa o relé que controla a bomba d’água.

- Cada acionamento reduz o nível do reservatório internamente.

- Se o nível de água atingir o mínimo definido, o sistema bloqueia a bomba e ativa um LED indicador.

3. Reabastecimento do Reservatório

- O circuito possui um botão físico conectado ao pino GPIO23.

- Quando pressionado, o nível de água é restaurado para 100%, permitindo novos ciclos de irrigação.

4. Dashboard IoT

O ESP32 publica dados no broker MQTT do Shiftr.io, permitindo acompanhar:

- Umidade atual do solo

- Temperatura (do DHT22)

- Estado da bomba

- Nível de água

A visualização pode ser feita pelo painel do Shiftr.io ou qualquer cliente MQTT.

5. Simulação Completa no Wokwi

O circuito foi montado integralmente no simulador Wokwi, incluindo:

- ESP32 DevKit

- Sensor DHT22

- Módulo Relé

- LEDs indicadores

- Botão de reabastecimento

- Protoboard e conexões internas

O projeto pode ser acessado pelo link presente no repositório.

## **Tecnologias Utilizadas**

- ESP32 DevKit V1

- MicroPython

- Protocolo MQTT

- Broker Shiftr.io

- Simulador Wokwi

- Módulo Relé

- DHT22 (simulação de umidade do solo)

## **Como Executar**

1. Abrir o projeto diretamente no Wokwi.

2. Executar o script principal main.py no microcontrolador.

3. Acessar o broker Shiftr.io.

4. Visualizar as leituras em tempo real.

5. Interagir via botão físico simulando o reabastecimento da caixa d’água.

## **Estrutura do Repositório**

- /diagram.json — circuito completo para simulação no Wokwi

- /main.py — firmware MicroPython responsável por toda a lógica

- README.md — documentação do projeto

- wowki-project.txt — Link do projeto do Wowki


## **Possíveis Extensões**

- Envio de alertas para Telegram ou e-mail

- Utilização de sensor de umidade do solo real fora da simulação

- Adição de display OLED para exibir valores localmente