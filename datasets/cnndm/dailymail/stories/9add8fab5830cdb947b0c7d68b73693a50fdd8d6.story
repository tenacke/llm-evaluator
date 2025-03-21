When your computer performs a spell check, opens a program or even just types a letter, it emits a tiny, imperceptible signal.

At least, it was thought to be imperceptible - but researchers say a new breed of hackers could 'listen' to these signals and find out what your computer is doing.

And now they are trying to devise methods to keep your computer safe from hackers employing this discreet technique.

Scroll down for video 

Georgia Institute of Technology researchers have revealed a new hacking method. They say hackers can 'listen in' to signals emitted by laptops and phones (stock image shown). This means, even when offline, they could find out what you are doing. It is very hard to track because the spying is 'silent'

The researchers at the Georgia Institute of Technology are investigating where these information 'leaks' originate so they can help hardware and software designers develop strategies to plug them.

Studying emissions from multiple computers, they have found a way to measure the strength of the leaks - known technically as 'side-channel signals' - and prioritise security efforts.

Worryingly, the signals don't even require your computer to be online - simply being active is enough for a hacker to listen in to what you are up to.

'People are focused on security for the internet and on the wireless communication side, but we are concerned with what can be learned from your computer without it intentionally sending anything,' said Dr Alenka Zajic, an assistant professor in Georgia Tech's School of Electrical and Computer Engineering.

In separate research, security experts recently revealed a massive security flaw that could let hackers listen in on private calls and read text messages on mobile networks.

One way in which such hackers - as well as some intelligence agencies - get access to such information is by using International Mobile Subscriber Identity (IMSI) catchers, or 'stingrays'.

These controversial tracking devices trick mobiles into connecting with them, and now developers have created an app that claims to detect such gadgets, and warn users if their data is at risk.

IMSI catchers - eavesdropping devices used for intercepting mobile phone traffic and tracking the movement of smartphone users - are controversial because they act like ‘fake’ mobile towers. 

Called SnoopSnitch, the app scans for signals that indicate a switch from a legitimate tower to such fake towers, called 'stingray', where information may be being collected.

'Even if you have the internet connection disabled, you are still emanating information that somebody could use to attack your computer or smartphone.'

Side-channel emissions can be measured several feet away from an operating computer using a variety of spying methods.

Electromagnetic emissions can be received using antennas hidden in a briefcase, for instance.

Acoustic emissions - sounds produced by electronic components such as capacitors - can be picked up by microphones hidden beneath tables.

Information on power fluctuations, which can help hackers determine what the computer is doing, can be measured by fake battery chargers plugged into power outlets adjacent to a laptop's power converter.

Some signals can be picked up by a simple AM/FM radio, while others require more sophisticated spectrum analysers.

And computer components such as voltage regulators produce emissions that can carry signals produced elsewhere in the laptop.

Because the spying is passive and emits no signals itself, users of computers and smartphones wouldn't know they're being watched.

'If somebody is putting strange objects near your computer, you certainly should beware,' said Dr Zajic. 'But from the user's perspective, there is not much they can do right now.

'Based on our research, we hope to develop something like virus scan software that will look for vulnerability in the code and tell developers what they should update to reduce this vulnerability.'

According to the researchers, different tasks carried out by a laptop or smarphone produces a signal of different intensity. Pictured is a still from their video showing the signal from a laptop. They say devices will need specialist software in order to patch up the vulnerability

As a demonstration, Dr Zajic typed a simulated password on one laptop that was not connected to the internet.

On the other side of a wall, a colleague using another disconnected laptop read the password as it was being typed by intercepting side-channel signals produced by the first laptop's keyboard software, which had been modified to make the characters easier to identify.

'There is nothing added in the code to raise suspicion,' said Dr Milos Prvulovic, an associate professor in the Georgia Tech School of Computer Science.

'It looks like a correct, but not terribly efficient version of normal keyboard driver software. And in several applications, such as normal spell-checking, grammar-checking and display-updating, the existing software is sufficient for a successful attack.'

Currently, there has been no mention in open literature of hackers using side-channel attacks, but the researchers believe it's only a matter of time before that happens.

The potential risks of side-channel emissions have been reported over the years, but not at the level of detail being studied by the Georgia Tech researchers.

'Of course, it's possible that somebody is using it right now, but they are not sharing that information,' Dr Zajic noted.

The signals are produced from the hardware of the computer (shown) when it performs a task. Currently, there has been no mention in open literature of hackers using side-channel attacks, but the researchers believe it's only a matter of time before that happens

To counter the threat, the researchers are determining where the leaks originate.

'We are trying to understand why these side channels exist and what can be done to fix these leaks,' said Dr Zajic.

'We are measuring computers and smartphones to identify the parts of the devices that leak the most. That information can guide efforts to redesign them, and on an architectural level, perhaps change the instructions in the software to change the device behavior.'

Each computer operation has a different potential for leaking information. 

The processor draws different amounts of current depending on the operation, creating fluctuations that can be measured.

Saving data to memory also requires a large amount of current, creating a 'loud' operation.

People in coffee shops could be at particularly risk (stock image shown), as in a public space hackers could more easily listen in to the signals from their laptop. 'If somebody is putting strange objects near your computer, you certainly should beware,' said Dr Zajic

'When you are executing instructions in the processor, you generate a different type of waveform than if you are doing things in memory,' explained Dr Zajic.

'And there is interaction between the two.'

To measure the vulnerability, Dr Zajic, Dr Prvulovic and graduate student Robert Callen developed a metric known as 'signal available to attacker' (Savat), which is a measure of the strength of the signal emitted.

They measured the level of Savat for 11 different instructions executed on three different laptops, and found the largest signals when the processors accessed off-chip memory.

'It is not really possible to eliminate all side-channel signals,' said Dr Prvulovic.

'The trick is to make those signals weak, so potential attackers would have to be closer, use larger antennas and utilise time-consuming signal analyses.

'We have found that some operations are much "louder" than others, so quieting them would make it more difficult for attackers.'

The researchers are also now studying smartphones, whose compact design and large differential between idle and in-use power may make them more vulnerable.

@highlight

Georgia Institute of Technology researchers reveal new hacking method

@highlight

They say hackers can 'listen in' to signals emitted by laptops and phones

@highlight

This means, even when offline, they could find out what you are doing

@highlight

It is very hard to track because the spying is 'silent'

@highlight

However, they say developers can create software to patch up the vulnerability in devices