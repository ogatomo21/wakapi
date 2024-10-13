from datetime import datetime as dt
from wakapi import manual as w

def total(secret, sec=False):
    url = "https://wakatime.com/api/v1/users/current/all_time_since_today"
    if(sec):
        json = w.reqJSON(secret, url)
        return w.sec(json["data"]["total_seconds"])
    else:
        return w.reqJSON(secret, url)

def date(secret, date, sec=False):
    url = f"https://wakatime.com/api/v1/users/current/durations?date={date}"
    if(sec):
        json = w.reqJSON(secret, url)
        return w.sec(sum(entry['duration'] for entry in json['data']))
    else:
        return w.reqJSON(secret, url)