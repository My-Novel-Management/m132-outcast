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
            "髪とかはゲートで説明したので割愛可能",
            "$akoと$noriは話しながら。話題は小説がいいかな。責任や義務といったもの。あるいはドストエフスキー",
            "キケロの『義務について』にしておく。そこで語られる「中間義務」と「絶対義務」についての話を混ぜておく",
            ako.come("教室に入ってくる"),
            nori.come("$Sも一緒に"),
            ako.do("同じ制服で髪も全員黒。長さも長すぎても短すぎても駄目"),
            ako.do("集まってしゃべるようなことはなく、全員が自分の席で端末を使い、今日のスケジュール確認をしている"),
            "ここで各自のルーティーンを見せる。スケジュール確認。あと教室の設備",
            "監視カメラにより撮影され、そこでの姿も全てが評価対象とされている、という注意書きなど",
            "電子黒板には情報が常に表示されている",
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
            "ここを前と連結して",
            "電子黒板に『四月期の成績表』として表示され、そこに$misoraが一番で$noriが二番目とする",
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
            w.cmd.change_time("midmorning"),
            w.cmd.change_date("Refusal"),
            w.br(),
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
            w.cmd.change_time("morning"),
            w.cmd.change_date("SuggestAI"),
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
            w.cmd.change_time("afternoon"),
            w.plot_note("しかしその日の終わり、$AIが出した結論はいじめはなくならないから輪番制で「ハミダシモノ」を作ろうという提案だった"),
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
            w.cmd.change_time("afternoon"),
            w.cmd.change_date("SuggestMeeting"),
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
            w.cmd.change_time("afternoon"),
            w.cmd.change_date("SuggestLimit"),
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
            w.cmd.change_time("morning"),
            w.plot_note("授業スケジュールが届かず、宿題も教えてもらえない"),
            "担任と一緒に教室に入る",
            "その際に色々と説明を受けている感じに",
            "明日からはどうするか、という問いに対して職員ゲートを通るようにと言いつけた",
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
            w.cmd.change_time("midmorning"),
            w.plot_note("$akoは別室での授業の時にも一人で教室に残り、自分で参考書を開く"),
            w.plot_note("完全に自立して学校の勉強をするようになった"),
            "移動教室の授業中、という感じに",
            "パソコン教室で授業が行われているが入室許可がなかった為にここで自発的に自習している、と",
            "この間に、$noriからメッセージが届くことに",
            ako.be("教室には$Sしかいない"),
            ako.do("$Sは一人参考書を開いて勉強している"),
            ako.do("机の上に出した端末はエラー画面のままで時刻だけ表示している"),
            ako.do("ハミダシモノに登録されると学内設備が全て使えなくなる"),
            ako.do("スケジュールも通知されず、移動教室も分からない"),
            ako.do("出席も受け付けず、完全にいないものとして扱われていた"),
            ako.do("それでも気にせず$Sは一人黙々と勉強をする"),
            ako.do("そこに生徒たちが戻ってくる"),
            misora.come(),
            misora.do("$akoを見て不敵な笑みの$S"),
            misora.talk("教室の空気が以前よりもすっきりとしているような気がするわ",
                "本当に$AIによる管理というのは不純物をきっちりと排除できる素晴らしいシステムだと思わない？"),
            misora.do("周囲は$misoraに同調する"),
            ako.do("わざと端末を床に落として、大きな音が響く"),
            misora.do("$Sは歩いてきてそれを拾い上げ、何も言わずに机に置く"),
            misora.talk("手が汚れたから洗ってきますね"),
            misora.go("そう言って教室を出ていく$S"),
            )


def regular_evaluation(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("ハミダシモノの定期評価",
            w.cmd.change_stage("Classroom"),
            w.cmd.change_time("morning"),
            w.cmd.change_date("EvalTimeJune"),
            w.plot_note("月始めに前月の成績が発表される"),
            w.plot_note("$akoの名前は「ランク外」という特別項目に記載されていた"),
            w.plot_note("評価点が得られないと前期終了後に退学勧告がなされると書かれている"),
            ako.be(),
            misora.be(),
            mizu.be("教壇に立ち、電子黒板に何か表示している"),
            mizu.talk("みなさん、先月の成績が発表されています",
                "各自の端末で確認して下さい"),
            ako.do("$Sは一応自分の端末を見る",
                "先月は結果を見ることすらできなかったが、今回はアクセスすることができた"),
            ako.do("声が漏れる"),
            ako.do("成績表には「ランク外」という項目が設けられ、そこに$akoの名前があった"),
            mizu.talk("五月分もトップは$fn_misoraさんです", "この調子でがんばってください"),
            misora.talk("まあ、当然の結果だと思います",
                "それよりこちらにランク外とありますが、成績の著しく低い生徒は退学処分と学則にあるのですが、",
                "この方は大丈夫なのでしょうか？"),
            mizu.talk("退学については総合的に$sivaが判断するようです",
                "ただ成績評価が悪ければおそらく前期の終わりには何かしらの処分が出ると思いますよ"),
            misora.talk("ですって", "わかりました",
                "$meたちはこうならないように気をつけましょうね、みなさん"),
            ako.do("その「みなさん」に自分は含まれていないのだと$Sは理解した"),
            )


def free_alone(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("自由な孤独",
            w.cmd.change_stage("Classroom"),
            w.cmd.change_time("midmorning"),
            w.cmd.change_date("HamidashiDay2"),
            w.plot_note("しかしそんな状況下にあっても$akoは平気で暮らしていた"),
            w.plot_note("むしろ自由に自分で計画が立てられ、教科書も早くに勉強を終えてしまえる"),
            w.plot_note("授業には参加していたが、決して当てられることもないので、常に参考書や小説を読んでいた"),
            "慣れた様子の$akoで、授業から完全に空気扱いになっている様を",
            "それと同時に夏休みが近づいている描写を",
            ako.be("授業中"),
            misora.be(),
            mizu.be("教壇に立ち、国語の授業中"),
            ako.do("一人だけ参考書を開いている$S"),
            ako.do("輪番制のはずが翌月になってもハミダシモノは$Sのままだった"),
            ako.do("完全に空気のような扱いで、授業で当てられることもない"),
            ako.do("それは得点機会が全くなく、評価のあげようがないということでもある"),
            misora.talk("あはれ、とはしみじみとした趣がある、という意味です"),
            mizu.talk("ありがとう", "こういった基本的な意味は全て暗記してしまって下さい",
                "特に現代語との差が大きな言葉についてテストされることが多いので、それらを中心に見ておくように"),
            )


def jealousy(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    noza = w.get("noza")
    return w.scene("嫉妬勢",
            w.cmd.change_stage("Classroom"),
            w.cmd.change_time("afterschool"),
            w.cmd.change_date("BeforeSummerDay"),
            w.plot_note("そんな$akoの姿に一部からは嫉妬や憧れが出てくる"),
            w.plot_note("クラスグループのチャット欄には成績評価さえなければ自分もハミダシモノになると言い出す者も"),
            "徐々に嫉妬が募っている様",
            "また夏休みに入る、ということを教える",
            "夏休み間に他の生徒たちは実家に帰省するという話を",
            "$akoについては一人で寮に残る、的なの",
            ako.be("教室に一人でいる"),
            misora.come("そこに$Sたちと取り巻きが入ってくる"),
            noza.come(),
            noza.talk("あ、いる",
                "なんでまだアイツがここにいるんだろ"),
            misora.talk("$fn_nozaさん、そんなこと言わないのよ",
                "例の方は一人で罰ゲームを続けてくれているのですから",
                "あの方のお陰でクラスで問題は起こらず、$meたちも学生生活に集中できるというものです"),
            noza.talk("それもアイツ読んでるの、漫画じゃないの",
                "校則で禁じられてはいないけど、でも風紀は乱してるわ"),
            misora.talk("まあまあ。あの程度の反抗くらいは見逃してあげませんと",
                "これ以上評価点下げてどうするつもりなのか知らないけれど、どうせ前期であの方は学校を去ることになるのよ"),
            noza.talk("ま、そうだけどね"),
            noza.do("でもどこか羨ましそうに"),
            ako.do("本を畳んで立ち上がり、教室を出ていく"),
            ako.do("誰もが$Sから距離を取るが、その視線の中には一部羨ましそうな目が混ざっていた"),
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
            w.cmd.change_time("morning"),
            w.cmd.change_date("AfterSummerDay"),
            w.plot_note("しかし翌月の評価では何故かハミダシモノのはずの$akoがトップとなっていた"),
            "夏休み開け、を描写",
            "$akoの髪が短くなっているのを目にして、少し驚いている風に",
            ako.be(),
            misora.be(),
            mizu.be(),
            ako.do("夏休みを終え、九月始めに七月八月を合わせた分の結果が発表された"),
            ako.do("そこには何故かトップに$akoの名が載っていた"),
            ako.do("クラス全員が言葉を失い、担任の$mizuは顔が青ざめている"),
            )


def protest(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    noza = w.get("noza")
    mizu = w.get("mizu")
    return w.scene("抗議",
            w.cmd.change_stage("Classroom"),
            w.cmd.change_time("midmorning"),
            w.plot_note("$AIによる前期の中間判定が出されたことに対して生徒たちはみな文句を言った"),
            w.plot_note("担任の$mizuもおかしいと思って抗議をしたが、$AIによる判定に従うこととしか言われない"),
            w.plot_note("生徒たちは$akoに対して嫉妬の嵐で、彼女を潰そうと実力行使に出ていた"),
            w.plot_note("しかし校則違反をした者として処罰され、退学処分になっていく"),
            "抗議をした生徒たちが戻ってきて教室で愚痴る、という展開",
            "ここでは何かいいたそうになるが、まだ黙っていること",
            ako.be("#一人で教室で本を読んでいる"),
            ako.do("エアコンが入っているから窓を開けないように、と注意書きが教室の前の壁に貼り付けられていたが、",
                "誰が開けていったのか窓が一つだけ開いていた",
                "日中は残暑というよりも真夏の暑さでそこから温風が流れ込んでくる",
                "$Sはシャツの下に汗が滲むのを感じながら文庫本のページを捲っていた",
                "読んでいるのは$noriから進められたドストエフスキーだ",
                "名前は知っていたけれどロシア文学の名前の覚えづらさからなかなか手に取れなかった",
                "けれどゆっくり時間のできた今年の夏に挑戦を決意したのだ"),
            misora.come("と、生徒たちの騒々しい声が廊下から響いてくる",
                "どうやら職員室に抗議に向かった女子たちが戻ってきたらしい"),
            noza.come(),
            noza.talk("なんで$misoraはもっと言ってくれなかったのよ？",
                "どう考えたっておかしいでしょ？",
                "アイツはハミダシモノなのよ？",
                "授業だって真面目に受けてない、学生生活だって全然協力的じゃないし、何の役割も負っていない",
                "評価すべき点なんてテストの点数以外に何もないはずなのにどういう理屈でトップになれるって言うのよ！"),
            ako.do("入ってくるなり手前の机を蹴りつけたのは$nozaだった",
                "いつも以上に甲高い声で小動物みたいな顔を真っ赤にしている"),
            misora.talk("何を言ったところで聞き入れてもらえないということが分かっただけでも収穫はあったと思いますよ",
                "おそらく$mizu先生も成績に関しての権限は一切持っていないということでしょう",
                "ただ今回の挙動がコンピュータのバグによるものかどうか調査してくれると仰ってましたから、",
                "その結果を待ちましょう"),
            noza.talk("よくそんな悠長なこと言ってられるわね？",
                "$misoraはいいわよ",
                "テストの点数に関しては心配する必要ないから",
                "けど$meたちは今月の評価と前期最終試験だけが頼りなのよ",
                "もしそこでも今回みたいな成績出されたら落第だって視野に入ってくるの", "分かってるの？"),
            ako.do("まあまあ落ち着いて、と$misoraは彼女たちを宥めながら自分の席に座る",
                "トップから落ちたとはいえそれでもまだ二位だった$misoraには一見余裕がありそうに見えた", "&"),
            misora.do("けれど手にしていた端末が抜け落ちるようにして床に転がると、腰を下ろした拍子で左足の先で蹴飛ばしてしまう", "&"),
            ako.do("床を滑りながらそれは$Sの足元までやってくると、上履きに触れて止まった"),
            ako.do("$Sは本に栞を挟んでから席を立ち、ハンカチで足元の端末を拾う",
                "その一連の動作の間、誰一人として声を上げず、$Sが$misoraの机の上にそっと置いてから教室を出ていくまで、",
                "まるで教室の時間が止まっているかのようにも思えた"),
            ako.go("#教室を出ていく"),
            )


def new_outcast(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("新しいハミダシモノ",
            w.cmd.change_stage("Classroom"),
            w.cmd.change_time("morning"),
            w.cmd.change_date("MisoraHamidashi"),
            w.plot_note("そんな中で$misoraはハミダシモノに立候補する"),
            w.plot_note("ハミダシモノになった$misoraは評価が上がる"),
            w.plot_note("生徒たちは次々とハミダシモノになり、クラスには「まともな生徒」が不在になる"),
            "朝に発表する",
            # TODO
            ako.be(),
            misora.be(),
            mizu.be(),
            ako.do("しかしその翌日、$misoraがハミダシモノに立候補した"),
            ako.do("他の生徒たちが驚く中、$mizuはそれを認める"),
            misora.do("微笑を見せる$S"),
            ako.do("その九月分の評価は$misoraがトップ、$akoが二番手となり、他の正規の生徒とは大きく差が開いた"),
            ako.do("その結果を受け、次々と生徒たちはハミダシモノになっていく"),
            )


def alone_regular(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("孤独な正規者",
            w.cmd.change_stage("Classroom"),
            w.cmd.change_time("afternoon"),
            w.cmd.change_date("OutHamidashi"),
            w.plot_note("$akoはハミダシモノをやめる"),
            w.plot_note("$akoだけが「正常な生徒」となった"),
            ako.be("電子黒板には大きく『自習』と表示されていた"),
            ako.do("$Sは窓際の席で一人参考書を開き、それに書き込みをしている",
                "けれど教室内でそんなことをしているのは彼女と$misoraくらいなもので、",
                "あとは楽しそうにおしゃべりをしたり、漫画を読んだり、ゲーム機を持ち込んで遊んでいたり、",
                "中にはお菓子を広げてまるでカラオケボックスのように大声で歌い始める集団までいた"),
            ako.do("今この中にはハミダシモノしかいない"),
            ako.do("おそらく他のクラスであれば学級崩壊と言われてもおかしくない惨状なのに、",
                "それに対して担任すら文句を言わなかった"),
            ako.do("誰かはこれを「自由」だと言った"),
            misora.be("#参考書を開いている"),
            ako.do("人間的欲望の本質は自由である――そう言ったのはドイツの哲学者ヘーゲルである",
                "あるいはフランスの哲学者サルトルによれば「人間は自由という刑に処せられている」と『存在と無』で論じた",
                "幸いにもというべきか、このクラスで倫理を選択するような生徒はおらず、こういった知識に特に興味を持たない同年代ばかりであろうが、",
                "$Sはいつも都合の良いように言葉の解釈を上書きして利用する彼女たちという存在こそが自由という言葉の具現化だと思えて、",
                "一人鼻先で笑ってしまった"),
            misora.talk("何か面白いことでもあったのかしら"),
            ako.do("ちょうどその場面を目撃してしまったのだろう",
                "前の方の席から立ち上がり、$Sの机までやってきた$misoraはつまらなそうにそう言って唇を結ぶ"),
            ako.talk("責任を取るべきだ、という意見を以前言ったのは覚えてるか？"),
            misora.talk("$fn_noriさんに対する責任があるのではないか、というようなことは言ったかも知れませんね",
                "けれどもうその問題については片付いたようなものじゃありません？",
                "彼女はこのまま前期で退学になるだろうし、あなたも総合的に見れば退学相当であってもおかしくはない",
                "それなのに$fn_akoさんは特に何も感じていらっしゃらないようにお見受けするんだけど、どうなの？"),
            ako.do("これまで通り$misoraは威圧的な態度を見せようとしていたが、腕組みをしながらもどこか視線は彷徨っている",
                "$Sは「特に何も思っていない」と端的に答え、一度だけ見上げた目をすぐに参考書へと戻した"),
            misora.talk("不快ね",
                "たった一度だけ機械のバグによって評価を受けたようなあなたがどうしてそこまで自信を持っていられるのか、",
                "理解に苦しみます",
                "成績は気にならないの？",
                "そもそも同級生のことをどう思っているの？",
                "他の子たちは手に取るように分かるのにあなただけは全く読めない",
                "それこそアンドロイドか何かなのかしらって思うくらいに"),
            ako.think("自分がアンドロイドだ、という意見は斬新な気がして思わず吹き出しそうになった",
                "それでもここで笑ってしまえば更に彼女を不快にさせるだけだと分かっていたのでぐっと堪え、",
                "$Sは彼女に対して一つだけ忠告をしておいてあげる"),
            ako.talk("$fn_misoraさんは薄々感づいているかも知れないと思うから敢えて言っておくけど、",
                "$sivaが何を基準に審査しているか、それを今一度考えてみた方がいいと思う",
                "そもそも点数のいい、よく規則を守る従順な人間を選ぶだけなら何もあんな$AIを導入する必要はなかったはずだからね"),
            misora.talk("何が、言いたいの？"),
            ako.think("彼女のその問いかけが分からないふりをして更に情報を引き出したいだけだと分かった$Sは、鼻で笑うと参考書を畳み、",
                "立ち上がる"),
            ako.talk("$meは今日でハミダシモノを辞めるわ",
                "それじゃあ"),
            misora.talk("$full_ako？"),
            ako.go("鞄を手にするともう一言も口にせず、$Sはハミダシモノだらけの教室を出ていく",
                    "廊下に出ても彼女たちの騒ぎ声はよく響いていて、それらの全ては監視カメラに付属しているマイクの性能があまりよくなくても充分に拾えているだろうな、と思った"),
            )


def dropout_outcasts(w: World):
    ako, misora = w.get("ako"), w.get("misora")
    mizu = w.get("mizu")
    return w.scene("ハミダシモノたちの退学",
            w.cmd.change_stage("Classroom"),
            w.cmd.change_time("morning"),
            w.cmd.change_date("Withdrawal"),
            w.plot_note("前期の最後の評価、再び$akoだけが評価され、ハミダシモノとなった他の生徒は落第の判定が出た"),
            w.plot_note("全員に退学処分が課せられ、そのうえ責任を取って担任はくびになる"),
            ako.be(),
            ako.do("十月に入り、前期の最終成績評価がその日、電子黒板には表示されていた",
                "ゲートチェックを終えて教室に入ってきた生徒たちは誰もがそこに書かれていた名前と文言を見て言葉を失ったという"),
            ako.do("Ｆ判定",
                "つまりは落第相当であり、事前に通告されていた通りこの判定を受けたものは退学処分となるとわざわざ注意書きがなされていた", "&"),
            ako.do("何人かその判定を受けたのかは黒板を見るまでもなく、",
                "教室に入って一分後には各自の端末にメッセージが着信し、誰もが赤字の警告文を目にしただろう"),
            ako.do("その日一番最後に入室した$akoだけが、その通知を受けなかった"),
            ako.do("つまり彼女だけが$sivaにより成績評価を得られたのだ", "それもＡ判定として"),
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
            ako.be("#一人で教室で本を読んでいる$S"),
            ako.do("$Sは読んでいたドストエフスキーの文庫本に栞を挟み、一旦机の上に置くと、",
                "立ち上がって窓からグラウンドを見下ろした",
                "道路脇の銀杏並木がすっかり黄色く色づき、大量の要らない葉が風で落下していく",
                "それを大型のブロワーで緑色の制服を着た作業員が集めていた"),
            nori.come("#そこに$Sがやってくる"),
            ako.do("不意に教室の戸が開けられた",
                "そこに姿を見せたのは見慣れた眼鏡で髪を随分と短くした$noriだった"),
            nori.talk("あれ？　みんなは？"),
            nori.do("彼女は椅子と机がほとんど撤去された部屋を見てその小さな口に右手を当てている"),
            ako.talk("おはよう、$nori"),
            nori.talk("うん、おはよう。$k_ako", "ねえ、他のみんなは？"),
            ako.talk("みんなって……$meと$noriだけだよ", "もうハミダシモノはいないから"),
            )
