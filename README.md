# Refrigerator-manager

The readme document will guide you to have a holistic understanding of this system, which is called refrigerator manager.

## Aim

The system is built for fresh foods, especially fruits. 

![image](https://user-images.githubusercontent.com/71794241/113421148-26174400-93fd-11eb-8c38-90412bca3af6.png)

We buy and eat fruits regularly in our daily life. There are 2 questions: 
1. Do you want to know how many calories you have gotten from those lovely fruits? 
2. Do you want a reminder to help you eat them in their optimal period?

Then use our system!

## Hardware requirements

The project is centered by Raspberry Pi embedded in the domestic refrigerators. The Raspberry Pi is 3b generation, and it has 256MB memory and 1G swap settings.

![image](https://user-images.githubusercontent.com/71794241/113420739-675b2400-93fc-11eb-8bfb-0d9ca3bd88e5.png)

Two extra devices are needed. One is camera located on the top of the preservation layer. Another is the weight sensor embedded in the bottom of the layer.

![image](https://user-images.githubusercontent.com/71794241/113421316-77273800-93fd-11eb-8910-e737a961e74d.png) ![image](https://user-images.githubusercontent.com/71794241/113421354-84dcbd80-93fd-11eb-93cf-55108f73bfd7.png)

The camera and the weight sensor will work collaboratively. The camera only turns on to catch images of the fruits after the weight sensor feeling weight changes. Then, the images and weight data will send to Raspberry Pi and processing in it.

Finally, we add the system to a wi-fi based LAN to make it participated in the network of smart home. We believe it will show huge energy after version iteration.

![image](https://user-images.githubusercontent.com/71794241/113417215-85715600-93f5-11eb-9e79-2c5fd4d5c2f5.png)

## Methods

Now, let’s see how to implement the system in 4 steps.

First, what can we do by the camera? It will turn on by the signal of weight changing and send several images to the raspberry Pi. There is an agent trained by AI technics to recognize different fruits.

Second, weighting module. We choose HX711 model to get the weight signal and send it to Raspberry Pi. The putting date will be recorded as well.

Now we have all the data we want. It will all processing in the Raspberry Pi and work out the calories by the weight and fruit species. We will also get the expected optimal eating period by current images and fruit species.

# Realization

## Solftware requirement

1. Burning Raspberry Pi system
2. Install OpenCV and tensorflow

The system is developed in Linux environment, and main used C++.

## First test

![image](https://github.com/Shuanggao58/RefrigeratorManager/edit/main/gif/Orange.mp4)
