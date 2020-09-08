# -*- coding: utf-8 -*-
'''
Stage: "食堂"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def nothing_right(w: World):
    ako = w.get("ako")
    return w.scene('権利がない',
            w.cmd.change_stage("Cafeteria"),
            w.plot_note("食券も配られずに自腹"),
            w.plot_note("食事は自分で作った弁当を持参する"),
            )

