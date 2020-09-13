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
from scenes import Cafeteria
from scenes import Classroom
from scenes import Corridor
from scenes import Dormitory
from scenes import Gate
from scenes import Ground
from scenes import Gymnasium
from scenes import HighSchool
from scenes import Library
from scenes import PCRoom
from scenes import Room
from scenes import Toilet


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K
#   4. Spec
#   5. Plot         - 1/4: 2K
#   6. Scenes
#   7. Conte        - 1/2: 4K
#   8. Layout
#   9. Draft        - 1/1: 8K
#
################################################################

# Constant
TITLE = "ハミダシモノ、はじめました"
MAJOR, MINOR, MICRO = 0, 9, 0
COPY = "はみだすことは、悪だった"
ONELINE = "約8000字の青春短編。クラスで「ハミダシモノ」に立候補した少女は翌日から無視される"
OUTLINE = "クラスでなんとなく空気に馴染めずにいた少女は、中心的存在が募集した「ハミダシモノ」に立候補する。大切な人を守る為、翌日から孤独な戦いが始まった"
THEME = "はみ出すのはそれほど恐ろしいことなのか？"
GENRE = "青春／ヒューマンドラマ"
TARGET = "10-20years"
SIZE = "8K"
CONTEST_INFO = "妄想コンテスト「○○、はじめました」"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["ドラマ", "青春", "学生生活", "いじめ"]
RELEASED = (9, 10, 2020)


# Episodes
def ep_highschool(w: World):
    return w.episode("先進的学校",
            w.plot_setup("$akoは高校生"),
            Gate.checking(w),
            w.plot_setup("高校はテストケースの進学校で全寮制、全生徒にタブレットが支給される"),
            Classroom.this_rule(w),
            w.plot_setup("$akoと$noriは中学一年以来の知人"),
            Gymnasium.old_friend(w).omit(),
            w.plot_setup("生徒の評価は$AIにより行われ、誰もそれに口出しできないでいた"),
            Classroom.evaluation(w),
            w.plot_setup("$noriが不登校になる"),
            Gymnasium.bullying(w).omit(),
            Classroom.refusal(w),
            )

def ep_hamidashimono(w: World):
    return w.episode("ハミダシモノ",
            w.plot_setup("いじめがあったとタレコミがある"),
            Classroom.tips(w).omit(),
            w.plot_turnpoint("$AIは解決策として輪番制の「ハミダシモノ」を作ることを提案する"),
            Classroom.AIs_suggestion(w).omit(),
            w.plot_develop("しかし誰もハミダシモノになりたがらない"),
            Classroom.meeting(w).omit(),
            w.plot_develop("$akoはハミダシモノに立候補する"),
            Classroom.outcast(w),
            w.plot_develop("$akoは翌日から空気として扱われる"),
            Gate.outcast_morning(w).omit(),
            Classroom.outcast_status1(w).omit(),
            w.plot_develop("授業スケジュールは送られてこず、全てを自力で解決する必要があった"),
            Library.nothing_right2(w).omit(),
            PCRoom.nothing_right(w).omit(),
            Classroom.alone_class(w),
            Cafeteria.nothing_right(w).omit(),
            Ground.alone_run(w).omit(),
            w.plot_develop("$AIの定期評価ではランク外になる$ako"),
            Classroom.regular_evaluation(w).omit(),
            w.plot_develop("孤立しても平気で生活を続ける$ako"),
            Classroom.free_alone(w).omit(),
            w.plot_develop("やがて$AIの評価に怯えない自由な$akoの姿に嫉妬と憧れが集まる"),
            Classroom.jealousy(w).omit(),
            w.plot_develop("けれど誰もハミダシモノの次の番を引き受けようとはしなかった"),
            Classroom.continued(w).omit(),
            Toilet.nori_thought(w).omit(),
            w.plot_develop("一方、そんな中、夏休みに入る",
                "$akoは$noriとメッセージでやり取りを続けていた"),
            w.plot_turnpoint("そこに$sivaからメッセージが届いた"),
            Dormitory.backto_domitory(w),
            Room.mystery_message(w),
            w.plot_turnpoint("$AIによる月末の成績評価で、何故かハミダシモノの$akoがトップになる"),
            Classroom.reversal(w),
            )

def ep_AI_result(w: World):
    return w.episode("AIの評価",
            w.plot_resolve("生徒たちは誰もが文句を言ったが$AI判定は覆らない"),
            Classroom.protest(w),
            w.plot_resolve("$misoraがハミダシモノに立候補した"),
            Classroom.new_outcast(w),
            w.plot_resolve("次々と生徒がハミダシモノになり、やがてクラスは崩壊する"),
            w.plot_resolve("$ako一人だけがハミダシモノではなくなった"),
            Classroom.alone_regular(w),
            w.plot_resolve("次の月末評価で、今度は$akoだけが成績評価され、ハミダシモノは全員落第の判定が出た"),
            Classroom.dropout_outcasts(w),
            w.plot_resolve("$ako一人だけがいる教室に、$noriがやってくる"),
            w.plot_resolve("「みんなは？」という$noriに「ここにいるのがみんなだよ」と$akoは笑って答えた"),
            Classroom.new_class(w),
            )


def ch_main(w: World):
    return w.chapter('main',
            ep_highschool(w),
            ep_hamidashimono(w),
            ep_AI_result(w),
            w.symbol("（了）"),
            )


# Notes
def write_note(w: World):
    return w.writer_note("覚書",
            "はみだすことを嫌がる",
            "和を大切にとか、空気を読もうとか、そんな言葉で個人の心を縛り付ける",
            "社会や組織とはそういうものであり、個人が勝手に動くことに対して抵抗力の強い集団が形成されてしまっている",
            "本作ではその最たるものである「学校」という集団の中で、強制的に「ハミダシモノ」を作る",
            "自らそれに立候補するというイレギュラーにより「協調性」を最優先としている学校制度に対して本当にそうなのかどうかを提示する",
            "これは学校への反逆の物語だ",
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

def characters(w: World):
    return (chara_ako(w),
            chara_misono(w),
            chara_mizu(w),
            chara_nori(w),
            )

def chara_ako(w: World):
    return w.chara_note("$akoの履歴書",
            "父親は外交官で母は華道の先生、という家に生まれる",
            "両親とも忙しく、実際の面倒は祖母に見てもらった",
            "祖母は元々は農家を営んでいて、自然と沢山触れるように$akoのことを教育した",
            "それが気に入らなかった両親、特に母親は、進学校で有名だったこの学校に娘を入れる",
            "中学入試は通ったものの、半分はコネだった",
            "高校に入り、特進コースに振り分けられた",
            "その年からちょうど$AIによる新教育カリキュラムが組まれ、優秀とされる生徒が集められたという経緯もあった",
            )

def chara_misono(w: World):
    return w.chara_note("$misoraの履歴書",
            "国家公務員の父と事務官の母の下に生まれる",
            "三人姉妹の二番目で、よくできた姉と比べられて育つ",
            "学校では成績が良いのは当たり前で、どうすれば他人に対して優位に立てるかを考えて振る舞うようになる",
            "そういった人の上に立つ方法を姉たちから学ぶ",
            "特進クラスに選ばれ、そこでも一番になることを考えていたら、なんと$AIによる評価というのでどうすればいいか様子を伺いながらの生活となる",
            )

def chara_mizu(w: World):
    return w.chara_note("$mizuの履歴書",
            "栃木県の田舎町で生まれる",
            "農家をやりながらの中学教師と農協職員の下で育ち、兄二人妹と弟二人という大家族でうるさい中で育つ",
            "中学のときに教えてもらった国語教師に感動し、教師を目指す",
            "勉強の難しさから高校教師として就職する",
            "教え方がうまく、また教師同士の人間関係のやりくりがうまかった為に何故かとんとんと評価が上がり、",
            "特進クラスの担任に選ばれる",
            "しかしそこは$AIによる評価が行われるという前代未聞のクラスだった",
            )

def chara_nori(w: World):
    return w.chara_note("$noriの履歴書",
            "会社経営者の父と料理研究家の母の下に生まれる",
            "一人の兄、一人の姉の下で育つ",
            "小さい頃からあまり積極的ではなく、人付き合いも下手だった",
            "ただ勉強はよくできて、本もよく読んでいたので、成績だけは良かった",
            "中学からは進学校に入り、そこでも評価が高かった",
            "高等部で特進クラスに選抜され、どうしようかと困っていたところに、中学一年の時に同じクラスだった$akoと再会する",
            "あまり話さなかったが本や勉強を通して対等な関係だと思っていた",
            "しかし特進クラスは$AIによる評価で、成績がトップだった$noriは他の生徒から嫉妬される",
            "$SNSなどでいじめを受け、徐々に不登校になる",
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
            "人間だけでなく、AIによる評価を導入して、そこに対する反逆の物語も描く",
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
            "AIによる評価",
            )

def materials(w: World):
    return w.writer_note("素材",
            "２学期制について",
            "前期後期にする。学校によりいろいろ違っているが、十月初旬までを前期、十月中旬からを後期とする。秋休みが作れる（九月の連休にかませる）",
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
            *characters(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            materials(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

