"""Unit tests for the driverless car program."""

import unittest


# Importing only the classes that are needed for testing instead of a wildcard import
from driverless_car import (LaneDetectionSensor, ObstacleAvoidanceSensor,
                            TrafficSignalRecognitionSensor, LaneDetectionDecision,
                            ObstacleAvoidanceDecision, TrafficSignalRecognitionDecision)


class TestDriverlessCarProgram(unittest.TestCase):
    """Unit tests for the driverless car program."""

    def test_lane_detection_sensor(self):
        """Test the lane detection sensor."""
        sensor = LaneDetectionSensor()
        data = sensor.process_data()
        self.assertIsNotNone(data)
        self.assertIn('lane_status', data)

    def test_obstacle_avoidance_sensor(self):
        """Test the obstacle avoidance sensor."""
        sensor = ObstacleAvoidanceSensor()
        data = sensor.process_data()
        self.assertIsNotNone(data)
        self.assertIn('obstacle_type', data)

    def test_traffic_signal_recognition_sensor(self):
        """Test the traffic signal recognition sensor."""
        sensor = TrafficSignalRecognitionSensor()
        data = sensor.process_data()
        self.assertIsNotNone(data)
        self.assertIn('traffic_light_state', data)

    def test_lane_detection_decision(self):
        """Test the lane detection decision."""
        decision_maker = LaneDetectionDecision()
        data = {"lane_status": "Detected",
                "lane_width": 3.5, "road_condition": "Dry"}
        decision = decision_maker.make_decision(data)
        self.assertIsNotNone(decision)
        self.assertIn("Stay in Lane", decision)

    def test_obstacle_avoidance_decision(self):
        """Test the obstacle avoidance decision."""
        decision_maker = ObstacleAvoidanceDecision()
        data = {"obstacle_type": "Car",
                "distance_to_obstacle": 15, "relative_speed": -5}
        decision = decision_maker.make_decision(data)
        self.assertIsNotNone(decision)
        self.assertIn("Change Lane or Slow Down", decision)

    def test_traffic_signal_recognition_decision(self):
        """Test the traffic signal recognition decision."""
        decision_maker = TrafficSignalRecognitionDecision()
        data = {"traffic_light_state": "Green",
                "time_to_change": 5, "weather": "Sunny"}
        decision = decision_maker.make_decision(data)
        self.assertIsNotNone(decision)
        self.assertIn("Go", decision)


if __name__ == '__main__':
    unittest.main()
