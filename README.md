# Don't-Cry Ransomware PoC

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Requires-Cython-yellow?logo=python&logoColor=white" alt="Cython">
  <img src="https://img.shields.io/badge/Rust-1.87.0%2B-orange?logo=rust&logoColor=white" alt="Rust >= 1.87.0">
  <img src="https://img.shields.io/github/license/memecoder12345678/DCry-Ransomware?style=flat&logo=open-source-initiative&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows-blue?logo=windows&logoColor=white" alt="Platform">
</div>

![DCry](imgs/dcry.png)
PoC ransomware in Python targeting Windows systems 💀💀💀

---

## Setup & Installation

### Server

1. Install the required packages:

```powershell
pip install -r requirements-server.txt
```

2. Run the server:

```powershell
gunicorn -b 0.0.0.0:8080 src.server:app
```

> Or for debugging:

```powershell
python src/server.py
```

### Client

1. Install the required packages:

```powershell
pip install -r requirements-other.txt
```

---

## Usage

1. Open [`src/dcry.py`](src/dcry.py)

   * Replace `YOUR_URL` with your encoded URL using `dx42`:

   ```python
   YOUR_URL = dx42(encoded_url).decode()
   ```

   * Replace `YOUR_PROXY`, `YOUR_BITCOIN_ADDRESS`, `YOUR_EMAIL_ADDRESS` similarly.

2. Open [`src/decryptor.py`](src/decryptor.py)

   * Set `dev_mode = False` if not using development mode.

3. Build the Cython code:

```powershell
python src/setup.py build_ext --inplace
Move-Item -Path file_crypto.*.pyd -Destination src -Force
```

4. Run the server (WSGI):

```powershell
gunicorn -b 0.0.0.0:8080 src.server:app
```

5. Run the ransomware:

```powershell
python src/dcry.py
```

6. Run the decryptor:

```powershell
python src/decryptor.py
```

---

## Warning

> [!WARNING]
> This project is a ransomware simulation for educational purposes only.

---

## FAQ

* See details in [FAQ.md](docs/FAQ.md)

## Contributing

* See contribution guidelines in [CONTRIBUTING.md](docs/CONTRIBUTING.md)

## Code of Conduct

* See our community standards in [CODE\_OF\_CONDUCT.md](docs/CODE_OF_CONDUCT.md)

## Security

* See the security policy in [SECURITY.md](docs/SECURITY.md)

## License

* This project is licensed under the terms of the [Apache License 2.0](./LICENSE)

