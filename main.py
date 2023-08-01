import subprocess
import re
from flask import Flask 
import time
google = "google.com"
google_ip = "8.8.8.8"
kyle = "home.reneau.me"
kyle_ip = "209.236.90.132"
regexp="(?<=time=)[0-9.]+"

def ping_host(hostname):
    ping = subprocess.Popen(
    ["ping", "-c", "1", "-w", "5", hostname],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE)
    out, error = ping.communicate()
    return str(out)

def check_response(response):
    if str(type(response)) == "<class \'NoneType\'>":
        print("fail")
    else:
        return response[0]

google_response=re.search(regexp, ping_host(google))
google_ip_response=re.search(regexp, ping_host(google_ip))
kyle_response=re.search(regexp, ping_host(kyle))
kyle_ip_response=re.search(regexp, ping_host(kyle_ip))

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    google_response=re.search(regexp, ping_host(google))
    google_ip_response=re.search(regexp, ping_host(google_ip))
    kyle_response=re.search(regexp, ping_host(kyle))
    kyle_ip_response=re.search(regexp, ping_host(kyle_ip))
    return f"""
<meta http-equiv="refresh" content="1" /> 
Google:       {check_response(google_response)} <br>
Google\'s IP: {check_response(google_ip_response)} <br>
Kyle\'s:      {check_response(kyle_response)} <br>
Kyle\'s IP:   {check_response(kyle_ip_response)}"""

if __name__ == "__main__":
        app.run(port=80)
