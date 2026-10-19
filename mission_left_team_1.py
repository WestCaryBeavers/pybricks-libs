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
from lib_attachment_control import run_by_degrees, home, run_to_angle
from lib_sensor_gyro import reset_heading, wait_until_stationary

def front():
    return robot.front_attachment
def mission_1_2():
    mission_1()
    mission_2()

# back line at back
def mission_1():
    #run_by_degrees(front(), 50, speed=100)
    run_by_degrees(front(), -60, speed=100)
    drive_straight(740,speed=200) 
    drive_straight(-740,speed=700)  # Example additional movement
    # not doing this part
    #drive_straight(50,speed=100)
    #run_by_degrees(front(), -50, speed=100)  # Example additional movement
    #turn_in_place(-30)
    #drive_straight(50,speed=200)
    #turn_in_place(-40)


# aline on back line wheel on side line
def mission_2():
# mision 2
    front().run_target(300, 30,)
    #run_by_degrees(front(), -30, speed=300)
    drive_straight(115, speed=500)
    turn_in_place(-45)
    drive_straight(410, speed=200)  # Example movement after lowering the attachment
    #run_by_degrees(front(), -90, speed=500)
    run_by_degrees(front(), -20, speed=100, wait=False)
    drive_straight(-50, speed=80)
    drive_straight(-300, speed=800)
    front().run_target(300, 30,)
    #run_by_degrees(front(), 100, speed=300)
    
def mission_3():
# mission 3, left side at side line
    run_by_degrees(front(), -150, speed=300)
    drive_straight(450, speed=300)
    drive_straight(-450, speed=300)
    #run_by_degrees(front(), 30, speed=300)
    #run_by_degrees(front(), -100, speed=300)
    #drive_straight(370, speed=300)
    #run_by_degrees(front(), 40, speed=300)
    #drive_straight(-100, speed=500, wait=False)
    #run_by_degrees(front(), 40, speed=200)
    #run_by_degrees(front(), -90, speed=300)
    #drive_straight(100, speed=300)
    #run_by_degrees(front(), 40, speed=300)
    #drive_straight(-100, speed=500, wait=False)
    #run_by_degrees(front(), 80, speed=200)
    #drive_straight(-280, speed=300)

def testing():
    run_by_degrees(front(), -200, speed=300)
if __name__ == "__main__":
# run_mission_selector()
    drive_straight(100, speed=300, wait=False)

def mission_4_checkseed():
    home(robot.front_attachment)
    run_to_angle(robot.front_attachment, 70, speed=100)
    drive_straight(180,speed=200) 
    turn_in_place(-90)  # Example turn, adjust the angle as needed
    drive_straight(670,speed=300)  # Example additional movement
    turn_in_place(-35)  # Example turn, adjust the angle as needed
    drive_straight(60,speed=100)  # Example additional movement
    run_by_degrees(robot.front_attachment, -70, speed=30)
    wait(500)
    run_by_degrees(robot.front_attachment, 90, speed=30)
    turn_in_place(30)
    drive_straight(-670, speed=200)  # Example additional movement


def mission_4_grabseed():
    home(robot.front_attachment)
    run_to_angle(robot.front_attachment, 10, speed=100)
    drive_straight(280,speed=200) 
    turn_in_place(-90)  # Example turn, adjust the angle as needed
    drive_straight(650,speed=300)  # Example additional movement
    turn_in_place(-47)  # Example turn, adjust the angle as needed
    drive_straight(70,speed=100)  # Example additional movement
    run_to_angle(robot.front_attachment, 50, speed=100)
    drive_straight(-70,speed=300)  # Example additional movement
    turn_in_place(47)  # Example turn, adjust the angle as needed
    drive_straight(-650,speed=300) 

def mission_5():
    run_by_degrees(front(), 100, speed=300)
    drive_straight(180, speed=300)
    turn_in_place(-90)
    drive_straight(710, speed=275)
    run_by_degrees(front(),-35, 45,)
    turn_in_place(20)
    drive_straight(-70, speed=300)
    run_by_degrees(front(),-50, 50)
    drive_straight(175, speed=50)

if __name__ == "__main__":
# run_mission_selector()
    mission_4_checkseed()
    # change arms
    mission_4_grabseed()