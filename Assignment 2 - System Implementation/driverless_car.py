"""
This python program is based on the design of the driverless car system.
I used my original design classes then added on 
what I thought could be additional scenarios for the prgram to handle.
"""

import random
from abc import ABC, abstractmethod


# I chose to keep the design classes from my design document.
# I think that they are a good representation of the system that I am trying to create.
# As I'm not creating a true "dynamic" system,
# and also trying not to over complicate the program, I'm going to keep it simple.

# Initial design classes
class Sensor(ABC):
    """
    The sensor class will process incoming data from the various sensors on the car.
    """
    @abstractmethod
    def process_data(self):
        "processes the data from the sensors."


class Decision(ABC):
    """The decision class will process the data from the sensors."""
    @abstractmethod
    def make_decision(self, data):
        "makes a decision based on the data from the sensors."


class Control:
    """
    The control class will process the decision from the decision class 
    and control the car accordingly.
    """

    def __init__(self):
        self.sensor_data = {}

    def execute_decision(self, decision):
        """Executes the decision from the decision classes."""
        self.sensor_data[decision] = decision
        print(f"Executing decision: {decision}")


# Exception classes

#Im implementing my own custom exception classes.
# This is because the program is not dynamic (limited user input),
# so I don't need to use the built in exception classes.
# Meaning there won't be any unforseen errors that the program could encounter
# (With exception to the ValueError class)



class InvalidSensorDataError(Exception):
    """Handles any invalid sensor data errors"""


class InvalidDecisionError(Exception):
    """Handles any invalid decision errors"""


# """
# The bulk of the program will consist of 2 Subclasses, the Sensor and Decision subclasses.
# These will be used to process the data from the sensors and make a decision on what to do next.
# Each Sensor subclass will have a corresponding Decision subclass.

# So in a way simulating how the system would work in real life.
# Sensors such as Lane Detection, Obstacle Detection, etc.
# will be used to detect the environment around the car and pass on the data to the decision class.
# """

# Sensor subclasses


class LaneDetectionSensor(Sensor):
    """
    The Lane Detection Sensor class will process data 
    and pass it on to the corresponding decision class.
    """

    def process_data(self):
        try:
            lane_data = {
                "lane_status": random.choice(["Detected", "Not Detected", "Not Defined"]),
                "lane_width": random.randint(1, 10),
                "road_condition": random.choice(["Dry", "Wet", "Snowy", "Icy"]),
            }
            if not lane_data:
                raise InvalidSensorDataError(
                    "Lane detection data is empty or invalid.")
            return lane_data
        except InvalidSensorDataError as err:
            print(err)
            return {}


class ObstacleAvoidanceSensor(Sensor):
    """The Obstacle Avoidance Sensor class will process data and pass it on to the corresponding decision class."""

    def process_data(self):
        try:
            obstacle_data = {
                # I'm using random.choice to randomly select a value from the list. This will simulate the sensor detecting a car or pedestrian.
                # I could add more choices to the list to make it more realistic, but for now I will keep it Car or Pedestrian.
                "obstacle_type": random.choice(["Pedestrian", "Car"]),
                "distance_to_obstacle": 15,
                "relative_speed": -5,
            }
            if not obstacle_data:
                raise InvalidSensorDataError(
                    "Obstacle avoidance data is empty or invalid.")
            return obstacle_data
        except InvalidSensorDataError as err:
            print(err)
            return {}


class TrafficSignalRecognitionSensor(Sensor):
    """The Traffic Signal Recognition Sensor class will process data and pass it on to the corresponding decision class."""

    def process_data(self):
        try:
            traffic_data = {
                "traffic_light_state": random.choice(["Red", "Green", "Yellow"]),
                "time_to_change": 5,
                "weather": "Sunny"
            }
            if not traffic_data:
                raise InvalidSensorDataError(
                    "Traffic signal recognition data is empty or invalid.")
            return traffic_data
        except InvalidSensorDataError as err:
            print(err)
            return {}

# Decision subclasses


class LaneDetectionDecision(Decision):
    """The Lane Detection Decision class will process the data from the Lane Detection Sensor"""

    def make_decision(self, data):
        try:
            if not data:
                raise InvalidDecisionError(
                    "Invalid data for lane detection decision.")
            if data["lane_status"] == "Detected":
                return f"Stay in Lane (Width: {data['lane_width']}m, Road Condition: {data['road_condition']})"
            elif data["lane_status"] == "Not Detected":
                return "Drive Cautiously, Lane Not Defined"
            elif data["lane_status"] == "Not Defined":
                return "Slow Down, Lane Not Detected"
            else:
                raise InvalidDecisionError("Unable to determine lane status.")
        except InvalidDecisionError as err:
            print(err)
            return "Unable to determine lane status."


class ObstacleAvoidanceDecision(Decision):
    """The obstacle avoidance decision class will process the data from the obstacle avoidance sensor."""

    def make_decision(self, data):
        try:
            if not data:
                raise InvalidDecisionError(
                    "Invalid data for obstacle avoidance decision.")
            if data["obstacle_type"] == "Pedestrian":
                return f"Slow Down and Wait for Pedestrian (Distance: {data['distance_to_obstacle']}m, Relative Speed: {data['relative_speed']}km/h)"
            elif data["obstacle_type"] == "Car":
                return f"Change Lane or Slow Down (Distance: {data['distance_to_obstacle']}m, Relative Speed: {data['relative_speed']}km/h)"
            else:
                raise InvalidDecisionError("No obstacle detected.")
        except InvalidDecisionError as err:
            print(err)
            return "Error: The obstacle avoidance sensor is not working properly. Applying brakes, The vehicle will slow down and wait for recalibration."


class TrafficSignalRecognitionDecision(Decision):
    """ The traffic signal recognition decision class will process the data from the traffic signal recognition sensor."""

    def make_decision(self, data):
        try:
            if not data:
                raise InvalidDecisionError(
                    "Invalid data for traffic signal recognition decision.")
            if data["traffic_light_state"] == "Red":
                return f"Stop (Time to Change: {data['time_to_change']}s, Weather: {data['weather']})"
            elif data["traffic_light_state"] == "Yellow":
                return f"Slow Down (Time to Change: {data['time_to_change']}s, Weather: {data['weather']})"
            elif data["traffic_light_state"] == "Green":
                return f"Go (Time to Change: {data['time_to_change']}s, Weather: {data['weather']})"
            else:
                raise InvalidDecisionError(
                    "Unable to determine traffic light state.")
        except InvalidDecisionError as err:
            print(err)
            return "Unable to determine traffic light state."


# Main program
def start_driverless_car(choice):
    """Starts the driverless car"""
    # initiate the subclasses
    # sensor classes
    try:
        lane_sensor = LaneDetectionSensor()
        obstacle_sensor = ObstacleAvoidanceSensor()
        traffic_sensor = TrafficSignalRecognitionSensor()

        # decision classes
        lane_decision = LaneDetectionDecision()
        obstacle_decision = ObstacleAvoidanceDecision()
        traffic_decision = TrafficSignalRecognitionDecision()

        control = Control()
        # Instead of using if-else statements, I'm using a list to store the sensor and decision classes.
        # I find this method easier to read.
        if choice in range(1, 4):
            sensors = [lane_sensor, obstacle_sensor, traffic_sensor]
            decisions = [lane_decision, obstacle_decision, traffic_decision]

            sensor_data = sensors[choice - 1].process_data()
            decision = decisions[choice - 1].make_decision(sensor_data)
            control.execute_decision(decision)
        else:
            raise ValueError("Invalid choice.")
    except ValueError as err:
        print(err)
        return

# I decided to create a helper function to handle the user input menu options.
# This was done to clean up the main program.
def get_user_choice():
    """Gets the user's choice from the menu"""	
    print("\nWelcome to the Driverless Car Program (Tesla Home Edition))\n")
    print("Please select a sensor to test:")
    print("1. Lane Detection Sensor")
    print("2. Obstacle Avoidance Sensor")
    print("3. Traffic Signal Recognition Sensor")
    print("4. Exit\n")
    # Additional error handling to incase user enters a string.
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")
        return get_user_choice()

if __name__ == "__main__":
    while True:
        user_choice = get_user_choice()
        if user_choice == 4:
            break
        start_driverless_car(user_choice)
