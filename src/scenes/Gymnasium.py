# -*- coding: utf-8 -*-
'''
Stage: "体育館"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def old_friend(w: World):
    return w.scene('旧友との再会',
            w.plot_note("中学一年以来の再会である$noriは、他の生徒から邪険に扱われていた"),
            )

