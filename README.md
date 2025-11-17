# 💧 Sistema Inteligente de Irrigação com ESP32 e Dashboard IoT

## Visão Geral do Projeto

Este projeto implementa um **sistema integrado de irrigação automática** utilizando o microcontrolador **ESP32**, focado na simulação de um ambiente IoT completo. O sistema monitora o estado do solo (simulado), controla uma bomba d'água via relé e utiliza o protocolo **MQTT** para comunicação em tempo real com um dashboard no **Shiftr.io**.

O principal objetivo é demonstrar a automação de processos agrícolas ou de jardinagem, oferecendo ao usuário uma visualização em tempo real dos parâmetros críticos do sistema.

**Integrantes:** Gabriel Caldeira, Gustavo Marchiori e João Weslen.

## Funcionalidades Principais

O sistema atua como um controlador automático de irrigação, realizando as seguintes funções:

1.  **Monitoramento Simulado:** Acompanhamento contínuo da umidade do solo (simulada via sensor DHT22 no Wokwi) e do nível de água do reservatório (variável interna).
2.  **Controle Automático:** Acionamento da bomba d'água (controlada por relé) quando a umidade do solo cai abaixo de um limite configurado.
3.  **Gestão de Recursos:** Bloqueio da irrigação quando o nível de água do reservatório atinge o mínimo, com ativação de um LED indicador.
4.  **Interação Física:** Possibilidade de reabastecer o reservatório (simulado) através de um botão físico.
5.  **Visualização IoT:** Envio de todos os dados de monitoramento (umidade, temperatura, estado da bomba, nível de água) para um dashboard MQTT em tempo real no Shiftr.io.

## Tecnologias Utilizadas

| Componente | Tecnologia/Plataforma | Função |
| :--- | :--- | :--- |
| **Microcontrolador** | ESP32 DevKit V1 | Processamento da lógica de controle e conectividade Wi-Fi. |
| **Firmware** | MicroPython | Linguagem de programação embarcada. |
| **Comunicação** | Protocolo MQTT | Envio de dados em tempo real para o dashboard. |
| **Broker IoT** | Shiftr.io | Servidor MQTT para hospedagem do dashboard. |
| **Simulação** | Wokwi | Ambiente de simulação online para o circuito e firmware. |
| **Sensores/Atuadores** | DHT22 (simulado), Módulo Relé | Simulação de leitura de umidade/temperatura e controle da bomba. |

## Funcionamento Detalhado

### 1. Leitura de Umidade

O ESP32 realiza leituras periódicas do sensor DHT22 (conectado ao pino `GPIO4`). Para fins de simulação no Wokwi, a umidade lida é interpretada como a **umidade do solo**.

### 2. Lógica de Controle da Bomba

A lógica de controle é baseada em um limiar de umidade:
*   Se a umidade estiver **abaixo** do valor configurado (solo seco), o relé é ativado, ligando a bomba d'água.
*   Cada ciclo de irrigação bem-sucedido reduz o nível de água do reservatório internamente.
*   Se o nível de água atingir o mínimo definido, o sistema **bloqueia** o acionamento da bomba e ativa um LED indicador de reservatório vazio.

### 3. Reabastecimento do Reservatório

Um botão físico (conectado ao pino `GPIO23`) simula o reabastecimento do reservatório. Ao ser pressionado, o nível de água interno é restaurado para **100%**, permitindo que novos ciclos de irrigação sejam iniciados.

### 4. Dashboard IoT (Shiftr.io)

O microcontrolador publica continuamente os seguintes dados no broker MQTT do Shiftr.io:
*   `Umidade atual do solo`
*   `Temperatura` (lida pelo DHT22)
*   `Estado da bomba` (Ativa/Desativada)
*   `Nível de água`

A visualização e o acompanhamento em tempo real podem ser feitos diretamente pelo painel do Shiftr.io ou por qualquer cliente MQTT configurado.

## Simulação Completa no Wokwi

O projeto foi integralmente montado e testado no simulador Wokwi, garantindo a reprodutibilidade do circuito e do firmware.

**Componentes Simulados:**
*   ESP32 DevKit
*   Sensor DHT22
*   Módulo Relé
*   LEDs indicadores
*   Botão de reabastecimento
*   Protoboard e conexões

O link direto para a simulação está disponível no arquivo `wowki-project.txt` no repositório.

## Estrutura do Repositório

| Arquivo/Diretório | Descrição |
| :--- | :--- |
| `diagram.json` | Arquivo de configuração do circuito completo para simulação no Wokwi. |
| `main.py` | Firmware principal em MicroPython, contendo toda a lógica de controle e comunicação MQTT. |
| `README.md` | Documentação detalhada do projeto (este arquivo). |
| `wowki-project.txt` | Link direto para o projeto no simulador Wokwi. |

## Como Executar

Para testar e visualizar o projeto, siga os passos abaixo:

1.  **Acessar o Wokwi:** Abra o link do projeto contido no arquivo `wowki-project.txt`.
2.  **Executar o Firmware:** Inicie a simulação no Wokwi para executar o script `main.py` no ESP32.
3.  **Monitorar o Dashboard:** Acesse o broker Shiftr.io para visualizar as leituras em tempo real.
4.  **Interagir:** Utilize o botão físico simulado para reabastecer a caixa d’água e observe a lógica de controle da bomba.

## Possíveis Extensões

O projeto pode ser expandido com as seguintes melhorias:

*   **Notificações:** Implementação de envio de alertas para plataformas como Telegram ou e-mail em caso de reservatório vazio ou falha na irrigação.
*   **Hardware Real:** Substituição do sensor DHT22 simulado por um sensor de umidade do solo real (capacitivo ou resistivo) para aplicação em hardware físico.
*   **Interface Local:** Adição de um display OLED ou LCD para exibir os valores de umidade e nível de água localmente, sem depender do dashboard.
*   **Configuração Remota:** Adicionar a capacidade de configurar o limiar de umidade remotamente via MQTT.
