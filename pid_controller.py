"""A small, reusable PID controller.

Used by line_follow.py, and available for any custom control loop a team
wants to write (custom heading holds, arm balancing, etc.) without pulling
in DriveBase or any specific hardware.
"""

from pybricks.tools import StopWatch

from math_utils import clamp


class PID:
    def __init__(self, kp, ki=0.0, kd=0.0, integral_limit=None, output_limits=None):
        """
        kp, ki, kd: PID gains.
        integral_limit: max absolute value the accumulated integral term may
            reach, to prevent windup. None disables clamping.
        output_limits: (min, max) tuple to clamp the returned output, or
            None to leave the output unclamped.
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral_limit = integral_limit
        self.output_limits = output_limits

        self._integral = 0.0
        self._previous_error = 0.0
        self._watch = StopWatch()
        self._first_update = True

    def reset(self):
        """Clear accumulated integral/derivative state. Call this before
        starting a new maneuver that reuses the same PID object."""
        self._integral = 0.0
        self._previous_error = 0.0
        self._first_update = True
        self._watch.reset()

    def update(self, error, dt_ms=None):
        """Compute the next control output for the given error.

        dt_ms: time elapsed since the last update, in milliseconds. If not
        given, it is measured automatically using an internal stopwatch.
        """
        if dt_ms is None:
            dt_ms = self._watch.time()
        self._watch.reset()

        dt_s = dt_ms / 1000 if dt_ms > 0 else 0.001

        self._integral += error * dt_s
        if self.integral_limit is not None:
            self._integral = clamp(self._integral, -self.integral_limit, self.integral_limit)

        if self._first_update:
            derivative = 0.0
            self._first_update = False
        else:
            derivative = (error - self._previous_error) / dt_s
        self._previous_error = error

        output = self.kp * error + self.ki * self._integral + self.kd * derivative

        if self.output_limits is not None:
            low, high = self.output_limits
            output = clamp(output, low, high)

        return output
