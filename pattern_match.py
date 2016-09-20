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


# determines if one keyword is found in a string

# keywords = "funds"
#
# str = "hello hello hello hello funds"
# str = str.split()
# print(str)
#
# def keyword_match(str):
#
#     if keywords in str:
#         print("this is a scam")
#         print(filter(lambda x: keywords in x, str))
#     else:
#         print("not a scam")
#
# keyword_match(str)



# nek4life and zev mod
# 
# import string
# 
# PUNCTUATION_TABLE = str.maketrans({key: None for key in string.punctuation})
# 
# from_ = ('human@inter.net')
# 
# body_ = ('My Name is Mrs Maria Peterside you have been selected to use my fund to serve the poor for '
#          'charity since I can not live because of cancer contact me blessedmaria@yandex.com')
# 
# advancefee_Scam = ['charity', 'fund', 'funds', 'transfer', 'deliver', 'beneficiary', 'trust', 'confident', 'sum',
#                    'large', 'mutual', 'million', 'account', 'money', 'bank', 'release', 'contact', 'secret',
#                    'receipt', 'loan', 'offer', 'reliable', 'export', 'foreign', 'partner', 'lottery', 'cash', 'receive',
#                    'ATM', 'help']
# 
# romance_Scam = ['hello', 'dear', 'good', 'response', 'reply', 'await', 'wait', 'nice to meet you', 'my name is',
#                 'what is your name', 'facebook', 'online', 'pleasure',
#                 'interesting', 'interested', 'communicate', 'details', 'profile', 'about me', 'pics', 'images',
#                 'photos', 'pictures', 'saw your profile', 'friend', 'genuine', 'waiting to hear from you',
#                 ]
# 
# attachment_Scam = ['attached file', 'please open', 'open']
# 
# undeliverable_Email = ['undeliverable', 'returned to sender']
# 
# blacklisted_UIDs = ['', '', '']
# 
# 
# 
# 
# def find_intersection(keyword_list, email_message):
#     # Remove punctuation with punctuation translation table all mapped to None
# 
#     email_message = "".join(char
#                        for char in email_message
#                        if char not in string.punctuation)
# 
#     # Normalize case
#     email_message = email_message.lower()
# 
#     # print('\n')
#     # print(email_message)
# 
#     # Make a list of words from the sentence
#     email_message_parts = email_message.split(' ')
# 
#     # print('\n')
#     # print(email_message_parts)
#     # print('\n')
# 
#     # count the words appearing in both the sentence and word_list
#     # via a list comprehension (probably could just increment a counter)
#     num_of_words_that_appear_in_sentence = len([word
#                                                 for word in email_message_parts
#                                                 if word in keyword_list])
# 
#     # Find the percentage
#     hit_percentage = num_of_words_that_appear_in_sentence / len(keyword_list) * 100
# 
# 
#     if hit_percentage >= 10:
#         result = True
#     else:
#         result = False
# 
#     print(keyword_list)
#     print(bool(hit_percentage), hit_percentage)
#     print(result)
#     print('\n')
# 
# 
# find_intersection(advancefee_Scam, body_)
# find_intersection(romance_Scam, body_)
# find_intersection(attachment_Scam, body_)
# find_intersection(undeliverable_Email, from_)
# find_intersection(blacklisted_UIDs, from_)
