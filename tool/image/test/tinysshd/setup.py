#!/usr/bin/env python

#
# setup dropbear machine
#

from nspawn.setup import *

import os
import sys

# import shared config
project_root = os.popen("git rev-parse --show-toplevel").read().strip()
python_module = f"{project_root}/tool/module"
sys.path.insert(0, python_module)
from arkon_config import machine_tinysshd
from arkon_config import image_tinysshd_url

# invoke image identity
IMAGE(url=image_tinysshd_url)

# container name
MACHINE(name=machine_tinysshd)