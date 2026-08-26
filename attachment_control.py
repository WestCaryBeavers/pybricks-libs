"""Generic controls for attachment motors (front/back mechanisms: arms,
lifts, spinners, linear actuators, etc.).

Every function here takes the motor as its first argument, so it works with
robot.front_attachment, robot.back_attachment, or any other Motor object,
rather than being hardcoded to one attachment.
"""

from pybricks.parameters import Stop


def run_to_angle(motor, target_angle, speed=500, then=Stop.HOLD, wait=True):
    """Rotate the attachment to an absolute angle (degrees), as measured
    from wherever the motor's angle was last reset to 0.
    """
    motor.run_target(speed, target_angle, then=then, wait=wait)


def run_by_degrees(motor, degrees, speed=500, then=Stop.HOLD, wait=True):
    """Rotate the attachment by a relative number of degrees from its
    current position. Positive degrees follow the motor's configured
    positive direction.
    """
    motor.run_angle(speed, degrees, then=then, wait=wait)


def run_until_stall(motor, speed=300, duty_limit=None, then=Stop.COAST):
    """Run the attachment until it stalls (e.g. hits a mechanical end
    stop), then stop. Returns the angle at which it stalled.

    duty_limit caps the motor's effort (0-100%) while trying to reach
    `speed`, so it stalls against light resistance instead of forcing
    through it; leave as None to use the motor's default limit.
    """
    return motor.run_until_stalled(speed, then=then, duty_limit=duty_limit)


def reset_position(motor, angle=0):
    """Redefine the motor's current physical position as `angle` degrees,
    without moving it. Use this once you know the attachment is at a known
    reference position (e.g. right after homing).
    """
    motor.reset_angle(angle)


def home(motor, speed=-200, duty_limit=30, reset_to=0, then=Stop.HOLD):
    """Drive the attachment into its mechanical end stop at low effort,
    then define that position as `reset_to` degrees.

    This is the standard "garage" pattern for FLL attachments: run a
    negative (or positive) speed with a low duty_limit so the motor stalls
    gently against a hard stop instead of straining the gears, then treat
    that stall point as a known zero position for the rest of the match.
    """
    motor.run_until_stalled(speed, then=Stop.COAST, duty_limit=duty_limit)
    motor.reset_angle(reset_to)
    if then == Stop.HOLD:
        motor.hold()
    elif then == Stop.BRAKE:
        motor.brake()
