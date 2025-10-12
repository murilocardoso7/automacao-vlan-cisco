[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/murilocardoso7/automacao-vlan-cisco/blob/main/LICENSE)

# Cisco VLAN Automation in Python

> 🇧🇷 Leia este README em Português [aqui](README.md)

## Overview

This project demonstrates VLAN provisioning automation on **Cisco IOS** devices using **Python** with asynchronous support through `asyncio` and Telnet communication via the `telnetlib3` library.  
The solution is designed for **EVE-NG** environments — ideal for **labs, testing, and learning network automation** — serving as a foundation for future enterprise applications.

---

## Purpose

Automate the configuration and naming of multiple VLANs on Cisco devices, reducing manual setup time and standardizing network operations.  
The application performs dynamic authentication, sends sequential IOS commands, and displays the full configuration result in the terminal.

---

**Execution Flow:**

1. Establish Telnet session.  
2. Automatic authentication (username and password).  
3. Execute predefined IOS commands.  
4. Asynchronously read and display responses.  
5. Controlled connection termination.

**Technical pillars:**

* Asynchronous programming (async/await)  
* Cisco IOS device automation  
* Low-level communication with telnetlib3  
* Session control and synchronization via asyncio

---

## Requirements

* **Python:** 3.8 or higher  
* **Dependencies:**

  ```bash
  pip install telnetlib3
  ```
* **Environment:**

  * Cisco device (physical or virtual)  
  * Telnet port (23) enabled

---

## Usage

```bash
git clone https://github.com/murilocardoso7/automacao-vlan-cisco.git
cd automacao-vlan-cisco
python script_telnet_config_vlan.py
```

During execution, the script prompts for credentials, connects to the device, and automatically applies VLANs 2 through 7, naming them according to the pattern defined in the code.

---

## Demonstration

<p align="center">
  <img src="https://github.com/user-attachments/assets/a3386567-4990-4dd2-bafd-b1a933d82210" width="600">
</p>

**Figure 1 — Output of the `show vlan brief` command after running the Python automation script.**

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Murilo Cardoso**  
[GitHub](https://github.com/murilocardoso7)
