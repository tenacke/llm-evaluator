By
Mark Prigg

A major online security alert has been issued after experts found a bug in one of the web's most common security systems.

Called the 'heartbleed' bug, it allows hackers to eavesdrop on supposedly secure communications.

The vulnerability was found by Google researchers in the OpenSSL cryptographic library, which is believed to be used in some way by roughly two-thirds of all websites on the Internet and is part of the most common server software in use.

Experts say the bug could leave up to 66% of sites vulnerable to hackers if their encryption software is not updated. It compromises secret keys used to identify the service providers and to encrypt web traffic. This includes the names and passwords of the users and actual content, such as credit card numbers

OpenSSL is open-source software that is widely used to encrypt web communications.

It is used to protect websites, instant messaging, email servers, virtual private networks and other communications.

It is used in two of the most widely used Web servers, Apache and nginx.

It is claimed heartbleed can reveal the contents of a server's memory, where the most sensitive of data is stored, including private data such as usernames, passwords, and credit card numbers.

The flaw also allows an attacker can get copies of a server's digital keys, which can be used to impersonate servers or to decrypt communications from the past or potentially the future, too.

The flaw was introduced in OpenSSL in December 2011, and was been 'in the wild' until yesterday, when a new version fixing the flaw was released.

Experts have confirmed the flaw is real.

'We were able to scrape a Yahoo username & password via the Heartbleed bug,' tweeted Ronald Prins of security firm Fox-IT, showing a censored example.

Developer Scott Galloway, 'Ok, ran my heartbleed script for 5 minutes, now have a list of 200 usernames and passwords for yahoo mail...TRIVIAL!'

The problem was uncovered by a team of researchers from Google Security and Codenomicon.

Research by analytics firm Netcraft says almost 500,000 websites could be affected.

'The serious overrun vulnerability in the OpenSSL cryptographic library affects around 17% of SSL web servers,' it says.

Its research found Twitter, GitHub, Yahoo, Tumblr, Steam, Flickr, HypoVereinsbank, PostFinance, Regents Bank, Commonwealth Bank of Australia, and the anonymous search engine DuckDuckGo are all affected.

The bug means hackers can eavesdrop and leave no trace in server logs. The flaw was introduced in OpenSSL in December 2011, and was 'in the wild' until Monday, when a new version fixing the flaw was released

Researchers have even given the bug its own logo

'The heartbleed bug allows anyone on the internet to read the memory of the systems protected by the vulnerable versions of the OpenSSL software,' according to a website the researchers who found the flaw set up to explain their find.

'This compromises the secret keys used to identify the service providers and to encrypt the traffic, the names and passwords of the users and the actual content.

'This allows attackers to eavesdrop communications, steal data directly from the services and users and to impersonate services and users.'

The vulnerability has been dubbed the Heartbleed Bug because it was discovered 'in the OpenSSL's implementation of the TLS/DTLS (transport layer security protocols) heartbeat extension (RFC6520),' the team said.

'This bug has left large amount of private keys and other secrets exposed to the Internet," they warned.

'Considering the long exposure, ease of exploitation and attacks leaving no trace this exposure should be taken seriously.'

The Heartbleed bug allows anyone on the Internet to read the memory of the systems protected by the vulnerable versions of the OpenSSL software.

This compromises the secret keys used to identify the service providers and to encrypt the traffic, the names and passwords of the users and the actual content.

This allows attackers to eavesdrop on communications, steal data directly from the services and users and to impersonate services and users.

Daniel Foster of hosting firm 34SP.com warned firms with eCommerce capabilities to be extra cautious.

'With potentially all web users affected by the recent ‘heartbleed’ security bug that has hit OpenSSL software, which is the software that protects credit card transactions - it is important that eCommerce businesses contact their web hosting providers to check that they have taken necessary actions to avoid their customers being affected by spying and eavesdropping,' he said.

@highlight

Experts urged server owners to upgrade to latest version of OpenSSL software

@highlight

Flaw allows hackers to eavesdrop on communications and steal encryption keys

@highlight

Believed over 66% of web sites could be affected - and experts say all web users will be at risk in some way

@highlight

Servers believed to be affected include those run by Twitter, Yahoo and Tumblr