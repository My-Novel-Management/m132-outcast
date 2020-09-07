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
    return w.scene('利用できない',
            w.plot_note("図書館の利用もできなくなった"),
            )

