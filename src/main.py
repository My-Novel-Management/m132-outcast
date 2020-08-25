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
MAJOR, MINOR, MICRO = 0, 1, 0
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
def ep_xxx(w: World):
    return w.episode('episode_title',
            outline="description")


def ch_main(w: World):
    return w.chapter('main',
            )


# Notes
def write_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            )

def stage_note(w: World):
    return w.writer_note("場所メモ",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
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

