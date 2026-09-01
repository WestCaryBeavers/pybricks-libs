"""Straight-line driving movements.

All of these go through DriveBase, which has gyro correction enabled once
(see robot.py: drive_base.use_gyro(True)). That means every function here is
already "gyro based": the hub's IMU is used to hold a steady heading while
driving, correcting for wheel slip or uneven mat friction, without any extra
code at the call site.
"""

from pybricks.parameters import Stop

from lib_robot import robot
import lib_config as config


def drive_straight(distance_mm, speed=None, then=Stop.HOLD, wait=True):
    """Drive straight for a signed distance in millimeters, gyro-corrected.

    Positive distance drives forward, negative drives backward. `speed`
    overrides the configured default straight speed (mm/s) for this call
    only; the previous setting is restored afterward.
    """
    drive_base = robot.drive_base
    if speed is None:
        drive_base.straight(distance_mm, then=then, wait=wait)
        return

    previous_speed, previous_accel, turn_rate, turn_accel = drive_base.settings()
    drive_base.settings(straight_speed=abs(speed))
    try:
        drive_base.straight(distance_mm, then=then, wait=wait)
    finally:
        drive_base.settings(straight_speed=previous_speed)


def drive_until_stalled(speed=200, then=Stop.HOLD):
    """Drive forward (or backward, if `speed` is negative) until both drive
    motors stall, e.g. the robot has driven into a wall or a fixed part of
    the field. Returns the distance traveled in millimeters.
    """
    drive_base = robot.drive_base
    drive_base.reset()
    drive_base.drive(speed, 0)
    while not (robot.left_motor.stalled() and robot.right_motor.stalled()):
        pass
    drive_base.stop()
    if then == Stop.HOLD:
        robot.left_motor.hold()
        robot.right_motor.hold()
    elif then == Stop.BRAKE:
        robot.left_motor.brake()
        robot.right_motor.brake()
    return drive_base.distance()


def drive_until(condition_fn, speed=None, max_distance_mm=None, then=Stop.HOLD):
    """Drive straight while `condition_fn()` returns False, then stop.

    Useful for "drive until the color sensor sees black" or "drive until the
    distance sensor sees an object within range" style moves. `condition_fn`
    takes no arguments and returns True when the robot should stop.
    max_distance_mm is an optional safety cap (always positive) so a mission
    can't run away if the condition never becomes true.
    """
    drive_base = robot.drive_base
    drive_speed = speed if speed is not None else config.DEFAULT_STRAIGHT_SPEED
    drive_base.reset()
    drive_base.drive(drive_speed, 0)

    while not condition_fn():
        if max_distance_mm is not None and abs(drive_base.distance()) >= abs(max_distance_mm):
            break

    drive_base.stop()
    if then == Stop.HOLD:
        robot.left_motor.hold()
        robot.right_motor.hold()
    elif then == Stop.BRAKE:
        robot.left_motor.brake()
        robot.right_motor.brake()
    return drive_base.distance()
