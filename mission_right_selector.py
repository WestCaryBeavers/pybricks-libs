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

from mission_right_team_1 import mission as mission_1
from mission_right_team_2 import mission as mission_2
from mission_right_team_3 import mission as mission_3
from mission_right_team_4 import mission as mission_4

MISSIONS = {
    "1": mission_1,
    "2": mission_2,
    "3": mission_3,
    "4": mission_4,
}


def run_mission_selector():
    """Show '1'-'4' on the hub matrix; Bluetooth button cycles, center
    (the selection made by hub_menu) runs the chosen mission.
    """
    selected = hub_menu(*MISSIONS.keys())
    MISSIONS[selected]()


if __name__ == "__main__":
    run_mission_selector()
