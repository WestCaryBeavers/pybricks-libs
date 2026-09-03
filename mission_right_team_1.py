"""Example mission structure and a hub-button mission selector.

This is a template, not a finished program: copy the pattern, replace the
example missions with your own, and rename this file (or its contents) to
whatever your Pybricks project uses as its main file.
"""


import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait

from lib_robot import robot
from lib_movement_straight import drive_straight
from lib_movement_turning import turn_in_place, pivot_turn, turn_with_radius
from lib_movement_stopping import stop_all
from lib_attachment_control import run_by_degrees, home
from lib_sensor_gyro import reset_heading, wait_until_stationary


def mission():
    """for station #7, #11."""  
    reset_heading(0)
    drive_straight(690, speed = 400)
    turn_in_place(90)
    drive_straight(396, speed=200)
    turn_in_place(45)
    drive_straight(270, speed=75)
    run_by_degrees(robot.front_attachment, 150, speed=600)
    drive_straight(-50, speed=200)
    turn_in_place(90)
    drive_straight(400, speed=400)
    turn_in_place(45)
    drive_straight(500, speed=400)
    # run_by_degrees(robot.front_attachment, 90, speed=400)
    # turn_in_place(90)
    # drive_straight(200)
    # run_by_degrees(robot.front_attachment, -90, speed=400)
    # turn_in_place(-90)
    # drive_straight(-700)
    # home(robot.front_attachment, speed=-200, duty_limit=30)
    stop_all(then=Stop.HOLD)

if __name__ == "__main__":
    mission()
