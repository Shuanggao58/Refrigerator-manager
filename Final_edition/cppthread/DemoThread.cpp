#include "DemoThread.h"
#include <iostream>
#include <stdio.h>
#include <chrono>
#include <thread>

void DemoThread::run() {
	int i = 0;
	//for(int i=0;i<100;i++) {
	while(i < 100){	
		//printf("%d\n",i+offset);
		//system("/home/pi/RefrigeratorManager/demo");
		if ((i+offset) % 2 == 0 )
		{
			//printf("%d\n",(i+offset));
			system("/home/pi/test/demo2");
			
			system("/home/pi/RefrigeratorManager/Calorie");
			
		}
		else
		{
			//printf("%d\n",(i+offset));
		}
		i = i + 2;
		std::this_thread::sleep_for(std::chrono::milliseconds(10));
	}
	
}
