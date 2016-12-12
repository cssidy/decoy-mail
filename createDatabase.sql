CREATE TABLE solicitations (
      solicitation LONGTEXT NOT NULL
    , solicitations_id INT(10) NOT NULL
    , PRIMARY KEY(solicitations_id)
);

INSERT INTO solicitations
(solicitation, solicitations_id)
VALUES
     ('Contact debbiepfizer31110 @ outlook.com details charity worth 5.1M GBP','1')
    ,('I Mr. Hamish N. Buchan, Chairman Remuneration Board Directors , appointed board November 2003. former chairman Association Investment Companies formerly Chairman NatWest Securitiesin Scotland. Chairman Personal Assets Trust , Director Aberforth Smaller Companies Trust anTempleton Emerging Markets Investment Trust.I privileged contact interest invest country business interestin following sectors : Electronics , Banking , Oil Sector , Real Estate , Stock Speculation Mining , Agriculture , Transportation Tobacco. If think solid background idea making good profit mentioned business sectors country , Please get back Thanks understanding I would wait get immediate response.','2')
	,('Dear Sir / Madam , compliment day. urgent business proposal , please check attachment. Please delete content email soon possible willing assist me. awaiting urgent reply.','3')
    ,('FUND CREDITING DEPARTMENT ( FCD ) ADVISE : YOUR FOREIGN PAYMENT NOTIFICATION Attention Beneficiary , Based investigation foreign payment , want to find re still alive sign dead assignment Mrs. Patricia Sanders Arizona receive fund,reply us : Your Full Name : Your Home/Office Address ( P.O Box Not Acceptable ) : Your Phone Fax Number : Your Current Occupation : We writting money approved favor for payment get information us fast fund released Mrs. Patricia Sanders. Best Regards , Raymon','4')
    ,('PLEASE MY FAMILY TRUST YOU OPEN ATTACHMENTS EMAIL US BACK.','5')
    ,('Dearest In Lord Jesus Christ Greetings,I Mrs.Kristina Leonid. aging widow suffering long time illness.i currently admitted private hospital Abidjan cote d Ivory , I funds I inherited late loving husband Mr.Daniel Leonid.The amount US $ 7.500 , 000.00 deposited one Bank Here I need honest God fearing person feelings human thatcan use funds Gods work 15 % total funds compensation work God. Please would able touse funds Lords work kindly reply me. May Grace Lord Jesus Christ love God sweet fellowship Lord withyou familys Amen. Your Sister In The Lord Mrs.Kristina Leonid','')
    ,('','')
    ,('','')
    ;

CREATE TABLE responses (
      response LONGTEXT NOT NULL
    , responses_id INT(10) NOT NULL
    , solicitations_id INT(10) NOT NULL
    , counters_id INT(10) NOT NULL
    , PRIMARY KEY(responses_id)
    , FOREIGN KEY(solicitations_id) REFERENCES solicitations (solicitations_id) ON DELETE CASCADE ON UPDATE CASCADE
    , FOREIGN KEY(counters_d) REFERENCES counters (counters_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO responses
(response, responses_id, solicitations_id, counters_id)
VALUES
     ('Hello, I am curious about your charity. How can I help?','1','1','1')
    ,('Yes I am very interested in helping you with your transaction. I am a very reliable person. My name is Arnold Goldsbalm, I am male, 43 years of age. I live at 33 Herald Street, Beaconville, Alabama. I am a carpenter. What more do you need to know?','2','2','2')
	,('I did not receive your original message. Sorry about that! Yes I am very interested in the funds. What are you proposing exactly?','3','3','3')
	,('I am excited to know that the money has been approved to me. I have not approved of anything to Mrs. Patricia Sanders. What is the amount of the fund exactly?','4','4','4')
    ,('My name is Dr. Gerald Berkovitz. I am mostly retired but my office is located at 192 Eastway Warbler Street, New York, NY and my cell phone is 16056559097. What else do I need to provide transfer the funds?','5','4','5')
    ,('Hello, yes, I cannot see your attachment it says the file is corrupt? Are you in need of help?','6','5','6')
    ;

CREATE TABLE counters (
      counter DECIMAL(10) NOT NULL
    , counters_id INT(10) NOT NULL
    , PRIMARY KEY(counters_id)
);

INSERT INTO counters
(counter, counters_id)
VALUES
     ('0', '1')
    ,('0', '2')
	,('0', '3')
	,('0', '4')
	,('0', '5')
	,('0', '6')
    ;
