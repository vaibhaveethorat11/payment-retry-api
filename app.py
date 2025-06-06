from flask import Flask, request, jsonify, render_template, redirect, url_for
from threading import Thread
import time
import uuid
import random

app = Flask(__name__)

payments = {}
retry_interval = 5  # seconds

def simulate_payment_result():
    return random.choice(["SUCCESS", "FAILED"])

def retry_failed_payments():
    while True:
        time.sleep(retry_interval)
        for payment_id, data in list(payments.items()):
            if data['status'] == "FAILED" and data['retries'] < 3:
                new_status = simulate_payment_result()
                data['status'] = new_status
                data['retries'] += 1
                data['logs'].append({"attempt": data['retries'], "status": new_status, "time": time.ctime()})

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user = request.form.get("user")
        if user:
            payment_id = str(uuid.uuid4())
            status = simulate_payment_result()
            payments[payment_id] = {
                "user": user,
                "status": status,
                "retries": 0,
                "logs": [{"attempt": 0, "status": status, "time": time.ctime()}]
            }
            result = {"payment_id": payment_id, "status": status}
    return render_template("index.html", result=result)

@app.route("/status", methods=["GET"])
def check_status():
    payment_id = request.args.get("payment_id")
    data = payments.get(payment_id)
    return render_template("index.html", status_data=data, pid=payment_id)

if __name__ == '__main__':
    Thread(target=retry_failed_payments, daemon=True).start()
    app.run(debug=True)
