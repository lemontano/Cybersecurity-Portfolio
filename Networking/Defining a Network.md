# Defining a Network

Leonardo Montano

![image](https://github.com/user-attachments/assets/3cf8a4c3-2a51-41ef-84fb-b2c6af2a11f7)


Figure 1 Starbuck’s Network Diagram

What goes on when someone is trying to connect to the Wi-Fi? The first
step in the TCP/IP model is the individual trying to attempt to connect
via their internet of things (IOT) device. From there it sends a radio
signal to the Wi-Fi access point. Once that signal is received, the Link
Layer will acknowledge the signal from straight-through processing (STP)
and send it back to the device letting it know it is ready to connect.
The response sent back is a service set identifier (SSID) that will
sometimes include a token of request for a password this will let the
device know what is needed for connection or if on public Wi-Fi accept
terms and conditions. After that is established the network layer will
come into play identifying the IP address then it will start to
transport the data via IPv4 or IPv6 with a TCP/UDP request for reliable
transmission. After all this is set and done then the user will be able
to surf the web on the Wi-Fi using http for nonsecure cites and https
for secure sites.

After connecting to the Wi-Fi Timmy forgot he has to send an email from
work at the coffee shop, but that email has to be sent from a secure
network. How would he do that? Timmy will first have to set up his
network to be secure since he is connected to a public network using
IPv4. He will have to reestablish the network again but now using a
virtual private network known as a VPN. The VPN software Timmy is using
sends a request to the wireless access point (WAP) which is the router
from the coffee shop. A point-to-point protocol (PPP) framing and 802.11
framing will occur sending us to the network layer. In the network later
IP addresses will be given but since Timmy is on a VPN his address will
be masked by a Network Address Translation (NAT) Protocol. What this
does it hides the real IP preventing attackers from gaining information
in your device. That is why the protocol that is going to be used is
IPSec which tunnels your IP address through protocol 50 and
Encapsulating Security Payload (ESP). The ports that are going to be
used are UDP 500 for Internet Key Exchange (IKE) for encryption and UDP
port 4500 for IPSec NAT-Traversal (NAT-T). Once that session is secure
then Timmy from the coffee shop can start typing up that email. A few
minutes went by, and Timmy has his email all typed up ready to go. This
email contains a JPEG and other sensitive information that needs to be
encrypted before sending. The proper tunneling for this message is to
digitally sign this message with his private key and the public key of
the person receiving this email to keep the integrity of the message.
This will attach a secure shell (SSH) to the email sending it through
secure mail transfer protocol (SMTP) port 25.

That is why it is important when connecting to public Wi-Fi you are
using a VPN that way your information is being transmitted through IPSec
and not regular unprotected protocols. People will drive through
neighborhoods and perform attacks. This attack is called wardriving.
They try and access vulnerable networks with a laptop or a smartphone
but more commonly with a laptop. They will scan for SSID and signal
strength that way penetrate the network and start capturing data. Once
this data is captured, they are able to read over the data through a
software like Wireshark. If data was unprotected, they could sometimes
capture sensitive data allowing them to install malicious malware. This
all happens in the Link Layer of the TCP/IP model. It is important to
make sure to change the Wi-Fi password when getting a new router.
Attackers will research what routers companies will have and research
the default password. Take extra time to change the password at your
house before you become a victim. No one is safe not even at your own
house from a cyber-attack.

This attack will then move into the Internet Layer of the TCP/IP model.
They will start to eavesdrop, which is called IP spoofing which could
intercept signals creating a fake SSID. The way this occurs is by the
attacker modifying the IP header making the device think it is the
correct destination. Once that connection is established then the
attacker can retrieve all the information like packets being sent to and
from the device connected to the wrong network. Now that the attacker is
connected it is given another shot at another attack within the network
it is currently hosting. You can minimize this attack by putting up a
firewall that filters out connections that don’t seem legit. Other
measures that can be taken into consideration are implementing
encryption such as a VPN and a MFA known as multi factor authentication.

A common attack used in the transport layer once the attacker has access
to the network is a SYN flood attack. This attack occurs with
transmission control protocol (TCP) which is one of the disadvantages
when using this over UDP. The way this attack works is by flooding the
network with a high volume of request not allowing to complete the
handshake process which is SYN, SYN-ACK, and ACK. The attacker sends
botnets to every device making it hard to see what requests legit and
what request malicious malware are. Another attack that occurs at this
level is User Datagram Protocol (UDP) flooding. UDP floods come in huge
amounts of packets causing victims devices to crash or become
unresponsive. Although this might sound scary starting from someone
wardriving it can all be mitigated by installing intrusion detection
systems (IDPS) and setting up a limit of request that can be sent from a
UDP packet that way it times it out and the request is cancelled. This
will help the device from crashing since it is not being flooded from
all the packets coming in. At the end of the day the attacker is there
to create significant financial harm, political gain, or physically harm
someone.

The application layer is the meat and potatoes for attackers to get all
their information from the victim. This is where the attacker is most
deadly with its victim in my opinion. As mentioned before in the link
layer of the TCP/IP model when the attacker is already eavesdropping,
and they get enough information this can turn into the Man in the Middle
(MiTM) attack. Once this is established the attacker can start sending
other types of attacks like emails containing malicious malware which
are known as phishing attacks. Once that malicious malware is opened it
can start a malicious SQL Code that then is injected into the device
which is known as Cross-Site Scripting (XSS) attack. This malicious
malware could then create a backdoor allowing the user to come and go as
they please. Once the attacker is in your devices home it can start to
track everything you do and if you use your device to log into personal
sites this can get ugly quick. No matter if the site is secure, if the
attacker has access to your keystrokes, it can trace every letter,
number, and symbol you typed in to get into Facebook, Instagram, or yet
even worse your banks website! Most of the time what they do since they
are aware of the security measures of the websites, they will create a
fake website that way you are redirected say to a fake WelsFargo website
which I purposely misspelled it with only one L. The proper way it is
spelled is WellsFargo. Unfortunately, in today’s world technology is
advancing and so are attackers. There are ways we can mitigate attacks,
but we will always be vulnerable since there are always new attacks
coming out which are called zero-day attacks. As mentioned before the
best way to fight back is by setting up strong firewall rules, IDPS, and
web applications firewalls (WAFs) to detect and block malicious traffic.
Conduct regular security audits of your network to see who is supposed
to be on there.

Just remember if you got to Starbucks or Dunking donuts think of Timmy.
Timmy did the right thing by setting up a secure network with VPN and
encrypting his email, that way it is harder for those people with bad
intent to capture his data while transmitting.

**References**

*Learn about connecting to Oracle Cloud and vmware resources*. Oracle
Help Center. (2020, August 6).
https://docs.oracle.com/en/solutions/connect-oraclecloud-vmware-resources/understand-remote-access-vpn-options.html#GUID-07EA03F0-B8A7-40C5-AF13-48054885954E

Moved. (n.d.).
https://docs.oracle.com/cd/E19253-01/816-4554/ipov-10/index.html#:~:text=The%20data%2Dlink%20layer%20identifies,Point%20Protocol%20(PPP)%20framing.

OConnor, T. (2023, January 16). *Emily Neuens*. SANS Institute.
https://www.sans.org/white-papers/33513/

S, D. E. L. (2021, December 13). *Common TCP/IP OSI layer attacks*.
Medium.
https://systemweakness.com/common-tcp-ip-osi-layer-attacks-51e4b9f99fb1
