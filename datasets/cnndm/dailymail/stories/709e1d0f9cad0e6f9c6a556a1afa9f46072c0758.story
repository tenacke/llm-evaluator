Security experts have revealed a major flaw in dating app Tinder's security that could allow a someone to pinpoint the exact location of a user.

The flaw was discovered in October, when security firm IncludeSec first told Tinder of the bug.

However, they waited until now - when the flaw was fixed - to go public because of the huge security risk it posed.

Scroll down for video

The flaw revealed the exact location of any Tinder user in code sent from the app to servers. It would allow hackers to easily triangulate where a user was.

The team found the Tinder app revealed the exact distance from the match in code sent to its sever.

By intercepting this, it was possible to find the exact distance from the user.

By creating three fake accounts and locations and looking at the target user, they could triangulate the exact location of the user.

'Being a dating app, it's important that Tinder shows you attractive singles in your area,' said Max Veytsman of IncludeSec, which uncovered the flaw.

'To that end, Tinder tells you how far away potential matches are.'

The firm said that in July 2013 it found Tinder was actually sending latitude and longitude co-ordinates of potential matches to the iOS client.

'Anyone with rudimentary programming skills could query the Tinder API directly and pull down the co-ordinates of any user. '

However, the firm said Tinder soon fixed the bug - but introduced a new bug as they did.

'By proxying iPhone requests, it's possible to get a picture of the API the Tinder app uses.

'Of interest to us today is the user endpoint, which returns details about a user by id.

The researchers even created a private web app called Tinder finder to show off their discovery - but did not reveal until the flaw was fixed

One of the fake profiles created by the researchers - using their flaw, they were able to pinpoint the user exactly

'This is called by the client for your potential matches as you swipe through pictures in the app.'

The team found the API revealed the exact distance from the match.

By creating three fake accounts and locations, they could triangulate the exact location of the user.

The team even built a special site to show exactly where a user was, automating the entire process.

'I can create a profile on Tinder, use the API to tell Tinder that I'm at some arbitrary location, and query the API to find a distance to a user.

'When I know the city my target lives in, I create 3 fake accounts on Tinder.

'I then tell the Tinder API that I am at three locations around where I guess my target is.

'Then I can plug the distances into the formula on this Wikipedia page.'

The firm stressed the app was never made available, and that the flaw had now been fixed  by tinder - even though it was first reported in October last year.

'This is a serious vulnerability, and we in no way want to help people invade the privacy of others.'

By setting up three accounts and looking at the same user, the hackers could triangulate their exact location

'At IncludeSec we specialize in application security assessment for our clients, that means taking applications apart and finding really crazy vulnerabilities before other hackers do. 

'The API calls used in this proof of concept demonstration are not special in any way, they do not attack Tinder's servers and they use data which the Tinder web services exports intentionally.

'There is no simple way to determine if this attack was used against a specific Tinder user.'

Sean Rad, Tinder's cofounder and CEO, told MailOnline: 'Include Security identified a technical exploit that theoretically could have led to the calculation of a user’s last known location.

'Shortly after being contacted, Tinder implemented specific measures to enhance location security and further obscure location data.

'We did not respond to further inquiries about the specific security remedies and enhancements taken as we typically do not share the specifics of Tinder's security measures.

'We are not aware of anyone else attempting to use this technique.

'Our users’ privacy and security continue to be our highest priority.

@highlight

App maker was notified of serious privacy flaw in October

@highlight

Code in the app allowed any user to easily triangulate a users exact location

@highlight

Tinder says exploit was 'theoretical'