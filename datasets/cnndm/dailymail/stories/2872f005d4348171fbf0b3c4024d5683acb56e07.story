By
Mark Prigg

Researchers have uncovered a series of major security holes in traffic light systems that allowed them to to control 100 signals in Michigan.

Researchers say there were major flaws in the system, which is used in 40 states across America..

They worked with a local road agency to investigate the problems - and say they found a 'systemic lack of security' that allowed them to control lights.

Scroll down for video 

University of Michigan researchers hacked into nearly 100 wirelessly networked traffic lights - and were able to control every light on the system from a single laptop.

Wirelessly networked traffic lights have four key components. 

There are sensors that detect cars, controllers that use the sensor data to control the lights at a given intersection, radios for wireless communication among intersections, and malfunction management units (MMUs), which return lights to safe fallback configurations if an 'invalid' configuration occurs. 

For example, if somehow every light at an intersection is green, the system might fall back to having them all become flashing red lights.  

With permission from a local road agency, the University of Michigan researchers hacked into nearly 100 wirelessly networked traffic lights.

The team say the flaws they uncovered - which included the use of unsecured wireless networks and default passwords were used - are likely to be founds across the country.  

'The vulnerabilities we discover in the infrastructure are not a fault of any one device or design choice, but rather show a systemic lack of security consciousness,' the researchers report in a paper.

After gaining access to one of the controllers in their target network, the researchers were able to turn all lights red or alter the timing of neighboring intersections—for example, to make sure someone hit all green lights on a given route. 

They did not disclose exactly where in Michigan they did the research.

The team, led by University of Michigan computer scientist J. Alex Halderman, said there were three major weaknesses in the traffic light system: unencrypted wireless connections, the use of default usernames and passwords that could be found online, and a debugging port that is easy to attack.

'The safety critical nature of traffic infrastructure requires that it be secure against computer-based attacks, but this is not always the case,' the team said.

'We investigate a networked traffic signal system currently deployed in the United States and discover a number of security flaws that exist due to systemic failures by the designers.

'We leveraged these flaws to create attacks which gain control of the system, and we successfully demonstrate them on the deployment.'  

'The safety critical nature of traffic infrastructure requires that it be secure against computer-based attacks, but this is not always the case,' the team said.

The team called for manufacturers and operators to improve their systems. 

 'Our attacks show that  an adversary can control traffic infrastructure to cause disruption, degrade safety, or gain an unfair advantage.' 

'They need to be worrying about this and think about security - it needs to be one of their top priorities,' Branden Ghena, a graduate student who worked on the project told MIT Technology Review. 

'It's hard to get people to care about these things in the same way that it's hard to get people to change their passwords.'

Researchers said traffic-system administrators should not use default usernames and passwords, and should stop broadcasting communications unencrypted for 'casual observers and curious teenagers' to see.

They also warned that devices like voting machines and even connected cars could suffer similar flaws. 

 

@highlight

Claims of a 'systemic lack of security' in traffic light system

@highlight

Michigan researchers hacked into system used by 40 states

@highlight

Were able to control signals for 100 lights using a standard laptop 

@highlight

Unsecured wireless networks and default passwords were used 