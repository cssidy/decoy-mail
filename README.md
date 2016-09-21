# Shell
## Playing the shell game with email spammers. Preventing future spam.

The Internet as a living organism. It's like a lichen; a symbiotic relationship
between hardware, software, information and humans. Spam clogs up its
functioning, making servers have to process a bulk of data that nobody wants.
This results in wasted electricity and physical storage for ISPs and, for the
end user, time wasted being annoyed and having to further filter spam, empty
spam boxes, and the risk of falling prey to malicious, unintentionally
downloaded software and scams. The Internet would be a healthier organism
without spam, and now we can build intelligent software agents to function as a protective immune system for it.

### What is the solution?

Shell is spam prevention software for ISPs' mailservers and email-clients. Shell prevents spam by employing autonomous, distributed, and intelligent software agents to engage with spammers and flood their servers with convincingly gullible (but false) leads. Ultimately, this wastes spammers' time, induces spammer frustration, reduces spammers' motivation to spam, and render careers in spamming unprofitable to pursue. Shell prevents future spam.

### Why?

At this point in time we have systems that are very good at recognizing spam. However, most spam-fighting methods in use today are passive in comparison to Shell's approach; they rely on Bayesian filtering to remove spam mail that has already been successfully delivered. This is inefficient because it doesn't stop the root motivation, that 5 out of 100,000 emails (that take only an hour, maybe $100 and little thought to send) will slip through the statistical filters and hook a gullible victim and their credit card. Sad but true, that's pretty good odds of success for such a small investment. Shell takes it a step further: what happens if we shift those odds...say, 30 gullible, very "human" victims respond? Or 100? Or 300? or 100,000? How will the spammer know who to pursue? They will become confused, frustrated, and exhausted. There will be no reason to spam anymore because it will take more time and energy to find the victim than it's worth.


### About this software

Shell is written in Python 3.5 with PyCharm Community Edition. This version is designed to log into Gmail mail servers. It requires an Internet connection and Gmail account and credentials to run. I am trying to avoid 3rd party libraries/APIs as much as possible. Eventually this software will have to be tailored to run on diverse systems, communicating with other diverse systems with their own unique configurations (which may be different than Google's).

This idea is not necessarily new. Check out scam-baiting, a popular computer nerd hobby on the [419 Eater Forums](http://www.419eater.com/) for an understanding of what this software is trying to automate. And, check out this disbanded Perl project of a similar nature, [Autobait](http://www.autobait.com/).

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

### Why is this open source?

Attempting to fund this sort of project would prolong its completion because I do not have the resources to build a company to develop it. And, after the hypothetical company is formed, there are no guarantees that I'd make my investment back. So, instead of being secretive with my ideas and proof-of-concept, I feel it's more beneficial to release it into the wild and see what happens. This is the sort of code that is for the public good, anyways. I hope that it spurs research into more innovative, effective ways of combating spam.

What happens if spammers see this and device more innovative, effective ways of countering Shell? That could happen. But those spammer could also, in effect, show how to make the Shell software more robust and more "human". Because of the very nature of spam and its mediums, there still has to be someone on the other end who decides if the victim is worth pursuing and attempt to get money/personally identifiable information from them. I'm not sure yet how a spammer will be able to circumvent that. Maybe spammers will create bots to antagonize Shell bots, but what good would that do in getting them closer to their objective? At least it will give them something to do besides sending out mass emails.

## Usage

Create a `_config.py` file with your credentials (this is .gitignored)...
