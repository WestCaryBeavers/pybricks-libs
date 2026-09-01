"""Example mission structure and a hub-button mission selector.

This is a template, not a finished program: copy the pattern, replace the
example missions with your own, and rename this file (or its contents) to
whatever your Pybricks project uses as its main file.
"""

import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait

from lib_robot import robot
from lib_movement_straight import drive_straight
from lib_movement_turning import turn_in_place, pivot_turn, turn_with_radius
from lib_movement_stopping import stop_all
from lib_attachment_control import run_by_degrees, home
from lib_sensor_gyro import reset_heading, wait_until_stationary


def mission_one():
    """Example: drive out, run an attachment, turn, come back."""
    reset_heading(0)
    drive_straight(500)
    run_by_degrees(robot.front_attachment, 90, speed=400)
    turn_in_place(90)
    drive_straight(200)
    run_by_degrees(robot.front_attachment, -90, speed=400)
    turn_in_place(-90)
    drive_straight(-700)
    stop_all(then=Stop.HOLD)


def mission_two():
    """Example: sweep an arc, pivot around one wheel, home an attachment."""
    reset_heading(0)
    drive_straight(300)
    turn_with_radius(radius_mm=250, angle_deg=90)
    pivot_turn(90, pivot="right")
    home(robot.back_attachment, speed=-200, duty_limit=30)
    drive_straight(-300)
    stop_all(then=Stop.HOLD)

# Add every runnable mission here; the selector below cycles through this
# list in order.
MISSIONS = [
    ("Mission 1", mission_one),
    ("Mission 2", mission_two),
]

_SELECTOR_COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW, Color.ORANGE,
                     Color.CYAN, Color.MAGENTA, Color.WHITE]


def _wait_for_button_release():
    while robot.hub.buttons.pressed():
        wait(10)


def run_mission_selector():
    """Show a mission picker on the hub: LEFT/RIGHT cycles the selected
    mission (shown as a light color), CENTER runs it.
    """
    selected = 0
    robot.hub.light.on(_SELECTOR_COLORS[selected % len(_SELECTOR_COLORS)])

    while True:
        pressed = robot.hub.buttons.pressed()

        if Button.RIGHT in pressed:
            selected = (selected + 1) % len(MISSIONS)
            robot.hub.light.on(_SELECTOR_COLORS[selected % len(_SELECTOR_COLORS)])
            _wait_for_button_release()

        elif Button.LEFT in pressed:
            selected = (selected - 1) % len(MISSIONS)
            robot.hub.light.on(_SELECTOR_COLORS[selected % len(_SELECTOR_COLORS)])
            _wait_for_button_release()

        elif Button.CENTER in pressed:
            _wait_for_button_release()
            name, mission_fn = MISSIONS[selected]
            robot.hub.speaker.beep(frequency=500, duration=100)
            wait_until_stationary(timeout_ms=2000)
            mission_fn()
            robot.hub.speaker.beep(frequency=1000, duration=150)

        wait(10)


if __name__ == "__main__":
    # run_mission_selector()
    mission_one()
