# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long
"""
This python program is based on the design of the driverless car system. 
I used my original design classes then added on what I thought could be additional scenarios for the prgram to handle.

"""


"""
I chose to keep the design classes from my design document. I think that they are a good representation of the system that I am trying to create. 
As I'm not creating a true "dynamic" system, and also trying not to over complicate the program, I'm going to keep it simple. 
"""
# Initial design classes
class Sensor:
  """
  The sensor class will process incoming data from the various sensors on the car.(the sensor subclasses)
	"""
  pass


class Decision:
	"""
	The decision class will process the data from the sensors and make a decision on what to do next.
	"""
	pass


class Control:
	"""
	The control class will process the decision from the decision class and control the car accordingly.
	"""
	pass


# Exception classes
"""
Im implementing my own custom exception classes. This is because the program is not dynamic (limited user input), so I don't need to use the built in exception classes. Meaning there won't be any unforseen errors that the program could encounter (With exception to the ValueError class)
"""

class InvalidSensorDataError(Exception):
  """Handles any invalid sensor data errors"""
  pass


class InvalidDecisionError(Exception):
  """Handles any invalid decision errors"""
  pass

"""
The bulk of the program will consist of 2 Subclasses, the Sensor and Decision subclasses. These will be used to process the data from the sensors and make a decision on what to do next. Each Sensor subclass will have a corresponding Decision subclass.

So in a way simulating how the system would work in real life. 
Sensors such as Lane Detection, Obstacle Detection, etc. will be used to detect the environment around the car and pass on the data to the decision class. 
"""

# Sensor subclasses
class LaneDetectionSensor(Sensor):
  pass

class ObstacleAvoidanceSensor(Sensor):
  pass

class TrafficSignalRecognitionSensor(Sensor):
  pass


# Decision subclasses
class LaneDetectionDecision(Decision):
  pass

class ObstacleAvoidanceDecision(Decision):
  pass

class TrafficSignalRecognitionDecision(Decision):
  pass

