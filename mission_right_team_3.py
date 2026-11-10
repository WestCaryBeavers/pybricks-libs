"""Example mission structure and a hub-button mission selector.

This is a template, not a finished program: copy the pattern, replace the
example missions with your own, and rename this file (or its contents) to
whatever your Pybricks project uses as its main file.
"""


import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait

from lib_robot import robot
from lib_robot_right import activate
from lib_movement_straight import drive_straight
from lib_movement_turning import turn_in_place, pivot_turn, turn_with_radius
from lib_movement_stopping import stop_all
from lib_attachment_control import run_by_degrees, home
from lib_sensor_gyro import reset_heading, wait_until_stationary

# negative means left, positive means right

def mission():
  activate()
  #to_forest
  drive_straight(640, speed=600)
  turn_in_place(-90)
  #deposit
  drive_straight(100, speed=50)
  run_by_degrees(robot.right_team_front_attachment, -75, speed=80)
  run_by_degrees(robot.right_team_front_attachment, -50, speed=100)
  # mad_dash
  run_by_degrees(robot.right_team_front_attachment, 100, speed=500)
  drive_straight(-80, speed=600)
  turn_in_place(90)
  drive_straight(700, speed=750, then=Stop.NONE)
  turn_with_radius(radius_mm=-300, angle_deg=90)

  stop_all(then=Stop.HOLD)


if __name__ == "__main__":
  mission()