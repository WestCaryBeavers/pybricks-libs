"""Check that drive_straight() distances are accurate.

Distance comes from wheel rotation times WHEEL_DIAMETER_MM in lib_config.py.
The gyro does not correct distance, so if the diameter is off by 1 mm, every
500 mm drive is off by about 9 mm.

How to use:
  1. Mark the floor at the front of the robot (tape or a ruler).
  2. Run this program. The robot drives TEST_DISTANCE_MM forward slowly.
  3. Measure how far it actually went, in mm.
  4. Update WHEEL_DIAMETER_MM in lib_config.py using the printed formula,
     and run again until the robot lands within 1-2 mm.
Run it on the same surface you compete on (the mat), since tires grip
differently on tables.
"""

from lib_robot import robot
from lib_movement_straight import drive_straight
from lib_sensor_gyro import reset_heading, wait_until_gyro_ready
import lib_config as config

TEST_DISTANCE_MM = 1000

print("Keep the robot still while the gyro calibrates...")
wait_until_gyro_ready()
reset_heading(0)
robot.hub.speaker.beep(frequency=800, duration=150)

drive_straight(TEST_DISTANCE_MM, speed=150)

print("Done. Measure the distance actually driven (mm), then set:")
print("  WHEEL_DIAMETER_MM = {} * measured / {}".format(config.WHEEL_DIAMETER_MM, TEST_DISTANCE_MM))
print("Example: if it drove 990 mm, WHEEL_DIAMETER_MM = {:.2f}".format(
    config.WHEEL_DIAMETER_MM * 990 / TEST_DISTANCE_MM))
print("Battery: {} mV".format(robot.hub.battery.voltage()))
