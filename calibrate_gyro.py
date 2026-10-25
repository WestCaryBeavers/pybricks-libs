"""Measure this hub's gyro error and save the correction on the hub.

Every hub's gyro is slightly off: it may report e.g. 357 degrees for a real
360 degree turn. That error is added to every turn, so 90 degree turns land
at 89.3 degrees and errors pile up over a run. Pybricks can correct for it
(hub.imu.settings(heading_correction=...)) once you measure it.

How to use (do this once per hub, and again after a firmware update):
  1. Put the robot on a flat table, with one side pressed against a straight
     edge (a wall, a book, a ruler taped down).
  2. Run this program and do not touch the robot until it beeps.
  3. Lift and turn the robot by hand exactly 5 full turns clockwise (seen
     from above), then put it back against the same edge, lined up exactly.
  4. Press the RIGHT button. The result is printed and saved on the hub.
  5. Turn the hub off normally (hold the center button) so the setting is
     stored.
"""

from pybricks.parameters import Axis, Button
from pybricks.tools import wait

from lib_robot import robot

TURNS = 5

hub = robot.hub
print("Current IMU settings:", hub.imu.settings())

print("Keep the robot still while the gyro calibrates...")
while not hub.imu.ready():
    wait(10)
hub.speaker.beep(frequency=800, duration=150)

start = hub.imu.rotation(-Axis.Z, calibrated=False)
print("Now turn the robot by hand exactly", TURNS, "full turns clockwise,")
print("line it up again, then press the RIGHT button.")

while Button.RIGHT not in hub.buttons.pressed():
    wait(10)
while Button.RIGHT in hub.buttons.pressed():
    wait(10)

measured = abs(hub.imu.rotation(-Axis.Z, calibrated=False) - start) / TURNS
print("Measured degrees per real 360 degree turn:", measured)

if 340 <= measured <= 380:
    hub.imu.settings(heading_correction=measured)
    print("Saved heading_correction =", measured)
    print("Turn the hub off normally to store it.")
    hub.speaker.beep(frequency=1200, duration=300)
else:
    print("That is too far from 360. Did you do exactly", TURNS, "turns?")
    print("Nothing was saved. Run the program again.")
    hub.speaker.beep(frequency=300, duration=600)
