# -*- coding: utf-8 -*-
'''
Stage: "女子トイレ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def nori_thought(w: World):
    ako = w.get("ako")
    nori = w.get("nori")
    return w.scene("$noriの気持ち",
            w.cmd.change_stage("Toilet"),
            ako.be("女子トイレの個室に入って、端末を見ている"),
            ako.do("端末には$noriからのメッセージがあった"),
            nori.voice("学校生活はどう？　$meはあそこはもう無理かなって思ってる",
                "うん。調子はかなり良くなったよ",
                "親にはまだいい出せてないけど、転校をお願いしてみるつもり",
                "$k_akoと一緒に転校できたらな、って思うけど……ね",
                "また、連絡します"),
            ako.think("最後まで戦い抜く覚悟を固める$S"),
            )
