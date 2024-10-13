import base64
import math
import requests

def token(secret):
    token_encoded = base64.b64encode(secret.encode()).decode('ascii')
    return f"Basic {token_encoded}"

def reqJSON(secret, url):
    res = requests.get(url, headers={"Authorization": token(secret)})
    return res.json()

def sec(sec):
    sec = math.floor(sec)
    days, remainder = divmod(sec, 86400)  # 1日 = 86400秒
    hours, remainder = divmod(remainder, 3600)  # 1時間 = 3600秒
    minutes, seconds = divmod(remainder, 60)  # 1分 = 60秒
    return {
        "days": days,
        "hours": hours,
        "min": minutes,
        "sec": seconds
    }