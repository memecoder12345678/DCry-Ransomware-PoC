# QnA

## ❓ *Don't Cry Ransomware* là gì?

Là mã độc tống tiền PoC viết bằng Python + Cython, dùng cho mục đích học và phân tích. Nó mã hóa file bằng AES-256-GCM, vô hiệu hóa công cụ phục hồi, diệt antivirus, gửi key về C2 và hiện thông báo đòi tiền chuộc.

---

## 💾 Sao file nặng thế?

Vì dùng Python 😩. PyInstaller gói luôn cả mã, trình thông dịch Python, và thư viện (`cryptography`, `requests`, v.v.) vào 1 file `.exe`. Không phải code nặng, mà nó vác nguyên cái hệ sinh thái 🐢.

Malware xịn thì dùng C/C++/Go/Rust, có nén, nhẹ lắm. Đây chỉ là PoC mập ú 😅.


---

### 🛠️ Nó có thật sự mã hóa và giải mã được không?

Có. DCry dùng AES-256-GCM để mã hóa file an toàn, và RSA-OAEP để mã hóa khóa AES. Nếu có private key RSA từ server, bạn có thể giải mã bằng script `Decryptor.py`.

---

### 🧩 Sao phải mã hóa URL, email, proxy?

Để không bị lộ thông tin server (C2) hoặc các dữ liệu quan trọng trong mã nguồn. Dùng hàm `ex42()` để mã hóa chuỗi, rồi `dx42()` để giải mã khi chương trình chạy.

---

### 🦠 Có bị antivirus phát hiện không?

Có thể có, nhất là khi bạn chạy code trực tiếp. Muốn tránh bị phát hiện thì nên dùng Cython để biên dịch, mã hóa chuỗi, hoặc pack file bằng UPX, Themida,…

---

### 🧪 Mục đích của project này là gì?

Phục vụ học tập và nghiên cứu bảo mật. Dự án giúp người học, nhà nghiên cứu hoặc dân phân tích mã độc hiểu được cách ransomware thật hoạt động.

**Đây là PoC – đừng dùng vào việc xấu nha 😇**
