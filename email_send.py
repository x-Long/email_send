import requests
import datetime
from requests.cookies import RequestsCookieJar
import re
import datetime
import time

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
import json


def send_email():
    miss_time = datetime.datetime(2018, 2, 14)
    r = requests.get(
        "http://api.tianapi.com/txapi/tianqi/index?key=b94e1eda3886cba96d37aac1c2cc6d48&city=西安")
    r1 = requests.get(
        "http://api.tianapi.com/txapi/saylove/index?key=b94e1eda3886cba96d37aac1c2cc6d48")

    for i in range(0, 10):

        if json.loads(r.text)['newslist'][i]['date'] == datetime.datetime.now().strftime('%Y-%m-%d'):
            info = json.loads(r.text)['newslist'][i]
            break

    today = datetime.datetime.now()
    days = int((today - miss_time).days)

    email_info = "xxx你好：\n\n\t从我们在一起到现在已经是第" + str(
        days) + "天~" + "\n\n\t特殊时期，口罩常备多喝水~ \n\n\t另外，小喇叭为您奉上明日天气，祝您天天好心情~~今天是" + info["date"] + "，天气：" + info[
                     "weather"] + "，实时温度：" + info["real"] + "，明天最高温度：" + info['highest'] + "\n\n\t" + "小贴士给您说：" + info[
                     "tips"] + "\n\n-♥--♥--♥--♥--♥--♥-\n\n" + "♥♥♥ 今日份情话To Lemon ♥♥♥" + "\n\n" + \
                 json.loads(r1.text)["newslist"][0][
                     "content"] + "\n\nYou are the apple of my eyes~\n-♥--♥--♥--♥--♥--♥-\n\n"

    # 这里使用SMTP_SSL 默认使用465端口
    smtp = SMTP_SSL("smtp.163.com")
    smtp.set_debuglevel(1)

    smtp.ehlo("smtp.163.com")
    smtp.login("simonlts@163.com", "KXLFOUFTRMKNXDUJ")

    msg = MIMEText(email_info, "plain", "utf-8")
    msg["Subject"] = Header("Lemon私人邮件", "utf-8")
    msg["from"] = "simonlts@163.com"
    # msg["to"] = email
    smtp.sendmail("simonlts@163.com", ["710450053@qq.com"], msg.as_string())
    smtp.quit()


def main(h=21, m=38):
    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            send_email()
        time.sleep(60)


if __name__ == '__main__':
    main()
