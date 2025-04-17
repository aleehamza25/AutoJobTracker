import smtplib
from email.message import EmailMessage

def send_email_with_attachment(subject, body, to_email, attachments, smtp_config):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = smtp_config['email']
    msg['To'] = to_email
    msg.set_content(body)
    
    for filepath in attachments:
        with open(filepath, 'rb') as f:
            file_data = f.read()
            file_name = filepath.split("/")[-1]
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(smtp_config['email'], smtp_config['password'])
        smtp.send_message(msg)