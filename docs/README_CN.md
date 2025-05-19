# Don't-Cry 勒索软件
![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)
![Cython](https://img.shields.io/badge/Requires-Cython-yellow?logo=python&logoColor=white)
![License](https://img.shields.io/github/license/memecoder12345678/DCry-Ransomware?style=flat&logo=open-source-initiative&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-blue)
![Status](https://img.shields.io/badge/Status-Temporarily--Inactive-orange)
![DCry](./DCRY.png)
使用 Python 编写的勒索软件 💀💀💀
## 使用方法
* 打开 [`DCry.py`](src/DCry.py) 文件。
* 使用 `dx42` 函数替换 `YOUR_URL` 变量，方法如下：
  ```python
  YOUR_URL = dx42(b"YOUR_ENCODED_URL").decode()
  ```
  （先使用 `edx42` 模块中的 `ex42` 函数对你的 URL 进行编码。）
  
   示例：
    ```python
    encoded_url = ex42(b"https://your-tor-server.onion")
    YOUR_URL = dx42(encoded_url).decode()
  ```
* 同样用你的编码代理字符串替换 `YOUR_PROXY` 变量：
  ```python
  YOUR_PROXY = dx42(b"YOUR_ENCODED_PROXY").decode()
  ```
* 用你的比特币地址字符串替换 `YOUR_BITCOIN_ADDRESS`。
* 用你的邮箱地址字符串替换 `YOUR_EMAIL_ADDRESS`。
* 将 `dev_mode` 设置为 `False` 来关闭开发模式。
* 使用以下命令安装所需依赖：
  ```bash
  pip install -r requirements.txt
  ```
* 使用以下命令构建 Cython 代码：
  ```bash
  python src/setup.py build_ext --inplace
  ```
* 使用以下命令运行服务器：
  ```bash
  python src/server.py
  ```
* 使用以下命令运行勒索软件：
  ```bash
  python src/DCRY.py
  ```
* 使用以下命令运行解密程序：
  ```bash
  python src/decryptor.py
  ```
## 警告
> \[!WARNING]
> 此项目仅为教育目的的勒索软件模拟。
## 许可证
* 本项目依据 [Apache License 2.0](./LICENSE) 许可协议发布。
