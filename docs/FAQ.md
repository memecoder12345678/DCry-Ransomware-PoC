# FAQ
## What is *Don't Cry Ransomware*?

It's a PoC ransomware written in Python + Cython, made for education and malware analysis. It encrypts files using AES-256-GCM, disables recovery tools, kills antivirus, sends the key to a C2 server, and shows a ransom note.

---

## WTF why is the file so big?

Because it's Python 😩. Tools like PyInstaller pack your code, Python itself, and all libraries (like `cryptography`, `requests`, etc.) into one huge `.exe`. It's not your code's fault&mdash;it's carrying a whole ecosystem.

Real malware? They use C/C++/Go/Rust and compression to stay lean. This is just a chonky PoC 😅.

---

### Can it really encrypt and decrypt files?

Yes. AES-256-GCM is used for secure encryption, and the AES key is protected with RSA-OAEP. If you have the RSA private key (from the C2 server), you can decrypt all affected files using the Decryptor script.

---

### Why are the URLs, emails, proxies encoded?

To avoid exposing important info (like the C2 server) in the source code. You use `ex42()` to encode, and `dx42()` to decode them during runtime.

---

### Will antivirus detect it?

Likely yes, especially if you're just running the script directly. To avoid detection, use Cython compilation, obfuscate strings, and maybe even pack it with tools like UPX or Themida.

---

### What's the goal of this project?

For educational purposes. To help researchers, students, reverse engineers understand how real ransomware works, and also to prove that Python is not useless, we are.
**It's 100% PoC. Don't use it for evil 😇.**

