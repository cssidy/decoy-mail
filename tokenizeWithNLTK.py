#! python3

#open mail server connection with IMAP
#import imapclient
#imapObj = imapclient.IMAPClient('imap.myserver.com', ss1=True)
#imapObj.login('myemailaddress@myserver.com', 'mypassword')

#increase search size limits
#import imaplib
#imaplib._MAXLINE = 10000000 

#search for spam mail to respond to
#UIDs = imapObj.search(['TEXT "charity funds transaction urgent deposited bank"', 'UNANSWERED'])
#UIDs

#get email body content

#prepare email body content for database

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

emailbodytext = ('Dearest In the Lord Jesus Christ Greetings,I am Mrs.Kristina Leonid. an aging widow suffering from long time illness.'
                 'i am currently admitted in a private hospital here in Abidjan cote d Ivory, I have some funds I inherited from my late loving husband Mr.Daniel Leonid.'
                 'The amount of US$7.500, 000.00 which he deposited in one of the Bank Here and I need a honest and God fearing person who have the feelings of human that'
                 'can use this funds for Gods work and 15% out of the total funds will be for your compensation for doing this work of God. Please if you would be able to'
                 'use these funds for the Lords work kindly reply to me. May the Grace of our Lord Jesus Christ the love of God and the sweet fellowship of the Lord be with'
                 'you and your familys Amen. Your Sister In The Lord Mrs.Kristina Leonid.'
                 )
stop_words = set(stopwords.words('english'))

words = word_tokenize(emailbodytext)

#filtered_sentence = []

#for w in words:
    #if w not in stop_words:
        #filtered_sentence.append(w)

filtered_sentence = [w for w in words if not w in stop_words]

#for i in filtered_sentence:
    #print(i),

#remove punctuation and quotation marks from filtered_sentence
#replace all punctuation with spaces

#filtered_sentence.translate(string.maketrans(string.punctuation, ' '*len(string.punctuation)))

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
tokenizer(filtered_sentence)
print filtered_sentence,

#Note that if you use this option, you lose natural language features special to word_tokenize like splitting apart contractions.
#You can naively split on the regex \w+ without any need for the NLTK.
    
#put filtered sentence into mysql database

#pattern-matching, choose best response

#tally any response success



#open mail server connection with SMTP
#import smtplib
#smtpObj = smtplib.SMTP('')
#smtpObj.ehlo()
#smtpObj.starttls()
#smtpObj.login('','')


#compose email
#smtpObj.quit
