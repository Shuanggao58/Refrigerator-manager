

#include<fstream> 
#include<iostream>
#include<string>    
#include<cmath>

#include "opencv2/opencv.hpp"
using namespace cv;
using namespace std;

int main()
{

	waitKey(15);
	VideoCapture capture(10);

	
	Mat frame;

	Mat dst,  detected_edges;
	
	int x0 = 0, y0 = 0, w0 = 0, h0 = 0;
	int x0max = 0, y0max = 0, w0max = 0, h0max = 0;

	int biggest = 0;

	while(true){
		capture >> frame;

		cvtColor(frame, dst, CV_BGR2GRAY);

		threshold(dst, dst, 128, 255, CV_THRESH_BINARY_INV);

		vector<vector<Point>> contours;
		vector<Vec4i> hierarcy;
		findContours(dst, contours, hierarcy, CV_RETR_EXTERNAL, CHAIN_APPROX_NONE);

		vector<Rect> boundRect(contours.size());
		

		for (int i = 0; i<contours.size(); i++)
		{
			boundRect[i] = boundingRect((Mat)contours[i]); 
			drawContours(frame, contours, i, Scalar(0, 0, 255), 2, 8);  
			x0 = boundRect[i].x;  
			y0 = boundRect[i].y; 
			w0 = boundRect[i].width; 
			h0 = boundRect[i].height; 


			if (w0 * h0 > biggest)
			{
				biggest = w0 * h0;
				x0max = x0;
				y0max = y0;
				w0max = w0;
				h0max = h0;
			}
		}
		Rect rect(x0max, y0max, w0max, h0max);
		Mat image_rect = frame(rect);
		if (image_rect.size != 0)
		{
			bool write_bool = imwrite("/home/pi/test/capture.jpg", image_rect);
		}

		string s;
		ifstream inf;
		inf.open("/home/pi/test/result.txt");
		/*while (getline(inf, s))
		{
			cout << s << endl << endl;
		}*/
		rectangle(frame, Point(x0max, y0max), Point(x0max + w0max, y0max + h0max), Scalar(0, 255, 0), 2, 8);
		putText(frame, s, Point(x0max, y0max), FONT_HERSHEY_SIMPLEX, 0.8, Scalar(255, 255, 255), 2);
		imshow("result", frame);
		cout << contours.size() << endl;

		waitKey(15);	//delay
		if (waitKey(100) == 27) break;//Esc-->break
	}
}



