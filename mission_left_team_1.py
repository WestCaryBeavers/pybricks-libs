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
from lib_robot_left import activate
from lib_movement_straight import drive_straight
from lib_movement_turning import turn_in_place, pivot_turn, turn_with_radius
from lib_movement_stopping import stop_all
from lib_attachment_control import run_by_degrees, home, run_to_angle
from lib_sensor_gyro import reset_heading, wait_until_stationary
from mission_right_team_1 import mission

def front():
    return robot.left_team_front_attachment
def back():
    return robot.left_team_back_attachment

# drone and the seed retrieval
def mission_1():
    activate()

    reset_heading(0)
    # to the drone
    drive_straight(-750,speed=190)
    drive_straight( 50, speed=100)
    drive_straight(-50, speed=100)
    # swing the arm to push the drone into base
    run_by_degrees(back(), 120, speed=500, wait=False)
    turn_in_place(-30)
    drive_straight(10,speed=200)
    turn_in_place(40)
    # back out
    drive_straight(400,speed=400)
    # turn toward the tree for the seed retrieval
    turn_with_radius(75, 130)  
    # back off to give more room for the bucket
    drive_straight(-20, speed=500)
    # lower the bucket
    run_by_degrees(front(), 200, speed=500)
    drive_straight(65, speed=200)
    # raise the bucket
    run_by_degrees(front(), -100, speed=500, wait=False)
    wait(400)
    # start backing off to peel off the seed
    drive_straight(-50, speed=90)
    # go to home base
    drive_straight(-300)

# rock flip, vine untangle
def mission_2():
    activate()
    # to the rock
    drive_straight(-300, speed=500)
    drive_straight(-180, speed=170)
    drive_straight(150, speed=500)
    turn_with_radius(-80, 180)
    # lower the arm all the way down
    home(front(), speed=200)
    # drive to the vine
    drive_straight(490, speed=500)
    # raise to the vine level and insert the bar into the hole
    run_by_degrees(front(), -40, speed=200)
    turn_in_place(15)    
    # start untangle step by step
    run_by_degrees(front(), -40)
    drive_straight(-20, speed=300)
    drive_straight(140, speed=300)
    turn_in_place(-15)
    drive_straight(-770, speed=1000)

if __name__ == "__main__":
    #run_mission_selector()
    mission_2()
