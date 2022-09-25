***K0K0$H@'S CUSTOM NETWORK INFORMATION DISPLAY CONSOLE*** 
 
THIS REPO IS A 2-PART PROJECT 
 
part 1: cross-platform network information 
No matter which machine K0K0$H@ works on, he likes to have a lot of information about the network he's on.  
Informative display console can be used almost as a powerful desktop widget, except it spawns many terminals. 
Ideally, I could also program a way to organize and hide them. 
When using Linux, it's enough to have the display console work from bash in a similar manner. 

network info: 
nmap -p0-65535 localhost    // local machine port scan 

 
*part 2: LINUX ONLY monitor-mode 802.11 sniffing* 
802.11 scanning utility can be found in my amon repository at https://github.com/K0K0SHA/amon/  
I was going to do a whole repository on this concept, but I figured I kind of already have one there. 
Plus, this type of attack vector is starting to die out as of 2022. Unless I can find a way to hack WPA3-SAE. 
Nevertheless, 802.11 information is good. Normally, people probably just use Wireshark for this. 

proof of concept Python code: 

# setup code 
import OS 
import miscX 
if(!X.checkroot()): 
  exit(1) 
X.check_install_hard("airodump-ng") 
X.check_install_hard("wash") 
#X.safe_execute("amon") 
X.amon() 

# netinfo console code for attacking nearby 802.11 
# runs airodump-ng alongside wash on the same network adapter. 
# put these commands in different terminals 
X.execute_in_new_terminal_window("wash amon")                       # finding targets for Reaver 
X.execute_in_new_terminal_window("airodump-ng start amon")          # airodump-ng for local 802.11 scanning TODO add # of visible clients a-la WiFite 
