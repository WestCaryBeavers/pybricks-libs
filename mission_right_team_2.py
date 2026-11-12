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
from lib_attachment_control import run_by_degrees, home, run_to_angle
from lib_sensor_gyro import reset_heading, wait_until_stationary

# negative means left, positive means right

def mission():
    activate()
    # lower the arm to the floor
    # run_by_degrees(robot.right_team_front_attachment, -100, speed=400)
    home(robot.right_team_front_attachment, speed=-200)
    # raise to the ring level
    run_by_degrees(robot.right_team_front_attachment, 35, speed=100)
    # drive to the ring and insert
    drive_straight(90, speed=300)
    # lift up the ring
    run_by_degrees(robot.right_team_front_attachment, 15, speed=100)
    # back off to bring to the post
    drive_straight(-160, speed=75)
    # release and back off
    turn_in_place(10, wait=False)
    run_by_degrees(robot.right_team_front_attachment, -20, speed=25)
    # from from the ring
    drive_straight(-30, speed=200)

    # turn to the deposit box
    run_by_degrees(robot.right_team_front_attachment, 90, speed=400)
    turn_with_radius(radius_mm=-150, angle_deg=100)
    drive_straight(420, speed=600)
    turn_in_place(90)
    #deposit
    drive_straight(-150, speed=200)
    run_by_degrees(robot.right_team_back_attachment, -75, speed=80)
    run_by_degrees(robot.right_team_back_attachment, -50, speed=100)
    # mad_dash
    run_by_degrees(robot.right_team_back_attachment, 100, speed=500)
    drive_straight(80, speed=600)
    turn_in_place(90)
    drive_straight(-700, speed=750, then=Stop.NONE)
    turn_with_radius(radius_mm=300, angle_deg=-90)

    
    stop_all(then=Stop.HOLD)

if __name__ == "__main__":
    mission()

