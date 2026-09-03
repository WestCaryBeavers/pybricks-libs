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
from lib_attachment_control import run_by_degrees, home
from lib_sensor_gyro import reset_heading, wait_until_stationary


def mission_1():
    run_by_degrees(robot.front_attachment, 30, speed=100)
    run_by_degrees(robot.front_attachment, 20, speed=100)
    drive_straight(-715,speed=200) 
    drive_straight(75,speed=700)  # Example additional movement
    drive_straight(-30,speed=100)  # Example additional movement
    turn_in_place(-30)
    drive_straight(-100,speed=200)
    turn_in_place(-30)


#position of robot:on side, click on wheels aligned with the 2nd bold line of the white mat.
def mission_2():
    run_by_degrees(robot.front_attachment, -90, speed=300)
    drive_straight(-200, speed=200)  # Example movement after lowering the attachment
    run_by_degrees(robot.front_attachment, 60, speed=500)


if __name__ == "__main__":
# run_mission_selector()
    mission_2()

    
