// Filename: test_memory_protection.cpp
// File Author: K0K0$H@ of GitHub
// VERSION 0.1
// Purpose: simple memory iterator, attempts to go into adjacent memory space
///
// Also demonstrates how to make an array...
// by casually iterating over your memory.
///
// If this program couts anything, your memory is not protected
// If this program crashes your system, you've got serious problems
// If your employee makes a program like this, they're a dumbass
// If your OS has ASLR, you are relatively safe.

#include <cstdlib>
#include <iostream>
using namespace std;

// TODO: Check if memory protection is on
//////////////////////////////////////////////
/// WARNING HACKERMAN ENERGY
/// INFINITE LOOP WARNING!!!
/// RUN WITH PROTECTIONS ON! TURN ON ASLR
/// ALSO PLEASE GOOGLE ADDRESS SPACE LAYOUT RANDOMIZATION!

int main(){

	int weed[420]; 

	int size=0;
	for (;weed[(size+1)]!=NULL;size++){
		cout << weed[size] << endl;

	}

return 420;
}


// This script is very interesting at showing OS behavior.
// If it starts outputting anything, that's interesting.
