#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8
#   4. Spec
#   5. Plot         - 1/4
#   6. Scenes
#   7. Conte        - 1/2
#   8. Layout
#   9. Draft        - 1/1
#
################################################################

# Constant
TITLE = "ハミダシモノ、はじめました"
MAJOR, MINOR, MICRO = 0, 2, 0
COPY = "はみだすことは、悪だった"
ONELINE = "約8000字の青春短編。クラスで「ハミダシモノ」に立候補した少女は翌日から無視される"
OUTLINE = "クラスでなんとなく空気に馴染めずにいた少女は、中心的存在が募集した「ハミダシモノ」に立候補する。大切な人を守る為、翌日から孤独な戦いが始まった"
THEME = "はみ出すのはそれほど恐ろしいことなのか？"
GENRE = "青春／ヒューマンドラマ"
TARGET = "10-20years"
SIZE = "規定サイズ"
CONTEST_INFO = "コンテスト情報"
CAUTION = "注意事項"
NOTE = "備考"
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["ドラマ", "青春", "学生生活", "いじめ"]
RELEASED = (1, 1, 2020)


# Episodes
def ch_main(w: World):
    return w.chapter('main',
            )


# Notes
def write_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "クラスで「ハミダシモノ」の募集があり、少女はそれに立候補する",
            "ハミダシモノは昔でいえば「人身御供」である",
            "誰か一人をターゲットにして、自分の身の安全が保証される",
            "ただその一人は空気として扱われる",
            "完全に孤立し、影でいろいろと言われる",
            "グループにも参加できず、連絡網も回らず",
            "SNSの発達した学校で起こった悲劇",
            "しかし少女は逆にそれを利用し、孤立した",
            "やがてハミダシモノは派閥を広げ始める",
            "ハミダシモノは大きな集団となり、クラスを仕切っていた女子が孤立した",
            "彼女は自分もハミダシモノになりたいと言い出すが、誰もそれに賛同しなかった",
            "彼女は自分の負けを認めたが、そんなもの最初から気にしていなかった",
            "くだらない、と吐き捨て、ハミダシモノ騒動は幕を下ろした",
            "翌日から元のクラスが戻る",
            "しかしもう彼女に友人はいなかった",
            "少女は一人変わらずにハミダシモノを続けている",
            "それでも今までのように完全に孤立はしていない",
            "彼女が消しゴムを落としても誰も拾わなかったが、少女は立ち上がり、拾ってあげた",
            "あたしはハミダシモノだから、と笑いかけると「ありがとう」と彼女は泣いた",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "・主人公の少女：ハミダシモノの立候補し、自分からいじめの輪へと飛び込む",
            "・ボスの女子：クラスをコントロールしている女子",
            )

def stage_note(w: World):
    return w.writer_note("場所メモ",
            "学校（中学か高校）",
            "校舎は新しく、一人一台の端末が貸与される進学校",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "孤独、はみだすこと、なのかな",
            "孤独は友人つるむ派からは恐れられている",
            "しかし現代はSNSを介して様々なコミュニティを形成可能なので、クラスでの孤立、",
            "現実生活での孤立はそこまで恐れるものでもない",
            "でもネットで群れられるからこそ現実でも群れが欲しい、という気持ちもあるだろう",
            "群れの中にいた方が安全なのだから防衛本能からすればそれは納得できる",
            "いじめからの自殺はまだまだ多い、と思われる",
            "自殺件数そのものは減少傾向だが、ミクロで見ると中高生の自殺はやや増加か前年と大差ない推移をしている",
            "SNSによりいじめもより陰湿になったというが、死に至るには精神的にも肉体的にも孤立が必要となる",
            "一番の問題は家庭にあると思われるが、SNSの普及で、親に頼らずとも相談できる相手を得られる可能性が高まっている",
            "他方、それを悪用した犯罪も増えているので、一長一短である",
            "同調圧力の権化であるスマホ",
            "これを放棄することこそが、今回のテーマである",
            "そこから脱却することで、ハミダシモノとなる",
            "そういう反逆の物語",
            )

def motif_note(w: World):
    return w.writer_note("モチーフ",
            "孤立", "はみだす",
            "孤独",
            "学園生活", "学生",
            "集団",
            "個人",
            "ライングループ",
            "部活",
            "昼休み", "お弁当",
            "休み時間",
            "体育の時間",
            )

# Main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            write_note(w),
            plot_note(w),
            chara_note(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

