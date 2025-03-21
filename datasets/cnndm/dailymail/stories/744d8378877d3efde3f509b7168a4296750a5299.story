By
Victoria Woollaston

A bug that leaves email attachments vulnerable to attack has been spotted on Apple’s iOS 7 software. 

The flaw was discovered by a security expert in Germany and it causes attachments to be sent unencrypted, even if the operating system’s data protection feature is enabled. 

Apple has acknowledged the bug and said it is working on a fix, but did not reveal how long the bug had been active or when the fix would be issued.

Scroll down for video

The bug was discovered by a security expert in Germany.  It causes attachments to be sent unencrypted via the Mail app on iOS 7 devices, pictured. It occurs even if iOS 7's Data Protection feature is enabled. Apple has acknowledged the bug and said it is working on a fix

Data protection is available for devices that offer hardware encryption, including iPhone 3GS and later, all iPad models, as well as the iPod touch from the 3rd generation.

The feature was designed to enhance the built-in hardware encryption by protecting the encryption keys with a user’s passcode. 

According to Apple, this provides an 'additional layer of protection for email messages attachments, and third-party applications'.

To enable data protection, go to Settings, General and Passcode. 

Once a passcode is set, the 'Data protection is enabled' becomes visible. 

Andreas Kurtz, a researcher for NESO Security Labs in Germany, announced the vulnerability on his blog last week.

He wrote: ‘A few weeks ago, I noticed email attachments within the iOS 7 MobileMail.app are not protected by Apple's data protection mechanisms. 

'Clearly, this is contrary to Apple's claims that data protection "provides an additional layer of protection for (..) email messages attachments".'

He said he verified the issued by restoring an iPhone 4 to the most recent iOS versions; iOS 7.1 and 7.1.1, and setting up an IMAP email account to give him test emails and attachments. 

By mounting the iOS data partition to a computer, he was able to find the email folder and see all the attachments without any encryption or restriction.

The flaw was produced on an iPhone 4, 5S, pictured, and iPad 2 running iOS 7.0.4 to 7.1.1. Despite the flaw, experts have stated it is difficult to exploit because the attacker would need access to the device and need to know the passcode

He was also able to reproduce the flaw on an iPhone 5S and an iPad 2 running iOS 7.0.4. 

Kurtz confirmed the data protection feature was enabled elsewhere on the phone by attempting, and failing, to access the Protected Index file, in the email message database.

In a statement, Apple said: 'We're aware of the issue and are working on a fix which we will deliver in a future software update.'

Despite the flaw, experts have stated it is difficult to exploit because the attacker would need access to the device and need to know the passcode.  

@highlight

The bug was discovered by a security expert in Germany

@highlight

It was produced on an iPhone 4, 5S and iPad 2 running iOS 7.0.4 to 7.1.1

@highlight

It causes email attachments to be sent unencrypted on iOS 7 devices

@highlight

This occurs even if iOS 7’s Data Protection feature is enabled

@highlight

Apple has acknowledged the bug and said it is working on a fix