
# Python Port Scanner
A fast, multi-threaded Python port scanner to identify open ports on a target system — built for ethical hacking, recon, and pentesting labs.

---

## 🧠 Why I Built This

After creating an SSH brute-forcer to test weak credentials, I realised the first thing an attacker or red teamer would do is **recon** — to find *what* services are exposed.

So I built this **port scanner** to:
- Quickly identify open ports (e.g. SSH, HTTP, FTP)
- Prepare targets for ethical brute-force or service-specific testing
- Learn how real tools like Nmap work under the hood

---

## 🚀 Features

- ✅ **Multi-threaded scanning** (fast ⚡)
- 🛠️ Customisable port ranges
- 🧪 Clean terminal output
- ⏱️ Scan timing metrics
- 🧑‍💻 Works cross-platform (Linux, Mac, Windows)

---

## 🖥️ Usage

```bash
git clone https://github.com/Cybernuel/port-scanner.git
cd port-scanner
python scanner.py
````

Then enter the IP you want to scan (e.g. `127.0.0.1`, or `scanme.nmap.org`).

---

## 🛠 Example Output

```bash
🔍 Scanning 127.0.0.1 from port 1 to 100...

✅ Scan complete in 0.82 seconds.
🔓 Open Ports: [22, 80]
```

---

## 🤖 How It Works

* Uses `socket` to attempt TCP connections to each port
* Uses `concurrent.futures.ThreadPoolExecutor` for multi-threading
* Reports open ports instantly as they’re discovered

---

## 🧠 Future Plans

* Add service mapping (e.g. 22 = SSH, 80 = HTTP)
* Export results to `.txt` or `.json`
* Integrate with my **SSH brute-forcer** for chained attacks

---

## 📎 Related Projects

* 🔐 [SSH Brute Forcer](https://github.com/Cybernuel/SSh-Brute-force): Test weak SSH logins ethically.
* 🧠 Honeypot (Coming Soon): Log and detect attacker behavior in real-time.

---

## 🧑‍💻 Author

**Cybernuel** — MSc Cybersecurity grad & aspiring Red Teamer
🔗 [LinkedIn](https://www.linkedin.com/in/thedamilare)

---

## 🛡️ Disclaimer

This tool is for **educational purposes** only. Use responsibly and **do not scan** systems you don’t own or have permission to test.


