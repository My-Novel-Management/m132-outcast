# -*- coding: utf-8 -*-
'''
Stage: "学生寮"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def backto_domitory(w: World):
    return w.scene("寮でも一人",
            w.cmd.change_stage("Dormitory"),
            w.cmd.change_time("night"),
            "寮に戻った$akoが不審な動きをしている風に",
            "$AIとのやり取りを見せる",
            )
