import smtplib
from email.message import EmailMessage

# Configuration
SMTP_SERVER = "smtp.mail.me.com"
SMTP_PORT = 587 # Use 587 for iCloud, not 465
SENDER_EMAIL = "jr77sullivan@icloud.com"
SENDER_PASSWORD = "yesg-uqie-agjv-tiud" # Your App-Specific Password

msg = EmailMessage()
msg.set_content("Hey mama! this is an Automated message sent by a python script! Cool eh?")
msg["Subject"] = "Automated Python message"
msg["From"] = SENDER_EMAIL
msg["To"] = "erin211au@yahoo.com"

try:
    # 1. Connect to the server on the standard port
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    
    # 2. Identify yourself to the server
    server.ehlo()
    
    # 3. Secure the connection (This is where the 'version' magic happens)
    server.starttls()
    
    # 4. Login and send
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()
    print("Success! The version error is gone.")
except Exception as e:
    print(f"Error: {e}")
