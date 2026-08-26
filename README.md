# FLL Challenge Movement & Attachment Library (Pybricks)

A reusable library of drivebase movements, attachment controls, and sensor
helpers for a LEGO SPIKE Prime robot running Pybricks, built for FIRST LEGO
League Challenge.

## Setup

1. Open [Pybricks Code](https://code.pybricks.com) (or the Pybricks VS Code
   extension) and create a new project.
2. Add every `.py` file in this repo to that project as a separate file
   (Pybricks Code supports multi-file projects; these files use plain
   top-level imports like `from robot import robot`, so keep them all in the
   same flat project — no subfolders).
3. Edit **`config.py`** first:
   - Set the motor/sensor ports to match your build.
   - Set `LEFT_DRIVE_MOTOR_DIRECTION` / `RIGHT_DRIVE_MOTOR_DIRECTION` so that
     positive speeds drive the robot forward (flip a direction if a wheel
     spins backwards).
   - Measure and set `WHEEL_DIAMETER_MM` and `AXLE_TRACK_MM` on your actual
     robot — this is the single most important calibration step; every
     straight-distance and turn/arc angle depends on it.
4. Use `mission_example.py` as a starting template for your own missions,
   or import individual functions directly into your own main file.

## File guide

| File | Category | Contents |
|---|---|---|
| `config.py` | Config | Ports, directions, wheel/axle dimensions, tuning constants. Edit this, not the others. |
| `robot.py` | Core | Builds the hub, motors, `DriveBase`, and sensors once as a shared `robot` object. Enables gyro-assisted driving (`drive_base.use_gyro(True)`). |
| `movement_straight.py` | Movement | `drive_straight`, `drive_until_stalled`, `drive_until` (drive to a sensor condition). Gyro-corrected via DriveBase. |
| `movement_turning.py` | Movement | `turn_in_place`, `turn_to_heading` (absolute), `turn_with_radius` (arc), `pivot_turn` (rotate around one wheel). |
| `movement_stopping.py` | Movement | `stop_coast`, `stop_brake`, `stop_hold`, `stop_all` (drivebase + attachments). |
| `attachment_control.py` | Attachments | `run_to_angle`, `run_by_degrees`, `run_until_stall`, `reset_position`, `home` (drive to a hard stop and zero the encoder). |
| `sensor_gyro.py` | Sensors | Raw IMU access: `heading`, `reset_heading`, `angular_velocity`, `is_stationary`, `wait_until_stationary`. |
| `sensor_color.py` | Sensors | `read_color`, `read_reflection`, `is_color`, `wait_for_color`, `wait_for_reflection`. |
| `sensor_distance.py` | Sensors | `read_distance_mm`, `object_detected`, `wait_for_object`, `wait_for_clear`. |
| `sensor_touch.py` | Sensors | `get_force`, `is_pressed`, `is_touched`, `wait_for_press`, `wait_for_release`. |
| `line_follow.py` | Sensors + Movement | Single-sensor PID edge line following: `follow_line_for_distance`, `follow_line_until`. |
| `pid_controller.py` | Utility | Generic `PID` class used by line following (and available for your own control loops). |
| `math_utils.py` | Utility | `normalize_angle`, `clamp`, `sign`. |
| `mission_example.py` | Example | A template mission + a hub-button mission selector (LEFT/RIGHT to pick, CENTER to run). |

## Why "gyro based"?

`robot.py` turns on `drive_base.use_gyro(True)` once, globally. Every
straight-line drive, in-place turn, absolute heading turn, arc, and pivot
turn in `movement_straight.py` / `movement_turning.py` goes through that
same `DriveBase`, so all of them automatically use the hub's IMU to correct
for wheel slip and drift — there's nothing extra to call per-movement.

`sensor_gyro.py` exposes the raw IMU (heading, angular velocity, stationary
check) directly for missions that need it — e.g. logging heading drift, or
making sure the robot has stopped shaking before reading a sensor.

## Notes on sign conventions

- Positive angle/turn = **clockwise** (turns right), viewed from above.
  This matches `DriveBase.turn()` and `hub.imu.heading()`.
- For `turn_with_radius` / `pivot_turn`, a **positive radius** means the
  circle's center is to the robot's **right**.
- `pivot_turn(angle, pivot="right")` keeps the right wheel planted;
  `pivot="left"` keeps the left wheel planted. This is equivalent to
  `turn_with_radius(radius_mm=AXLE_TRACK_MM/2 (or its negative), ...)`.

## Tuning line following

`line_follow.py` needs one thing tuned per robot: which side of the line
the sensor is on. If the robot swerves away from the line instead of
tracking it, call the function with `edge="left"` instead of the default
`edge="right"` (or vice versa). PID gains live in `config.py` as
`LINE_FOLLOW_KP/KI/KD`.
