"""Stopping behaviors for the drivebase and attachment motors.

Stop.COAST: motors spin freely and slow down on their own (least resistance,
    lets momentum carry the robot a little further).
Stop.BRAKE: motors resist being turned but don't actively hold position.
Stop.HOLD: motors actively hold their current position/heading.
"""

from pybricks.parameters import Stop

from lib_robot import robot


def stop_coast():
    """Stop the drivebase and let it coast to a stop."""
    robot.drive_base.stop()
    robot.left_motor.stop()
    robot.right_motor.stop()


def stop_brake():
    """Stop the drivebase and brake (resist motion, don't actively hold)."""
    robot.drive_base.stop()
    robot.left_motor.brake()
    robot.right_motor.brake()


def stop_hold():
    """Stop the drivebase and actively hold the current position/heading."""
    robot.drive_base.stop()
    robot.left_motor.hold()
    robot.right_motor.hold()


def stop_all(then=Stop.COAST):
    """Stop the drivebase and every configured attachment motor. Intended
    as an emergency/end-of-mission stop. Defaults to coasting, which is the
    gentlest option on gears and mechanisms.
    """
    robot.drive_base.stop()
    for motor in (robot.left_motor, robot.right_motor, robot.front_attachment, robot.back_attachment):
        if motor is None:
            continue
        if then == Stop.HOLD:
            motor.hold()
        elif then == Stop.BRAKE:
            motor.brake()
        else:
            motor.stop()
