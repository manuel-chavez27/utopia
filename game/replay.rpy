## Replay screen ##############################################################
##
## This is a screen that displays the replay menu. 
##

screen replay:
    tag menu
    add "gui/replay/replay_background.png"
    hbox:
        yalign 0.075
        xalign 0.5
        imagebutton:
            idle im.Scale("gui/replay/replay_left_button.png", 150, 111)
            action Return()
        imagebutton:
            idle im.Scale("gui/replay/select_chapter_asset.png", 650, 153)
            left_margin -0.02
            top_margin -0.02
        imagebutton:
            #left_margin 0.275
            idle im.Scale("gui/replay/replay_right_button.png", 150, 111)
            left_margin -0.03
            action Return()
    hbox:
        xalign 0.5
        yalign 0.25
        vbox:
            fixed xsize 533 ysize 358:
                if persistent.sandstorm_scene:
                    imagebutton action Replay('ch0'):
                        idle im.Scale("Backgrounds/Sandstorm_Scene.png", 470, 290)
                        xpos 0.06
                        ypos 0.09
                    add im.Scale("gui/replay/replay_unlocked_chapter_box.png", 533, 358)
                else:
                    add im.Scale("gui/replay/replay_locked_chapter_box.png", 533, 358)
            add im.Scale("gui/replay/replay_button_chapter_0.png", 316, 60):
                xalign 0.6
                yoffset -40
        vbox:
            fixed xsize 533 ysize 358:
                add im.Scale("gui/replay/replay_locked_chapter_box.png", 533, 358)
                if not persistent.sandstorm_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Sandstorm_Scene.png', 'background_book'):
                        idle im.Scale("Backgrounds/Sandstorm_Scene.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            add im.Scale("gui/replay/replay_button_chapter_1.png", 316, 60):
                xalign 0.6
                yoffset -40
    hbox:
        xalign 0.5
        yalign 0.8
        vbox:
            fixed xsize 533 ysize 358:
                add im.Scale("gui/replay/replay_locked_chapter_box.png", 533, 358)
                if not persistent.sandstorm_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Sandstorm_Scene.png', 'background_book'):
                        idle im.Scale("Backgrounds/Sandstorm_Scene.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            add im.Scale("gui/replay/replay_button_chapter_2.png", 316, 60):
                xalign 0.6
                yoffset -40

        vbox:
            fixed xsize 533 ysize 358:
                add im.Scale("gui/replay/replay_locked_chapter_box.png", 533, 358)
                if not persistent.sandstorm_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Sandstorm_Scene.png', 'background_book'):
                        idle im.Scale("Backgrounds/Sandstorm_Scene.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            add im.Scale("gui/replay/replay_button_chapter_3.png", 316, 60):
                    xalign 0.6
                    yoffset -40