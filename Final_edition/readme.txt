The training part is in the Debug folder, using python language. The sample collection link is https://www.kaggle.com/shangdong/source-image-fruit-recongnition-on-raspberry.

There are two test methods. 
The main program is to call the main file in the test folder and the Weight file in the RefrigeratorManager folder. There are two different identification methods. One is to call the python classification program in Debug (using tensorflow to call the ckpt model) , The other is to call the classification function in RefrigeratorManager (using opencv.dnn) to call the pb model, which is located in the test folder. Due to the high real-time nature of extracting camera pictures and weighing, they are not put into the cppthread file. Calling cppthread can output the results and calculate the calorific value of the recognition results in real time.

The recognition result is stored in the RefrigeratorManager folder.
