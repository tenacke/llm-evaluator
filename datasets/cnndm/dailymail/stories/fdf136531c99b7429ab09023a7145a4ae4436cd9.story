Warnings have been issued about a 'catastrophic' security flaw affecting one of the most important interfaces powering the web.

Known as the 'Bash' bug, the flaw could be 'bigger than Heartbleed' which put every computer user at risk earlier this year.

Experts claim the bug may pose a serious threat to computers using Unix-based operating systems including Linux and Apple's Mac OS X - and in turn, could spread to all internet-connected devices.

Errata security researcher Robert Graham tweeted (pictured) an example of how the bug can be exploited, and how code can be added, to websites on Macs running OSX. He warned that Bash is 'probably a bigger deal than Heartbleed' because it could threaten the security of millions of websites

The bug makes all Apple Mac computers, around half of all websites and most internet connected home appliances vulnerable.

The danger is that it can run in the background, without a user ever knowing. And once it does, a hacker will be able to take control of your device.

For instance, the bug could be used to read or send emails, copy banking data, turn on a webcam or listen in on a computer's microphone.

Essentially, this means if your computer will do something without asking for a password, then someone using the bug can also do the same.

Anyone using these devices will need to include a 'patch' update to the software as soon as it is released. As well as computers, the public is being warned they may need to update their internet-connected devices, such as smart locks, separately.  

Bash is the software used to control the command prompt on many Unix computers, and the bug can exploit it to take complete control of a system.

Linux is used in everything from cars to cameras, as well as the Raspberry Pi, and the bug could also affect Android, Windows and IBM machines.

‘The impact is very severe, it’s not overstating it to say it’s a more serious bug than Heartbleed,’ Professor Tim Watson, Director of the Cyber at Warwick University told MailOnline.

‘The primary way this is going to be exploited is through the web… a hacker can use the bug to put malicious things on the website or to steal information, like banking details.’ 

The bug, which also goes by the name 'Shellshock', could potentially allow hackers to gain access to every internet-enabled device in a person's home using something as innocuous as a smart lightbulb.

The danger with this, in particular, is that once it has access to an internet-connected device it can jump onto others. This includes smart locks that open front doors.

Errata security researcher Robert Graham tweeted an example of how the bug can be exploited, and how code can be added, to websites on Macs running OSX.  

By comparison, 'Heartbleed' - dubbed a 'critical security flaw' at the time - only allowed hackers to spy on computers, not take control of them.

Bash stands for Bourne Again Shell. It is what's called a command-line shell that lets users control software programs and features. Commands are sent to these programs by typing text into a particular area of code. This code is typically restricted to programmers, but the Bash bug leaves it open to attack from anyone

Bash does not require users to rush change their passwords, but it does provide another way for hackers to take control of computers and devices.

'The method of exploiting this issue is also far simpler. You can just cut and paste a line of code and get good results,' according to Dan Guido, chief executive of a cybersecurity firm Trail of Bits.

Its potential to disrupt Apple Mac computers, which uses the Bash software, is of particular concern, experts warned.

Bash stands for Bourne Again Shell. It is what's called a command-line shell that lets users control software programs and features. 

Commands are sent to these programs by typing text into a particular area of code. 

This area is typically restricted to programmers and website owners, but the Bash bug leaves it open to attack from anyone.

For example, Mac OS X users can run it by from their Terminal, as can people running devices on the Linux operating system.

Windows is not affected in the same way, but if a hacker exploits malicious code through the flaw, they could gain access to any device, in theory, including PCs. 

The bug is said to have existed for 25 years, and was discovered by Linux expert Stéphane Chazelas. 

As an example, the Apache web server runs Bash in the background to carry out tasks, including processing personal data entered into online form. 

A hacker who exploits Bash could send a request for the information, and then add malicious code to the server to send the user to other sites, or to install a virus on their computer. 

Once the hacker has access, they could launch an attack on every visitor that users the site - and users could be none the wiser.

According to experts, there haven't been any reports of real-word attacks, but that doesn't mean they won't ever be affected, nor does it mean they haven't happened in the past, without being detected. 

Reports are suggesting Apple has patched the flaw that explicitly affects the terminal on its Mac software, but the firm has not officially confirmed this. 

The responsibility to fix the flaw lies with the website owners, meaning everyday users can't do anything to protect themselves. 

Website owners, especially running on Linux-based servers, are being told to check and patch their systems immediately.

The Heartbleed flaw in Open SSL encryption affected millions of sites earlier this year. By comparison, Heartbleed only allowed hackers to spy on computers; not take control of them

The only solution is to update every device that is vulnerable with a patch. And this can only be done by website or server owners. 

Tod Beardsley, an engineering manager at cybersecurity firm Rapid7, warned the bug was rated a '10' for severity, meaning it has maximum impact.

He also rated it 'low' for complexity of exploitation, meaning it is relatively easy for hackers to launch attacks.

'Using this vulnerability, attackers can potentially take over the operating system, access confidential information, make changes, et cetera,' Mr Beardsley said.

'Anybody with systems using Bash needs to deploy the patch immediately.'

‘While antivirus software and firewalls are the basic line of defence for most organisations, they’re not going to be able to stop the attackers getting in this way,’ said Ross Brewer, vice president at Log Rhythm. 

US-CERT advised computer users to obtain operating systems updates from software makers.

It said that Linux providers including Red Hat had already prepared them, but it did not mention an update for OS X. Apple representatives could not be reached.

Tavis Ormandy, a Google security researcher, said via Twitter that the patches seemed 'incomplete.'

However, Mr Ormandy could not be reached to elaborate, but several security experts said a brief technical comment provided on Twitter raised concerns.

The bug could allow hackers to gain access to every internet-enabled device in a person's home.The danger with this is that once it has access to a internet-connected device it can jump onto others in the home. This includes smart locks, such as the August lock (pictured), that open front doors remotely

Unlike Heartbleed, which only affected a specific version of OpenSSL, the Bash bug has been around for a long time.

'That means there are lots of old devices on the network vulnerable to this bug,' said Robert Graham, of security firm Errata.

'The number of systems needing to be patched, but which won't be, is much larger than Heartbleed.'

The Heartbleed bug allowed hackers to spy on millions of computers all over the world.

Bash, however, allows hackers to read information, edit, delete or copy files, and run programmes. All of this can take place without the user knowing.

Unlike Heartbleed, which forced users to change their passwords, Bash doesn't have an easy fix. It will largely be up to system administrators and software companies to issue patches.

'That means some systems could be exploited even though they are patched,' said Chris Wysopal, chief technology officer with security software maker Veracode.

He said corporate security teams had spent the day combing their networks to find vulnerable machines and patch them, and they would likely be taking other precautions to mitigate the potential for attacks in case the patches proved ineffective.

'Everybody is scrambling to patch all of their Internet-facing Linux machines. That is what we did at Veracode today,' he said.

'It could take a long time to get that done for very large organisations with complex networks.'

'Heartbleed,' discovered in April, is a bug in an open-source encryption software called OpenSSL.

The bug put the data of millions of people at risk as OpenSSL is used in about two-thirds of all websites.

It also forced dozens of technology companies to issue security patches for hundreds of products that use OpenSSL.

Bash is a shell, or command prompt software, produced by the non-profit Free Software Foundation. Officials at that group could not be reached for comment.

@highlight

Bug poses a threat to devices using Unix-based operating systems 

@highlight

It includes Linux used in many devices such as cars and cameras

@highlight

It can also affect Android, Windows, IBM and Apple Mac OS X machines

@highlight

Bug, also called 'Shellshock', may let hackers take control of devices

@highlight

Solution is to update every vulnerable device with a software patch 

@highlight

Some patches have already been released, but are still 'incomplete'