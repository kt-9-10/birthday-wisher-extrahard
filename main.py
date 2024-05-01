##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and
#    replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import datetime as dt
import random
from email.mime.text import MIMEText
import smtplib

LETTER_TEMPLATES_LIST = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthday_members = []
my_email = "test@tmail.com"
password = "QWERTY"

# CSVを読み、メンバーリスト作成
data = pandas.read_csv("./birthdays.csv")
member_list = data.to_dict(orient="records")

# 今日の月日
now = dt.datetime.now()
today = {'month': now.month, 'day': now.day}

# 誕生日では無いメンバーを、メンバーリストから削除
for member in member_list:
    if today['month'] == member['month'] and today['day'] == member['day']:
        birthday_members.append(member)

# バースデイメール送信処理
for member in birthday_members:
    # テンプレートの選択
    letter_template_name = random.choice(LETTER_TEMPLATES_LIST)
    with open("./letter_templates/" + letter_template_name, "r") as letter_template:
        letter_text = letter_template.read()

    # 宛名のリプレイス
    letter_text = letter_text.replace("[NAME]", member['name'])

    # MIMETextオブジェクトを作成し、メールの内容を設定する
    msg = MIMEText(letter_text, 'plain', 'utf-8')
    msg['Subject'] = "Happy Birthday!"
    msg['From'] = my_email
    msg['To'] = member["email"]

    with smtplib.SMTP("smtp.tmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(msg)
