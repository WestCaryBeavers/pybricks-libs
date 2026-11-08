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
    return robot.left_team_front_attachment
def back():
    return robot.left_team_back_attachment

# back line at back
def mission_1():
    run_by_degrees(back(), 100, speed=300)
    reset_heading(0)
    drive_straight(-750,speed=190)
    drive_straight( 50, speed=100)
    drive_straight(-50, speed=100)
    run_by_degrees(front(), 120, speed=500, wait=False)
    #run_by_degrees(front(), 50, speed=100)
    # run_by_degrees(front(), -60, speed=100)
    # drive_straight(740,speed=200) 
    # Example additional movement
    # not doing this part
    #drive_straight(50,speed=100)
    #run_by_degrees(front(), -50, speed=100)  # Example additional movement
    turn_in_place(-80)  # Example turn, adjust the angle as needed
    drive_straight(10,speed=200)  # Example additional movement
    turn_in_place(80)
    drive_straight(740,speed=200)  # Example additional movement

def mission_1_2():
    #run_by_degrees(front(), -50, speed=300)
    home(front(), -200)
    reset_heading(0)
    drive_straight(-750,speed=190)
    drive_straight( 50, speed=100)
    drive_straight(-50, speed=100)
    run_by_degrees(back(), 120, speed=500, wait=False)
    turn_in_place(-30)  # Example turn, adjust the angle as needed
    drive_straight(10,speed=200)  # Example additional movement
    turn_in_place(40)
    drive_straight(500,speed=400)
    turn_with_radius(100,145)  
    run_by_degrees(front(), 200, speed=500)  # Example additional movement
    drive_straight(75,speed=200)
    run_by_degrees(front(), -100, speed=500, wait=False)
    drive_straight(-50,speed=90)
    drive_straight(-300)
    #run_by_degrees(front(), 200, speed=500, wait=False)


# aline on first line wheel on side line
def mission_2():
# mision 2
    run_by_degrees(back(), -30, speed=300)
    drive_straight(-200, speed=500)
    turn_in_place(-45)
    drive_straight(-350, speed=170)  # Example movement after lowering the attachment
    #run_by_degrees(front(), -90, speed=500)
    run_by_degrees(back(), -100, speed=100, wait=False)
    drive_straight(50, speed=80)
    drive_straight(300, speed=800)
    front().run_target(300, 30,)
    #run_by_degrees(front(), 100, speed=300)
    
def mission_3():
# mission 3, left side at side line
    #run_by_degrees(front(), -150, speed=300)
    drive_straight(-400, speed=300)
    drive_straight(400, speed=300)
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


def mission_4_checkseed():
    home(front())
    # run_to_angle(robot.left_team_front_attachment, -70, speed=100)
    drive_straight(180,speed=200) 
    turn_in_place(-90)  # Example turn, adjust the angle as needed
    drive_straight(690,speed=300)  # Example additional movement
    turn_in_place(-50)  # Example turn, adjust the angle as needed
    drive_straight(60,speed=100)  # Example additional movement
    run_by_degrees(front(), 155, speed=30)
    wait(500)
    run_by_degrees(front(), -130, speed=100)
    turn_in_place(30)
    drive_straight(-470, speed=200)  # Example additional movement
    turn_in_place(90)
    drive_straight(-350, speed=400)


def mission_4_grabseed():
    home(front())
    run_to_angle(front(), 10, speed=100)
    drive_straight(280,speed=200) 
    turn_in_place(-90)  # Example turn, adjust the angle as needed
    drive_straight(650,speed=300)  # Example additional movement
    turn_in_place(-47)  # Example turn, adjust the angle as needed
    drive_straight(70,speed=100)  # Example additional movement
    run_to_angle(front(), 50, speed=100)
    drive_straight(-70,speed=300)  # Example additional movement
    turn_in_place(47)  # Example turn, adjust the angle as needed
    drive_straight(-650,speed=300) 

def mission_5():
    print("mission 5")
    home(front(), speed=100)
    run_to_angle(front(), -30, speed=500)
    drive_straight(175, speed=300)
    turn_in_place(-90)
    drive_straight(770, speed=275)
    run_by_degrees(front(), -20, speed=500)
    turn_in_place(15)    
    run_by_degrees(front(), -40)
    drive_straight(-20, speed=300)
    run_by_degrees(front(), 30, speed=100)
    drive_straight(-30, speed=300)
    run_by_degrees(front(), -40, speed=50)
    drive_straight(150, speed=100)
    drive_straight(-770, speed=275)
    
def mission_4():
    mission_4_checkseed()
    wait(1000)
    # change arms
    mission_4_grabseed()

def mission_3_5():
    drive_straight(-400, speed=200)
    drive_straight(70, speed=500)
    turn_with_radius(-93, 180)
    home(front(),200)
    run_by_degrees(front(),-30,speed=500)
    drive_straight(430, speed=500)
    run_by_degrees(front(), -20, speed=500)
    turn_in_place(15)    
    run_by_degrees(front(), -40)
    drive_straight(-20, speed=300)
    run_by_degrees(front(), 30, speed=100)
    drive_straight(-30, speed=300)
    run_by_degrees(front(), -40, speed=50)
    drive_straight(150, speed=300)
    turn_in_place(-15)
    drive_straight(-770, speed=500)
    

def testing():
    turn_with_radius(-100, 180)
    drive_straight(front(),125)

if __name__ == "__main__":
    #run_mission_selector()
    mission_3_5()
