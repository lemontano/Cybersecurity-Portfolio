# Ethical Manner to Use the Cyber Kill Chain in a Pen Test

Leonardo E. Montano

**Abstract**

With technology advancing and companies relying more on technology,
companies are facing challenges they have never faced before. Companies
need to make safeguarding their digital assets their number one
priority. Making sure that your network and environment have the best
defense is crucial to a successful business. Penetration testing is an
aggressive way to play defense. Identifying the vulnerabilities early in
the game does not make you appear weak. Penetration testing helps you
strengthen your cyber security posture and helps you develop better
security policies within your company. Compliance Assurance is part of a
company’s promise to make sure they are meeting industry standards and
requirements to keep their business open. This means you are doing
penetration tests within your company adhering to compliance, that way
you do not face legal issues. Although you might find vulnerabilities in
your systems you are reducing the risk of becoming a victim of a
cyber-attack. Wouldn’t you want to find out first by your penetration
tester rather than your security operations team? All it takes is for
one employee to click a link and your network could be breached. This
could be mitigated by doing the annual Security Awareness and Training.
A simple one-hour class can prevent an employee from clicking a link and
divert you from facing financial damages, lawsuits, and public
humiliation. No one wants to be a part of a company that would have
prevented the breach by just investing money in their Cyber defense
program.

# Table of Contents

## Abstract

## Different Types of Penetration Test

Types of attacks5

## Cyber Kill Chain

## Penetration Test Report

## Conclusion

## References

# **Different Types of Penetration Testing**

When it comes to Penetration Testing there are many ways and forms on
how to penetrate a company. The most popular form of penetration testing
done in today’s world is virtual. We all have either heard of what
hacking is or have seen it in a movie where someone has a ton of
monitors trying to access a program or save the world. In the real
world, you need permission to conduct any sort of test. Companies will
hire a penetration tester or have someone who works for them internally
conduct a test. The use of penetration testing contributes to a healthy
mature cyber defense program that protects companies from financial ruin
and embarrassment.

There are three different types of penetration testing which come in
different box colors. The box colors are white box, black box, and gray
box testing. These different colors have different meanings and levels.
When it comes to the white box you have full knowledge of the system.
You know the internet protocol address, source code, operating system
version, and other information that black box and gray box do not
receive. White box penetration testers usually work internally meaning
they will do a more rigorous test. Moving onto the black box testing
which is more popular for those who are usually hired externally. The
black box is just like it sounds you are in the dark and have no clue
who and what you are attacking. All you know is that you need to try and
find a vulnerability in the system.

This is where you act like a hacker in movies and try to breach the
network. The big difference is that the penetration tester has
permission to accomplish this task. As you can see this is the most
challenging box since it will also require more time because of the
trial-and-error attempts. When it comes to the gray box penetration
testing you have a little bit of white box and black box. What happens
when you mix a little bit of white and black paint? You guessed it, the
paint turns grey!

Same concept with the grey box penetration testing. The penetration
tester will have some information like maybe some internet protocol
addresses, employee names, or something along those lines that will help
the tester. They won’t give all the information like they do to a white
box but they will give just enough information for you to accomplish the
task sooner than a black box would. Now that you have found out what
type of color of box tester you are, who are your targets and what type
of attack are you doing?

**Types of Attacks**

There are different types of penetration testing when it comes to
targets which are Networking, Mobile, Web Application, Client-side, and
Social Engineering. Networking has to do with any sort of computer
networking, typically companies that rely on the cloud and have high
amounts of data. Mobile testing would be leaning more toward
applications we use on our phones like bank applications, games, or
anything of that sort. One of the most popular targets is web
applications. You are testing web browsers and the different components
that it offers. Client-side tests include local threats, outdated
software, or anything that involves third-party applications.

It brings us to our last test which is my favorite one Social
Engineering. Social engineering is the type of attack we have all seen
or maybe been a part of. It is that phone call you get where they say
they are the IRS or are calling for life insurance. We all know that
they are spam calls or emails but if done correctly you can acquire
information. That is why it is important to build rapport and get to
know the target before you attempt any sort of attack.

According to Wiley (2010), “Influence is defined as the process of
getting someone else to want to do, react, think, or believe in the way
you want them to.” What this means is that when you are doing an attack
you want to influence the target, that way you can connect with them and
have a higher chance of success. That is why building rapport is
important when comes to social engineering attacks. The purpose of this
paper is to demonstrate how a social engineering attack works from start
to finish during a penetration test.

**Cyber Kill Chain**

When it comes to a good Cyber Defense Program you need to make sure that
you are performing tests and investing in the security tools. The
attacker never sleeps so that is why it is important to know how an
attack works. Most of the attackers follow the same plan which is the
Cyber Kill Chain. Not only do attackers follow this plan but also people
and companies enhance their visibility into an attack and help them
understand an attacker’s mindset. The cyber kill chain consists of seven
steps which are also known as phases. The first phase is reconnaissance
which is the brain of the operation.

This is where you start collecting data on anything and everything about
your target. From network infrastructure to employee details. You need
to look at their security policies if allowed depending on what color
box of penetration testing you are doing. If you are doing white or grey
box testing, then you should be allowed to look at their security
policies to find any openings in the system. The next section you want
to look at is the network infrastructure, which is the internet protocol
address, Wi-Fi name, local area network (LAN), wide-area network (WAN),
metropolitan area network (MAN), and subnet mask. This will help the
penetration tester have a better understanding of how the network works
and ways the tester can try to penetrate the network.

As mentioned before, attacks are not only done on networks but on
employees’ as well. Part of the reconnaissance phase includes gathering
employees email addresses, phone numbers, and social media accounts.
Many more forms of reconnaissance can be done but the last one that you
might want to know is the host information. This will give you specifics
on the operating system type, version, and other internal software that
is used. According to EC-Council (2013), “The goal of reconnaissance is
to identify as many potential attack vectors as possible.” The top
passive recon tools used to gather this information stated above are
Wireshark, Google, FindSubDomains.com, VirusTotal, and Shodan.

For active recon tools penetration testers use Nmap, Nessus, OpenVAS,
Nikto, and Metasploit. The difference between active and passive is that
active tools are to interact directly with the machines of the target.
Passive recon tools are the opposite which are used more for looking for
unintentional data leaks found on the internet. That is why Google is
listed under that category. Poston (2019) says this about
reconnaissance:

> Reconnaissance is an important first stage in any ethical
> hacking attempt. Before it’s possible to exploit a vulnerability in
> the target system, it’s necessary to find it. By performing
> reconnaissance on the target, an ethical hacker can learn about the
> details of the target network and identify potential attack vectors.
> <https://resources.infosecinstitute.com/topics/hacking/top-10-network-recon-tools/>

Moving onto the next phase of the Cyber Kill Chain which is
weaponization. This happens after all the information is gathered from
the reconnaissance phase. This is where the penetration tester or
attacker starts to put everything together that they discovered. This
can range from getting an employee’s personal phone number to an IP
address that a Penetration tester can use to then develop malware to
crash the network. By getting an IP address you can find out what ports
are open and then you can set up Wireshark to monitor what type of
requests are being sent from and to with that IP address.

The Penetration tester needs to determine what type of weapon they are
going to create. The two components that are to be considered are if the
attack is going to be a Remote Access Trojan (RAT) or an Exploit. Soare
(2023) describes a Remote Access Trojan as “a piece of software that
executes on the machine of the victim and allows the intruder remote,
secret, and unobserved entry.” When you sit here and think about all the
possible outcomes that can be done when someone can access all your
information remotely is frightening. The second component is the exploit
portion of the development and creation of the weaponization.

This part of the malware is going to be the delivery driver for the RAT.
The main goal of this component is to evade user detection and build a
backdoor that way the RAT has access. Soare (2023) explains on the
different forms of “infections sources, such as MS Office files, PDFs,
audio/video, or web pages. More vulnerabilities such as privilege
escalation exploits can be sued on the target after having RAT
installed…”. Once the malware is created, we move onto the Delivery
phase which is step 3 in the Cyber Kill Chain.

Execution of the plan is going to be crucial when it comes to
penetration testing. Making sure that the delivery is effective and as
productive as possible is going to be either a bust or a success in the
entire attack. The delivery is going to be responsible for a
well-organized dominant attack on the target. As a penetration tester,
you do not have to be worried about leaving traces behind since you are
being hired by a company to do a test on them. As for unethical hackers,
they tend to carry out attacks by masking themselves from compromised
email addresses or hacked websites.

Popular ways to deliver malware are going to be email attachments,
Drive-by downloads, USB/Removal Media, and DNS Poisoning. Email
attachments are going to be any sort of file attached to an email like a
PDF file, Microsoft Document, or audio/video that contains malware.
Images can also be used to send malware. It is called steganography
where you modify the original image. Drive-by download is when a user
for example accesses a website, and that website starts to download
malware code and is executed on the target’s computer without the
target’s permission. USB/Removal Media is a physical device that lets
you insert malware from a drive into a computer that then exploits
malware into the operating system.

The last one is DNS Poisoning where you attack the network. There are
many types of poisoning, but the popular ones are man-in-the-middle
(MITM), DNS hijacking, and cache poisoning. Those are just some of the
methods used to deliver malware to a network when using DNS Spoofing
methods. Step number four is the Exploitation of the weapon. At this
point the penetration tester gathered all the information in the
reconnaissance phase, built the weapon, and shipped it off. The weapon
has now arrived, and it is time to unpackage it and start the
exploitation phase.

This is the phase where you want to make sure the target has not
installed the latest version of the operating system. The reason behind
it is if you found a vulnerability in the old software that
vulnerability might still be open creating a higher chance of success
when carrying out the attack. That is why it is important to update your
software when an update comes out. According to Soare (2023), “The
exploit will only work on outdated systems and most probably will not be
picked up by traditional security tools, like Antivirus or Firewalls.”
Phase five of the cyber kill chain can happen simultaneously with the
delivery of the weapon depending on the attack.

If the attack is carried out by USB, then the installation which is step
five would be implemented right away. Unfortunately, as technology
advances so does malware. Attackers find different ways to install
malware relying heavily on droppers and downloaders to install the
malware. This is where the mailman delivers the RAT with the exploit and
starts creating backdoors for unwanted malware or command-line
interfaces. Once the malware has been installed, we move into the
driver’s seat of the command and control of the cyber kill chain. This
is where the RAT is now installed, and the back door is open.

At this point anyone is welcome, and the penetration tester has the key
to the house. Gyongyosi (2023) states that “Hackers can use C&C or C2
servers to create botnets and launch DDoS attacks, steal, delete, and/or
encrypt data. A command-and-control (C2) server facilitates the
communication between a threat actor and its target. The attacks are
frequently executed over DNS.” When you hear about ransomware attacks
this is when an attacker encrypts all your data, and you are unable to
access anything on your computer.

They usually demand money to be deposited into a specific account or
else they will delete everything on your computer. The sky is the limit
once the penetration tester has command and control of the network or
the target’s Internet of Things (IoT) device. They can move laterally in
the network to different areas, obfuscate data, and encrypt their
footsteps making it harder to track. Depending on the threat actor or
penetration tester they have an overall end goal. They might not want to
crash your computer or do a ransomware attack but just register each
stroke.

There are many reasons why an attacker might want to do an attack on a
particular company or country. As for penetration testers, the main goal
is to make sure that the company that hired them has the best cyber
defense and an updated security policy. The last phase of the cyber kill
chain is Actions on Objective. Lockheed Martin defines this as hands-on
Keyboard access; intruders accomplish their original goals. This means
that the attacker or penetration tester has reached the finish line, and
your company or employee has not been a victim of a cyber security
attack.

There is a reason why companies do penetration testing. Back in 2015,
there was a massive data breach with Experian. Over 15 million
consumers’ data was breached, and it could have been prevented if they
had done a penetration test on their web application. That is why it is
important to change your password as soon as possible when making a new
account or if a password is given to you. Multiple companies become
victims because people don’t take the time to make a different password.

Even with your Wi-Fi password at home, it is important to change it
because all an attacker or penetration tester must do is look for the
make and model and look for passwords then sit on the side of a street
in a neighborhood and perform attacks on Wi-Fi in that area. Once that
is set up the attacker can set up an active monitoring device and start
gathering data about the different internet protocol addresses in the
home. You could become a victim simply because you decided not to change
your Wi-Fi password.

**Penetration Test Report**

Now that you know how the cyber kill chain works and how every phase has
its role in the attack it is time for the penetration tester to put it
all together and do a penetration test on a company called Observable
Pet. Billy has been hired as a penetration tester to find
vulnerabilities in the company. They have been worried about their cyber
defense because of all the occurrences they’ve seen in the news
recently. The owner Henry Palmer gave Billy a few details about the
company but not much. Since Billy got information that a normal person
would not get, this is going to be considered a grey box attack since he
has some knowledge of the company. Billy received employees’ emails and
phone numbers.

The first box on Billy’s checklist is to start the reconnaissance phase
of the cyber kill chain. Billy’s specialty when it comes to penetration
tests is going to be social engineering. According to Fincher and
Hadnagy (2015) “One statistic states that more than 60 percent of all
attacks had the “human factor” as either the crux of or a major piece of
the attack.” (p.2) When you start to think of the odds when performing a
social engineering attack the odds are in your favor because of the
human factor that is stated above. Moving onto how a social engineering
attack is performed and organized.

**Company Overview**

Observable Pet Care is a company that cares for and treats pets. They
offer veterinarian services and insurance. Observable Pet Care has been
in service for 15 Years and has won over 45 awards for its great work.
Owner Henry Palmer takes pride in his work and wants to continue to help
families with their fur babies. Observable Pet Care is a small company
located in CyberApolis.

The actual location of the company is a blue building that looks like a
house. It is close to a U-Haul Rental Center and a residential area. The
address of the company is 729 Object Street, CyberApolis. From the
emails that were provided by the owner, it seems that the standard
format is <firstnameinitial.lastname@obspet.com>.

**Tools Utilized**

The tools used to perform this attack were open information sources. The
sources that were used are Google, Social Park, Google Maps, and
<https://observablepet.website/>. All these tools were used to help
gather the necessary information for the penetration test. Without these
tools, the penetration tester would not be able to acquire the
information needed to continue. Making sure that the appropriate tools
are annotated is important because the Owner needs to know how the
information was obtained and what can be done to secure information that
was leaked or found.

**Open-Source Intelligence (OSINT)**

Gill (2023) defines Open-Source Intelligence as “intelligence produced
by collecting, evaluating, and analyzing publicly available information
with the purpose of answering a specific intelligence question.”
Open-Source information can be found from public records, News media,
Libraries, Social media platforms. Images, Videos, Websites, and The
Dark Web. Everyone uses this every day but does not realize it since it
is just normal. An example of everyday use would be if you looked for
someone from high school on the internet. You are using open-source
intelligence to look for old friends.

The way an OSINT is notated in a report in the following format:

Open-Source Tool used to find information: For example, Google Search:
“Observable Pet Care” AND “Employees”

Results: This is going to be the URL of the website where you found the
information

Information Found: Website Name

Possible PRETEXT: What PRETEXT stands for is a rough draft of the social
engineering attack.

Moving onto the actual report on what Billy the penetration tester found
during his reconnaissance phase of the social engineering penetration
test. Billy focused on the Vet Technician Kathleen Goggin. The
penetration tester was given her email address which is
<K.Goggin@obspet.com> and the role she plays in the company. Billy first
started a Google search looking for “Kathleen Goggin” AND “CyberApolis”.
The reason the search is in quotations including a capitalized “AND” in
the middle is because it will only be for Kathleen Goggin from
CyberApolis. Instead of having a million results in Google, it will
focus on those terms within the quotations.

Upon reviewing the results Billy came across a Social Park account under
the name Kat Goggin. It seems that Kathleen from Observable Pet Care
goes by Kat and not her full name. Billy made sure that he was looking
at the correct person and not someone else by the same name. He made
sure by looking at the Observable Pet Care website where she is listed
as a Veterinarian Technician. The penetration tester noticed that Kat
does multiple fundraisers for dogs that are up for adoption and
volunteers at the local shelter. He also noticed that she has a dog
named Max who is a male beagle.

The reason Billy is looking into Kat’s life and what she does is to
build rapport. By building rapport you start to build a relationship
with the target. The more you know the better the attack is going to be
and the success rate is going to be higher. You can’t just start sending
out emails or call the target if you do not know anything about their
life. That is why it is important to find as much information as
possible.

The penetration tester was able to find Kat’s personal email address,
personal phone number, and where she lives by searching on
FastpeopleSearch.com and going to CyberApolis.Property.gov. Now Billy
knows where she lives, her phone number, both work/personal email
addresses, her dog’s name, and what she does in her spare time.

**Google Search:** “Kathleen Goggin” AND “CyberApolis”

**Results:** <https://socialpark.com/KathleenGoggin>

**Information Found:** Target helps do fundraisers and volunteers at the
local shelter on Sundays. She has a dog named Max who is a male beagle.
She is also a full-time Veterinarian Technician with Observable Pet
Care.

**Possible PRETEXT:** Call Kat to her work and see if she can go over
your dog’s medication. Send email an with a PDF file that contains
malware so once she opens it malware is downloaded into the operating
system.

**Google Search**: “Kathleen Goggin” AND “CyberApolis”

**Results**: <https://fastpeoplesearch.com/KathleenGoggin>

**Information Found**: 32-year-old and was born on January 12, 1991. The
current address is 1501 Meadow Dr, CyberApolis. Her phone number is
555-234-4415 and her email address is <Kat.Goggin@cmail.website>.

**Possible PRETEXT**: Email Target about doing a fundraiser for the
local shelter. State that you want to help raise money, that way the
shelter has more opportunities to help animals in the local area.

Now that the penetration tester has found out more information about
Kat, he can start moving to the second phase of the cyber kill chain
which is weaponization and Pretext development. The goal is to
manipulate the human element and get them to click the link or follow
instructions on the phone. Billy will make a series of phone calls. If
the phone calls do not work and he cannot get Kat on the phone, then he
will send 2 emails to her company email.

If she does take the call then the message to her will be “Hello, my
name is Jason Williams (Billy) and I brought my dog Max over and I had
some questions about his medication. Is it possible to go over his
medication with me over the phone? I have sent you an email with the
medication as a PDF file. You should be receiving an email from
<jasonwilliams1@cmail.website>.” That is the message I will be using to
try and convince Kat to open the email with the file. If the file does
not work then I can add a domain login-dropbox.com if the PDF file does
not work.

For Kat Billy started to build malware that will be inserted in a PDF
file. Since the target works at a veterinarian’s office Billy decided
that if doing a vishing attack combined with a phishing attack he will
have more success. CompTIA (n.d.) states the following:

> “Most social engineers find ways to wrap a lie inside of many truths.
> A well-prepared attacker can find it relatively easy to create the
> right kind of situation to make you feel comfortable or make you feel
> that the attacker is worthy of your trust. Once that one lie (a bad
> hyperlink in an email, or a simple request for information, for
> example) is carefully couched inside a plausible – but fraudulent –
> context, the attacker can get you to take action. It’s all about
> context and a social engineer’s ability to manipulate your natural
> human instincts.”

When having that mindset during the weaponization phase you can
influence and manipulate the target into doing anything you want them to
do. CompTIA (n.d.) also said that when a human is distracted and not
paying attention, they can lower their natural defense mechanisms or
take an action they normally will not do.

The PDF file that Billy is going to make is going to contain back door
malware allowing the penetration tester to perform a remote access
trojan attack. This will then open the door for the penetration tester
to start gaining access to the operating systems and sorts of data. At
this point, the Penetration tester has gathered information about their
target, developed a Pretext, and created a weapon. The weapon has been
created so now it is time to infiltrate it. The next phase will be the
delivery method. As mentioned before the way the penetration tester will
deliver this weapon is through a phishing and vishing attempt.

A phishing attempt is when emails are sent, and Vishing is when someone
calls. The first part of the delivery method the penetration tester is
going to use is the Vishing attempt. Billy will disguise himself as
Jason Williams. The penetration tester will download a free application
that will enable him to use a local area code. Once the target is on the
phone then the tester will instruct the target on the next steps. The
second step will be to send an email with the PDF file and link to
login-dropbox.com in case the file does not open. The penetration tester
will make sure to tell the target that there is an email coming from
<jasonwilliams1@cmail.website>. The penetration tester then can
influence the target by having her check her spam in case it gets
filtered by the Observable Pet Care information technology team.

Social engineering is based on how good your research is and how good
your delivery is. That is why it is important to build rapport with your
target and use the principles of influence. The principles of influence
are Reciprocity, Commitment and Consistency, Social Proof, Authority,
Liking, and Scarcity. The call was taken from Kat and the delivery has
started. The penetration tester sent the target an email to
<K.Goggin@obspet.com> which was delivered and opened by Kat. As soon as
the attachment was opened, and the link was clicked it was game on. The
time has come to exploit the operating system.

The PDF file did not open but Billy was able to get Kat to click on the
link with the domain name login-dropbox.com. He stated that the link was
working and was not sure why it was not functioning. Billy told her that
he would walk in better since technology decided not to work. Little
does Kat know but a backdoor malware had started downloading without her
knowledge. Once the operating system has been exposed it is time to
install the malware on the asset.

At this point, Kat has no idea that her computer at work is being
attacked by malware and she has now become a victim of a cyber-attack.
The installation phase has been initiated and a remote access trojan is
currently installing on her computer. Once the remote access trojan is
installed the penetration tester will have full access to the operating
system. Rash (2022) defines “A Remote Access Trojan, otherwise known as
a RAT, is a type of spyware that allows a cybercriminal to take control
of the computer or other device it's installed on. RATs are malicious
software that constitutes a major cybersecurity threat.” As you can see
once a RAT is installed that is a massive breach to your operating
system.

The remote access trojan has now been installed and it is time for Billy
to start the command and control (C2) of the operating system. This is
where Billy has total control of the operating system and can do what he
pleases with the computer. Actions on the objections are where the
penetration tester starts to use the keyboard and mouse. The penetration
tester now can accomplish the original goals. The original goal was to
get as much information as possible from the company.

Billy’s goal is to install malware that will record every keyboard
stroke that is used when operating the system. The reason the
penetration tester wants to record every keyboard stroke is that he
wants to get passwords and usernames. Once those credentials are
retracted then the penetration tester can dive deeper into the system
without anyone noticing. This malware turns on once the computer boots
up, that way it can get any registered keystrokes.

Keystroke malware has picked up Kat’s credentials for their customer
database for credit card applications and other consumer personal
information. Thus far Billy has performed a social engineering attack on
Kat, manipulating her to open a file that had malware, once the file was
opened malware started downloading for a back door to be installed and
later a remote access trojan. Following the remote access trojan a
keylogger malware was installed to record keystrokes for increasing the
possibility of acquiring credentials to their web applications. The
keystroke malware was successful and was able to gather Kats credentials
to the credit card applications and other consumer personal information.

# **Conclusion**

The use of penetration testing contributes to a healthy mature cyber
defense program that protects companies from financial ruin and
embarrassment. When Billy was first contracted by Henry Palmer from
Observable Pet Care, he mentioned that he wanted to make sure that his
cyber defense was well protected since they deal with consumers’ social
security and personal information. Henry emphasized that no matter the
cost he wanted the penetration tester to do what he had to do to make
sure the company was secure.

The penetration tester always wants to make sure they do everything in
their ability to gain unauthorized access to any part of the company.
Whether it is from penetrating the network from a DDoS Attack,
War-driving, or a social engineering attack. Any sort of breach of an
operating system or its environment is a successful attempt from by a
penetration tester or the attacker. As far as Observable Pet Care Billy
the penetration tester was able to gain access. Billy decided to do a
social engineering attack on the Veterinarian technician Kathleen
Goggin. He conducted an in-depth investigation on Kat and he was able to
retrieve her personal phone number, email address, pet’s name, where she
volunteers, and her social media account.

Once all the information was found the penetration tester was able to
develop a pretext for a social engineering attack. The tester used pets
as one the of tools to manipulate the target. He knew that the target
loved animals and that she wouldn’t reject him if he had some questions
about his dog’s medication. The penetration tester started the attack
with a Vishing attempt. Once the target took the call the tester was
able to send a phishing attempt via email. The email contained a PDF
file under the name Max Medication with a brief description in the body
of the email. The penetration tester then added a link in case the file
did not open, and the malware did not download correctly.

Moving forward, the malware was downloaded into the operating system and
a remote access trojan was installed giving command and control to the
penetration tester. The penetration tester then installed malware where
keystrokes are being registered every time the operating system boots
up. At this point, the penetration tester had access to an employee’s
credentials and now has access to the web applications. If you are an
owner of this company, you must be extremely concerned about your
company’s cyber defense. Although the attack did not come from the
network it was still exposed.

An example penetration testers use for people to understand is to think
about a building. If you were in the building and no one noticed that
you entered or knew that you were an unauthorized person there the
attempt was successful. You could have picked a lock, breached a window,
or stolen someone’s badge to enter. It is the same concept with cyber
security all the penetration tester did was hitch a ride with Kat. Many
roads lead to Rome and that is the same metaphor used by a penetration
tester.

One of the biggest reasons penetration tests are done is to see where
the company is slacking and needs work. Companies tend to put it off
because they assume it will never happen to them until it does.
Arampatzis (2023) states that there are “5 Reasons Why Your Business
Needs Penetration Testing which are Uncover hidden system
vulnerabilities before criminals do, strengthen security processes and
strategies, Lower remediation costs and reduce dwell time, Adhere to
regulatory compliance around security and privacy, and lastly Preserve
Brand reputation and customer loyalty.” No company wants to announce
they have become a victim of a cyber security attack. Look at Target,
they are a Fortune 500 company, and their data was breached. Can you
just imagine how much money they lost because of that breach? The
lawsuits that followed and the embarrassment they faced could have all
been prevented.

When it comes to Observable Pet Care Henry Palmer did not fail his
company or customers. Henry went out of his way to look for a
penetration tester who could find any weaknesses or vulnerabilities in
his company. Although the penetration tester was able to get into the
network and breach their web application that does not mean the company
is exposed and should let the media know. These tests are done to better
prepare the company against future attacks.

The penetration tester took the social engineering route and was able to
successfully get in. You may ask yourself how do you stop someone from
opening a file or clicking a link? Most of the time employees are not
trained. Companies put too much trust in their employees so they often
do not take the time to train them. All it takes sometimes is an
hour-long class with a penetration tester to go over the do’s and do
nots. As mentioned before companies have this idea in their head that it
will not happen to them until it does. At that point, it is too late,
and they should have invested in a penetration tester.

When updating security policies, it could be as simple as if someone
calls in, make sure the employees looks for the customer calling in the
system before answering any questions. While doing this it can minimize
the chances of opening an email from someone you do not know. For
example, Kat could have taken the call, asked for Jason’s information,
and seen that he was not in the system. At that point, Kat could have
said according to our policy we are unable to provide any medical
information or advice since it seems you are not our customer. I would
suggest you come to visit us for our doctor to give his professional
advice. All it takes sometimes is someone to raise awareness at work and
employees will follow all directions. Security policies are there for a
reason and employees must follow this for Cyber Defense.

Businesses should view penetration testing as a wall around their
castle. Adding more walls to a castle can help against attackers who are
trying to invade your kingdom. No one wants their home to be invaded and
taken over by attackers.

**  
**

# **References**

Anconina, D. (2023). *What are the different types of white hat
penetration testing?*. XM Cyber.
https://xmcyber.com/blog/what-are-the-different-types-of-white-hat-penetration-testing/#:~:text=That’s%20the%20principle%20behind%20white,organizations%20identify%20their%20weak%20spots

Arampatzis Guest Writer View Profile, A. (2023). *5 reasons why your
business needs penetration testing*. Tripwire.
https://www.tripwire.com/state-of-security/5-reasons-business-needs-penetration-testing#:~:text=A%20penetration%20test%20can%20demonstrate,company%20safe%20from%20potential%20threats

Gill, R. (2023). *What is Open-Source Intelligence?*. SANS Institute.
https://www.sans.org/blog/what-is-open-source-intelligence/

Gyongyosi, L. (2023). *Command-and-control servers explained. techniques
and DNS Security risks*. Heimdal Security Blog.
https://heimdalsecurity.com/blog/command-and-control-servers-explained/

Hadnagy, C., Fincher, M., & Dreeke, R. (2015). *Phishing dark waters:
The offensive and defensive sides of malicious e-mails*. Wiley.

Hunt, B. (2022). *Council post: To prevent Cyberattacks, make
reconnaissance harder*. Forbes.
https://www.forbes.com/sites/forbestechcouncil/2021/12/02/to-prevent-cyberattacks-make-reconnaissance-harder/?sh=7501aa4919b2

Malik, K. (2023). *Types of penetration testing: A comprehensive guide*.
Astra Security Blog.
https://www.getastra.com/blog/security-audit/types-of-penetration-testing/

Poston, H. (2019). *Top 10 network recon tools*. Infosec.
https://resources.infosecinstitute.com/topics/hacking/top-10-network-recon-tools/

Praveen. (2023). *What are footprinting and reconnaissance?*.
Cybersecurity Exchange.
https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/basics-footprinting-reconnaissance/

Rash, W. (2022). *What is a rat? \| U.S. news*. U.S.News.
https://www.usnews.com/360-reviews/privacy/what-is-rat

Soare, B. (2023). *The Cyber Kill Chain (CKC) explained*. Heimdal
Security Blog.
https://heimdalsecurity.com/blog/cyber-kill-chain-model/#:~:text=2.-,Weaponization,(RAT)%20will%20be%20used

*What is a social engineering attack - types and preventative tips:
Comptia*. CompTIA.org. (n.d.).
https://www.comptia.org/content/articles/anatomy-of-a-social-engineering-attack
