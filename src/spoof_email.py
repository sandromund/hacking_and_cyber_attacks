import smtplib

from decouple import config

username = config("EMAIL_USER")
password = config("EMAIL_PASSWORD")


fake_from = "donaldtrump@gmail.com"
fake_name = "Donald Trump"

to_email = "sandromund@gmail.com"
to_name = "Sandro Mund"

subject = "Bonjour"
content = "This is the fbi. OPEN UP"


message = f"From: {fake_name} <{fake_from}>" \
          f"To: {to_name} <{to_email}>" \
          f"Subject: {subject}\n\n{content}"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(username, password)
server.sendmail(username, to_email, message.encode())
server.close()
