#include<iostream>
#include<string>    
#include<cmath>

#include "opencv2/opencv.hpp"
using namespace cv;
using namespace std;

int main()
{	
	
	string s;
	ifstream inf;
	inf.open("/home/pi/RefrigeratorManager/result.txt");
	while (getline(inf, s))
	{
		cout << s << endl << endl;
	}
}
