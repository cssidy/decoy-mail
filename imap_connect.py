#! /usr/bin/python3

import imaplib
from login_credentials import gmail_credentials


def start_imap_connection():

    # Connect to the imap server
    print('\n')
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
    imap_server.ehlo()
    # Login to email account
    print('Logging in to IMAP server...')
    imap_server.login(gmail_credentials.get('username', 0), gmail_credentials.get('password', 0))
    print('Success.')

start_imap_connection()

# TODO: search for emails to bait that are in the spam box
# refer to pattern_match.py for exact keywords

# imap_server.select()
# typ, data = imap_server.search([SPAM, 'ALL'])
# for num in data[0].split():
#     typ, data = imap_server.fetch(num, '(RFC822)')
#     print('Message %s\n%s\n' % (num, data[0][1]))
# imap_server.close()
# imap_server.logout()
# print('\nLogged out.')

# TODO: fetch content from emails (from, subject, body) and store in a dictionary of some sort
# fetch_dictionary = {}

# TODO: close imap server connection
# imap_server.quit()



