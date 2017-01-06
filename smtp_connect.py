#! /usr/bin/python3

import smtplib
from fetch_mail import from_, subject_
from pattern_match import email_result

if email_result is True:
    print("TRUE")

def smtp_connection(verbose=True):
    # ENTER YOUR EMAIL
    email_account = 'xxxxx@gmail.com'
    # ENTER YOUR PASSWORD
    password = 'xxxxx'
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    print('Logging in as', email_account)
    server.login(email_account, password)
    print('Log in success.')
    print('\n')

    def compose_email(email_result):
        sender = email_account
        to = from_
        subject = ('Re: ' + subject_)
        body = "Yes, that would be delightful."

        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sender, ", ".join(to), subject, body)

        try:
            server.sendmail(sender, to, email_text)
            server.close()

            print('Email delivered.')

        except:
            print('Unable to send email.')

    compose_email(email_result)

    return server
    server.logout()

# prints results of def open_connection
if __name__ == '__main__':
    with smtp_connection(verbose=True) as c:
        print(c)

