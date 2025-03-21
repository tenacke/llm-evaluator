Security experts recently revealed a massive security flaw that could let hackers listen in on private calls and read text messages on mobile networks. 

One way in which such hackers - as well as some intelligence agencies - get access to such information is by using International Mobile Subscriber Identity (IMSI) catchers, or 'stingrays'.

These controversial tracking devices trick mobiles into connecting with them, and now developers have created an app that claims to detect such gadgets, and warn users if their data is at risk.  

An app called SnoopSnitch (homescreen pictured left) claims to detect IMSI catchers (right) - eavesdropping devices used for intercepting mobile phone traffic and tracking the movement of smartphone users - and warn smartphone users if their devices are giving up their personal information and connecting to them

Called SnoopSnitch, the app scans for signals that indicate a switch from a legitimate tower to a 'stingray', where information may be being collected.

IMSI catchers - eavesdropping devices used for intercepting mobile phone traffic and tracking the movement of smartphone users - are controversial because they act like ‘fake’ mobile towers.

IMSI catchers are known as 'stingrays' and are eavesdropping devices for intercepting mobile phone traffic and tracking the movement of mobile phone users.

A 'fake' mobile tower acts between the target smartphone and service provider's real towers.

In this way, it is considered a 'man-in-the-middle attack' and can be detected by the app.

Catchers work by exploiting a security hole. 

The GSM specification - the default global standard for mobile communications - requires a smartphone to authenticate to the network, but doesn't require the network to make itself known to the handset.

The IMSI catcher masquerades as a base station and logs IMSI numbers of all the mobile stations in the area, as they attempt to attach to the IMSI-catcher.

It forces mobile phones connecting to it to use no call encryption, or to use breakable encryption, making call data easy to intercept and convert to audio.

They sit between a real phone and telecom tower to launch a man-in-the-middle attack and intercept data.

Once a phone has connected to a stingray, it makes it easy for a hacker to intercept and convert data to audio, enabling experts to listen to people's phonecalls.

While experts may be using the techonology to target specific handsets of suspected criminals, it is almost impossible to avoid capturing data from other 'innocent' smartphones in the process, too. 

As a result, the use of stingrays has been banned in certain countries and US states such as Florida, for example. 

Reacting to public privacy concerns, security  researchers Alex Senier, Karsten Nohl, and Tobias Engel from SRLabs in Berlin created the SnoopSnitch Android app. 

They presented the findings at the Chaos Computer Congress’ annual meeting in Hamburg. 

The free Android app’s Google Play listing reads: ‘SnoopSnitch collects and analyses mobile radio data to make you aware of your mobile network security and to warn you about threats like fake base stations (IMSI catchers), user tracking, and SS7 attacks.’ 

Mr Nohl told Motherboard that the app gathers information from the stingray, which is used to analyse if one is in close proximity. 

It is rumoured that some law enforcement agencies across the globe and using the technology to collect information. This map produced using SnoopSnitch data so far, shows  network security in Europe. There is not enough US data collected to make a map yet

A massive security flaw that could let hackers listen in on private calls and read text messages was revealed last month.

The flaw, is in a global telecom network called Signal System 7 (SS7).

SS7 helps phone carriers across the world, including AT&T and Verizon, route calls and texts. 

Although the extent of the flaws was not revealed, it is believed hackers can locate callers anywhere in the world, listen to calls as they happen or record hundreds of encrypted calls and texts at a time for later decryption.

‘The phone receives information that's useful for the attacker, but it's also useful for the defender,’ he said.

‘There's no one set of information, taken by itself, that allows you to detect an IMSI catcher, but we do stream analysis of everything that happens on your phone, and can come out with a warning if it crosses a certain threshold.’

Crucially, the app can’t prevent a smartphone from connecting to stingrays, but lets a user known there is surveillance in a certain area.

The app currently only works with rooted Android handsets that have Qualcomm chips inside, such as Sony and Samsung Galaxy models.

Rooted smartphones are ones where the owner can access system files and change features that they can usually only read.

But the app creators are working out how to extract information needed by the app to detect stingrays, in other ways.

 

 

 

@highlight

SnoopSnitch app claims to detect so-called IMSI catchers or 'stingrays'

@highlight

These devices trick phones into connecting to them, before accessing data

@highlight

They are controversial and are rumoured to be used in the US and UK

@highlight

App scans for signals that indicate a switch from a legitimate tower to a 'stingray', where information may be being collected

@highlight

SnoopSnitch currently only works with rooted Android handsets that have Qualcomm chips inside, but its makers are developing more options