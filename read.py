#! /usr/bin/python3

import imaplib

from models import Email


class EmailFetcher:
    """connects to IMAP server and fetches matching emails.
    
    usage:

    >>> with EmailFetcher(config_dict) as ef:
            ef.fetch_emails(['FROM', 'Mom', 'SUBJECT', 'rent'])
    
    """

    def __init__(self, config_dict, verbose=True):
        self.verbose = verbose                

        self.hostname = config_dict['HOSTNAME']
        self.username = config_dict['USERNAME']
        self.password = config_dict['PASSWORD']

    def __enter__(self):
        self.connection = self.connect()
        return self

    def __exit__(self, _a, _b, _c):
        self.connection.close()
        self.connection.logout()

    def connect(self):
        """connect to IMAP server and returns the connection."""

        if self.verbose:
            print('\n')
            print('Connecting to', self.hostname)

        server = imaplib.IMAP4_SSL(self.hostname)

        if self.verbose:
            print('Logging in as', self.username)
            print('\n')

        server.login(self.username, self.password)
        return server

    def fetch_emails(self, criteria):
        """fetch matching emails from open IMAP connection.
        
        note: as of Sep 21, 2016, this doesn't return anything. 

        arguments:
            criteria: a list with alternating email field name string
                      and keyword string
        """

        self.connection.select('INBOX')

        charset = None

        _, [msg_ids] = self.connection.search(charset, *criteria)

        for num in msg_ids.split():

            _, msg_data = self.connection.fetch(message_set=num, 
                                  message_parts='(RFC822)')

            for raw_email in msg_data:
                # raw_email is a tuple of len==2, we need the 2nd item:
                if len(raw_email) >= 2:
                    email_bytes = raw_email[1]
                    cleaned_up_email_text = clean_up_email_text(email_bytes)
                    # print('\n'.join(cleaned_up_email_text))
                    email = Email(cleaned_up_email_text)
                    print(email)


def clean_up_email_text(email_bytes):
    """convert bytes to utf-8, return a list of lines."""

    converted_email = email_bytes.decode('utf-8')
    email_lines = converted_email.rstrip().split('\r\n')
    return email_lines
