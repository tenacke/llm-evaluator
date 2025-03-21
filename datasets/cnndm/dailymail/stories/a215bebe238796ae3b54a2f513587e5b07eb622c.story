By
Mark Prigg

A major security flaw in Google's Play Store that could expose user's private data has been revealed by researchers.

The bug, which the team has worked with Google, Facebook and other app makers to fix before revealing it, put millions of users at risk, the researchers said.

The bug would allow hackers to steal user data from Facebook, Amazon and others using 'secret' keys the team uncovered.

The Columbia Engineering Team found thousands of secret keys in android apps (shown by red arrows) that could be used to steal user data

The researchers created an app called PlayDrone, which used various hacking techniques to circumvent Google security to successfully download Google Play apps and recover their sources.

They were then able to decompile the apps to see their code.

They then found developers often store their secret keys in their apps software, similar to usernames/passwords info, and these can be then used by anyone to maliciously steal user data or resources from service providers such as Amazon and Facebook.

The research was revealed in a a paper presented—and awarded the prestigious Ken Sevcik Outstanding Student Paper Award—at the ACM SIGMETRICS conference.

Jason Nieh, professor of computer science at Columbia Engineering, and PhD candidate Nicolas Viennot said they were stunned by the scale of their find.

'Google Play has more than one million apps and over 50 billion app downloads, but no one reviews what gets put into Google Play—anyone can get a $25 account and upload whatever they want. Very little is known about what’s there at an aggregate level,' says Nieh

'Given the huge popularity of Google Play and the potential risks to millions of users, we thought it was important to take a close look at Google Play content.'

Nieh and Viennot’s paper is the first to make a large-scale measurement of the huge Google Play marketplace.

The researchers created an app called PlayDrone, which used various hacking techniques to circumvent Google security to successfully download Google Play apps and recover their sources.

PlayDrone scales by simply adding more servers and is fast enough to crawl Google Play on a daily basis, downloading more than 1.1 million Android apps and decompiling over 880,000 free applications.

Google Play, the Android app store, has more than one million apps and over 50 billion app downloads

Nieh and Viennot discovered all kinds of new information about the content in Google Play, including a critical security problem: developers often store their secret keys in their apps software, similar to usernames/passwords info, and these can be then used by anyone to maliciously steal user data or resources from service providers such as Amazon and Facebook.

These vulnerabilities can affect users even if they are not actively running the Android apps.

Nieh claims that even “Top Developers,” designated by the Google Play team as the best developers on Google Play, included these vulnerabilities in their apps.

'We’ve been working closely with Google, Amazon, Facebook, and other service providers to identify and notify customers at risk, and make the Google Play store a safer place,' says Viennot.

'Google is now using our techniques to proactively scan apps for these problems to prevent this from happening again in the future.'

In fact, Nieh adds, developers are already receiving notifications from Google to fix their apps and remove the secret keys.

@highlight

Bug put millions of users at risk

@highlight

Team worked with Google, Facebook and others to fix before revealing their work