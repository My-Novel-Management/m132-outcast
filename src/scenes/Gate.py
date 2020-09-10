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
    girl = w.get("woman")
    noza = w.get("noza")
    return w.scene('機械による朝のチェック',
            "冒頭で学校だけど特殊な状況で$AIによる管理を全面に出す",
            w.cmd.change_camera("ako"),
            w.cmd.change_stage("Gate"),
            w.cmd.change_time("morning"),
            w.cmd.change_date("FirstTime"),
            w.plot_note("進学校の高等部の特別クラスに選抜された一人の$ako"),
            w.plot_note("そこではテストケースとして$AIによる成績評価を導入していた"),
            w.plot_note("生徒の選抜も$AIにより行われたらしい"),
            "手にしたスマホのクロースアップから",
            "ゲートは物々しい感じで空港にあるやつっぽい",
            "女子ばかり。制服もお硬いイメージを付ける",
            "髪の長さやスカート丈までが全てきっちり管理されている感じ",
            "監視カメラも動いている",
            "担任の$mizuの眼鏡の鋭さ",
            ako.come("全く同じスカート丈でやってくる多くの生徒に混ざってやってくるショートカットの女子"),
            ako.do("上履きに履き替えて、空港の手荷物検査のような金属製のゲートに向かう"),
            ako.do("誰もがスマホサイズの端末を手に、それを翳して"),
            ako.do("次々にピッという電子音で許可されてゲートをくぐる"),
            ako.do("一人の生徒がひっかかり、担当者の$mizuが彼女を呼ぶ"),
            ako.do("どうやら時間がなくてタイをしていなかったのが引っかかった要因らしい"),
            ako.do("彼女は許して下さいと懇願するが$sivaには逆らえないと言われてしまう"),
            mizu.be("担当で立っている"),
            girl.talk("許して下さい。今朝は時間が無くて"),
            misora.be("それを見ている$S"),
            noza.be("$misoraの取り巻きも薄ら笑いで見ている"),
            nori.come("やってきて、声を掛ける"),
            nori.talk("おはよう、$k_ako"),
            ako.talk("ああ"),
            )


def outcast_morning(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("ハミダシモノの朝",
            w.cmd.change_stage("Gate"),
            w.cmd.change_time("morning"),
            w.cmd.change_date("HamidashiDay1"),
            w.plot_note("ハミダシモノになるとクラスグループから外される"),
            "ここからハミダシモノが始まる",
            "どんな処遇を受けるのかを、端的に分からせる",
            "人工的に生み出されたいじめられっこ、に見せること",
            ako.come("翌朝、チェックゲートにやってくる"),
            ako.do("噂は他のクラスにも広まり、遠巻きに$Sのことを見ている"),
            ako.do("ゲートを潜ろうとして端末を翳したが、反応がない"),
            ako.do("$Sはゲートを潜ることすら許されない"),
            ako.do("担当の$mizuを見る"),
            mizu.do("よく状況が理解できていないよう"),
            mizu.talk("後ろがつかえてるから早くしなさい"),
            ako.do("少し考えて、端末を通さずにそのまま通ろうとする"),
            ako.do("ゲートが閉じたまま開かない"),
            ako.talk("故障しているみたいです"),
            mizu.talk("え？　そんなことはないと思うけど"),
            ako.do("$Sを横にどかして他の生徒を通してみると、通れるしチェックも行える"),
            ako.talk("壊れたのはこちらのようですね"),
            ako.do("$Sは端末を見せるが、$mizuは困ったまま"),
            ako.do("少し考えて、端末を確認する"),
            ako.do("ゲート通過の許可という項目がエラーになっていた"),
            )
