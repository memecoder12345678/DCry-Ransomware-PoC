# QnA
## ❓ What is *Don't Cry Ransomware*?

It’s a PoC ransomware written in Python + Cython, made for education and malware analysis. It encrypts files using AES-256-GCM, disables recovery tools, kills antivirus, sends the key to a C2 server, and shows a ransom note.

---

## 💾 WTF why is the file so big?

Because it’s Python 😩. Tools like PyInstaller pack your code, Python itself, and all libraries (like `cryptography`, `requests`, etc.) into one huge `.exe`. It’s not your code’s fault—it’s carrying a whole ecosystem 🐢.

Real malware? They use C/C++/Go/Rust and compression to stay lean. This is just a chonky PoC 😅.

