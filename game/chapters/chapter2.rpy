##----------------
## Chapter 2: The War Arrives
##----------------

image transition_background = im.Scale("Transition/Background_Transition.png", 1920, 1080)
image transition_line = im.Scale("Transition/Line_Transition.png", 1617, 269)
image transition_cap_number_2 = im.Scale("Transition/Cap_2_Number.png", 510, 198)
image transition_cap_title_2 = im.Scale("Transition/Cap_2_Text.png", 441, 92)

label ch2:
    play sound "audio/sfx/Intro_Transition.mp3"
    scene transition_background with scene_fade
    show transition_cap_number_2:
        xpos 0.37
        ypos 0.29
    with transition_dissolve
    show transition_line:
        xpos 0.08
        ypos 0.4
    with transition_dissolve
    show transition_cap_title_2 :
        xpos 0.38
        ypos 0.6
    with transition_dissolve
    pause

    scene scene_1 with scene_fade