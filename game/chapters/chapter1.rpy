##----------------
## Chapter 1: Frederick Marcus
##----------------

image transition_background = im.Scale("Transition/Background_Transition.png", 1920, 1080)
image transition_line = im.Scale("Transition/Line_Transition.png", 1617, 269)
image transition_cap_number_1 = im.Scale("Transition/Cap_1_Number.png", 510, 198)
image transition_cap_title_1 = im.Scale("Transition/Cap_1_Text.png", 441, 92)

image oase_city = "Backgrounds/Oase_City.png"
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

    $ textbox = "Narration"
    "The winds of the kingdom welcomed travelers from far and wide, coming out from between the heights of the mountains to bless the people with a breath of fresh air. The city stood in its might of shining glory from the middle of the plains between the hills."

    scene oase_wall with scene_fade

    $ textbox = "Dialogue"
    fm "So, this is it... Oase."
    $ textbox = "Narration"

    "The strapping young knight took careful steps forward with his horse, riding down the steep road of cobblestone. Goats grazed about the pastures without a care in the world, though they would be beckoned back by their shepherds, who saw the foreigner. Frederick could only awkwardly smile and wave as he rode past them."
    "Those unaccustomed to this road were easy to spot because of how they walked—or rode. The gatekeepers could spot them from a mile away, and Frederick was no exception. One of them approached the knight as he would near the gate, holding his spear steady in hand."

    show fc base serious:
        xcenter 0.85
        ypos 0
        darken
    with dissolve

    show cso base serious:
        xcenter 0.15
        ypos 0
        flip
        darken
    with dissolve

    show cso talking serious:
        xcenter 0.15
        ypos 0
        flip
        lighten

    $ textbox = "Dialogue"
    cso "Halt there. What business do you have in our city?"

    show cso base serious:
        xcenter 0.15
        ypos 0
        flip
        darken
    
    
    show fc talking serious:
        xcenter 0.85
        ypos 0
        lighten
    

    fm "I'm Frederick Marcus, son of Volker Marcus. Lord Horace Annot called for my father to come to his manor, and I have come here in his stead. Here’s the letter Lord Annot sent. Please look at its contents if you wish to verify."

    show fc base serious:
        xcenter 0.85
        ypos 0
        darken
    

    show cso talking serious:
        xcenter 0.15
        ypos 0
        flip
        lighten

    cso "Hmm… that's Lord Annot's seal, no doubt about it. Wait here for a moment."

    show cso base serious:
        xcenter 0.15
        ypos 0
        flip
        darken
    
    show fc talking serious:
        xcenter 0.85
        ypos 0
        lighten
    
    fm "Got it."

    hide cso base serious with dissolve
    hide fc talking serious with dissolve

    $ textbox = "Narration"
    "After taking the letter from Frederick, the guard approached the iron gates and passed the letter through. It was received by a tall, bald man with dark skin, and a large scar by the neck. The man opened the letter, read it briefly, and then went to look at Fredrick up and down."

    show fc base serious:
        xcenter 0.85
        ypos 0
        darken
    with dissolve

    show tm base serious:
        xcenter 0.15
        ypos 0
        flip
        darken
    with dissolve

    show tm talking serious:
        xcenter 0.15
        ypos 0
        flip
        lighten

    $ textbox = "Dialogue"
    tm "Yeah… looks about right. Open the gates."

    show tm base serious:
        xcenter 0.15
        ypos 0
        flip
        darken

    $ textbox = "Narration"
    "As Frederick approached, the tall man issuing orders reached out his hand for the knight to shake."

    show tm talking serious:
        xcenter 0.15
        ypos 0
        flip
        lighten

    $ textbox = "Dialogue"
    tm "You sure are the spitting image of your father, boy. How is he doing?"

    show tm base serious:
        xcenter 0.15
        ypos 0
        flip
        darken

    show fc talking serious:
        xcenter 0.85
        ypos 0
        lighten
    
    fm "He is doing quite well, thank you."

    hide tm base serious

    show fc base serious:
        xcenter 0.85
        ypos 0
        darken

    show ca talking serious:
        xcenter 0.15
        ypos 0
        flip
        lighten
    
    ca "Good to hear. I'm Constantine Appius, the captain of the city guards. Let me escort you to Lord Annot's manor, he has been waiting for your arrival."

    hide fc base serious
    hide ca talking serious