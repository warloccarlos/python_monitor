# Production_Sentinel.py 🛡️

A lightweight, zero-dependency Python utility designed for high-frequency synthetic monitoring and automated status-code validation of production endpoints.

## 📋 The Engineering Context
Commercial monitoring tools often introduce unnecessary overhead and licensing complexities. This utility was engineered to provide a portable, "drop-in" monitoring solution that can be deployed across restricted environments where third-party libraries (like `requests`) cannot be installed.

### Key Features
- **Zero External Dependencies:** Built entirely on Python 3.x Standard Libraries (`urllib`, `smtplib`, `logging`).
- **Decoupled Logic:** Monitored URLs and credentials are abstracted from the core execution logic.
- **Robust Error Handling:** Distinguishes between `HTTPError` (Server-side) and `URLError` (Network/DNS-side).
- **Automated Alerting:** Integrated SMTP support for real-time incident notification.

---

## 🏗️ Technical Architecture
The script operates as a synthetic user, performing periodic integrity checks against a defined set of endpoints.



## 🚀 Quick Start

### 1. Configuration
Update the `sites_to_monitor` list and SMTP credentials within the script:
```python
# Configure your endpoints
sites = ["[https://api.yourdomain.com](https://api.yourdomain.com)", "[https://app.yourdomain.com](https://app.yourdomain.com)"]
