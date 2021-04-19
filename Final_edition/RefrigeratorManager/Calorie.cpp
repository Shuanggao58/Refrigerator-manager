#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
using namespace std;

struct Type {

	char type[13];
};

const int N = 2;

int main() {
	
		sleep(0.5);
		int i, Num = 0;
		int weight = 0;
		
		Type num[N];

		ifstream infile1("/home/pi/RefrigeratorManager/result.txt", ios::in);
		ifstream infile2("/home/pi/RefrigeratorManager/weight.txt", ios::in);
		if (!infile1||!infile2)
		{
			cerr << "open error!" << endl;
			exit(1);
		}
		i = 0;
		while (!infile1.eof())
		{
			infile1 >> num[i].type;		
			++Num;
			++i;
		}
		infile1.close();
		infile2 >> weight;
		infile2.close();
		int calorie = 0;
		cout<<num[1].type<<endl;
		if (strcmp(num[1].type, "apple") == 0)
		{
			calorie = 0.53 * weight;
			cout << "Apple.  Weight:" << weight <<"g."<< " Calorie:" << calorie<<"Kcal" << endl;
		}
		else if (strcmp(num[1].type, "banana") == 0)
		{
			calorie = 0.93 * weight;
			cout << "Banana.  Weight:" << weight << "g."<< " Calorie:" << calorie << "Kcal" << endl;
		}
		else if (strcmp(num[1].type, "bell") == 0)
		{
			calorie = 0.18 * weight;
			cout << "Bell pepper.  Weight:" << weight << "g." << " Calorie:" << calorie << "Kcal" << endl;
		}
		else if (strcmp(num[1].type, "onion") == 0)
		{
			calorie = 0.40 * weight;
			cout << "Onion.  Weight:" << weight << "g." << " Calorie:" << calorie << "Kcal" << endl;
		}
		else if (strcmp(num[1].type, "Orange") == 0)
		{
			calorie = 0.44 * weight;
			cout << "Orange.  Weight:" << weight << "g." << " Calorie:" << calorie << "Kcal" << endl;
		}
		else if (strcmp(num[1].type, "tomato") == 0)
		{
			calorie = 0.15 * weight;
			cout << "Tomato.  Weight:" << weight << "g." << " Calorie:" << calorie << "Kcal" << endl;
		}
		else
			cout << "Warrning: Can't recongnize" << endl;
	
	
	return 0;
}
