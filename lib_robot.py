"""Single point of hardware initialization for the shared chassis.

Every other module imports the `robot` object from here to get an
already-configured hub, drive motors, and drivebase, instead of
constructing its own. Construct hardware exactly once by importing this
module; Python's module cache guarantees `Robot()` only runs on first import.

The 2 attachment motors (ports C/D) are NOT built here: only one team's
gear train can be physically mounted on them at a time, so
`robot.front_attachment`/`robot.back_attachment` start unset -- call
`lib_robot_right.activate()` or `lib_robot_left.activate()` (whichever
team's mission is about to run) to build/rebuild them with that team's
gear ratio before using them.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis
from pybricks.robotics import DriveBase

import lib_config as config


def make_motor(port, direction, gears=None):
    """Shared helper for building any Motor (drive or attachment) from a
    port/direction/gears triple, or None if the port isn't wired up.
    Used here for the drive motors and by lib_robot_right.py/
    lib_robot_left.py for the attachment motors.
    """
    return Motor(port, direction, gears=gears) if port is not None else None


class Robot:
    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)

        self.left_motor = make_motor(config.LEFT_DRIVE_MOTOR_PORT, config.LEFT_DRIVE_MOTOR_DIRECTION)
        self.right_motor = make_motor(config.RIGHT_DRIVE_MOTOR_PORT, config.RIGHT_DRIVE_MOTOR_DIRECTION)

        # Built on demand by lib_robot_right.activate() / lib_robot_left.
        # activate() -- whichever team's mission runs first calls its own
        # module's activate() before touching these.
        self.front_attachment = None
        self.back_attachment = None
        self.right_team_front_attachment = None
        self.right_team_back_attachment = None
        self.left_team_front_attachment = None
        self.left_team_back_attachment = None
        self.active_attachment_team = None

        self.drive_base = DriveBase(
            self.left_motor,
            self.right_motor,
            wheel_diameter=config.WHEEL_DIAMETER_MM,
            axle_track=config.AXLE_TRACK_MM,
        )
        self.drive_base.settings(
            straight_speed=config.DEFAULT_STRAIGHT_SPEED,
            straight_acceleration=config.DEFAULT_STRAIGHT_ACCELERATION,
            turn_rate=config.DEFAULT_TURN_RATE,
            turn_acceleration=config.DEFAULT_TURN_ACCELERATION,
        )
        # Use the hub's built-in IMU for low-drift straight driving, turning,
        # and arcs. This is what makes every "gyro based" movement in this
        # library gyro based: no extra code is needed per-call.
        self.drive_base.use_gyro(True)

        # self.left_color_sensor = self._make_color_sensor(config.LEFT_COLOR_SENSOR_PORT)
        # self.right_color_sensor = self._make_color_sensor(config.RIGHT_COLOR_SENSOR_PORT)
        # self.distance_sensor = self._make_ultrasonic_sensor(config.DISTANCE_SENSOR_PORT)
        # self.touch_sensor = self._make_touch_sensor(config.TOUCH_SENSOR_PORT)

    @staticmethod
    def _make_color_sensor(port):
        return ColorSensor(port) if port is not None else None

    # @staticmethod
    # def _make_ultrasonic_sensor(port):
    #     return UltrasonicSensor(port) if port is not None else None

    @staticmethod
    def _make_touch_sensor(port):
        return ForceSensor(port) if port is not None else None


robot = Robot()
