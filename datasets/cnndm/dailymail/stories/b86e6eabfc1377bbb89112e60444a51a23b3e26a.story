By
Victoria Woollaston

PUBLISHED:
  
  
      03:39 EST, 13 December 2013
    
  
 | 
  UPDATED:
  
  
      04:38 EST, 13 December 2013

Most of us have old tech gadgets lying around gathering dust, but one engineer has decided to put his to good use.

Jeff Keacher from Colorado successfully managed to wire up a 27-year-old Mac Plus - an early version of the Apple Mac computer - to the web using a Raspberry Pi and proxy server.

This is particularly impressive because the computer was built in 1986 - five years before the first web servers were switched on and the world wide web officially launched - and it is said to be '200,000 times slower' than modern-day desktop PCs.

Scroll down for video

Engineer Jeff Keacher from Colorado used an early web browser called MacWeb 2.0 to run basic versions of Wikipedia and Hacker News on his 1986 Mac Plus, pictured. Pages took 'minutes' to load, but Keacher was able to access the sites through a proxy server

Manufactured in 1986

4MB RAM and 8MHz MC68000 CPU

100MB Zip disk

50MB hard drive

512 x 384 pixel black-and-white screen

System 7.0

MacWeb v2.0 browser (1994)

This means it didn’t have a web browser, couldn’t read web addresses and didn’t even have an Ethernet port in order to connect it to Keacher’s router.

The full process of how Keacher managed to connect his now antique hardware is available on his blog.

He began by installing a version of MacWeb 2.0 - an early version of the Mac web browser that runs on the Mac System 7 operating system. 

To connect the computer to the router, 
without an Ethernet port, Keacher used a series of old adapters to to connect a Raspberry Pi to the Mac Plus. He then 
connected the Pi to the router.

To connect to his home network, Keacher had to wire up his computer to a Raspberry Pi, pictured, and then connect the Pi to his router. This was necessary because the Mac Plus is so old it doesn't have an Ethernet port, so couldn't connect to the router directly

MacWeb 2.0 is not capable of reading web addresses and serving links and pages in the same way as modern-day browsers because it doesn’t recognise computer languages such as Javascript or CSS.

Instead, Keacher recruited a friend to write a proxy program that took the URL of websites, removed all modern-day computer language, cookies and images and turned the sites into basic text versions.

Keacher was then able to read Wikipedia pages and access Hacker News through the retro browser.

On
 his blog, Keacher explained: ‘Yes, in a certain sense, my Mac has 
already been on the internet through dial-up shell sessions.

A Wikipedia page viewed through the MacWeb 2.0 browser. MacWeb 2.0 isn't capable of reading web pages because it doesn't recognise computer languages such as Javascript of CSS. Instead, Keacher used a program that stripped the sites of this computer language and turned them into basic text versions

The Mac Plus was manufactured in 1986. It has 4MB RAM and is powered by an 8MHz MC68000 CPU. The black and white screen has 512 x 384 pixels and it runs on the System 7.0 from 1991. According to Keacher the computer is '200,000 times' slower than modern-day PCs

‘What it never did was run a TCP/IP stack of its own. It was always just a dumb terminal on the ‘net, never a full-fledged member.’

‘Sure, it was slow as hell, but it worked! Data loaded, pages rendered, and links were clickable. Even forms sort of worked.’

Keacher has a Master of Science Degree in Management Science and Engineering from Stanford University. he also holds a Bachelor of Science degree in Electrical Engineering from Rose-Hulman Institute of Technology.

@highlight

Engineer Jeff Keacher wanted to connect his 1986 Mac Plus to the internet

@highlight

He used an early web browser called MacWeb 2.0 to run on the system

@highlight

By connecting a Raspberry Pi to the Mac, he could connect it to a router

@highlight

He then set up a proxy server to run text versions of various websites

@highlight

Although Keacher admitted the pages took 'minutes' to render