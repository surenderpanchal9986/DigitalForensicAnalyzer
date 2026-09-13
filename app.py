from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

# JimmyWilson Investigation data
case_data = {
    "web_history": 136,
    "web_search": 17,
    "emails": 27,
    "usb_devices": 9,
    "deleted_files": 2208,
    "exif_metadata": 14,
    "installed_programs": 260,
    "recent_documents": 17,
    "web_cookies": 124,
    "shell_bags": 45
}


def calculate_hash(file):
    sha256 = hashlib.sha256()

    while True:
        data = file.read(4096)

        if not data:
            break

        sha256.update(data)

    return sha256.hexdigest()


@app.route("/", methods=["GET", "POST"])
def home():

    hash_result = None
    filename = None

    if request.method == "POST":

        uploaded_file = request.files.get("evidence")

        if uploaded_file and uploaded_file.filename:

            filename = uploaded_file.filename
            hash_result = calculate_hash(uploaded_file)

    return render_template(
        "index.html",
        data=case_data,
        hash_result=hash_result,
        filename=filename
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)