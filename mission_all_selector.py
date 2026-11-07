"""Single-slot mission selector for the right-team robot.

This robot's codebase defines 4 missions, one `mission()` function per
`mission_right_team_1.py`..`mission_right_team_4.py` file. Rather than
uploading each as its own program (and burning a separate hub slot per
mission, with only 5 slots total on the hub), this file is the ONE program
you upload: it shows a menu on the hub matrix, you pick a mission with the
Bluetooth button, and it runs.

Upload only this file as your main program (plus every `lib_*.py` file and
the `mission_right_team_*.py` files it imports from, as extra files in the
same Pybricks Code project) -- that's a single hub slot covering all 4
missions.
"""

import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.tools import hub_menu

from mission_left_team_1 import mission_1 as mission_1L, mission_2 as mission_2L, mission_3 as mission_3L, mission_4 as mission_4L, mission_5 as mission_5L

MISSIONS = {
    "1L": mission_1L,
    "2L": mission_2L,
    "3L": mission_3L,
    "4L": mission_4L,
    "5L": mission_5L
}


def run_mission_selector():
    """Show '1L'-'5L' on the hub matrix; Bluetooth button cycles, center
    (the selection made by hub_menu) runs the chosen mission.
    """
    selected = hub_menu(*MISSIONS.keys())
    MISSIONS[selected]()


if __name__ == "__main__":
    run_mission_selector()
