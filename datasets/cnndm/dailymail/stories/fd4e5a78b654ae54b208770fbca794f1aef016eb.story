By
Sarah Griffiths for MailOnline

Smartphone users are increasingly aware of the need to take precautions to protect their personal data.

But now a team of researchers have identified a new weakness in Android, Windows and iOS mobile operating systems that could be used to steal personal information from unsuspecting users.

Experts found the method was successful 92 per cent of the time when they tried to hack Gmail accounts and said that other apps were also easily accessible using the new technique.

Scroll down for video 

A team of researchers have identified a new weakness in Android, Windows and iOS mobile operating systems. They found that their method was successful 92 per cent of the time when they tried to hack Gmail accounts (stock image) and said that other apps were also easily accessible

Scientists at the University of California, Riverside Bourns College of Engineering and the University of Michigan demonstrated the hack in an Android phone.

They found it was successful between 82 per cent and 92 per cent of the time on six of the seven popular apps they tested, including Gmail, Chase Bank and H&R Block - a tax filing app.

Amazon was the only app they tested that was difficult to penetrate, with just a 48 per cent success rate.

The experts predicted there was a security risk with so many apps running on the same shared operating system, which gave them the idea of pinpointing the vulnerability.

‘The assumption has always been that these apps can't interfere with each other easily,’ said Zhiyun Qian, of the Computer Science and Engineering Department at UC Riverside.

‘We show that assumption is not correct and one app can in fact significantly impact another and result in harmful consequences for the user.’

The hack works by accidentally downloading a malicious app, which gives a hacker access to a newly-discovered public side channel - numbers describing the shared memory of a process, which can accessed without asking a smartphone user’s permission. This shared memory is a common operating system feature in Windows, Android (pictured left) and iOS (right) operating systems

The computer scientists found their hacking technique was successful between 82 per cent and 92 per cent of the time on six of the seven popular apps they tested. These included:

Gmail - 92 per cent

H&R Block - 92 per cent

Newegg - 86 per cent

WebMD - 85 per cent

Chase Bank - 83 per cent

Hotels.com - 83 per cent

Amazon - 48 per cent

Researchers hacked into apps by getting a mobile user to download a seemingly benign - but in fact malicious - app such as one for background wallpaper on a phone.

Once it was installed, the experts could exploit a newly discovered 'public side channel' containing a shared memory of processes, which can be accessed without asking a smartphone user’s permission.

They said that shared memory is a common operating system feature, which efficiently allows processes to share data.

While they only used it to exploit the Android system, the experts believe the method would work on Apple and Windows operating systems too.

The experts monitored changes in the shared memory and linked them to users’ actions such as logging into Gmail or taking a picture of a cheque they wanted to deposit via the Chase Bank app.

They showed that it is possible to track which apps people are using in real time.

To keep smartphones as secure as possible, Dr Qian advises users not to install untrusted apps, which could give hackers (illustrated with a stock image) access. He said that in the future, side channels should be eliminated or more carefully regulated within operating systems

In order to launch an attack, they started the hack at the precise moment the user logged into an app or took a photo and they did this inconspicuously by calculating the timing.

‘By design, Android allows apps to be pre-empted or hijacked,’ Dr Qian said.

‘But the thing is, you have to do it at the right time so the user doesn't notice. We do that and that's what makes our attack unique.’

He explained that Amazon’s app was more difficult to attack because it allows one activity to lead to almost any other activity, which increases the difficulty of guessing which activity someone will conduct next.

To keep smartphones as secure as possible, Dr Qian advised users not to install untrusted apps.

He said that side channels should be eliminated or more carefully regulated and operating systems more carefully designed to enable them to be easy to use, but also secure.

MailOnline has contacted Google for comment.

@highlight

Researchers at the University of California, Riverside Bourns College of Engineering and the University of Michigan identified a new weakness

@highlight

Vulnerability affects Windows, iOS and Android operating systems

@highlight

Method was 92% successful in hacking Gmail accounts, in the scenario

@highlight

They exploited a newly discovered public side channel – which details shared memory used to make apps work efficiently - and is easily accessible 

@highlight

The attack relied on 'users' downloading a malicious app and the hackers timing their attacks precisely to correspond to useful actions