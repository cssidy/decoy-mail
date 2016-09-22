# Decoy Mail
#### Diverting today's spam, preventing tomorrow's spam.

#### Learn more about Decoy Mail's mission at [http://cassidybrooke.net/decoy-mail/](http://cassidybrooke.net/decoy-mail/).

### About this software

Decoy Mail is written in Python 3.5 with PyCharm Community Edition. This version is designed to log into Gmail mail servers. It requires an Internet connection and Gmail account and credentials to run. I am trying to avoid 3rd party libraries/APIs as much as possible. Eventually this software will have to be tailored to run on diverse systems, communicating with other diverse systems with their own unique configurations (which may be different than Google's).

### Usage


### Flow chart

[![flow chart.png](http://s10.postimg.org/4czq6yyk9/flow_chart.png)](http://postimg.org/image/d80khhncl/)

### Video demonstration

This proof of concept logs into a Gmail account, enters the inbox, starting at the first email looks through the list, fetches the first email it finds with a spam keyword, then composes and sends a new email to the sender of the spam.

Quick tour of the files:

[![Alt text for your video](http://img.youtube.com/vi/HqinRVduHdA/0.jpg)](http://www.youtube.com/watch?v=HqinRVduHdA)

Fetching, matching, and responding to an email:

[![Alt text for your video](http://img.youtube.com/vi/p-Qi0shD78Y/0.jpg)](http://www.youtube.com/watch?v=p-Qi0shD78Y)


### Milestones (and to-do list)

- [x] ~~Flow chart~~
- [x] ~~Proof of concept~~
- [ ] Obfuscate bot's sent email meta data
- [ ] Fine tune SMTP email's appearance, make it look legitimate
- [ ] Compose email that is in response to the previous email (as part of a thread, not a new email)
- [ ] Loop through mailbox until nothing to respond to or sort, then print report
- [ ] Create and query database of email spam messages and appropriately gullible responses
- [ ] Success and failure rate tracking via the database
- [ ] Multiple personalities and their own set of responses
- [ ] Learn new conversations and responses
- [ ] Choose the best conversations based on previous conversation situations
- [ ] Attach images to emails if requested
- [ ] Have VoIP conversations with spammers with pre-recorded audio clips
- [ ] Automatically DDoS links found inside email spam messages
- [ ] Create a software tailored for mailservers (Linux, considering it powers most of the Internet?) or email clients (Gmail gadget? Thunderbird plugin? Outlook Ad-in?)
- [ ] Test software
- [ ] Collect statistics

