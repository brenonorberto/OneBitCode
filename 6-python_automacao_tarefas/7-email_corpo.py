from email.message import EmailMessage
import smtplib
import ssl

password = open('.senha', 'r').read()
from_email = 'brenodev05@gmail.com'
to_email = 'brenodev05@gmail.com'
subject = 'Proposta de parceria'
body = open('files/corpo.txt', 'r', encoding='utf-8').read()

# 1 - Estruturando a mensagem via email
mensage = EmailMessage()
mensage['From'] = from_email
mensage['To'] = to_email
mensage['Subject'] = subject

mensage.set_content(body)
safe = ssl.create_default_context()

# 2 - Enviando o email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email, 
        to_email, 
        mensage.as_string()
        )
    
print('Email enviado')