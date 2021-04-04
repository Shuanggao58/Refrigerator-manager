//#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
//using namespace cv;

//int main()
//{
//	Mat image = imread("C:\\Users\\78109\\Desktop\\1Banana.jpg");
//	imshow("show image", image);
//	waitKey(0);
//	return 0;
//}

//#include<opencv2\opencv.hpp>
//#include<iostream>
//#include<math.h>


/*using namespace cv;


int main(int argc, char** argv)
{
	
	Mat src = imread("C:\\Users\\78109\\Desktop\\test.jpg");
	
	if (src.empty()) {
		printf("couldn't load image");
		
		getchar();
		
		return -1;
	}

	namedWindow("original image", CV_WINDOW_NORMAL);
	
	imshow("original image", src);
	
	
	Mat output_image;
	
	cvtColor(src, output_image, CV_BGR2GRAY);
	namedWindow("grey image", CV_WINDOW_NORMAL);
	imshow("grey image", output_image);
	
	//imwrite("wencai.png",output_image);

	
	waitKey(0);
	return 0;
}*/
//#include <opencv2/core/core.hpp>  
//#include <opencv2/highgui/highgui.hpp>  
//#include <opencv2/imgproc/imgproc.hpp>  
#include <iostream>
//using namespace cv;
using namespace std;

/*int main() {
	
	Mat srcImage, srcImage1, srcImage2, newImage;
	Mat srcImage_B, srcImage_G, srcImage_R;
	vector<Mat> channels_BGR;

	

	srcImage = imread("C:\\Users\\78109\\Desktop\\test.jpg");
	if (srcImage.empty())
	{
		cout << "读取图像有误，请重新输入正确路径！\n";
		getchar();
		return -1;
	}

	int matrix_size = 3000;
	Mat image_mini; 

	resize(srcImage, image_mini, cv::Size(matrix_size /(1.54*4), matrix_size /(1.074*4))); 
	imshow("mini of original image", image_mini);
	waitKey(5);
	
	//imshow("src original image", srcImage);  
	
	split(image_mini, channels_BGR);
	
	srcImage_B = channels_BGR.at(0);
	srcImage_G = channels_BGR.at(1);
	srcImage_R = channels_BGR.at(2);
	//imshow("srcImage_B", srcImage_B);   
	//imshow("srcImage_G", srcImage_G);
	//imshow("srcImage_R", srcImage_R);

	
	Mat gray;
	cvtColor(image_mini, gray, CV_RGB2GRAY);
	int thR = 50;
	int thB = 50; 
	int thG = 70;
	Mat binary;
	
	//threshold(gray, binary, thR, 255, CV_THRESH_BINARY);
	Mat red_binary;
	Mat blue_binary;
	Mat green_binary;
	threshold(srcImage_B, blue_binary, thB, 255, CV_THRESH_TOZERO);
	threshold(srcImage_G, green_binary, thG, 255, CV_THRESH_TOZERO);
	threshold(srcImage_R, red_binary, thR, 255, CV_THRESH_TOZERO);
	//cout << red_binary << endl;

	
	  
	
	cout << green_binary.rows << endl;
	cout << green_binary.cols << endl;
	for (int i = 0; i < green_binary.rows; i++)
	{
		uchar*data1 = blue_binary.ptr<uchar>(i);
		uchar*data2 = green_binary.ptr<uchar>(i);
		for (int j = 0; j < green_binary.cols; j++)
		{
			if (data1[j] * 1 < 10)
			{
				data1[j] = 180;
			}
			//if (data2[j] * 1 < 10)
			//{
			//	data2[j] = 255;
			//}
			
		}
		uchar*data3 = red_binary.ptr<uchar>(i);
		for (int j = 0; j < green_binary.cols; j++)
		{
			if (data3[j] * 1 < 10)
			{
				data3[j] = 255;
			}
		}
	}

	imshow("G channnel + threshold ", green_binary);
	imshow("B channnel + threshold", blue_binary);
	imshow("R channnel + threshold", red_binary);

	channels_BGR.at(2) = red_binary;
	channels_BGR.at(1) = green_binary;
	channels_BGR.at(0) = blue_binary;

	merge(channels_BGR, newImage);
	imshow("R+G+B re conbine image", newImage);
	waitKey(0);
	return 0;

}*/