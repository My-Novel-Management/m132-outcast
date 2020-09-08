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
            ("HR", "ＨＲ"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

