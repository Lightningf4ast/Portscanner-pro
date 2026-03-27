# 🚀 Pro Port Scanner

<p align="center">
  <b>High-performance, modular port scanner built with Python</b><br>
  Async scanning • GUI + CLI • Service detection • Export system
</p>

---

## 📌 Overview

**Pro Port Scanner** is a fast and modular network scanning tool designed to identify open ports and associated services on a target system.

This project demonstrates real-world engineering concepts including:

* Asynchronous programming (`asyncio`)
* Concurrent execution
* Network socket handling
* Clean modular architecture

---

## ✨ Key Features

* ⚡ **Async Port Scanning** — high-speed concurrent scanning using `asyncio`
* 🖥️ **GUI Interface** — simple and clean interface using Tkinter
* 💻 **CLI Mode** — fast terminal-based scanning
* 🧠 **Service Detection** — maps ports to known services
* 📊 **Progress Tracking** — real-time scan updates
* 💾 **Export Results** — save scans as TXT and JSON
* 🧱 **Modular Codebase** — clean separation of logic (core, GUI, utils)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Lightningf4ast/Portscanner-pro.git
cd port-scanner-pro
```

### 2️⃣ Install Dependencies

```bash
sudo apt install python3 python3-tk
```

---

## ▶️ Usage

### 🖥️ Run GUI

```bash
python3 main.py
```

### 💻 Run CLI

```bash
python3 cli.py
```

---

## 🧪 Example Test (Recommended)

### Step 1: Start a Local Server

```bash
python3 -m http.server 8000
```

### Step 2: Scan Locally

```
Target IP: 127.0.0.1
Port Range: 7900–8100
```

### Expected Output

```
[OPEN] 8000 (HTTP)
```

---

## ⚙️ How It Works

* Uses TCP socket connections to probe ports
* Async tasks allow thousands of concurrent checks
* Open ports are mapped to known services
* Results are streamed to GUI/CLI in real time
* Data can be exported for later analysis

---

## 📊 Skills Demonstrated

* Network Programming (Sockets)
* Asynchronous Programming (`asyncio`)
* Multithreading Concepts
* GUI Development (Tkinter)
* Modular Software Design
* File Handling (JSON/TXT)

---

## ⚠️ Disclaimer

This tool is strictly for **educational and authorized testing purposes only**.

Unauthorized scanning of networks or systems may be illegal.

---

## 🔥 Future Enhancements

* SYN Scan (raw packets)
* UDP Scanning
* Advanced service fingerprinting
* Web dashboard interface
* Vulnerability detection layer

---

## 🏆 Why This Project Stands Out

Unlike basic scanners, this project includes:

* Async architecture (performance-focused)
* Dual interface (GUI + CLI)
* Clean modular structure
* Export + usability features

👉 Built not just to work — but to demonstrate **engineering thinking**

---


## ⭐ Contributing

Contributions, ideas, and improvements are welcome.
Feel free to fork the repo and submit a pull request.

---

## 📌 Final Note

This project is a stepping stone toward understanding how professional tools like Nmap work internally — not a replacement for them.
