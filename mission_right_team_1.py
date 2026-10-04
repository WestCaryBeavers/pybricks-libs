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

def mission_1():
    """for station #7, #11."""  
    #seed_part
    reset_heading(0) 
    drive_straight(470, speed = 400)
    turn_in_place(45)
    drive_straight(130, speed=200)
    turn_in_place(-45)
    #to_ant
    drive_straight(150, 100)
    turn_in_place(90)
    drive_straight(280, speed=300)
    turn_in_place(45)
    drive_straight(300, speed=75)
    #flip_fungus
    run_by_degrees(robot.front_attachment, 150, speed=700)
    #to_roots
    drive_straight(-50, speed=200)
    turn_in_place(90)
    drive_straight(400, speed=400)
    turn_in_place(45)
    #to_tree_support
    drive_straight(-260, speed=400)
    turn_in_place(90)
    run_by_degrees(robot.back_attachment, 130, speed=600)
    drive_straight(-140, speed=200)
    run_by_degrees(robot.back_attachment, -200, speed=700)
    #to_greenhouse
    drive_straight(40, speed=300)
    turn_in_place(-30)
    #open_compost
    run_by_degrees(robot.back_attachment, 200, speed=600)
    drive_straight(45, speed=100)
    turn_in_place(-10)
    #uncover_nest
    run_by_degrees(robot.back_attachment, -90, speed=50)
    run_by_degrees(robot.front_attachment, 45, speed=100)
    drive_straight(30, speed=200)
    #end_mission
    turn_in_place(-45)
    drive_straight(750, speed=200)

def mission_2():
    run_by_degrees(robot.front_attachment, -35, speed=700)
    drive_straight(220, speed=700)
    run_by_degrees(robot.front_attachment, 20, speed=700)
    drive_straight(100, speed=300)
    run_by_degrees(robot.front_attachment, -60, speed=700)


    stop_all(then=Stop.HOLD)

if __name__ == "__main__":
    mission_2()
