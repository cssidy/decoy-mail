#! /usr/bin/python3

import smtplib
from login_credentials import gmail_credentials

# login to smtp server
def start_imap_connection():

    # connect to smtp server
    print('\n')
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    # log in to email account
    print('Logging in to SMTP server...')
    smtp_server.login(gmail_credentials.get('address', 0), gmail_credentials.get('password', 0))
    print('Log in success.')

# TODO: open database
    email_addresses = ['1@gmail.com', '2@gmail.com', '3@gmail.com', '4@gmail.com']

# TODO: bring in variables from pattern_match.py (to, subject, from, body)

# TODO: send mail

    for email_address in email_addresses:
        content = "Subject: Test\nInitial test"
        print('Sending email to %s...' % email_address)

        send_mail_status = smtp_server.sendmail(gmail_credentials.get('address', 0), email_address, content)
        if send_mail_status != {}:
            print('There was a problem sending email to %s: %s' % (email_address, send_mail_status))
        else:
            print('Success.')
    smtp_server.quit()

