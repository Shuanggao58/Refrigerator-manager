# Refrigerator-manager

The readme document will guide you to have a holistic understanding of this system, which is called refrigerator manager.

## Aim

The system is built for fresh foods, especially fruits. 

We buy and eat fruits regularly in our daily life. There are 2 questions: 
1. Do you want to know how many calories you have gotten from those lovely fruits? 
2. Do you want a reminder to help you eat them in their optimal period?

Then use our system!

## Hardware requirements

The project is centered by Raspberry Pi embedded in the domestic refrigerators.2 extra devices are needed. One is camera located on the top of the preservation layer. Another is the weight sensor embedded in the bottom of the layer.

The camera and the weight sensor will work collaboratively. The camera only turns on to catch images of the fruits after the weight sensor feeling weight changes. Then, the images and weight data will send to Raspberry Pi and processing in it.

Finally, we add the system to a wi-fi based LAN to make it participated in the network of smart home. We believe it will show huge energy after version iteration.
