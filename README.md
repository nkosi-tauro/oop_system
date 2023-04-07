<h1 align="center">Driverless Car System (Tesla At Home Edition)</h1>



## About
This is a Python program that simulates the operation of a driverless car system. The program processes data from various sensors and makes decisions based on the processed data. The main goal of this project is to give you an idea of how a driverless car system could work and handle different scenarios. It is important to note that this is just a simulation and not an actual implementation of a driverless car system.

## Design Choices and Solution Implemented ##  

### Classes ## 

I chose to implement the program using an object-oriented approach with classes and subclasses to represent the different components of the driverless car system. The main classes are Sensor, Decision, and Control. These classes are the foundation of the program, and they represent the data processing, decision-making, and control aspects of the system.

The Sensor class is an abstract base class that represents the general concept of a sensor. It has subclasses for each specific type of sensor, such as LaneDetectionSensor, ObstacleAvoidanceSensor, and TrafficSignalRecognitionSensor. Each subclass processes data relevant to its specific sensor type.

Similarly, the Decision class is an abstract base class that represents the general concept of decision-making. It has subclasses for each specific type of decision, such as LaneDetectionDecision, ObstacleAvoidanceDecision, and TrafficSignalRecognitionDecision. Each subclass makes a decision based on the data from its corresponding sensor.

The Control class is responsible for executing the decisions made by the decision classes. It takes the decision as input and updates the internal state of the car accordingly.

### Exception Handling ##  

I implemented custom exception classes for handling errors specific to this program, such as InvalidSensorDataError and InvalidDecisionError. These exceptions help in identifying and handling errors that might occur due to invalid data or decisions within the program. Since the program is not dynamic and has limited user input, these custom exceptions are sufficient to handle most errors that may arise.

### Simulating Sensor Data ##  

To simulate sensor data, I used the random module to generate random values for the different sensor attributes. For example, the LaneDetectionSensor generates random lane statuses, lane widths, and road conditions. This random data simulates real-world variability and allows the program to handle different scenarios.

### Decision-Making ##  
The decision classes use the processed data from the sensors to make decisions about how the car should respond. For example, the LaneDetectionDecision class makes a decision based on the lane status, such as staying in the lane, driving cautiously, or slowing down. The decisions are designed to prioritize safety and ensure the car responds appropriately to its environment.

### OpenCV Integration ##   

In addition to the basic sensor and decision classes, I've also implemented an advanced version of the TrafficSignalRecognitionSensor class using OpenCV, a popular computer vision library. This class processes an image of a traffic signal and detects its color using color masking and contour detection. The corresponding TrafficSignalRecognitionDecisionCV class makes a decision based on the detected color of the traffic signal.

## Usage ##  
The program provides a simple menu for the user to choose which sensor to test. The user can select one of the following options:

- Lane Detection Sensor
- Obstacle Avoidance Sensor
- Traffic Signal Recognition Sensor
- Traffic Signal Recognition Sensor using OpenCV  

Based on the user's choice, the program processes the corresponding sensor data, makes a decision, and executes the decision using the Control class. The program logs information about the sensor data, decision, and any errors that occur during the process.

## Running ##

Before starting, you need to have [python 3](https://www.python.org/downloads/) installed.  
Alternatively, instead of using the terminal to run the program, you can also use an IDE like PyCharm or VSCode.
I have made use of **Python 3.10.10** in this project.  

The following libraries are required to run the program:
- OpenCV
- Numpy

To install the libraries, run the following command in the terminal:

```bash	
# Install the libraries
$ pip install opencv-python
$ pip install numpy
```

To run the program, follow the steps below:

```bash
# Clone this project
$ git clone https://github.com/nkosi-tauro/oop_system

# Access
$ cd oop_system\\system_implementation

# Run the project in the terminal
Linux/Mac:
$ python3 driverless_car.py

Windows:
$ python driverless_car.py

```

## Testing ##
For testing, I've used the `unittest` module to create unit tests for the different classes in the program. The tests check the functionality of the classes and ensure that the program works as expected.  

While in the `system_implementation` folder, run the following command in the terminal:  
Alternatively, instead of using the terminal to run the test file, you can also use an IDE like PyCharm or VSCode.

```bash
# Run the Tests in the terminal
Linux/Mac:
$ python3 driverless_car_unittest.py

Windows:
$ python driverless_car_unittest.py
```


## References and Resources ##  

The following references and resources were used to build this project:


Krishna, A. (Feb 2, 2022) Object-Oriented Programming in Python. *FreeCodeCamp*. Available at: [Object-Oriented Programming in Python](https://www.freecodecamp.org/news/object-oriented-programming-in-python/) [Accessed 20 March 2023]  

Ajitsaria, A. Logging in Python. *Real Python*. Available at: [Logging in Python](https://realpython.com/python-logging/) [Accessed 30 March 2023]  

Shaw, A. (Oct 22, 2018) Getting Started With Testing in Python. *Real Python*. Available from: [Getting Started With Testing in Python](https://realpython.com/python-testing/) [Accessed 01 April 2023]  



OpenCV Resources:  

[Multiple Color Detection in Real-Time using Python-OpenCV](https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/) (Geeks for Geeks, 2023) [Accessed 04 April 2023]  
[OpenCV-Python FreeCodeCamp Tutorial](https://www.youtube.com/watch?v=oXlwWbU8l2o) [Viewed 01 April 2023]  
[Image Processing in OpenCV](https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html) [Accessed 05 April 2023]    
[Color models and color spaces](https://programmingdesignsystems.com/color/color-models-and-color-spaces/index.html#:~:text=HSV%20is%20a%20cylindrical%20color,on%20the%20RGB%20color%20circle.)[Accessed 05 April 2023]   

## License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE) file.


Made with ❤️ by <a href="https://github.com/nkosi-tauro" target="_blank">Nkosilathi Tauro</a>


