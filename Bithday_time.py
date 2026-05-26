import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time

sender = "anshika.tiwari.gnmba27@iilm.edu"
password = "shtq igrh vrge svec"    
receiver = input("Enter receiver email :")
name = input("Enter name of the person :")
birthday_date = input("Enter birthday date (dd-mm): ")

send_hour = 3
send_minute = 42

print("Waiting for birthday wish to be sent on the birthday date.")


while True:
     now = datetime.now()
     today_date = now.strftime("%d-%m")

     if birthday_date == today_date and now.hour == send_hour and now.minute == send_minute:
         
         msg = MIMEText(f""" 🎂Happy Birthday!
    Dear {name},

    Wishing you a very happy birthday🍰!
    May your day be filled with joy, laughter, and wonderful memories. Enjoy your special day to the fullest!
    Best wishes💕,
    [Your {name}]
    """)
         msg['Subject'] = "Happy Birthday!"
         msg['From'] = sender
         msg['To'] = receiver    
         
        
         try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

            server.login(sender, password)

            server.send_message(msg)
            server.quit()
            print("message send successfully")

         except Exception as e:
            print(f"Failed to send email: {e}")
     break
time.sleep(30)