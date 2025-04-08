from flask import Flask
import os
from datetime import datetime
import subprocess
import pytz
import getpass


app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "kanuri sathvika"  # Replace with your real name
    # username = os.getlogin()
    username = getpass.getuser()

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    top_output = subprocess.getoutput("top -bn1")

    return f"""
    <h1>/htop</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
