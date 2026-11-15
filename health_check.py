import urllib.request
from datetime import datetime

websites = ["https://google.com", "https://github.com"]

for site in websites:
    try:
        response = urllib.request.urlopen(site, timeout=5)
        status = f"UP (Code {response.status})"
    except Exception as e:
        status = f"DOWN ({e})"

    log_line = f"{datetime.now()} - {site} is {status}\n"
    print(log_line.strip())

    with open("uptime.log", "a") as f:
        f.write(log_line)
