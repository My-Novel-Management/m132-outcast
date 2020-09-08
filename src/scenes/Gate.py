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
    ako, misora = w.get("ako"), w.get("misora")
    nori = w.get("nori")
    mizu = w.get("mizu")
    return w.scene('機械による朝のチェック',
            "冒頭で学校だけど特殊な状況で$AIによる管理を全面に出す",
            w.cmd.change_camera("ako"),
            w.cmd.change_stage("Gate"),
            w.plot_note("進学校の高等部の特別クラスに選抜された一人の$ako"),
            w.plot_note("そこではテストケースとして$AIによる成績評価を導入していた"),
            w.plot_note("生徒の選抜も$AIにより行われたらしい"),
            ako.come("全く同じスカート丈でやってくる多くの生徒に混ざってやってくるショートカットの女子"),
            ako.do("上履きに履き替えて、空港の手荷物検査のような金属製のゲートに向かう"),
            ako.do("誰もがスマホサイズの端末を手に、それを翳して"),
            ako.do("次々にピッという電子音で許可されてゲートをくぐる"),
            ako.do("一人の生徒がひっかかり、担当者の$mizuが彼女を呼ぶ"),
            ako.do("どうやら時間がなくてタイをしていなかったのが引っかかった要因らしい"),
            ako.do("彼女は許して下さいと懇願するが$sivaには逆らえないと言われてしまう"),
            )


def outcast_morning(w: World):
    return w.scene("ハミダシモノの朝",
            w.plot_note("ハミダシモノになるとクラスグループから外される"),
            )
