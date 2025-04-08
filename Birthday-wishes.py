<<<<<<< HEAD

import smtplib
import datetime as dt
import pandas
import random

PLACEHOLDER = '[NAME]'
MY_EMAIL = "appindia564@gmail.com"
PASSWORD = "byazkptaoxlxexau"
#----------------------------------Take birth date from csv file------------------#

birthday_file = pandas.read_csv(r"100days_project\projects\birthday-wisher-extrahard-start\birthdays.csv")
month_list = birthday_file['month'].to_list()  
day_list =  birthday_file['day'].to_list() 


def bdy_msg(name):

    with open(rf'100days_project\projects\birthday-wisher-extrahard-start\letter_templates\letter_{random.randint(1,3)}.txt') as letter_data:
        data = letter_data.read()
        new_data = data.replace(PLACEHOLDER,name)

    return new_data


def send_mail(receiver_mail,message):
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=receiver_mail,
                            msg=f"Subject:Happy Birthday\n\n{message}")


now = dt.datetime.now()

if now.month in month_list:
    if now.day in day_list:
        receiver_mail = birthday_file[birthday_file.month == now.month].email
        name = birthday_file[birthday_file.month == now.month].name.item()
      
        message = bdy_msg(name)
        send_mail(receiver_mail,message)




# now.day

# print(check_date())
