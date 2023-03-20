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

