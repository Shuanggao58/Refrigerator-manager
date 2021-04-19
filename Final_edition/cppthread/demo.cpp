#include <stdio.h>
#include "DemoThread.h"


#include <iostream>
#include <chrono>
#include <thread>
int main( int argc, const char* argv[] ) {
	
	DemoThread myThread(0);
	DemoThread myThread1(101);
	//DemoThread myThread2(20);
	myThread.start();
	myThread1.start();
	//myThread2.start();
	myThread.join();
	myThread1.join();
	//myThread2.join();
}
