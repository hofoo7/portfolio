from flask import Flask, render_template, request, redirect
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
 
app = Flask(__name__)
 
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/form', methods=["POST"])
def form():
  email = request.form.get("email")
  messagetext = request.form.get("message")

  sender_email = email
  receiver_email = "hofericamario@gmail.com"

  message = MIMEMultipart("alternative")
  message["Subject"] = email
  message["From"] = email
  message["To"] = receiver_email

  part1 = MIMEText(messagetext, "plain")
  message.attach(part1)

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login("hofericamario@gmail.com", "Modelarstvo7")
  server.sendmail(email, "hofericamario@gmail.com", message.as_string())

  if not email or not message:
    error_statement = "Potrebné vyplniť obe polia..."
    return render_template('index.html',
      error_statement = error_statement,
      email = email,
      message = message
    )

  print(email)
  print(message)

  title = "Ďakujem! Ozvem sa hneď, ako to bude možné..."
  return render_template('index.html', title = title)


if __name__ == "__main__":
  app.run(debug=True)
 