# -*- coding: utf-8 -*-
'''
Stage: "パソコンルーム"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def nothing_right(w: World):
    ako = w.get("ako")
    return w.scene('入室できない',
            w.cmd.change_stage("PCRoom"),
            w.plot_note("パソコンルームにも入れなくなる（正規の生徒でないと入室不可能）"),
            )

