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
    """for station #7, #11."""
    activate()
    # to ant
    run_by_degrees(robot.right_team_front_attachment, 120, wait=False)
    drive_straight(480, speed=600)
    turn_with_radius(radius_mm=250, angle_deg=137)
    # lower the arm half way
    run_by_degrees(robot.right_team_front_attachment, -100, wait=False)
    drive_straight(80, speed=200)
    drive_straight(115, speed=50)
    #flip_fungus
    run_by_degrees(robot.right_team_front_attachment, 150, speed=500)
    #to_roots
    drive_straight(-40, speed=200)
    turn_in_place(90)
    drive_straight(400, speed=400)
    turn_in_place(45)
    #to_tree_support
    drive_straight(-270, speed=400)
    run_by_degrees(robot.back_attachment, 130, speed=600, wait=False)
    turn_in_place(90)
    drive_straight(-140, speed=200)
    run_by_degrees(robot.back_attachment, -55, speed=900)
    #to_greenhouse
    drive_straight(40, speed=300)
    turn_in_place(-35)
    #open_compost
    run_by_degrees(robot.back_attachment, 200, speed=600)
    drive_straight(45, speed=100)
    turn_in_place(-10)
    #uncover_nest
    run_by_degrees(robot.back_attachment, -65, speed=30)
    run_by_degrees(robot.back_attachment, 50, speed=30)
    #end_mission
    turn_with_radius(radius_mm=-300, angle_deg=120)


if __name__ == "__main__":
    mission()
