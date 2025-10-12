[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/murilocardoso7/automacao-vlan-cisco/blob/main/LICENSE)
[![Languages](https://img.shields.io/badge/Languages-EN%20%7C%20PT--BR-blue.svg)](README_pt.md)

# Cisco VLAN Automation in Python

> 🇧🇷 Leia este README em português [aqui](README_pt.md)

## Overview

This project demonstrates VLAN provisioning automation on **Cisco IOS** devices using **Python**, leveraging asynchronous support via `asyncio` and Telnet communication through the `telnetlib3` library.  
It is designed for **EVE-NG environments**, ideal for **network automation labs, testing scenarios, and educational setups**, serving as a foundation for future enterprise automation applications.

---

## Objective

To automate the configuration and naming of multiple VLANs on Cisco devices, minimizing manual work and ensuring standardized network operations.  
The application performs dynamic authentication, sequentially sends IOS commands, and displays the complete configuration output in the terminal.

---

### Execution Flow

1. Establish Telnet session  
2. Automatic authentication (username and password)  
3. Execution of predefined IOS commands  
4. Asynchronous reading and output display  
5. Controlled connection termination  

---

### Technical Pillars

- Asynchronous programming (`async/await`)  
- Cisco IOS device automation  
- Low-level Telnet communication via `telnetlib3`  
- Session control and synchronization with `asyncio`  

---

## Requirements

- **Python:** 3.8 or higher  
- **Dependencies:**
  ```bash
  pip install telnetlib3
  ```
- **Environment:**
  - Cisco device (physical or virtual)  
  - Telnet port (23) enabled  

---

## Execution

```bash
git clone https://github.com/murilocardoso7/automacao-vlan-cisco.git
cd automacao-vlan-cisco
python script_telnet_config_vlan.py
```

During execution, the script requests credentials, connects to the device, and automatically applies VLANs 2 through 7, naming them according to the predefined standard in the code.

---

## Demonstration

Execution result from a Cisco EVE-NG lab, representing real device automation:

<img width="575" height="394" alt="Image" src="https://github.com/user-attachments/assets/a3386567-4990-4dd2-bafd-b1a933d82210" />

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Murilo Cardoso**  
[GitHub](https://github.com/murilocardoso7)
