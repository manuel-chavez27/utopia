##----------------
## Chapter 0: Dream Of The Past
##----------------

image transition_background = im.Scale("Transition/Background_Transition.png", 1920, 1080)
image transition_line = im.Scale("Transition/Line_Transition.png", 1617, 269)
image transition_cap_number_0 = im.Scale("Transition/Cap_0_Number.png", 510, 198)
image transition_cap_title_0 = im.Scale("Transition/Cap_0_Text.png", 441, 92)

image scene_1 = "Backgrounds/Sandstorm_Scene.png"
image scene_2 = "Backgrounds/Room_With_Bed.png"

label ch0:
    play sound "audio/sfx/Intro_Transition.mp3"
    scene transition_background with fade
    show transition_cap_number_0:
        xpos 0.37
        ypos 0.3
    with transition_dissolve
    show transition_line:
        xpos 0.08
        ypos 0.4
    with transition_dissolve
    show transition_cap_title_0 :
        xpos 0.38
        ypos 0.6
    with transition_dissolve
    pause

    #Black Background Scene
    stop sound
    scene black
    play music facing_uncomfort loop
    $ persistent.sandstorm_scene = True

    "Was he always meant to betray us?"
    "Was I always meant to kill him?"

    ##----------------
    ## Sandstorm Scene
    ##----------------
    scene scene_1 with scene_fade

    "I dream of that violent sandstorm closing in, the sight and smell of rotting, dead bodies… my mentor… my friend… the traitor, coming for my life."
    "As he approaches, I see my decision unfold— the price I paid to fulfill my promise… I try to do it differently, I try to reason with him, but to no effect. Everything continued to happen as I recalled it."
    "Just as the battle finishes"

    #Black Background Scene
    scene black with scene_fade

    "I wake up."

    ##----------------
    ## Room with Bed Scene
    ##----------------
    scene scene_2 with scene_fade
    $ textbox = "Narration"

    "As the man woke up, he had ragged breath and sweat drops going down his face, he looked at his trembling hands and turned around to see his wife resting beside him."
    "He took a deep breath and put his hands on his face, wiping the sweat and tears he had."

    window hide

    show hs base:
        xpos 0.3
        ypos 0
    with dissolve

    show ws base:
        xpos 0
        ypos 0
    with dissolve

    $ textbox = "Dialogue"
    ws "Are you okay, darling…? Can't sleep?"

    hs "Sorry, did I wake you?"
    hs "I was just dreaming… no, remembering about the day I became the emperor…"

    ws "Why now? It's been a long time since then. You did everything you could, what you had to do. With that decision, you saved everyone. You reached the dream you shared with your brother… the dream everyone shared."
    ws "Don't let that torment you any longer, and let the past rest."

    hs "I cannot forget it. I don't regret it, I never will. I know it was the right choice, but I mustn't forget."
    hs "Sorry for waking you up, let's go back to sleep."

    hide hs base with dissolve
    hide ws base with dissolve
    stop music fadeout 1.0

    jump ch1