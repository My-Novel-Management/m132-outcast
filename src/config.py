# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("ako", "亜子", "沢井,亜子", 16,(1,1), "female", "高校生", "me:あたし"),
            ("misora", "美空", "和木,美空", 16,(1,1), "female", "高校生", "me:わたし"),
            ("mizu", "水口", "", 37,(1,1), "male", "教師", "me:私"),
            ("nori", "典子", "相良,典子", 16,(1,1), "female", "高校生", "me:私:k_ako:沢井さん"),
            ("noza", "佳苗", "野崎,佳苗", 16,(1,1), "female", "高校生", "me:ワタシ"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("HighSchool", "高校", "Tokyo"),
            ("Classroom", "教室", "HighSchool"),
            ("Gate", "チェックゲート", "HighSchool"),
            ("Corridor", "廊下", "HighSchool"),
            ("Gymnasium", "体育館", "HighSchool"),
            ("Ground", "グラウンド", "HighSchool"),
            ("PCRoom", "パソコン室", "HighSchool"),
            ("Library", "図書室", "HighSchool"),
            ("Cafeteria", "食堂", "HighSchool"),
            ("Toilet", "トイレ", "HighSchool"),
            ("Dormitory", "学生寮", "HighSchool"),
            ("Room", "亜子の部屋", "Dormitory"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ("FirstTime", "はじめの日", 5,11, 2020),
            ("BullyDay", "いじめの日", 5,12, 2020),
            ("Refusal", "$noriの不登校開始日", 5,25, 2020),
            ("SuggestAI", "提案日", 6,2, 2020),
            ("SuggestMeeting", "提案会議", 6,3, 2020),
            ("SuggestLimit", "提案締切日", 6,5, 2020),
            ("HamidashiDay1", "ハミダシモノの初日", 6,8, 2020),
            ("EvalTimeJune", "六月の成績評価", 7,1, 2020),
            ("HamidashiDay2", "ハミダシモノの日常", 7,10, 2020),
            ("BeforeSummerDay", "夏休み前", 7,22, 2020),
            ("AfterSummerDay", "夏休み開けた日", 8,25, 2020),
            ("MisoraHamidashi", "美空がハミダシモノに立候補", 9,1, 2020),
            ("OutHamidashi", "ハミダシモノを辞めた日", 9,11, 2020),
            ("Withdrawal", "ハミダシモノたちの退学", 10,9, 2020),
            ("NewTerm", "新学期", 10,19, 2020),
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ("id", "ＩＤ"),
            ("AI", "ＡＩ"),
            ("SNS", "ＳＮＳ"),
            ("LINE", "ＬＩＮＥ"),
            ("siva", "ＳＩＢＡ"), # System of Intelligence Brain for Assessment
            ("full_siva", "System of Intelligence Brain for Assesment"),
            ("jpn_siva", "評価のための人工頭脳システム"),
            ("HR", "ＨＲ"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ("臙脂", "｜臙脂《えんじ》"),
            ("磨き", "｜磨《みが》き"),
            ("沢井亜子", "沢井亜子《さわいあこ》"),
            ("相良典子", "相良典子《さがらのりこ》"),
            ("野崎佳苗", "野崎佳苗《のざきかなえ》"),
            ("概ね", "概《おおむ》ね"),
            ("和木美空", "和木美空《わきみそら》"),
            ),
        }

