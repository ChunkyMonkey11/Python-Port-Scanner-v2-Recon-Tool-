# 🔍 Network Port Scanner v2

**Network Port Scanner v2** is a high-performance, Python-based tool that scans IP addresses or entire subnets to detect open TCP ports and identify running services via banner grabbing. Designed for both educational and practical use, this project mimics core features of tools like Nmap and provides hands-on experience with network reconnaissance techniques.

---

## 🚀 Features

- ✅ **CIDR Support** – Input entire subnets (e.g. `192.168.1.0/24`)
- ✅ **Multi-threaded Scanning** – Fast, concurrent scans using `concurrent.futures`
- ✅ **Banner Grabbing** – Identify services via open port banners
- ✅ **Custom Port Targeting** – Specify individual ports (e.g. `22,80,443`)
- ✅ **Output to CSV/JSON** – Save scan results for later analysis
- ✅ **Clean Error Handling** – Timeouts, unreachable hosts, and exception handling

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/port-scanner-v2.git
cd port-scanner-v2
pip install -r requirements.txt
