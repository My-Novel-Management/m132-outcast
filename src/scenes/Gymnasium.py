# -*- coding: utf-8 -*-
'''
Stage: "体育館"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def bullying(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    nori = w.get("nori")
    return w.scene("いじめ",
            w.cmd.change_stage("Gymnasium"),
            w.cmd.change_time("afternoon"),
            w.plot_note("やがて精神バランスを壊して$noriは入院という名の不登校になった"),
            "$noriいじめの兆候みたいな描写を入れてから、BR挟んで、翌週から空席ができた、で",
            "体育館の描写",
            "体育の時間で、運動が苦手な$noriに対しての嫌がらせ的ボール回し（バレー）",
            )



def old_friend(w: World):
    ako = w.get("ako")
    nori = w.get("nori")
    return w.scene('旧友との再会',
            w.cmd.change_stage("Gymnasium"),
            w.plot_note("中学一年以来の再会である$noriは、他の生徒から邪険に扱われていた"),
            )

