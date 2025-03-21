By
Ellie Zolfagharifard

A security expert has warned Apple’s iOS software contains potentially sinister tools that could be used by governments to spy on iPhone and iPad users.

Speaking at the 'Hackers on planet Earth' conference in New York, Jonathan Zdziarski said that most users are unaware of the lack of protection for iPhone data.

He added files found hidden within the firm's software contain a file-relay service 
that can be used to access the user's address book, photos, voicemail and any accounts configured on the 
device.

However, Apple has denied the claims the backdoor was created deliberately for government or surveillance purposes. 

A security expert has claimed that Apple's iOS operating system has potentially sinister tools that could be used for government surveillance. Speaking at the 'Hackers on planet Earth' conference in New York, Jonathan Zdziarski said most users are unaware of the lack of protection for iPhone data

His investigation followed earlier reports
 of the NSA spying on Apple products, which suggested a ‘backdoor’ in 
iOS could provide hackers with valuable information.

A backdoor is a hidden remote access port that can allow outside sources to access a device with little detection.

According to a report by Iain Thomson in The Register, iOS devices have data discovery tools that are separate from those used by Apple.

The conclusion was based on an analysis of 600 million iOS devices, with handsets running the most recent versions of the software at particular risk.

Apple and its CEO Tim Cook (right) have previously 
strenuously denied any collusion with the NSA in a backdoor spying 
program aimed at users of iPhones (pictured left). The conclusion was based on an analysis of 600 million iOS devices, with handsets running the most recent versions of the software at particular risk

A backdoor is a hidden remote access from an outside source to the device (stock image pictured) that enables the hacker to have almost full access with little detection

Mr Zdziarski added there is a file dubbed ‘com.apple.pcapd’ on the device that fires up without notifying the iOS device's owner.

What is a 'backdoor'? 

A backdoor is a hidden remote access from an outside source to the device that enables the hacker to have almost full access with little detection. 

Should you be worried if you use an Apple device?

Backdoors are not the type of thing an average hacker can easily exploit. So far there has been no evidence that they've been used for identity theft or a criminal attack

How would could the government potentially make use of these backdoors?

Backdoors can provide access to unencrypted information even if users have chosen to encrypt the data they back up.

Data can include the user's address book, stored photos, the voicemail database and any accounts configured on the device.

What are the main concerns? 

Mr Zdziarski focused on three particular services known by the technical names com.apple.pcapd, com.apple.mobile.file_relay and com.apple.mobile.house_arrest.

How do these hidden files work?

The pcapd service starts a 'packet sniffer' on an iOS device which records all data traffic to and from your iPhone.

It's installed by default on all iOS devices and gives the user no warning when it's activated. 

The file_relay service exists to sweep up large volumes of raw data from particular sources on an iPhone, and then release it in unencrypted form.

These include the address book, accounts, GPS logs, photos, notes, calendar files, call history, voicemail and other records.

The third service, house_arrest, originally allowed iTunes to copy documents to third-party apps. 

Now, as reported in ReadWrite, house_arrest has access to wider app-related data, including photos, databases, screenshots and temporary 'cached' information.

More information about Apple's diagnostic capabilities is available from the firm's support pages.

He explained this can record network traffic and HTTP request/response data from the device and could be targeted via Wi-Fi.

‘This software isn't some legacy code left on the device by Apple engineers for testing - it has been actively updated and expanded in various iOS revisions,’ The Register claimed.

Backdoors are not the type of thing an average hacker can easily exploit, and so far there has been no evidence they've been used for identity theft or a criminal attack 

Apple responded by saying the services identified by Mr Zdziarski are not deliberately provided for government agencies to exploit.

The company added they are for 'diagnostic' purposes, and to allow IT workers to manage their company’s devices.

More information about Apple's diagnostic capabilities is available from the firm's support pages.

‘The problem with this is that these services dish out data (and bypass backup encryption) regardless of whether or not 'Send Diagnostic Data to Apple' is turned on or off, and whether or not the device is managed by an enterprise policy of any kind,’ Mr Zdziarski said on his blog.

‘Every single device has these features enabled and there’s no way to turn them off, nor are users prompted for consent to send this kind of personal data off the device.’

In January, Apple strenuously denied it played any role in the National Security Agency's alleged efforts to hack the iPhone.

Documents published in Germany's Der Spiegel revealed the NSA actively worked on software that enabled it to remotely access iPhones and their text messages, photographs, contacts, location, voice mail and even their video.

The report included an NSA graphic dated 2008 that outlined a system in development called DROPOUTJEEP, described as a 'software implant' that allows infiltrators to push and pull and retrieve data from iPhones such as contact lists.

Der Spiegel referred to it as a 'trojan,' or malware that helps hackers get into protected systems.

The report did not suggest Apple had cooperated with the U.S. spying agency on so-called backdoors.

The Cupertino-based, company said at the time that it had never worked with the NSA to deliberately weaken its products, promising that it would 'defend our customers from security attacks, regardless of who's behind them.'

The investigation followed earlier reports of the NSA (headquarters pictured) spying on Apple products, which suggested a 'backdoor' in iOS could provide hackers with valuable information. Apple said at the time that it had never worked with the NSA to deliberately weaken its products

 

@highlight

A backdoor is a hidden remote access from an outside source to a device

@highlight

Jonathan Zdziarski made claim after reports of NSA spying on Apple

@highlight

He found iOS devices have data tools separate from those used by Apple

@highlight

Tools include a file-relay service that can collect details such as the user's address book, stored photos, voicemail and accounts on the cloud