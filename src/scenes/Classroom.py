# -*- coding: utf-8 -*-
'''
Stage: "教室"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def this_rule(w: World):
    return w.scene('この高校のルール',
            "教室：みんながタブレットを手にやり取りしている。その日の授業や課題を確認する",
            w.plot_note("担任の$mizuはきちんとルールを守り、今まで通りに生活すればいいと言う"),
            )


def evaluation(w: World):
    return w.scene("成績評価",
            w.plot_note("最初のテスト後に$AIの成績評価が出された"),
            w.plot_note("それはテストだけでなく、普段の生活でのポイントも加味されている"),
            w.plot_note("委員長に選出された$misoraがトップだった"),
            w.plot_note("しかし何もやってないはずの$noriが次点で、そこから彼女へのいじめが始まる"),
            )


def refusal(w: World):
    return w.scene("不登校",
            w.plot_note("やがて精神バランスを壊して$noriは入院という名の不登校になった"),
            )


def tips(w: World):
    return w.scene("タレコミ",
            w.plot_note("ある日$mizuから$AIに「クラスでいじめがあった」と報告が入っていたと言われる"),
            w.plot_note("個人個人の端末から$AIに通報することが簡単にできた"),
            w.plot_note("個人情報は秘匿され、担任の$mizuも誰が言ったのか分からないという"),
            w.plot_note("クラス会議で確認したが、いじめの事実はなかった"),
            w.plot_note("$mizuはそう伝えると言った"),
            )


def AIs_suggestion(w: World):
    return w.scene("$AIの提案",
            w.plot_note("しかし翌日、$AIが出した結論はいじめはなくならないから輪番制で「ハミダシモノ」を作ろうという提案だった"),
            )


def meeting(w: World):
    return w.scene("学級会議",
            w.plot_note("すぐに学級会議がもたれた"),
            w.plot_note("誰もハミダシモノに立候補しない"),
            w.plot_note("投票でハミダシモノを選ぼうという話になるが「生徒の自主性を大切にする」という項目の評価点が下がると$misoraが指摘する"),
            w.plot_note("そこから立候補が出るまで問題は据え置きにされる"),
            )


def outcast(w: World):
    return w.scene("ハミダシモノ",
            w.plot_note("その週末、ハミダシモノ立候補の締切がやってくる"),
            w.plot_note("$akoは会議の冒頭でハミダシモノに立候補し、そのまま彼女が最初のハミダシモノに決定した"),
            )


def outcast_status1(w: World):
    return w.scene("ハミダシモノの生活",
            w.plot_note("授業スケジュールが届かず、宿題も教えてもらえない"),
            )


def alone_class(w: World):
    return w.scene("孤独な授業",
            w.plot_note("$akoは別室での授業の時にも一人で教室に残り、自分で参考書を開く"),
            w.plot_note("完全に自立して学校の勉強をするようになった"),
            )


def regular_evaluation(w: World):
    return w.scene("定期評価",
            w.plot_note("月始めに前月の成績が発表される"),
            w.plot_note("$akoの名前は「ランク外」という特別項目に記載されていた"),
            w.plot_note("評価点が得られないと前期終了後に退学勧告がなされると書かれている"),
            )


def free_alone(w: World):
    return w.scene("自由な孤独",
            w.plot_note("しかしそんな状況下にあっても$akoは平気で暮らしていた"),
            w.plot_note("むしろ自由に自分で計画が立てられ、教科書も早くに勉強を終えてしまえる"),
            w.plot_note("授業には参加していたが、決して当てられることもないので、常に参考書や小説を読んでいた"),
            )


def jealousy(w: World):
    return w.scene("嫉妬勢",
            w.plot_note("そんな$akoの姿に一部からは嫉妬や憧れが出てくる"),
            w.plot_note("クラスグループのチャット欄には成績評価さえなければ自分もハミダシモノになると言い出す者も"),
            )


def continued(w: World):
    return w.scene("ハミダシモノは続く",
            w.plot_note("輪番制だったハミダシモノだが、次のハミダシモノを決める時にも誰も立候補せず"),
            w.plot_note("そのまま$akoが続けてハミダシモノとなることが決定した"),
            )


def reversal(w: World):
    return w.scene("逆転",
            w.plot_note("しかし翌月の評価では何故かハミダシモノのはずの$akoがトップとなっていた"),
            )


def protest(w: World):
    return w.scene("抗議",
            w.plot_note("$AIによる前期の中間判定が出されたことに対して生徒たちはみな文句を言った"),
            w.plot_note("担任の$mizuもおかしいと思って抗議をしたが、$AIによる判定に従うこととしか言われない"),
            w.plot_note("生徒たちは$akoに対して嫉妬の嵐で、彼女を潰そうと実力行使に出ていた"),
            w.plot_note("しかし校則違反をした者として処罰され、退学処分になっていく"),
            )


def new_outcast(w: World):
    return w.scene("新しいハミダシモノ",
            w.plot_note("そんな中で$misoraはハミダシモノに立候補する"),
            w.plot_note("ハミダシモノになった$misoraは評価が上がる"),
            w.plot_note("生徒たちは次々とハミダシモノになり、クラスには「まともな生徒」が不在になる"),
            )


def alone_regular(w: World):
    return w.scene("孤独な正規者",
            w.plot_note("$akoはハミダシモノをやめる"),
            w.plot_note("$akoだけが「正常な生徒」となった"),
            )


def dropout_outcasts(w: World):
    return w.scene("ハミダシモノたちの退学",
            w.plot_note("前期の最後の評価、再び$akoだけが評価され、ハミダシモノとなった他の生徒は落第の判定が出た"),
            w.plot_note("全員に退学処分が課せられ、そのうえ責任を取って担任はくびになる"),
            )


def new_class(w: World):
    return w.scene("新しいクラス",
            w.plot_note("教室には$akoだけがいた"),
            w.plot_note("ドアが開き、新しい生徒が入ってきたと思ったら復帰した$noriだった"),
            w.plot_note("彼女は「みんなは？」と尋ねたが$akoは「今ここにいるのが全生徒だよ」と笑った"),
            )
