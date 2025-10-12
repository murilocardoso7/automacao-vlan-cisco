[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/murilocardoso7/automacao-vlan-cisco/blob/main/LICENSE)

# Automação de VLANs Cisco em Python

## Visão Geral

Este projeto demonstra a automação do provisionamento de VLANs em dispositivos **Cisco IOS**, utilizando **Python** com suporte assíncrono via `asyncio` e comunicação Telnet por meio da biblioteca `telnetlib3`.
A solução foi estruturada para operação em ambientes **EVE-NG**, ideal para **laboratórios, ambientes de teste e aprendizado em automação de redes**, servindo como base para aplicações corporativas futuras.

---

## Objetivo

Automatizar a configuração e nomeação de múltiplas VLANs em dispositivos Cisco, reduzindo o tempo de configuração manual e padronizando as operações de rede.
A aplicação executa autenticação dinâmica, envia comandos IOS em sequência e exibe o resultado completo da configuração no terminal.

---

**Fluxo de execução:**

1. Estabelecimento da sessão Telnet.
2. Autenticação automática (usuário e senha).
3. Execução dos comandos IOS pré-definidos.
4. Leitura e exibição assíncrona da resposta.
5. Encerramento controlado da conexão.

**Pilares técnicos:**

* Programação assíncrona (async/await)
* Automação de dispositivos Cisco IOS
* Telnetlib3 para comunicação de baixo nível
* Controle de sessão e sincronização via asyncio

---

## Requisitos

* **Python:** 3.8 ou superior
* **Dependências:**

  ```bash
  pip install telnetlib3
  ```
* **Ambiente:**

  * Dispositivo Cisco (real ou virtual)
  * Porta Telnet (23) habilitada

---

## Execução

```bash
git clone https://github.com/murilocardoso7/automacao-vlan-cisco.git
cd automacao-vlan-cisco
python script_telnet_config_vlan.py
```

Durante a execução, o script solicita as credenciais, conecta-se ao equipamento e aplica automaticamente as VLANs 2 a 7, nomeando-as conforme padrão definido no código.

---

## Demonstração

<p align="center">
  <img src="https://github.com/user-attachments/assets/a3386567-4990-4dd2-bafd-b1a933d82210" width="600">
</p>

**Figura 1 — Saída do comando `show vlan brief` após execução do script Python.**

---

## Licença

Distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
