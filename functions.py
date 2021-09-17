import hashlib
import smtplib

# Configs email
MAIL_FROM = 'test@test.com'
PASSWORD = 'password'
MAIL_TO = 'testreceiver@test.com'
SMTP_SERVER = 'smtp.live.com'
PORT = 587


#   Functions
def set_original_hash():
    with open('content.txt', 'r') as content:
        original_hash = hashlib.sha256(content.read().encode('utf-8')).hexdigest()
    with open('original_hash.txt', 'w+') as file:
        file.write(original_hash)


def send_email():
    server = smtplib.SMTP(SMTP_SERVER, PORT)
    server.starttls()
    server.login(MAIL_FROM, PASSWORD)

    message = f'''
                From: {MAIL_FROM}
                To: {MAIL_TO}
                Subject: ALERTA
                
                ALERTA!!! O ARQUIVO MONITORADO FOI ALTERADO!!!
                '''

    server.sendmail(MAIL_FROM, MAIL_TO, message)
    server.quit()


def check_hashs():
    file = open('content.txt', 'r')
    original_hash = open('original_hash.txt', 'r').read()
    current_hash = hashlib.sha256(file.read().encode('utf-8')).hexdigest()
    file.close()

    if original_hash != current_hash:
        print('Enviando email...')
        send_email()
    else:
        print('Tudo certo...')
