import smtplib
from email.mime.text import MIMEText

sender = "anshika.tiwari.gnmba27@iilm.edu"
password = "kjev dlfc shka mwqf"

receiver =input("Enter receiver email :")


name = input("Enter name of the person :")

msg = MIMEText(f" Happy Birthday!\n\nDear {name},\n\nWishing you a very happy birthday! May your day be filled with joy, laughter, and wonderful memories. Enjoy your special day to the fullest!\n\nBest wishes,\n[Your Name]")

msg['From'] = sender
msg['To'] = receiver    
msg['Subject'] = "Happy Birthday!"

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

server.login(sender, password)

server.send_message(msg)

server.quit()

print("message send successfully")