"""Example mission structure and a hub-button mission selector.

This is a template, not a finished program: copy the pattern, replace the
example missions with your own, and rename this file (or its contents) to
whatever your Pybricks project uses as its main file.
"""

#Note:the placing of the robot is on the left white mat. with the dumpster arm on the middle line of the bold luines 1 and 2 facing the mission.


import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait

from lib_robot import robot
from lib_movement_straight import drive_straight
from lib_movement_turning import turn_in_place, pivot_turn, turn_with_radius
from lib_movement_stopping import stop_all
from lib_attachment_control import reset_position, run_by_degrees, home, run_to_angle
from lib_sensor_gyro import reset_heading, wait_until_stationary


def mission_4_checkseed():
    home(robot.front_attachment)
    run_to_angle(robot.front_attachment, 70, speed=100)
    drive_straight(180,speed=200) 
    turn_in_place(-90)  # Example turn, adjust the angle as needed
    drive_straight(670,speed=300)  # Example additional movement
    turn_in_place(-35)  # Example turn, adjust the angle as needed
    drive_straight(60,speed=100)  # Example additional movement
    run_by_degrees(robot.front_attachment, -70, speed=30)
    wait(500)
    run_by_degrees(robot.front_attachment, 90, speed=30)
    turn_in_place(30)
    drive_straight(-670, speed=200)  # Example additional movement


def mission_4_grabseed():
    home(robot.front_attachment)
    run_to_angle(robot.front_attachment, 10, speed=100)
    drive_straight(280,speed=200) 
    turn_in_place(-90)  # Example turn, adjust the angle as needed
    drive_straight(650,speed=300)  # Example additional movement
    turn_in_place(-47)  # Example turn, adjust the angle as needed
    drive_straight(70,speed=100)  # Example additional movement
    run_to_angle(robot.front_attachment, 50, speed=100)
    drive_straight(-70,speed=300)  # Example additional movement
    turn_in_place(47)  # Example turn, adjust the angle as needed
    drive_straight(-650,speed=300) 


if __name__ == "__main__":
# run_mission_selector()
    mission_4_checkseed()
    # change arms
    mission_4_grabseed()
