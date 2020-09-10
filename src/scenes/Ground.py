# -*- coding: utf-8 -*-
'''
Stage: "グラウンド"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def alone_run(w: World):
    ako = w.get("ako")
    return w.scene('孤独な走行',
            w.cmd.change_stage("Ground"),
            w.plot_note("体育は参加することもできず、一人で外を走っているだけ"),
            ako.be("一人きりで雨のグラウンドを走っている$S"),
            ako.do("体育館の方からは楽しそうにバレーボールをする声が響いてくる"),
            )

