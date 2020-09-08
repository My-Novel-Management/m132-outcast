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
    ako, misora = w.get("ako"), w.get("misora")
    mizu, nori = w.get("mizu"), w.get("nori")
    return w.scene('この高校のルール',
            w.cmd.change_stage("Classroom"),
            "教室：みんながタブレットを手にやり取りしている。その日の授業や課題を確認する",
            w.plot_note("担任の$mizuはきちんとルールを守り、今まで通りに生活すればいいと言う"),
            ako.come("教室に入ってくる"),
            ako.do("同じ制服で髪も全員黒。長さも長すぎても短すぎても駄目"),
            ako.do("集まってしゃべるようなことはなく、全員が自分の席で端末を使い、今日のスケジュール確認をしている"),
            ako.do("自分の席に就く"),
            nori.come("ぎりぎりの時間にやってくる$S"),
            nori.do("$akoを見て安心して駆け寄ってくる"),
            "$noriの外見特徴など",
            nori.talk("おはよう、$k_ako", "髪の毛ちゃんと縛ったのにゲートに引っかかっちゃった"),
            ako.talk("おはよう"),
            nori.do("自分の席に就く"),
            )


def evaluation(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu, nori = w.get("mizu"), w.get("nori")
    return w.scene("成績評価",
            w.cmd.change_stage("Classroom"),
            w.plot_note("最初のテスト後に$AIの成績評価が出された"),
            w.plot_note("それはテストだけでなく、普段の生活でのポイントも加味されている"),
            w.plot_note("委員長に選出された$misoraがトップだった"),
            w.plot_note("しかし何もやってないはずの$noriが次点で、そこから彼女へのいじめが始まる"),
            ako.be(),
            misora.be(),
            nori.be(),
            mizu.come("教室に入ってくる$S"),
            "$mizuの外見",
            mizu.talk("おはようございます"),
            mizu.talk("つい先程四月分の成績評価がアップされました",
                "この評価は全て$sivaによるものですので、$meに何か言われても上に報告することしかできないので、",
                "その辺りを考えて今後行動を改めるようにお願いします"),
            mizu.do("事務的な口調"),
            ako.do("先に他の生徒たちが声を漏らす"),
            ako.do("端末を操作して自分の席席を確認する$S"),
            ako.do("テストの点数に関しては概ねＡ評価のはずだけれど、$AIが下した結果は全体で８０点といったところだった"),
            ako.do("トップはクラス委員をしている$misoraで、次点が$noriだった"),
            misora.talk("$AIは総合評価をするように調整されているんでしょう",
                "テストの点数だけならこんな結果にならないもの"),
            ako.do("彼女の取り巻きたちは「それでもすごい」と連呼する"),
            ako.do("その集団を一瞥する"),
            ako.do("何の役割もしていないし、体育などでもいつもお荷物の$noriに非難の視線が集中していた"),
            )


def refusal(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    nori = w.get("nori")
    return w.scene("不登校",
            w.cmd.change_stage("Classroom"),
            w.plot_note("やがて精神バランスを壊して$noriは入院という名の不登校になった"),
            ako.be(),
            misora.be(),
            mizu.come("やってくる"),
            ako.do("教室には一つだけ空席があった"),
            mizu.talk("$fn_noriさんからは欠席の連絡を受けています",
                "それでは各自今日の予定を確認して、規律正しい一日を送って下さい"),
            mizu.go("それだけ言って出ていく"),
            )


def tips(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("タレコミ",
            w.cmd.change_stage("Classroom"),
            w.plot_note("ある日$mizuから$AIに「クラスでいじめがあった」と報告が入っていたと言われる"),
            w.plot_note("個人個人の端末から$AIに通報することが簡単にできた"),
            w.plot_note("個人情報は秘匿され、担任の$mizuも誰が言ったのか分からないという"),
            w.plot_note("クラス会議で確認したが、いじめの事実はなかった"),
            w.plot_note("$mizuはそう伝えると言った"),
            ako.be(),
            misora.be(),
            mizu.come("入ってくる$S"),
            ako.do("教室はざわついている"),
            ako.do("グループチャット内では$noriに対するアレがばれたと話題になっている"),
            mizu.talk("席について"),
            mizu.talk("実は先日、端末による通報がありました",
                "$fn_noriさんの欠席が長引いている件について、いじめが原因の不登校ではないかというものです",
                "こちらでも確認しましたが、体調を崩したことから大事をとって療養中ということです",
                "そもそも選抜された生徒によるいじめがある、というのは想定されていません",
                "そうならないように様々なデータから$sivaが選んだのです",
                "勝手な想像でものを言わないように"),
            ako.do("担任も自分の査定があるのでピリピリしている"),
            ako.do("けれどどう考えても$noriが四月の評価で二位になったことによるものだった"),
            )


def AIs_suggestion(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("$AIの提案",
            w.cmd.change_stage("Classroom"),
            w.plot_note("しかし翌日、$AIが出した結論はいじめはなくならないから輪番制で「ハミダシモノ」を作ろうという提案だった"),
            ako.be(),
            misora.be(),
            mizu.come("教室に青い顔で入ってくる$S"),
            mizu.talk("$fn_noriさんの件について、$sivaが対策を講じました",
                "みなさん端末を見て下さい"),
            ako.do("誰からも声が上がる"),
            ako.do("そこに表示されていたのは「輪番制のハミダシモノ」というタイトルだった"),
            )


def meeting(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("学級会議",
            w.cmd.change_stage("Classroom"),
            w.plot_note("すぐに学級会議がもたれた"),
            w.plot_note("誰もハミダシモノに立候補しない"),
            w.plot_note("投票でハミダシモノを選ぼうという話になるが「生徒の自主性を大切にする」という項目の評価点が下がると$misoraが指摘する"),
            w.plot_note("そこから立候補が出るまで問題は据え置きにされる"),
            ako.be(),
            misora.be(),
            mizu.be(),
            ako.do("翌日の$HR"),
            ako.do("最初のハミダシモノを決める会議が行われていた"),
            ako.do("だが誰一人として立候補しない"),
            misora.talk("このままだと永遠に決まりません",
                "投票という形にしてはいかがでしょうか？"),
            mizu.talk("その案については$sivaによって却下されているわ",
                "$sivaはこれを立候補で決めることが重要だと示しているの",
                "$meたちはそれに従うしかない"),
            ako.do("時間だけが過ぎる"),
            mizu.talk("締切は今週の金曜の十七時だから",
                "それまでに各自、立候補について考えておくように"),
            )


def outcast(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("ハミダシモノ",
            w.cmd.change_stage("Classroom"),
            w.plot_note("その週末、ハミダシモノ立候補の締切がやってくる"),
            w.plot_note("$akoは会議の冒頭でハミダシモノに立候補し、そのまま彼女が最初のハミダシモノに決定した"),
            ako.be(),
            misora.be(),
            ako.do("金曜の授業終わりだった"),
            ako.do("$misoraが$akoの前にやってくる"),
            misora.talk("$fn_akoさんは考えてきたかしら？　立候補のこと"),
            ako.talk("一応"),
            misora.talk("思うんだけどね、誰かが責任を取れってことなんじゃないかしら"),
            ako.do("何も答えない"),
            misora.talk("あなたは$fn_noriさんがクラスで孤立を知っていたわよね？",
                "それを助けようとしなかった",
                "お友達じゃなかったの？"),
            ako.talk("中学一年の時に同じクラスだった",
                "ここで再会したのは偶然だ",
                "それだけの関係を友達と呼ぶなら、そうなんだろうな"),
            misora.talk("責任という言葉の意味を、考えたことはある？"),
            ako.talk("どの責任について？", "法的？　それとも社会的責任？"),
            misora.do("意味が理解できずに困惑する"),
            misora.talk("よく考えて$fn_noriさんが不登校になったことに対して、あなたはどうすべきなのかということよ"),
            misora.do("自分の席に戻る"),
            mizu.come("教室に入ってくる$S"),
            ako.do("険しい表情の$mizu"),
            ako.do("クラスは静まり返っている"),
            misora.do("前に出て議事進行をする"),
            misora.talk("それでは本日がハミダシモノの締切となります",
                "立候補の方は挙手をお願いします"),
            ako.do("誰も上げない"),
            ako.do("クラスのみんながそう思っていたが、$Sの右手が真っ直ぐに上がっている"),
            ako.do("驚きの声がもれていた"),
            misora.talk("$fn_ako、さん？"),
            ako.talk("立候補します"),
            ako.do("こうしてハミダシモノになった"),
            )


def outcast_status1(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("ハミダシモノの生活",
            w.cmd.change_stage("Classroom"),
            w.plot_note("授業スケジュールが届かず、宿題も教えてもらえない"),
            ako.come("ゲート外の非常ドアを通って教室へと遅れてやってくる$S"),
            mizu.come("先生と共に教室に入る"),
            ako.do("教室の同級生たちの痛い視線"),
            ako.do("自分の席につく$S"),
            mizu.talk("おはようございます",
                "今朝は特に連絡事項はありません",
                "それでは各自スケジュールを確認し、規律正しい一日を送って下さい"),
            mizu.talk("あと、それから$fn_akoさん",
                "あとで職員室に来て",
                "一時間目が終わってからでいいから"),
            ako.talk("分かりました"),
            )


def alone_class(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("孤独な授業",
            w.cmd.change_stage("Classroom"),
            w.plot_note("$akoは別室での授業の時にも一人で教室に残り、自分で参考書を開く"),
            w.plot_note("完全に自立して学校の勉強をするようになった"),
            ako.be("教室には$Sしかいない"),
            ako.do("$Sは一人参考書を開いて勉強している"),
            ako.do("机の上に出した端末はエラー画面のままで時刻だけ表示している"),
            ako.do("ハミダシモノに登録されると学内設備が全て使えなくなる"),
            ako.do("スケジュールも通知されず、移動教室も分からない"),
            ako.do("出席も受け付けず、完全にいないものとして扱われていた"),
            ako.do("それでも気にせず$Sは一人黙々と勉強をする"),
            ako.do("そこに生徒たちが戻ってくる"),
            misora.come(),
            misora.do("$akoを見て不敵な笑み"),
            misora.talk(""),
            # TODO
            )


def regular_evaluation(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("定期評価",
            w.cmd.change_stage("Classroom"),
            w.plot_note("月始めに前月の成績が発表される"),
            w.plot_note("$akoの名前は「ランク外」という特別項目に記載されていた"),
            w.plot_note("評価点が得られないと前期終了後に退学勧告がなされると書かれている"),
            )


def free_alone(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("自由な孤独",
            w.cmd.change_stage("Classroom"),
            w.plot_note("しかしそんな状況下にあっても$akoは平気で暮らしていた"),
            w.plot_note("むしろ自由に自分で計画が立てられ、教科書も早くに勉強を終えてしまえる"),
            w.plot_note("授業には参加していたが、決して当てられることもないので、常に参考書や小説を読んでいた"),
            )


def jealousy(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("嫉妬勢",
            w.cmd.change_stage("Classroom"),
            w.plot_note("そんな$akoの姿に一部からは嫉妬や憧れが出てくる"),
            w.plot_note("クラスグループのチャット欄には成績評価さえなければ自分もハミダシモノになると言い出す者も"),
            )


def continued(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("ハミダシモノは続く",
            w.cmd.change_stage("Classroom"),
            w.plot_note("輪番制だったハミダシモノだが、次のハミダシモノを決める時にも誰も立候補せず"),
            w.plot_note("そのまま$akoが続けてハミダシモノとなることが決定した"),
            )


def reversal(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("逆転",
            w.cmd.change_stage("Classroom"),
            w.plot_note("しかし翌月の評価では何故かハミダシモノのはずの$akoがトップとなっていた"),
            )


def protest(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("抗議",
            w.cmd.change_stage("Classroom"),
            w.plot_note("$AIによる前期の中間判定が出されたことに対して生徒たちはみな文句を言った"),
            w.plot_note("担任の$mizuもおかしいと思って抗議をしたが、$AIによる判定に従うこととしか言われない"),
            w.plot_note("生徒たちは$akoに対して嫉妬の嵐で、彼女を潰そうと実力行使に出ていた"),
            w.plot_note("しかし校則違反をした者として処罰され、退学処分になっていく"),
            )


def new_outcast(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("新しいハミダシモノ",
            w.cmd.change_stage("Classroom"),
            w.plot_note("そんな中で$misoraはハミダシモノに立候補する"),
            w.plot_note("ハミダシモノになった$misoraは評価が上がる"),
            w.plot_note("生徒たちは次々とハミダシモノになり、クラスには「まともな生徒」が不在になる"),
            )


def alone_regular(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("孤独な正規者",
            w.cmd.change_stage("Classroom"),
            w.plot_note("$akoはハミダシモノをやめる"),
            w.plot_note("$akoだけが「正常な生徒」となった"),
            )


def dropout_outcasts(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("ハミダシモノたちの退学",
            w.cmd.change_stage("Classroom"),
            w.plot_note("前期の最後の評価、再び$akoだけが評価され、ハミダシモノとなった他の生徒は落第の判定が出た"),
            w.plot_note("全員に退学処分が課せられ、そのうえ責任を取って担任はくびになる"),
            )


def new_class(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    nori = w.get("nori")
    return w.scene("新しいクラス",
            w.cmd.change_stage("Classroom"),
            w.plot_note("教室には$akoだけがいた"),
            w.plot_note("ドアが開き、新しい生徒が入ってきたと思ったら復帰した$noriだった"),
            w.plot_note("彼女は「みんなは？」と尋ねたが$akoは「今ここにいるのが全生徒だよ」と笑った"),
            )
