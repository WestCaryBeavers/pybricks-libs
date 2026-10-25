"""Interactive REPL with all team libraries loaded.

How to use:
  1. Open this file and click Compile & Run in BlocklyPy.
  2. When "READY" appears in the terminal, click in the terminal and press Ctrl+C.
  3. You get a >>> prompt where drive_straight(), turn_to_heading(), robot, etc.
     all work. Type one line at a time, e.g.  drive_straight(100)

Why: a REPL started on its own only knows the built-in Pybricks modules. Your
lib_*.py files only reach the hub as part of a program, so this file uploads
them all, and Ctrl+C drops into the REPL with everything still loaded.
"""

import dev_stub  # noqa: F401

from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch

from lib_robot import robot
from lib_movement_straight import *
from lib_movement_turning import *
from lib_movement_stopping import *
from lib_attachment_control import *
from lib_sensor_gyro import *
from lib_sensor_color import *
from lib_sensor_distance import *
from lib_sensor_touch import *
from lib_line_follow import *
from lib_math_utils import *
from lib_pid_controller import PID

print("READY - click in the terminal and press Ctrl+C to get the >>> prompt")
while True:
    wait(100)
