# Contributing to Doppelganger Mail
#### Diverting today's spam, preventing tomorrow's spam.

How to get involved:

1. We are happy you are interested in the project. Whether you're an 'official' collaborator or not, feel free to fork the project and create a branch for the feature/issue you're going to create/address.
2. Write tests for the feature/issue if they don't already exist. You can see a list of milestones to complete below.
3. Write the code.
4. Make the tests pass.
5. Make a pull request to master.
6. Contact cssidy at cassidy at cassidybrooke dot net with any questions/comments.


### Milestones (and to-do list)

- [x] ~~Flow chart~~
- [x] ~~Proof of concept~~
- [ ] Bayesian statistical filtering, be able to accurately determine if an email is spam
- [ ] Remove spam emails from spambox to toy with them behind the scenes
- [ ] Obfuscate bot's sent email meta data/headers
- [ ] Handle both text and HTML content
- [ ] Fine tune SMTP email's appearance, make it look legitimate and potentially get past spam filters
- [ ] Compose email that is in response to the previous email (as part of a thread, not a new email)
- [ ] Loop through mailbox until nothing to respond to or sort, then print report
- [ ] Create and query database of email spam messages and appropriately gullible responses
- [ ] Success and failure rate tracking via the database
- [ ] Multiple personalities and their own set of responses
- [ ] Learn new conversations and responses
- [ ] Be able to judge if the email is part of a previous correspondence
- [ ] Choose the best conversations based on previous conversation situations
- [ ] Attach images to emails if requested, pull from a pool of fake images
- [ ] Have VoIP conversations with spammers with pre-recorded audio clips
- [ ] Automatically DoS links found inside email spam messages
- [ ] Create a software tailored for mailservers (Linux, considering it powers most of the Internet?) or email clients (Gmail gadget? Thunderbird plugin? Outlook Ad-in?), Create a Javascript extension for Thunderbird?
- [ ] Another interesting idea, create a web email client that uses this software under the hood, thus creating a distributed network that uses client computer information in sent email headers and DDoS attacks.
- [ ] GUI, show spam-hunt count, or spams-in-progress statistics, or simply make it invisible to end users.
- [ ] Collect statistics of usage and success rates
