# Doppelganger Mail
#### Diverting today's spam, preventing tomorrow's spam.

#### Learn more about Doppelganger Mail's mission at [http://cassidybrooke.net/doppelganger-mail/](http://cassidybrooke.net/doppelganger-mail/).

### Configuration & Usage

Modify your `_config.py` file's dictionary with your email account credentials (this is .gitignored). For example IMAP_HOSTNAME may become imap.gmail.com, SMTP_HOSTNAME may become smtp.gmail.com, USERNAME example@gmail.com and PASSWORD holymackerel keys.

Note: Doppelganger Mail is written in Python 3.5. This version is designed to work with a Gmail inbox. It requires an Internet connection and Gmail account and credentials to run. You will have to [turn off 2-Step Verification](https://support.google.com/accounts/answer/1064203?hl=en) to allow the email bot to access your Inbox, otherwise Google will block the action. I am trying to avoid 3rd party libraries/APIs as much as possible. Eventually this software will have to be tailored to run on diverse systems, Thunderbird, Outlook, etc. Hence, I am not using solely Google's Gmail API.

### Flow chart

[![flow chart.png](http://s10.postimg.org/4czq6yyk9/flow_chart.png)](http://postimg.org/image/d80khhncl/)

### Video demonstration

This proof of concept logs into a Gmail account, enters the inbox, starting at the first email looks through the list, fetches the first email it finds with a spam keyword, then composes and sends a new email to the sender of the spam.

Quick tour of the files:

[![Alt text for your video](http://img.youtube.com/vi/HqinRVduHdA/0.jpg)](http://www.youtube.com/watch?v=HqinRVduHdA)

Fetching, matching, and responding to an email:

[![Alt text for your video](http://img.youtube.com/vi/p-Qi0shD78Y/0.jpg)](http://www.youtube.com/watch?v=p-Qi0shD78Y)

Note: this is old, from when I was calling the project the poor name of "Shell" after the shell game.

