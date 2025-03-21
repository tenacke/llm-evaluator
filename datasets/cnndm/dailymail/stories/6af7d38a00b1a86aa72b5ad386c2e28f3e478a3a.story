Online greeting card service Moonpig has suspended its mobile apps following claims that a security flaw allowed access to any of its three million customer accounts.

Mobile app developer Paul Price discovered the apparent bug while examining the security settings of the code Moonpig uses in its Android and iOS applications.

He claimed that when submitting requests to the website through its app, it failed to authenticate the customers username and password.

Scroll down for video 

A warning on Moonpig's mobile app tells customers to use its main website after the company suspended access while investigating claims of a security flaw in the software the apps use to communicate with servers

Instead he said he found it was possible to put in any customer ID to access their account.

This would allow potential hackers to place orders, retrieve portions of their credit card details and obtain other personal information from their account.

18 August 2013: Paul Price says he emailed Moonpig to alert them to the flaw he claims he found in the API used by their app to communicate with the company's server. 

He says he received a few emails back before they finally said it was legacy code and that they would 'get right on it'.

26 September 2014: Mr Price sends a follow up email to Moonpig saying the issue had still not been resolved. Moonpig replies to say it will be 'before Christmas'.

5 January 2015: Vulnerability still exists. Mr Price decides to go public and publishes blog post about the flaw he discovered.

He said: 'Initially I was going to wait until they fixed their live endpoints but given the timeframes I've decided to publish this post to force Moonpig to fix the issue and protect the privacy of their customers. 17 months is more than enough time to fix an issue like this. It appears customer privacy is not a priority to Moonpig.'

6 January 2015: Moonpig suspends access to its mobile apps and posts a statement on its website.

He said he first discovered the problem in 2013 and when he contacted Moonpig they replied they would 'get right on it'.

Writing on his blog, Mr Price said that as of 5 January, the glitch was still in place and he decided to go public.

Moonpig, which allows customers to order and send personalised greeting cards, responded by immediately shutting down access to its mobile apps and launching an investigation into the claims.

Moonpig's mobile apps, which are used by 1.5 million customers, carried a message urging customers to use its normal website instead, which is unaffected.

The company, which was bought by Photobox for £120 million in 2011 and sells around 12 million cards a year, said all customer password and payment information was safe.

In a statement posted on its website, Moonpig said: 'We are aware of the claims made this morning regarding the security of customer data within our Apps.

'We can assure our customers that all password and payment information is and has always been safe.

'The security of your shopping experience at Moonpig is extremely important to us and we are investigating the detail behind today’s report as a priority.

Moonpig is the market leader in online personalised greeting cards and dispatched six million cards last year

Moonpig said that it had temporarily removed its app from Apple's App Store while it investigated the claims

'As a precaution, our Apps will be unavailable for a time whilst we conduct these investigations and we will work to resume a normal service as soon as possible.

'The desktop and mobile websites are unaffected.'

Although a message on Moonpig's website said it had removed its app from Apple's App store, it was still available for download. However the app carried a message saying it could not take orders. 

Mr Price said he found the problem when looking at application programming interface that Moonpig's mobile apps use to communicate with the company's servers.

He found that rather than sending information protected by a username and password, it tended to send static credentials that read '*redacted*:*redacted*'.

He said he created a second account, added an address and entered the new customer ID into the app and found he could access this and the saved address.

The statement posted on Moonpig's website insisted that payment information had not been compromised

Moonpig's apps have helped the company capture 90 per cent of the UK's personalised greeting card market

He said: 'I've seen some half-arsed security measures in my time but this just takes the biscuit.'

'There's no authentication at all and you can pass in any customer ID to impersonate them.

'An attacker could easily place orders on other customers accounts, add/retrieve card information, view saved addresses, view orders and much more.'

He also found he was able to obtain the credit card expiry date, the last four digits from the credit card and the name on the card when he carried out his test.

Passwords were not leaked nor enough credit card data to make a full purchase.

He said: 'I hit my test users a few hundred times in quick succession and I was not rate limited.

'Given that customer IDs are sequential an attacker would find it very easy to build up a database of Moonpig customers along with their addresses and card details in a few hours - very scary indeed.'

It is not the first problem with a greeting card website that Mr Price has found.

In October 2013 Mr Price exposed a vulnerability in the website of another greeting card company Funky Pigeon. 

This allowed an attacker to take over a user's account and gain access to personal data. This was fixed within a week.

Mr Price said he first contacted Moonpig about the fault in August 2013 and they responded to say it had been legacy code.

He said he followed up with an email in September 2014 and was promised it would be fixed by Christmas.

However as of 5 January 2015 the vulnerability still existed, he said.

Perhaps embarassingly for Moonpig, the company has also been recently advertising for an IT Security Officer. The advert was taken off its website after Mr Price reported the flaw. 

David Emm, principal security researcher at internet security consultancy Kaspersky Lab, said: 'As we understand it, the reported vulnerability has not so far been used to steal personal information of Moonpig customers. 

'However, it seems that the vulnerability, if confirmed, would allow an attacker to access the account details of other customers.

'It's important that companies take information about a vulnerability in their products very seriously. 

' If this vulnerability is confirmed, and it's true that Moonpig has previously failed to take any action to protect their customers for almost a year and a half, this is alarming - especially for a provider of an online shopping application used to transmit highly sensitive data.'

@highlight

App developer Paul Price claims to have found a flaw in the software used by Moonpig's mobile apps to communicate with the company's servers

@highlight

Loophole would give hackers access to credit card details and personal information of Moonpig's customers simply by using their customer ID 

@highlight

Moonpig is investigating the claims and has shut down its mobile apps

@highlight

Moonpig's Android and iOS apps are used by 1.5 million customers