"""Central configuration for the FLL robot.

Every other file in this library reads ports, physical dimensions, and
tuning constants from here instead of hardcoding them. Edit this file once
to match your robot's build; you should not need to touch the other files
to re-point ports or retune motion.
"""

from pybricks.parameters import Port, Direction

# ---------------------------------------------------------------------------
# Motor ports
# ---------------------------------------------------------------------------
LEFT_DRIVE_MOTOR_PORT = Port.A
RIGHT_DRIVE_MOTOR_PORT = Port.E
FRONT_ATTACHMENT_MOTOR_PORT = Port.D
BACK_ATTACHMENT_MOTOR_PORT = Port.C

# ---------------------------------------------------------------------------
# Motor directions
# ---------------------------------------------------------------------------
# Flip to the opposite Direction if a motor spins the "wrong" way when
# given a positive speed/angle/duty cycle.
LEFT_DRIVE_MOTOR_DIRECTION = Direction.COUNTERCLOCKWISE
RIGHT_DRIVE_MOTOR_DIRECTION = Direction.CLOCKWISE
FRONT_ATTACHMENT_MOTOR_DIRECTION = Direction.CLOCKWISE
BACK_ATTACHMENT_MOTOR_DIRECTION = Direction.CLOCKWISE

# Optional gear trains between an attachment motor and its output shaft, as
# accepted by pybricks.pupdevices.Motor(gears=...), e.g. [12, 36] for a
# 12-tooth driver into a 36-tooth driven gear. Leave as None for a direct
# (1:1) connection.
FRONT_ATTACHMENT_GEARS = [[32, 40], [12, 24]]
BACK_ATTACHMENT_GEARS = None

# ---------------------------------------------------------------------------
# Sensor ports
# ---------------------------------------------------------------------------
# Set any of these to None if that sensor is not present on your robot.
LEFT_COLOR_SENSOR_PORT = None
RIGHT_COLOR_SENSOR_PORT = None
DISTANCE_SENSOR_PORT = None
TOUCH_SENSOR_PORT = None

# ---------------------------------------------------------------------------
# Drivebase geometry (millimeters)
# ---------------------------------------------------------------------------
# Measure these directly on the robot. Getting these right matters more than
# any other constant in this file: every gyro-assisted straight/turn/arc
# still relies on wheel_diameter and axle_track for distance and radius math.
WHEEL_DIAMETER_MM = 87
AXLE_TRACK_MM = 144

# ---------------------------------------------------------------------------
# Default motion tuning (used by DriveBase.settings())
# ---------------------------------------------------------------------------
DEFAULT_STRAIGHT_SPEED = 300          # mm/s
DEFAULT_STRAIGHT_ACCELERATION = 400   # mm/s^2
DEFAULT_TURN_RATE = 150               # deg/s
DEFAULT_TURN_ACCELERATION = 300       # deg/s^2

# ---------------------------------------------------------------------------
# Line-following tuning (used by line_follow.py)
# ---------------------------------------------------------------------------
LINE_FOLLOW_KP = 1.2
LINE_FOLLOW_KI = 0.0
LINE_FOLLOW_KD = 0.3
LINE_FOLLOW_SPEED = 120                # mm/s
LINE_FOLLOW_EDGE_REFLECTION = 50       # midpoint between line and background reflection %

# ---------------------------------------------------------------------------
# Sensor thresholds
# ---------------------------------------------------------------------------
TOUCH_DEFAULT_FORCE_N = 3
DISTANCE_NO_OBJECT_MM = 2000  # UltrasonicSensor.distance() returns this when nothing is detected
