#! /usr/bin/python3

from imaplib_fetch_rfc822 import body_

email_result = ()
keywords1 = 'funds'
keywords2 = 'Sunday'
keywords3 = 'lake'
keywords4 = 'trust'

# determines if multiple keywords are found within a string

def keyword_match(data):
    s = "\n".join(data)
    for k in keywords1 or k2 in keywords2 or k3 in keywords3 or k4 in keywords4:
        if k or k2 or k3 or k4 in s:
            # print("this email is a scam")
            email_result = True
            print(email_result)
            print('Keyword match')
            print('\n')
            # then compose email
            break
        else:
            # print("email not a scam")
            email_result = False
            print(email_result)
            print('No keyword match')
            print('\n')
            # then move email to other folder
            break


keyword_match(body_)

