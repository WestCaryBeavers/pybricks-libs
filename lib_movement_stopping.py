"""Stopping behaviors for the drivebase and attachment motors.

Stop.COAST: motors spin freely and slow down on their own (least resistance,
    lets momentum carry the robot a little further).
Stop.BRAKE: motors resist being turned but don't actively hold position.
Stop.HOLD: motors actively hold their current position/heading.
"""

from pybricks.parameters import Stop

from lib_robot import robot


def stop_drive_base(then=Stop.HOLD):
    """Stop the drivebase with the given Stop mode.

    Uses DriveBase.hold()/brake()/stop() so both wheels stop together and,
    for HOLD, the gyro keeps holding the heading. (Stopping first and then
    holding each motor separately lets the robot coast a little and ignores
    the gyro.)
    """
    if then == Stop.HOLD:
        robot.drive_base.hold()
    elif then == Stop.BRAKE:
        robot.drive_base.brake()
    else:
        robot.drive_base.stop()


def stop_coast():
    """Stop the drivebase and let it coast to a stop."""
    stop_drive_base(Stop.COAST)


def stop_brake():
    """Stop the drivebase and brake (resist motion, don't actively hold)."""
    stop_drive_base(Stop.BRAKE)


def stop_hold():
    """Stop the drivebase and actively hold the current position/heading."""
    stop_drive_base(Stop.HOLD)


def stop_all(then=Stop.COAST):
    """Stop the drivebase and every configured attachment motor. Intended
    as an emergency/end-of-mission stop. Defaults to coasting, which is the
    gentlest option on gears and mechanisms.
    """
    stop_drive_base(then)
    for motor in (robot.front_attachment, robot.back_attachment):
        if motor is None:
            continue
        if then == Stop.HOLD:
            motor.hold()
        elif then == Stop.BRAKE:
            motor.brake()
        else:
            motor.stop()
