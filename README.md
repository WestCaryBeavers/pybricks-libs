# FLL Challenge Movement & Attachment Library (Pybricks)

A reusable library of drivebase movements, attachment controls, and sensor
helpers for a LEGO SPIKE Prime robot running Pybricks, built for FIRST LEGO
League Challenge.

## Setup

1. Open [Pybricks Code](https://code.pybricks.com) (or the Pybricks VS Code
   extension) and create a new project.
2. Add every `.py` file in this repo to that project as a separate file
   (Pybricks Code supports multi-file projects; these files use plain
   top-level imports like `from lib_robot import robot`, so keep them all in
   the same flat project — no subfolders). Library files are named with a
   `lib_` prefix so they sort together, ahead of the mission files.
3. Edit **`lib_config.py`** first:
   - Set the motor/sensor ports to match your build.
   - Set `LEFT_DRIVE_MOTOR_DIRECTION` / `RIGHT_DRIVE_MOTOR_DIRECTION` so that
     positive speeds drive the robot forward (flip a direction if a wheel
     spins backwards).
   - Measure and set `WHEEL_DIAMETER_MM` and `AXLE_TRACK_MM` on your actual
     robot — this is the single most important calibration step; every
     straight-distance and turn/arc angle depends on it.
4. Use `mission_example.py` as a starting template for your own missions,
   or import individual functions directly into your own main file.

`dev_stub.py` is desktop-only tooling (see "Testing on a desktop" below);
you don't need to upload it to the hub, though it's harmless if you do.

## Testing on a desktop

`pybricks` only exists on the real hub, so running a mission file with a
plain desktop `python3` needs a stand-in. `dev_stub.py` installs a minimal
stub implementation of `pybricks` (motors, sensors, drivebase, hub — all
no-ops) so you can sanity-check mission logic without hardware attached.

Any file you want to run standalone on a desktop machine should import it
before anything else:

```python
import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.parameters import Stop, Color, Button
...
```

No `PYTHONPATH` or extra setup needed — `python3 mission_example.py` just
works, because `dev_stub.py` lives right next to the mission files. On the
real hub, `pybricks` already exists, so the import becomes a no-op.

## File guide

| File | Category | Contents |
|---|---|---|
| `lib_config.py` | Config | Ports, directions, wheel/axle dimensions, tuning constants. Edit this, not the others. |
| `lib_robot.py` | Core | Builds the hub, motors, `DriveBase`, and sensors once as a shared `robot` object. Enables gyro-assisted driving (`drive_base.use_gyro(True)`). |
| `lib_movement_straight.py` | Movement | `drive_straight`, `drive_until_stalled`, `drive_until` (drive to a sensor condition). Gyro-corrected via DriveBase. |
| `lib_movement_turning.py` | Movement | `turn_in_place`, `turn_to_heading` (absolute), `turn_with_radius` (arc), `pivot_turn` (rotate around one wheel). |
| `lib_movement_stopping.py` | Movement | `stop_coast`, `stop_brake`, `stop_hold`, `stop_all` (drivebase + attachments). |
| `lib_attachment_control.py` | Attachments | `run_to_angle`, `run_by_degrees`, `run_until_stall`, `reset_position`, `home` (drive to a hard stop and zero the encoder). |
| `lib_sensor_gyro.py` | Sensors | Raw IMU access: `heading`, `reset_heading`, `angular_velocity`, `is_stationary`, `wait_until_stationary`. |
| `lib_sensor_color.py` | Sensors | `read_color`, `read_reflection`, `is_color`, `wait_for_color`, `wait_for_reflection`. |
| `lib_sensor_distance.py` | Sensors | `read_distance_mm`, `object_detected`, `wait_for_object`, `wait_for_clear`. |
| `lib_sensor_touch.py` | Sensors | `get_force`, `is_pressed`, `is_touched`, `wait_for_press`, `wait_for_release`. |
| `lib_line_follow.py` | Sensors + Movement | Single-sensor PID edge line following: `follow_line_for_distance`, `follow_line_until`. |
| `lib_pid_controller.py` | Utility | Generic `PID` class used by line following (and available for your own control loops). |
| `lib_math_utils.py` | Utility | `normalize_angle`, `clamp`, `sign`. |
| `mission_example.py` | Example | A template mission + a hub-button mission selector (LEFT/RIGHT to pick, CENTER to run). |
| `dev_stub.py` | Dev tooling | Desktop-only stub for `pybricks`, so mission files can run under a normal `python3` for testing. No-op on the hub. |

## Why "gyro based"?

`lib_robot.py` turns on `drive_base.use_gyro(True)` once, globally. Every
straight-line drive, in-place turn, absolute heading turn, arc, and pivot
turn in `lib_movement_straight.py` / `lib_movement_turning.py` goes through
that same `DriveBase`, so all of them automatically use the hub's IMU to
correct for wheel slip and drift — there's nothing extra to call per-movement.

`lib_sensor_gyro.py` exposes the raw IMU (heading, angular velocity, stationary
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

`lib_line_follow.py` needs one thing tuned per robot: which side of the line
the sensor is on. If the robot swerves away from the line instead of
tracking it, call the function with `edge="left"` instead of the default
`edge="right"` (or vice versa). PID gains live in `lib_config.py` as
`LINE_FOLLOW_KP/KI/KD`.
