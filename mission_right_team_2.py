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

# negative means left, positive means right

def mission():
    run_by_degrees(robot.front_attachment, 17, speed=100)
    drive_straight(331, speed=300)
    run_by_degrees(robot.front_attachment, 15, speed=100)
    drive_straight(-170, speed=75)
    turn_in_place(10, wait=False)
    run_by_degrees(robot.front_attachment, -20, speed=25)
    drive_straight(-150, speed=200)
    
    stop_all(then=Stop.HOLD)

if __name__ == "__main__":
    mission()

