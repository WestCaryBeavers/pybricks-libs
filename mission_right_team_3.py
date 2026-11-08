"""Example mission structure and a hub-button mission selector.

This is a template, not a finished program: copy the pattern, replace the
example missions with your own, and rename this file (or its contents) to
whatever your Pybricks project uses as its main file.
"""


import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait

import lib_config as config
from lib_robot import robot
from lib_movement_straight import drive_straight
from lib_movement_turning import turn_in_place, pivot_turn, turn_with_radius
from lib_movement_stopping import stop_all
from lib_attachment_control import run_by_degrees, home
from lib_sensor_gyro import reset_heading, wait_until_stationary

# negative means left, positive means right

def mission():
  config.require_active_team("right")
  #to_forest
  drive_straight(635, speed=600)
  turn_in_place(-90)
  #deposit
  drive_straight(40, speed=50)
  run_by_degrees(robot.right_team_front_attachment, -75, speed=80)
  turn_in_place(-10)
  run_by_degrees(robot.right_team_front_attachment, -100, speed=100)
  # mad_dash
  run_by_degrees(robot.right_team_front_attachment, 100, speed=25)
  drive_straight(-80, speed=600)
  turn_in_place(95)
  drive_straight(1050, speed=750)


if __name__ == "__main__":
  mission()