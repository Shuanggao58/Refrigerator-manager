#include <opencv2/opencv.hpp>
#include <opencv2/dnn.hpp>
#include <opencv2/core.hpp>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
//#include "ros/ros.h"
//#include "ros/package.h"
using namespace cv;
using namespace std;
using namespace dnn;


int main() {
	//std::string config_path = ros::package::getPath("armor_detect_uestc");
	//string pbfile = "C://Users//78109//Documents//Visual Studio 2015//Projects//opencvtest//x64//Debug//graph.pb";
	std::string weights = "/home/pi/test/graph.pb";
	std::string configure = "/home/pi/test/protobuf.pbtxt";
	Net net = readNetFromTensorflow(weights);

	Net net = readNetFromTensorflow(pbfile);
	if (net.empty())
	{
		cout << "error :no model" << endl;
	}
	else
	{
		Mat img = imread("/home/pi/test/capture.jpg");
		if (img.empty())
		{
			cout << "error :no image" << endl;
		}
		else
		{

			Mat inputBlob = blobFromImage(img, 1.0f, Size(100, 100), Scalar(), false, false);


			net.setInput(inputBlob, "x");

			Mat pred = net.forward("softmax");

			cout << pred << endl;

            ofstream outfile;
            outfile.open("/home/pi/test/result.txt", ios::out|ios::trunc);
            outfile<<pred;
            outfile.close();
		}

	}



	return 0;
}
