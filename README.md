# Cisco VLAN Automation

## Visão Geral

Script em **Python** para automatizar a **criação e nomeação de VLANs** em dispositivos **Cisco IOS**.  
A comunicação é feita via **Telnet**, utilizando a biblioteca `telnetlib3` e o modelo assíncrono de execução do Python (`asyncio`).  

O código foi desenvolvido para **laboratórios virtuais ou físicos**, com o objetivo de demonstrar **conceitos práticos de automação de redes**.

---

## Objetivo

Reduzir o tempo de configuração manual e garantir consistência na aplicação de comandos IOS, de forma simples e reproduzível em qualquer ambiente de emulação ou laboratório de rede.

---

## Tecnologias Utilizadas

- **Python 3.8+**
- **telnetlib3**
- **asyncio**
- **Cisco IOS (modo Telnet habilitado)**

---

## Execução

```bash
git clone https://github.com/murilocardoso7/cisco-vlan-automation.git
cd cisco-vlan-automation
pip install telnetlib3
python script_telnet_config_vlan.py
Durante a execução, o script solicitará credenciais, conectará ao dispositivo e aplicará as VLANs configuradas no código.
```
---
Saída show vlan brief após execução do script.

![Show Vlan Brief Screenshot](https://github-production-user-asset-6210df.s3.amazonaws.com/216113104/498866691-a3386567-4990-4dd2-bafd-b1a933d82210.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251020%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251020T001041Z&X-Amz-Expires=300&X-Amz-Signature=ae502f305737d4ec3544f86995b70f261235500351aa451576661c1e3181e8de&X-Amz-SignedHeaders=host)

