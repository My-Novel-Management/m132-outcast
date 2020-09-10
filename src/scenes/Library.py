# -*- coding: utf-8 -*-
'''
Stage: "図書室"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def nothing_right2(w: World):
    ako = w.get("ako")
    return w.scene('利用できない',
            w.cmd.change_stage("Library"),
            w.plot_note("図書館の利用もできなくなった"),
            )

