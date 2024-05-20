##----------------
## Chapter 1: Frederick Marcus
##----------------

image transition_background = im.Scale("Transition/Background_Transition.png", 1920, 1080)
image transition_line = im.Scale("Transition/Line_Transition.png", 1617, 269)
image transition_cap_number_1 = im.Scale("Transition/Cap_1_Number.png", 510, 198)
image transition_cap_title_1 = im.Scale("Transition/Cap_1_Text.png", 441, 92)

image oase_city = im.Scale("Backgrounds/Oase_City.png", 1920, 1080)
image oase_wall = "Backgrounds/Oase_Front_Gate_Daylight.png"

label ch1:
    play sound "audio/sfx/Intro_Transition.mp3"
    scene transition_background with scene_fade
    show transition_cap_number_1:
        xpos 0.37
        ypos 0.3
    with transition_dissolve
    show transition_line:
        xpos 0.08
        ypos 0.4
    with transition_dissolve
    show transition_cap_title_1 :
        xpos 0.38
        ypos 0.6
    with transition_dissolve
    pause

    scene oase_city with scene_fade
    play music gates_of_oase loop
    "The winds of the kingdom welcomed travelers from far and wide, coming out from between the heights of the mountains to bless the people with a breath of fresh air. The city stood in its might of shining glory from the middle of the plains between the hills."

    scene oase_wall with scene_fade

    f "So, this is it... Oase."

    "The strapping young knight took careful steps forward with his horse, riding down the steep road of cobblestone. Goats grazed about the pastures without a care in the world, though they would be beckoned back by their shepherds, who saw the foreigner. Frederick could only awkwardly smile and wave as he rode past them."
    "Those unaccustomed to this road were easy to spot because of how they walked—or rode. The gatekeepers could spot them from a mile away, and Frederick was no exception. One of them approached the knight as he would near the gate, holding his spear steady in hand."

    show fc serious:
        xpos 0.3
        ypos 0
    with dissolve

    "This is Frederick"

    show fc serious talking:
        xpos 0.3
        ypos 0

    f "Hello"

    show fc serious:
        xpos 0.3
        ypos 0

    "He talked"