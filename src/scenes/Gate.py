# -*- coding: utf-8 -*-
'''
Stage: "チェックゲート"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def checking(w: World):
    return w.scene('機械による朝のチェック',
            "冒頭で学校だけど特殊な状況で$AIによる管理を全面に出す",
            w.plot_note("進学校の高等部の特別クラスに選抜された一人の$ako"),
            w.plot_note("そこではテストケースとして$AIによる成績評価を導入していた"),
            w.plot_note("生徒の選抜も$AIにより行われたらしい"),
            )


def outcast_morning(w: World):
    return w.scene("ハミダシモノの朝",
            w.plot_note("ハミダシモノになるとクラスグループから外される"),
            )
