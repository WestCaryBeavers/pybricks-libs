"""Single point of hardware initialization.

Every other module imports the `robot` object from here to get
already-configured hub, motors, drivebase, and sensor objects, instead of
constructing its own. Construct hardware exactly once by importing this
module; Python's module cache guarantees `Robot()` only runs on first import.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis
from pybricks.robotics import DriveBase

import lib_config as config


class Robot:
    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)

        self.left_motor = Motor(config.LEFT_DRIVE_MOTOR_PORT, config.LEFT_DRIVE_MOTOR_DIRECTION)
        self.right_motor = Motor(config.RIGHT_DRIVE_MOTOR_PORT, config.RIGHT_DRIVE_MOTOR_DIRECTION)

        self.front_attachment = self._make_motor(
            config.FRONT_ATTACHMENT_MOTOR_PORT,
            config.FRONT_ATTACHMENT_MOTOR_DIRECTION,
            config.FRONT_ATTACHMENT_GEARS,
        )
        self.back_attachment = self._make_motor(
            config.BACK_ATTACHMENT_MOTOR_PORT,
            config.BACK_ATTACHMENT_MOTOR_DIRECTION,
            config.BACK_ATTACHMENT_GEARS,
        )

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

        self.left_color_sensor = self._make_color_sensor(config.LEFT_COLOR_SENSOR_PORT)
        self.right_color_sensor = self._make_color_sensor(config.RIGHT_COLOR_SENSOR_PORT)
        # self.distance_sensor = self._make_ultrasonic_sensor(config.DISTANCE_SENSOR_PORT)
        self.touch_sensor = self._make_touch_sensor(config.TOUCH_SENSOR_PORT)

    @staticmethod
    def _make_motor(port, direction, gears):
        return Motor(port, direction, gears=gears) if port is not None else None

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
