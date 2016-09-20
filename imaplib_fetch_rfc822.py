#! /usr/bin/python3

import imaplib
import imaplib_connect

with imaplib_connect.open_connection() as c:
    c.select('INBOX')
    typ, [msg_ids] = c.search(None, 'TEXT', 'Sunday')
    for num in msg_ids.split():
        typ, msg_data = c.fetch(num, '(RFC822)')
        for raw_email in msg_data:
            # raw_email is a tuple of len==2, we need the 2nd item:
            if len(raw_email) >= 2:
                b = raw_email[1]
                email = b.decode('utf-8').split('\r\n')
                subject_, from_, to_, body_, = ' ' + email[0], email[1], email[2], 'Body: ' + email[4]
                print(subject_, '\n', from_, '\n', body_, '\n')
            else:
                break
                # Use this for debugging if the raw_email is diff't length


#close imap server connection
