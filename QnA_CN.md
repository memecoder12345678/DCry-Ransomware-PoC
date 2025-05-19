# QnA

## ❓ 什么是 *Don't Cry Ransomware*？

它是用 Python + Cython 写的勒索软件 PoC，用于学习和恶意软件分析。它使用 AES-256-GCM 加密文件，禁用恢复工具，关闭杀毒软件，发送密钥到 C2 服务器，并显示勒索信息。

---

## 💾 为啥文件这么大？

因为是 Python 写的 😩。像 PyInstaller 会把代码、Python 解释器、还有所有依赖库（比如 `cryptography`, `requests` 等）全部打包成一个 `.exe`，就像背了整个生态系统 🐢。

真正的恶意软件用 C/C++/Go/Rust，还会压缩，轻巧又快。这个嘛，只是个胖胖的 PoC 😅。

