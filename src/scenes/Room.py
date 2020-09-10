# -*- coding: utf-8 -*-
'''
Stage: "亜子の部屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def mystery_message(w: World):
    return w.scene("謎のメッセージ",
            w.cmd.change_stage("Room"),
            w.cmd.change_time("night"),
            "自室の描写を簡単に",
            "$noriとのメッセージのやり取り",
            "最後に$sivaからメッセージが来る",
            )
