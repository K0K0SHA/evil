# evil
Evil "Destruction School" virus scripts and executables.
Designed to DOS by destroying a session or data.

Disclaimer:
Use this software in test labs on your own discretion.
Don't break the law using any of these tools (and praise Zion). 

Abstract
Think of this software as tools to destroy. For fun. 
You do need execution-level control to run these toys.
At first, I begun to experiment with fork-bombs on Linux.
Pretty fun way to (mostly) harmlessly destroy a session.
Then, I made a program called Bullsh1t.

BULLSH1T
Bullsh1t uses an infinite loop in C to spawn infinite terminals.
It crashes your Linux system pretty reliably.
Better yet, BULLSHIT does something that similar scripts don't: it prevents the poor user from being able to block it. Basically, *you can't interrupt BULLSHIT*. Normally, if a process within a terminal window is freezing your Linux machine, you would usually have a few defensive options. Normally, it would be possible to either keyboard interrupt eg CTRL+X or CTRL-C. If that doesn't work, a Linux sysadmin would probably close the terminal. But because Bullshit spams so many terminal spawns, the user cannon possibly gain enough control over the terminal to do anything. It's bullshit. 
Only a few simple code modifications would allow Bullshit to recursively delete/scramble files on the disk, DDOS the network via TCP amplification, and more. Basically, whatever you want to put in the "while" section of the loop in C.

REAL_BULLSHIT
The idea for Bullsh1t was a destructive virus in the form of a simple C binary. REAL_BULLSHIT seeks to improve upon Bullsh1t. Specifically, REAL_BULLSHIT is meant to add a feature which allows more attack vectors. Bullsh1t has to be compiled in C and run on the correct system. REAL_BULLSHIT should be able to launch an attack from Java, Python, C, shell, Android Installer, MSI, ps1 (P$), and batch. What would be even cooler is if REAL_BULLSHIT could figure out the system it was on, and scan for vulnerabilities. 

DDOS
I happen to be an expert in DDOS, so there is a whole folder full of DDOS tools and info.
