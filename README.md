# ⚙️ Automação de VLANs Cisco em Python

## 💡 Visão Geral

Automação para criação e nomeação de VLANs em dispositivos **Cisco**, utilizando **Python (asyncio + telnetlib3)**.
Projetado para operação em **EVE-NG**, **GNS3** ou infraestrutura real, com autenticação dinâmica e execução assíncrona de comandos.

## 🎯 Objetivo

Reduzir tarefas manuais e padronizar configurações de VLANs, garantindo consistência, rapidez e rastreabilidade nas implementações de rede.

## 🧩 Arquitetura Técnica

* **Linguagem:** Python 3.8+
* **Bibliotecas:** telnetlib3, asyncio, getpass
* **Protocolo:** Telnet (porta 23)
* **Fluxo:** conexão → autenticação → envio de comandos → leitura de resposta → encerramento seguro

## ⚙️ Requisitos

* Python 3.8 ou superior
* Instalar dependências:

  ```bash
  pip install telnetlib3
  ```
* Dispositivo Cisco com Telnet ativo

## ▶️ Execução

```bash
git clone https://github.com/murilocardoso7/automacao-vlan-cisco.git
cd automacao-vlan-cisco
python main.py
```

Informe credenciais quando solicitado.
O sistema executará os comandos e exibirá os resultados em tempo real.

## 🔍 Considerações Técnicas

Script projetado com foco em **automação assíncrona**, **simplicidade de integração** e **extensibilidade**.
Pode ser ampliado para suportar **SSH (Netmiko)**, **autenticação por chave**, ou integração com ferramentas como **Ansible** e **Nornir**.

## 📈 Próximos Passos

* Suporte a SSH e protocolos modernos.
* Log automatizado de sessões.
* Interface web para gerenciamento remoto.
* Integração com pipelines CI/CD de rede.

---

### 🧾 Licença

Distribuído sob a licença **MIT**. Consulte o arqu
