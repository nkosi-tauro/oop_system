"""
This python program is based on the design of the driverless car system.
I used my original design classes then added on 
what I thought could be additional scenarios for the prgram to handle.
"""
# pylint: disable=maybe-no-member
import random
from abc import ABC, abstractmethod
import numpy as np
import cv2

import logging

# Setting up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s: %(message)s')

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
        print(f"\nExecuting decision: {decision}")


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
            logging.error(err)
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
            logging.error(err)
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
            logging.error(err)
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
            logging.error(err)
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
            logging.error(err)
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
            logging.error(err)
            return "Unable to determine traffic light state."

# This version of the Traffic Signal Recognition Decision class is a bit more complex than the others.
# It utilizies the OpenCV library to detect the color of the traffic light.
class TrafficSignalRecognitionSensorCV(Sensor):
    """
    The Traffic Signal Recognition Sensor class will process data
    and pass it on to the corresponding decision class.
    """

    def process_data(self):
        """
        Use trafficstop.jpg to test for red
        Use trafficgo.jpg to test for green
        Use trafficslow.jpg to test for yellow
        One may need to adjust the HSV values to improve accuracy for other images
        """
        # Important: Please note depending on whether you are using a Mac\Linux or Windows machine,
        # you may need to change the path to the image file (Relative or Absolute Path).
        image = cv2.imread("Assignment 2 - System Implementation\\trafficgo.jpg")
        logging.info("Processing traffic recognition sensor data...")
        try:
            # Convert camera data to HSV format for better color detection
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            # Define color ranges for red, green, and yellow signals
            red_lower = np.array([0, 70, 50])
            red_upper = np.array([5, 255, 255])
            red_lower2 = np.array([175, 70, 50])
            red_upper2 = np.array([180, 255, 255])
            green_lower = np.array([35, 50, 50])
            green_upper = np.array([80, 255, 255])
            yellow_lower = np.array([15, 100, 100])
            yellow_upper = np.array([40, 255, 255])
            red_mask = cv2.inRange(hsv, red_lower, red_upper)
            red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
            red_mask = cv2.bitwise_or(red_mask, red_mask2)
            green_mask = cv2.inRange(hsv, green_lower, green_upper)
            yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
            # Combine masks to get final signal detection
            mask = cv2.bitwise_or(cv2.bitwise_or(
                red_mask, green_mask), yellow_mask)

            # Find contours in the image and extract the largest one
            contours, _ = cv2.findContours(
                mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                color = ""
                largest_contour = max(contours, key=cv2.contourArea)
                if cv2.contourArea(largest_contour) > 1000:
                    x, y, w, h = cv2.boundingRect(largest_contour)
                    # Determine the color of the bounding box based on the detected color
                    if cv2.countNonZero(red_mask[y:y+h, x:x+w]) > 0:
                        color = 'red'
                    elif cv2.countNonZero(green_mask[y:y+h, x:x+w]) > 0:
                        color = 'green'
                    elif cv2.countNonZero(yellow_mask[y:y+h, x:x+w]) > 0:
                        color = 'yellow'

                return {"traffic_signal": color}

            else:
                logging.warning("No traffic signal detected.")
                return {"traffic_signal": "none"}
        except InvalidSensorDataError as err:
            logging.error("Error processing data from traffic sensor: %s", err)
            return {}

class TrafficSignalRecognitionDecisionCV(Decision):
    """ 
    The traffic signal recognition decision class will process 
    the data from the traffic signal recognition sensor.
    """

    def make_decision(self, data):
        try:
            if not data:
                raise InvalidDecisionError(
                    "Invalid data for traffic signal recognition decision.")
            if data["traffic_signal"] == "red":
                return "Stop"
            elif data["traffic_signal"] == "yellow":
                return "Slow Down"
            elif data["traffic_signal"] == "green":
                return "Go"
            else:
                raise InvalidDecisionError(
                    "Unable to determine traffic light state.")
        except InvalidDecisionError as err:
            logging.error(err)
            return "Unable to determine traffic light state." 

# Main program
def start_driverless_car(choice):
    """Starts the driverless car"""
    try:
        lane_sensor = LaneDetectionSensor()
        obstacle_sensor = ObstacleAvoidanceSensor()
        traffic_sensor = TrafficSignalRecognitionSensor()
        traffic_sensor_cv = TrafficSignalRecognitionSensorCV()

        lane_decision = LaneDetectionDecision()
        obstacle_decision = ObstacleAvoidanceDecision()
        traffic_decision = TrafficSignalRecognitionDecision()
        traffic_decision_cv = TrafficSignalRecognitionDecisionCV()

        control = Control()



        if choice in range(1, 5):
            sensor_classes = [lane_sensor, obstacle_sensor, traffic_sensor, traffic_sensor_cv]
            decision_classes = [lane_decision, obstacle_decision, 
                                traffic_decision, traffic_decision_cv]

            sensor_data = sensor_classes[choice - 1].process_data()
            decision = decision_classes[choice - 1].make_decision(sensor_data)


            # Logging Output
            sensor = sensor_classes[choice - 1] # get which sensor class was active
            dec = decision_classes[choice - 1] # get which decision class was active
            logging.info("Sensor: %s, Decision: %s",
                        sensor.__class__.__name__, dec.__class__.__name__)
            logging.info("Raw data: %s", sensor_data)
            logging.info("Analysis result: %s", decision)

            control.execute_decision(decision)
        else:
            raise ValueError("Invalid choice.")
    except ValueError as err:
        logging.error(err)
        return

def get_user_choice():
    """Gets the user's choice from the menu"""    
    print("\nWelcome to the Driverless Car Program (Tesla Home Edition))\n")
    print("Please select a sensor to test:")
    print("1. Lane Detection Sensor")
    print("2. Obstacle Avoidance Sensor")
    print("3. Traffic Signal Recognition Sensor")
    print("4. Traffic Signal Recognition Sensor using OpenCV")
    print("5. Exit\n")
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        logging.error("Invalid choice. Please enter a number between 1 and 4.")
        return get_user_choice()

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(filename="driverless_car.log", level=logging.ERROR)

    while True:
        user_choice = get_user_choice()
        if user_choice == 5:
            break
        start_driverless_car(user_choice)
