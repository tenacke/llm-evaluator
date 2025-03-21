A security bug in the widely-used software used to secure the internet has been discovered by three Google researchers.

The flaw, dubbed 'Poodle', could allow hackers to gain access to information that should be encrypted in plain text allowing them to takeover accounts for email, banking and other services.

Makers of web browsers and server software yesterday asked users to disable use of the source of the bug: an 18-year old encryption protocol known as SSL 3.0.

Scroll down for video 

A security bug in the widely-used software used to secure the web has been discovered by three Google researchers. The flaw, dubbed 'Poodle', could be allow hackers to gain access to information that is meant to be encrypted in plain text allowing them to takeover accounts for email, banking and other services

The discovery of 'Poodle' - which stands for Padding Oracle
On Downloaded Legacy Encryption - is the third time this year that researchers have
uncovered a vulnerability in popular web technology.

It follows the discovery of April's 'Heartbleed' bug in OpenSSL and last month's
'Shellshock' bug in a piece of Unix software known as Bash.

Security experts said that hackers could steal browser
'cookies' in Poodle attacks, potentially taking control of
email, banking and social networking accounts.

Even so, experts
said the threat was not as serious as the two prior bugs, and that so far, no one has made use of the vulnerability to hack an account. 

Security experts said that hackers could steal browser'cookies' in 'Poodle' attacks, potentially taking control of email, banking and social networking accounts

'If Shellshock and Heartbleed were Threat Level 10, then
Poodle is more like a 5 or a 6,' said Tal Klein, vice president
with cloud security firm Adallom.

The threat was disclosed in a research paper published on
the website of the OpenSSL Project, which develops the most
widely used type of SSL encryption software.

SSL 3.0, in which the software is found, is currently used by Internet Explorer (IE) 6. 

Some other browsers all still l support SSL 3.0 as an option, so they may also be at risk.

To prevent a Poodle attack on Firefox, open about.config, search for 'security.enable,' and set 'security.enable_ssl3' to 'false', advises Steven Vaughan-Nichols writing in ZDNet. 

To stop an attack on Internet Explorer, go to the tools menu, click internet options, and then click on the Advanced tab.

Under the Advanced tab, look for the Security heading, and make sure that the SSL 3.0 check box is unchecked.

If you're running a web server, check with your code provider in the case of open-source programs, for how to turn SSL 3.0 support off.

Sergey Lozhkin, Security Expert at Kaspersky Lab has advised people to take the following steps to avoid possible incidents:

1. Do not use public Wi-Fi hotspots if you’re sending valuable information such as online banking, accessing social networks via browser. This is always a risk, but the Poodle vulnerability makes it even more dangerous.

2. Disable SSL v3 and all previous versions of the protocol in your browser settings. SSL v3 is 15 years old now and has been superseded by the more up-to-date and widely supported TSL protocol, supported by most modern web browsers.

 The TSL protocol is not affected by the Poodle vulnerability. However, keep in mind that disabling SSL v3 could cause compatibility problems, so be careful before implementing this measure. 

Rumours of a bug in SSL software had been circulating in
recent days, prompting some security professionals to prepare
for a major new threat this week.

Ivan Ristic, director of application security research with
Qualys, said 'Poodle' was not as serious as the previous threats
because the attack was 'quite complicated,' requiring hackers to
have privileged access to networks.

Jeff Moss, a cyber adviser to the U.S. Department of
Homeland Security, added attackers would need to launch a
'man-in-the-middle' attack.

This would involve placing themselves between victims
and websites using approaches such as creating rogue WiFi
'hotspots' in Internet cafes.

Google suggested a technical workaround to secure web
servers, but added on its blog that it hopes to eventually
remove support for SSL 3.0 from all client software.

Mozilla plans to disable SSL 3.0 by default in the next
version of its Firefox browser, to be released on November 25. 

SSL 3.0, in which the software is found, is currently used by Internet Explorer (IE) 6 (right).  'If Shellshock and Heartbleed (left) were Threat Level 10, thenPoodle is more like a 5 or a 6,' said Tal Klein, vice president with cloud security firm Adallom

'SSL version 3.0 is no longer secure,' Mozilla said on its
blog. 'Browsers and websites need to turn off SSLv3 and use more
modern security protocols as soon as possible.'

Microsoft Corp issued an advisory suggesting that
customers disable SSL 3.0 on Windows for servers and PCs.

Representatives with Apple could not be
reached and an Oracle spokeswoman had no immediate
comment.

Matthew Green, an assistant research professor of computer
science at Johns Hopkins University said that disabling SSL 3.0
can be difficult for some computer users.

'It's not going to take out the infrastructure of the internet. But it's going to be a hassle to fix,' Professor Green said. 

@highlight

Poodle allows hackers to see data meant to be encrypted in plain text

@highlight

This could allow access to accounts for email, banks and other services

@highlight

Source of flaw is a widely-used, outdated encryption protocol, SSL 3.0

@highlight

So far, no one has used the Poodle bug in SSL 3.0 to hack an account

@highlight

Web users can opt switch to using a browser that doesn't use SSL 3.0 

@highlight

'If Shellshock and Heartbleed were Threat Level 10, thenPoodle is more like a 5 or a 6,' said Tal Klein, vice president with cloud security firm Adallom 