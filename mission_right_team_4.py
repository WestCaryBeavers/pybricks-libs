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
  #to_forest
  drive_straight(640, speed=600)
  turn_in_place(-90)
  #deposit
  drive_straight(40, speed=50)
  run_by_degrees(robot.front_attachment, -75, speed=25)
  # mad_dash
  run_by_degrees(robot.front_attachment, 90, speed=25)
  turn_in_place(-90)
  drive_straight(750, speed=750)


if __name__ == "__main__":
  mission()