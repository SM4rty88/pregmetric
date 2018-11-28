import json
import requests
import time
import datetime

accessToken = ""
URL = "https://developer.lametric.com/api/v1/dev/widget/update/com.lametric.2c9ed5c266..."
now = time.localtime()
today = datetime.date(now.tm_year, now.tm_mon, now.tm_mday)
dDay = datetime.date(2019,3,6)
fDay = datetime.date(2018,5,19)

#difference in days: today to Stichtag
day_diff_dDay = dDay - today
days = day_diff_dDay.days

days_post = int(days)
print(days_post)

#week
day_diff_fDay = today - fDay
week = (day_diff_fDay.days / 7) - 1
plus = day_diff_fDay.days % 7
week = int(week)


week_post = "Week " + str(week) + " plus " + str(plus)
print(week_post)




def lametricpost (accessToken, URL, message1, message2):
    
    headers = {'X-Access-Token' : accessToken, 'Accept' : "application/json", 'Cache-Control' : "no-cache"}

    r = requests.post(URL, headers = headers, data = json.dumps({"frames" :[{'text' : message1, 'icon' : 'i379', 'index' : 0},{'text' : message2, 'icon' : 'i10499', 'index' : 1}]}))
    print(r.status_code, r.reason, r.text)


lametricpost(accessToken, URL, days_post, week_post)
