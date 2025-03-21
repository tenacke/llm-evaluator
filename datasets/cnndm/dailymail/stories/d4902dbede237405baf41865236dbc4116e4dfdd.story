By
Victoria Woollaston

Websites and their users have been left reeling this week after a flaw was exposed in a common encryption service.

Around two-thirds of websites are vulnerable to so-called ‘heartbleed hackers’, and now a password expert has created a tool to see if your favourite sites are affected.

LastPass’ Heartbleed Checker looks to see when a site’s secure encryption certificate was last valid and warns if the server may be at risk.

LastPass' Heartbleed Checker, pictured, looks to see when a site's secure encryption certificate was last regenerated and warns if the server may be at risk. It also reveals the websites that either aren't affected by the bug, or have updated their certificates

The heartbleed bug lets hackers eavesdrop on supposedly secure communications.

It was found by uncovered by a team of researchers from Google Security and Codenomicon in the OpenSSL cryptographic software.

OpenSSL is open-source software that is widely used to encrypt web communications.

It is used to protect websites, instant messaging, email servers, virtual private networks and other communications.

OpenSSL certificates are also used to protect credit card details on select services.

The software is used in two of the most widely used Web servers, Apache and nginx.

Research by analytics firm Netcraft found almost 500,000 websites could be affected.

In theory, if the site is vulnerable, 
any data that has been stored on it since 2011 - when the flaw is 
thought to have originated - could be at risk.

The tool also reveals the websites that either aren’t affected by the bug, or have updated their certificates.

Experts are advising people to change
 their passwords, but if a website is still vulnerable, the information 
may still be at risk.

Changing passwords will work on sites that have been updated, and if your details were stolen before the flaw was identified.

It's good practice to change passwords following a vulnerability either way, though.

The heartbleed bug lets hackers eavesdrop on supposedly secure communications.

It was uncovered by a team of researchers from Google Security and Codenomicon in the OpenSSL cryptographic software.

The software offers encryption services, such as when people log into internet banking, or into a webmail service like Yahoo.

The fault lets a hacker craft an attack which, under the right 
conditions, will return small chunks of information from the 
remote system or service.

For example, it has been demonstrated that hackers can steal other users’ usernames and passwords from Yahoo - although this flaw has now been fixed.

OpenSSL is open-source software that is widely used to encrypt web communications. According to the tool, pictured, Bing.com doesn't use OpenSSL so is not at risk

Instagram runs on the nginx server, which uses OpenSSL software, and its SSL certificate was last valid three years ago. LastPass has flagged it as a potential risk, pictured. The tool is a guide to affected services; it is not a definitive list

It is used to protect websites, 
instant messaging, email servers, virtual private networks and other 
communications from hackers.

The
 software is used in two of the most widely used web servers, including 
Apache and nginx, and is said to be used in one way or another by 
roughly two-thirds
 of all websites.

According to the tool, Bing.com doesn’t use OpenSSL so is not at risk.

The server details of Facebook and Twitter aren't reported, so LastPass was unable to confirm if they use OpenSSL.

However, it warns neither sites' SSL certificate has been updated since the flaw was identified.

Yahoo.com, which was confirmed as vulnerable by developers yesterday, has since updated its SSL certificate and is listed as secure again.

Instagram runs on the nginx server, which uses OpenSSL software, and its SSL certificate was last valid three years ago meaning LastPass has flagged it as a potential risk.

The tool is a guide to affected services; it is not a definitive list.

The bug means hackers can eavesdrop and leave no trace in server logs. The flaw was introduced in OpenSSL in December 2011, and was 'in the wild' until Monday, when a new version fixing the flaw was released

The flaw was introduced in OpenSSL in December 2011, and was 'in the wild' until Monday, when a new version fixing the flaw was released.Experts have confirmed the flaw is real.

'We were able to scrape a Yahoo username & password via the Heartbleed bug,' tweeted Ronald Prins of security firm Fox-IT, showing a censored example. 

Research by analytics firm Netcraft found almost 500,000 websites could be affected.

'The serious overrun vulnerability in the OpenSSL cryptographic library affects around 17 per cent of SSL web servers,' it said.

The
 Heartbleed bug lets anyone on the web read the memory of the 
systems protected by vulnerable versions of the OpenSSL software.

It compromises secret keys used to identify the service providers and 
to encrypt web traffic.

This includes the names and passwords of the users and the 
actual content, such as credit card numbers.

Attackers can 'eavesdrop' on communications between servers, steal data directly 
from the them, and use the information to impersonate services and users on other sites or platforms.

James Lyne, global head of research at security firm Sophos told MailOnline: 'This fault undermines the fundamental trust on the internet for anyone running the vulnerable software and it is widely 
integrated into the technology we all use every day.

'While the fault has now been fixed, providers must apply it manually, so many still are vulnerable.

'Worse still, the defect was in the code for over two years before being discovered by security researchers - attackers could have discovered this at any time during that period and retrieved large volumes of data without anyone knowing.

'At this point the best thing for consumers to do is to assume their passwords and alike have been leaked. They may not have been, but since it's very hard to actually tell retrospectively, it is better to be safe than sorry.

'As providers rush to patch [the flaw], consumers should apply typical IT security best practice: ensure you change passwords - once you know the issue has been fixed by your provider; update your computers; and don't use the same password across multiple sites or services.

'This is not the first defect of its kind and it certainly won't be the last, but it is one of the more serious faults we've seen in recent Internet history.'

'The heartbleed bug allows anyone on the internet to read the memory of the systems protected by the vulnerable versions of the OpenSSL software,' according to a website the researchers who found the flaw set up to explain their find.

'This compromises the secret keys used to identify the service providers and to encrypt the traffic, the names and passwords of the users and the actual content.

'This allows attackers to eavesdrop communications, steal data directly from the services and users and to impersonate services and users.'

Experts say the bug could leave up to 66% of sites vulnerable to hackers if their encryption software is not updated. It compromises secret keys used to identify the service providers and to encrypt web traffic. This includes the names and passwords of the users and actual content, such as credit card numbers

'This bug has left large amount of private keys and other secrets exposed to the Internet," they warned.

'Considering the long exposure, ease of exploitation and attacks leaving no trace this exposure should be taken seriously.'

Daniel Foster of hosting firm 34SP.com warned firms with eCommerce capabilities to be extra cautious.

'With potentially all web users affected by the recent ‘heartbleed’ security bug that has hit OpenSSL software, which is the software that protects credit card transactions - it is important that eCommerce businesses contact their web hosting providers to check that they have taken necessary actions to avoid their customers being affected by spying and eavesdropping,' he said.

@highlight

Around two-thirds of websites are vulnerable to ‘heartbleed hackers’

@highlight

Password expert has created a tool to see which sites are affected

@highlight

LastPass’ Heartbleed Checker looks to see when a site’s secure encryption certificate was last updated and warns if the server may be at risk

@highlight

The problem was found in the widely-used OpenSSL software

@highlight

Experts are urging server owners to upgrade to the latest version

@highlight

Flaw lets hackers eavesdrop on communications and steal encryption keys