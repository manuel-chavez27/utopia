##----------------
## Chapter 1: Frederick Marcus
##----------------

image transition_background = im.Scale("Transition/Background_Transition.png", 1920, 1080)
image transition_line = im.Scale("Transition/Line_Transition.png", 1617, 269)
image transition_cap_number_1 = im.Scale("Transition/Cap_1_Number.png", 510, 198)
image transition_cap_title_1 = im.Scale("Transition/Cap_1_Text.png", 441, 92)

image oase_city = "Backgrounds/Oase_City.png"
image oase_wall = "Backgrounds/Oase_Front_Gate_Daylight.png"
image oase_training_daylight = "Backgrounds/Oase_Training_Grounds_Daylight.png"
image oase_market_daylight = "Backgrounds/Oase_Market_Daylight.png"
image oase_smithery = "Backgrounds/Oase_Smithery.png"
image abandoned_houses = "Backgrounds/Abandoned_Houses.png"
image lord_annot_throne_room = "Backgrounds/Lord_Annot_Throne_Room.png"
image lord_annot_dinning_room = "Backgrounds/Lord_Annot_Dinning_Room.png"
image libertis_forest_road_daylight = "Backgrounds/Libertis_Forest_Road_Daylight.png"
image libertis_village_daylight = "Backgrounds/Libertis_Village_Daylight.png"
image libertis_wall_rampart_night = "Backgrounds/Libertis_Wall_Rampart_Night.png"
image interior_house = "Backgrounds/Interior_House.png"

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


    ##----------------
    ## Oase City Scene
    ##----------------
    scene oase_city with scene_fade
    play music gates_of_oase loop

    $ textbox = "Narration"
    "The winds of the kingdom welcomed travelers from far and wide, coming out from between the heights of the mountains to bless the people with a breath of fresh air. The city stood in its might of shining glory from the middle of the plains between the hills."

    ##----------------
    ## Oase Wall Scene
    ##----------------
    scene oase_wall with scene_fade    

    $ textbox = "Dialogue"
    fm "So, this is it... Oase."
    $ textbox = "Narration"

    "The strapping young knight took careful steps forward with his horse, riding down the steep road of cobblestone. Goats grazed about the pastures without a care in the world, though they would be beckoned back by their shepherds, who saw the foreigner. Frederick could only awkwardly smile and wave as he rode past them."
    "Those unaccustomed to this road were easy to spot because of how they walked—or rode. The gatekeepers could spot them from a mile away, and Frederick was no exception. One of them approached the knight as he would near the gate, holding his spear steady in hand."

    # show fc base happy:
    #     xcenter 0.85
    #     ypos 0
    #     darken 
    # with dissolve

    #$ show_character('fc', 'base happy', xpos=0.85, ypos=0)

    $ show_character("fc base happy", 0.85, 0, True, lighten, flip)

    show cso base serious:
        xcenter 0.15
        ypos 0
        flip
        darken
    with dissolve


    pause

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
    
    
    show fc talking happy:
        xcenter 0.85
        ypos 0
        lighten
    

    fm "I'm Frederick Marcus, son of Volker Marcus. Lord Horace Annot called for my father to come to his manor, and I have come here in his stead. Here's the letter Lord Annot sent. Please look at its contents if you wish to verify."

    show fc base happy:
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
    
    show fc talking happy:
        xcenter 0.85
        ypos 0
        lighten
    
    fm "Got it."

    show fc base happy:
        xcenter 0.85
        ypos 0
        darken

    hide cso base serious with dissolve
    hide fc talking serious with dissolve

    $ textbox = "Narration"
    "After taking the letter from Frederick, the guard approached the iron gates and passed the letter through. It was received by a tall, bald man with dark skin, and a large scar by the neck. The man opened the letter, read it briefly, and then went to look at Fredrick up and down."

    show fc base happy:
        xcenter 0.85
        ypos 0
        darken
    with dissolve

    show tm base happy:
        xcenter 0.15
        ypos 0
        flip
        darken
    with dissolve

    show tm talking happy:
        xcenter 0.15
        ypos 0
        flip
        lighten

    $ textbox = "Dialogue"
    tm "Yeah… looks about right. Open the gates."

    show tm base happy:
        xcenter 0.15
        ypos 0
        flip
        darken

    hide tm base happy with dissolve
    hide fc base happy with dissolve

    $ textbox = "Narration"
    "As Frederick approached, the tall man issuing orders reached out his hand for the knight to shake."

    show tm base happy:
        xcenter 0.15
        ypos 0
        flip
        darken
    with dissolve
    show fc base happy:
        xcenter 0.85
        ypos 0
        darken
    with dissolve

    show tm talking happy:
        xcenter 0.15
        ypos 0
        flip
        lighten

    $ textbox = "Dialogue"
    tm "You sure are the spitting image of your father, boy. How is he doing?"

    show tm base happy:
        xcenter 0.15
        ypos 0
        flip
        darken

    show fc talking happy:
        xcenter 0.85
        ypos 0
        lighten
    
    fm "He is doing quite well, thank you."

    hide tm base happy

    show fc base happy:
        xcenter 0.85
        ypos 0
        darken

    show ca talking happy:
        xcenter 0.15
        ypos 0
        flip
        lighten
    
    ca "Good to hear. I'm Constantine Appius, the captain of the city guards. Let me escort you to Lord Annot's manor, he has been waiting for your arrival."

    show ca base happy:
        xcenter 0.15
        ypos 0
        flip
        darken

    hide fc base happy with dissolve
    hide ca talking happy with dissolve

    ##----------------
    ## Oase Training Daylight Scene
    ##----------------
    scene oase_training_daylight with scene_fade
    $ textbox = "Narration"
    "As soon as they entered the city, the iron gates closed. Constantine guided Fredrick through a sizable clearance for the soldiers to train on, until they reached a large wooden gate."
    "This time, the guards immediately opened the gate, seeing the captain accompany the foreigner."

    ##----------------
    ## Oase Market Daylight Scene
    ##----------------
    scene oase_market_daylight with scene_fade
    "Once inside, they started walking through the city proper. The roads were built out of solid stone, with channels of water flowing freely from side to side, while the houses were made from wood."
    "Upon walking a few minutes, they reached a place where there were merchants surrounding the plaza in their wooden stalls selling different meat, fruit, and beverages."

    show fc base serious:
        xcenter 0.85
        ypos 0
        darken
    with dissolve

    show ca base serious:
        xcenter 0.15
        ypos 0
        flip
        darken
    with dissolve

    show fc talking serious:
        xcenter 0.85
        ypos 0
        lighten
    
    $ textbox = "Dialogue"
    fm "I don't see many people buying… "
    fm "Did the rush hour already pass?"

    show fc base serious:
        xcenter 0.85
        ypos 0
        darken
    
    show ca talking serious:
        xcenter 0.15
        ypos 0
        flip
        lighten

    ca "We have a small community. It doesn't get packed that often."

    show ca base serious:
        xcenter 0.15
        ypos 0
        flip
        darken
    
    show fc talking serious:
        xcenter 0.85
        ypos 0
        lighten
    
    fm "That's surprising, with the size of the city I would have thought there would be a lot of citizens."

    show fc base serious:
        xcenter 0.85
        ypos 0
        darken
    
    show ca talking serious:
        xcenter 0.15
        ypos 0
        flip
        lighten


    ca "There used to be, but times changed… Anyways let's go to the right, from here we will go uphill to Lord Annot's mano-."

    show ca base serious:
        xcenter 0.15
        ypos 0
        flip
        darken

    show cso base serious:
        xcenter 0.05
        ypos 0
        flip
        lighten
    with easeinleft
    
    $ textbox = "Narration"
    "As Constantine was about to finish his sentence, a soldier approached him, speaking to him by the ear so Frederick wouldn't hear."

    hide cso base serious with easeoutleft

    $ textbox = "Dialogue"

    show ca talking serious:
        xcenter 0.15
        ypos 0
        flip
        lighten
    
    ca "Forgive me, Frederick, it seems Lord Annot had to attend an urgent matter, mind waiting for a couple of minutes until he's ready? We can wait for him at his manor."
    
    show ca base serious:
        xcenter 0.15
        ypos 0
        flip
        darken
    
    menu:
        "Agree to wait at the manor.":
            show fc talking happy:
                xcenter 0.85
                ypos 0
                lighten
            
            fm "Sure, I can wait at the manor. That way I can meet Lord Annot as soon as possible."

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken
            
            show ca talking happy:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "Great! Let's continue as we were then."

            show ca base happy:
                xcenter 0.15
                ypos 0
                flip
                darken

            hide fc base happy with dissolve
            hide ca talking happy with dissolve

            $ textbox = "Narration"
            "Following the path, they eventually reached stairs that went up to the manor. As they were going through them, Frederick took a glimpse of the rest of the city. There seemed to be a whole area to the settlement he did not see while traversing it. It was full of houses, but they didn't seem to be in their best state.The area itself was  almost devoid of people, too."

            $ textbox = "Thought"
            fm "(It's weird how few people I've seen. The amount of houses doesn't add up. Something must have happened during the previous war… I shouldn't press the topic)"

            jump flow_chapter_1

        "Ask to explore the city in the meantime":
            show fc talking happy:
                xcenter 0.85
                ypos 0
                lighten

            fm "I see. Well, I'm honestly enjoying the view of the city… If we have time, mind if I explore the parts of the city I haven't seen?"

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken
            
            show ca talking serious:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "Mmm, well, I guess we have some time. I can take you to the farm, people might be a bit busy, so let's try not to get in their way too much."

            show ca base serious:
                xcenter 0.15
                ypos 0
                flip
                darken
            
            show fc talking happy:
                xcenter 0.85
                ypos 0
                lighten

            fm "Oh that's fine. I've seen my good share of farms back in my town, and I'm honestly more interested in a smithery, given you have your own mine here. I bet there will be something to learn even from just watching one of your smith's work."

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken
    
            show ca talking happy:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "You interested in smithing your own weapons? That's rather unusual."

            show ca base happy:
                xcenter 0.15
                ypos 0
                flip
                darken
            
            show fc talking happy:
                xcenter 0.85
                ypos 0
                lighten
            
            fm "Well, you never know when a skill will be useful, that's all."

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken
            
            show ca talking serious:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "Fine, we can go watch for a bit… but err…"

            show ca base serious:
                xcenter 0.15
                ypos 0
                flip
                darken
            
            show fc talking serious:
                xcenter 0.85
                ypos 0
                lighten
            
            fm "Is something the matter?"

            show fc base serious:
                xcenter 0.85
                ypos 0
                darken
            
            show ca talking serious:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "We'll go through areas we've not taken much care of in the last few years, nothing to worry about. Just bear in mind nobody really lives in that area. They are mainly mine workers who pass through on their way to and from work."

            show ca base serious:
                xcenter 0.15
                ypos 0
                flip
                darken
            
            show fc talking serious:
                xcenter 0.85
                ypos 0
                lighten
            
            fm "I see, don't worry, it doesn't bother me."

            show fc base serious:
                xcenter 0.85
                ypos 0
                darken
            
            show ca talking serious:
                xcenter 0.15
                ypos 0
                flip
                lighten

            ca "Yeah… But I don't want you to get the wrong impression here. I assure you, our citizens' houses are taken care of more diligently than these ones."

            show ca base serious:
                xcenter 0.15
                ypos 0
                flip
                darken

            hide fc base serious with dissolve
            hide ca talking serious with dissolve

            ##----------------
            ## Abandoned Houses Scene
            ##----------------
            scene abandoned_houses with scene_fade

            $ textbox = "Narration"
            "Constantine led the way towards the smithery, and sure enough, on the way there, Frederick saw some houses that seemed to have been abandoned for years, webs all over their roofs, dust thick enough you could practically breathe it, and swollen wood from the houses."
            "Frederick couldn't help but wonder what happened, why would they leave all this space to waste, houses vacant instead of housing happy families."

            show ca base serious:
                xcenter 0.15
                ypos 0
                flip
                darken
            with dissolve

            show fc base serious:
                xcenter 0.85
                ypos 0
                darken
            with dissolve
            
            show ca talking serious:
                xcenter 0.15
                ypos 0
                flip
                lighten

            $ textbox = "Dialogue"
            ca "Can't really blame you for being surprised, I did warn you though…"

            show ca base serious:
                xcenter 0.15
                ypos 0
                flip
                darken

            show fc talking serious:
                xcenter 0.85
                ypos 0
                lighten
            
            fm "Can I ask the reason?"

            show fc base serious:
                xcenter 0.85
                ypos 0
                darken
            
            show ca talking serious:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "Well, conflict left more than just this scar behind"

            $ textbox = "Narration"
            "Constantine pointed towards the scar in his face with a serious, almost grieving expression, but quickly put on a smile back."

            show ca talking happy:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            $ textbox = "Dialogue"
            ca "But those times are behind us now, the city has been flourishing these past few years, that's why Lord Annot requested for your father to come, it's time to look towards the future."
            ca "Next time you are here, we hope to see a very different landscape."
            ca "Anyways, let's not delay any longer, the smithery is just around the corner."

            show ca base happy:
                xcenter 0.15
                ypos 0
                flip
                darken

            show fc base happy:
                xcenter 0.85
                ypos 0
                lighten
            
            $ textbox = "Thought"
            fm "(Must have been during the last war… I heard from father it was fierce, but I didn't expect for it to affect a city such as this)"

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken

            hide ca base happy with dissolve
            hide fc base happy with dissolve

            ##----------------
            ## Oase Smithery Scene
            ##----------------
            scene oase_smithery with scene_fade

            $ textbox = "Narration"
            "Frederick chose not to press the topic further and silently followed Constantine towards the smithery."
            "Much as Frederick expected, the smither was quite talented, despite him working mostly alone, with only one assistant still learning the ropes, the old man was incredibly fast on his feet, and his work looked flawless."

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken
            with dissolve

            show ca base happy:
                xcenter 0.15
                ypos 0
                flip
                darken
            with dissolve

            show bj base serious:
                xcenter 0.50
                ypos 0
                flip
                darken
            with dissolve

            show fc talking happy:
                xcenter 0.85
                ypos 0
                lighten

            $ textbox = "Dialogue"
            fm "Just as good as I expected, it's great to see a master working hard at their job."

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken
            
            show ca talking happy:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "Ha… yeah, old man Jude has been going at that fire as far back as my memory goes."

            show ca base happy:
                xcenter 0.15
                ypos 0
                flip
                darken
            
            show bj talking serious:
                xcenter 0.50
                ypos 0
                flip
                lighten
            
            bj "Well, are you buying something Constantine boy?"

            show bj base serious:
                xcenter 0.50
                ypos 0
                flip
                darken

            show ca talking happy:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "Not today, gramps. Maybe another time."

            show ca base happy:
                xcenter 0.15
                ypos 0
                flip
                darken
            
            show bj sad:
                xcenter 0.50
                ypos 0
                flip
                lighten
            
            bj "Tch."
            bj "Then leave, the boy gets easily distracted, he's messed up the work since you arrived."

            show bj base serious:
                xcenter 0.50
                ypos 0
                flip
                darken

            show fc talking happy:
                xcenter 0.85
                ypos 0
                lighten

            fm "Sorry to bother you, thanks for showing us your work sir."

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken

            show bj excited:
                xcenter 0.50
                ypos 0
                flip
                lighten

            bj "Thank me next time when you come to buy, I can tell you now, you won't find better equipment than the one I make here."

            show fc talking happy:
                xcenter 0.85
                ypos 0
                lighten
            
            fm "I'll be sure to keep it in mind. Good day now."

            hide bj excited with dissolve

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken
            
            show ca talking happy:
                xcenter 0.15
                ypos 0
                flip
                lighten
            
            ca "Well then, ready to go to the manor? As you can see, the old man here likes his privacy."
            ca "Plus, Lord Annot should be about ready to receive you."

            show ca base happy:
                xcenter 0.15
                ypos 0
                flip
                darken
            
            show fc talking happy:
                xcenter 0.85
                ypos 0
                lighten
            
            fm "Sure thing, I'm eager to meet him!"

            show fc base happy:
                xcenter 0.85
                ypos 0
                darken

            hide ca base happy with dissolve
            hide fc base happy with dissolve

            ##----------------
            ## Oase City Scene
            ##----------------
            scene oase_city with scene_fade

            $ textbox = "Narration"
            "After that short visit to the smith, Frederick and Constantine went back to the main road, and following the path, they eventually reached stairs that went up to the manor. "

            scene oase_market_daylight with scene_fade

            jump flow_chapter_1



    label flow_chapter_1:
        $ textbox = "Narration"
        "They continued up the stairs until they were just a few more steps away from reaching the entrance of the manor, but before taking those steps he stopped momentarily as he saw a beautiful garden to the side, and a woman tending to it. He stopped to look, just for a moment…"

        show ca base serious:
            xcenter 0.15
            ypos 0
            flip
            darken
        with dissolve

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken
        with dissolve

        show ca talking serious:
            xcenter 0.15
            ypos 0
            flip
            lighten

        $ textbox = "Dialogue"
        ca "What's the hold up? Let's keep going."

        show ca base serious:
            xcenter 0.15
            ypos 0
            flip
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Sorry."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        hide fc talking serious with dissolve
        hide ca base serious with dissolve

        ##----------------
        ## Lord Annot Throne Room Scene
        ##----------------

        scene lord_annot_throne_room with scene_fade

        $ textbox = "Narration"
        "Entering the manor, Fredrick felt inspired by its beauty. Such careful craftsmanship went to the masonry, the windows, the red carpet on where they walked on… This was nothing like his hometown."

        show ca base serious:
            xcenter 0.15
            ypos 0
            flip
            darken
        with dissolve

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken
        with dissolve

        show ca talking serious:
            xcenter 0.15
            ypos 0
            flip
            lighten
        
        $ textbox = "Dialogue"
        ca "Here we are. Are you ready?"

        show ca base serious:
            xcenter 0.15
            ypos 0
            flip
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Yes."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken
        
        hide fc base serious with dissolve
        hide ca base serious with dissolve

        $ textbox = "Narration"
        "The guards opened the door for the throne room, where Lord Horace Annot awaited."

        show ha base serious:
            xcenter 0.50
            ypos 0
            lighten
        with dissolve

        pause

        show ha base serious:
            xcenter 0.15
            ypos 0
            lighten
        with easeinleft

        $ textbox = "Dialogue"
        ha "..."

        show ha base serious:
            xcenter 0.15
            ypos 0
            darken
        
        $ textbox = "Narration"
        "The lord sat on his throne, wearing something of a regal, if comfortable garb."
        "But that complexion… "

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken
        with dissolve

        show fc base serious:
            xcenter 0.85
            ypos 0
            lighten
        
        $ textbox = "Thought"
        fm "(What just happened to him in these last few years?)"

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Lord Horace had grown larger, paler, and his once radiant, flowing hair was now almost completely white, with just some vestiges of his vibrant black hair still remaining in spare strands."
        "His beard on the other hand looked well taken care of, at least, and had neatly trimmed sides, but just like his hair, it was almost completely white.."
        "Constantine approached closer to Lord Annot and kneeled before speaking to him, Fredrick following him."

        show ca base serious:
            xcenter 0.60
            ypos 0
            darken
        with dissolve

        show ca talking serious:
            xcenter 0.60
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ca "This is Frederick Marcus, my Lord. He came today to meet you, in his father's stead."

        show ca base serious:
            xcenter 0.60
            ypos 0
            darken
        
        hide ca base serious with dissolve

        show fc happy talking:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Thank you for receiving me in your manor, Lord Annot. My father couldn't join us today, but he sends his kind regards and best wishes to you."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        
        show ha talking happy:
            xcenter 0.15
            ypos 0
            lighten
        
        ha "Haha, it seems you've grown quite a bit since the last time we saw each other, young man. You really have taken after your father. Tall lads, both of you. You have the same blue eyes and face."
        ha "I guess you are only missing his big mustache, haha!"
        ha "Say, shouldn't you be at least growing some beard of your own already? How old are you?"

        show ha base happy:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Twenty-one, milord."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        
        show ha talking happy:
            xcenter 0.15
            ypos 0
            lighten

        ha "Just a year older than my daughter, huh?"

        show ha talking happy:
            xcenter 0.15
            ypos 0
            darken

        $ textbox = "Narration"
        "The lord broke a cold sweat."

        show ha talking happy:
            xcenter 0.15
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ha "Well, never mind that. How are your father and mother doing?"

        show ha base happy:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "They're doing great, thank you. My father's been training and taking my little brother Ulrick to hunt these days. Though, with so much going on, he's been relying on me to help with negotiations with other cities and settlements, among other things."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Though, Fredrick's father seemed rather nervous about Oase, for some reason…."

        show ha talking happy:
            xcenter 0.15
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ha "I see he's educating his children properly. I am glad to have you here, Frederick."

        show ha base happy:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "Thank you, milord."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten
        
        ha "Now, let's get right to the point of this meeting. I imagine you've heard the word regarding the Empire of Korzah? It seems Emperor Jason Morgan died around five months back, and his son, Diomedes, took power by succession."
        ha "This has caused a lot of turmoil, with Diomedes being quite young still…"
        ha "I imagine he's desperate to earn the respect and loyalty of the people."

        show ha base serious:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Yes, we are aware. Our town has never had any kind of relation to Korzah, so nothing has changed much for us, but I've heard from other places that their relations are no longer what they used to be."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten
        
        ha "That is exactly the problem. He seems to be quite hot-headed, that one."
        ha "I've heard he annihilated an entire city because its lord wouldn't pledge loyalty to him. The rumors regarding… this incident, well, they are quite disturbing."

        show ha thinking:
            xcenter 0.15
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Lord Horace Annot bore a heavy expression, as if in a mix of dread and confusion, or just plain disbelief. Fredrick gulped, unsure what could have come to make a lord behave this way."

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ha "No one knows exactly what happened, but the city vanished."

        show ha base serious:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "Vanished?  Have heard of this, but… is that not an exaggeration? Even if Diomedes decided to attack, just making an entire city cease to exist…"

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        $ textbox = "Narration"
        "The possibility of that happening would be next to none. Even if one gathered an entire country to pick away at the stones, it would not be an effort gone unnoticed or be left to rumor and conjecture…"

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ha "You are too young to know, but this is not the first time these kinds of rumors have surrounded the Morgan family. They are hard to believe indeed, but there can be truth behind it."

        show ha base serious:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "My father said something similar. Is there any truth to it all?"

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten
        
        ha "There very well could be."
        ha "Not only that, but the relations between the Empire of Korzah and the Empire of Ohgar seem to have gotten worse since the succession of the emperor. There's even the talk of war between the two."

        show ha base serious:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "That is one of the reasons my father couldn't make it today. He was to meet with other nobles to form an alliance, as we are all worried about this possibility."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten
        
        ha "As we should. If a war breaks out, my city and the rest, including your own town, would be right in the middle of it… I'll go directly to the point, we need men to defend the city, in case this war does happen."
        ha "We have soldiers of course, but they are hardly good enough. My people are starting to get restless, so I want to join forces with another settlement. Namely, yours."

        show ha thinking:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "Only ours? What about the rest of the settlements?"

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten

        ha "Of course, I could ask any other nearby town for their warriors, but I've known your father for a long time now. He's the best fighter I've seen from the past wars, and I'm aware that he trains his people well. Most importantly, I can trust him. I cannot think of better soldiers to protect my city with."
        ha "If you are all looking to ally yourselves with the rest of them, that is fine with me, so long as your father commands the army."

        show ha base serious:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "As I'm sure you are aware, milord, my father is trusted and respected by the other settlements. It is his intention to ally himself with them all, and I'm confident they would permit him to command the forces."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten

        ha "That is good to hear. Well then, that only leaves our alliance with you left, so please, deliver my intentions to him. I would like an answer soon."

        show ha base serious:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "You will not have to wait, milord. I came here today representing my town's interests, so any decisions I make here can be considered those of my people. I don't need my father's approval."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten
        
        ha "All right then. So, I shall now ask you formally: What do you think of forming an alliance?"

        show ha thinking:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "We are looking to make one too."
        fm "We want iron from your mine to have full equipment for our warriors."
        fm "In return, we can send our finest veterans to train your men, as well as to aid you in battle should the situation require."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten

        ha "I see. Sadly, I can only accommodate for a few sets of equipment right now. As I've already told you, we don't have enough men right now, and that applies to the mine workers too."

        show ha thinking:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "Don't be troubled by that, milord. My father and I were already prepared to help you with mine workers too. We can send our own workers in addition to the trainers, but we ask for complete sets of equipment to all our fighters in exchange."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        $ textbox = "Narration"
        "The equipment was a delicate matter. Even if Libertis was well-versed in the ways of war because of its history, resources at present handicapped their battle capability. It was still just some town with no mine and with little access to materials to craft and maintain war-worthy equipment."

        show ha talking serious:
            xcenter 0.15
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ha "All your soldiers, you say? That's too much. Way too much. Your town alone is what, of 1,500 people? I'll take the workers and trainers, but will only be able to give you a 100 sets of equipment for your dedicated soldiers. I trust there's no objection to this? "

        show ha thinking:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "I'm afraid that won't be enough, milord. We need around 350 sets of equipment for all our combatants, including conscripts, not just our dedicated warriors."
        fm "After all, if your city is attacked, we would be in the frontline protecting it, it is also in your best interest that we are well prepared for an all-out battle."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        $ textbox = "Narration"
        "Horace was slowly scratching his chin while listening to Frederick. After thinking for a moment, he smiled, and gave his answer."

        show ha talking happy:
            xcenter 0.15
            ypos 0
            lighten

        $ textbox = "Dialogue"
        ha "Very well, let's go with that, but be sure to send your best warriors to train my men. In how many days can I expect them to arrive, along with the workers?"

        show ha base happy:
            xcenter 0.15
            ypos 0
            darken

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "I'll leave tomorrow at the first light. You can expect my men in around five days, milord."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        show ha talking happy:
            xcenter 0.15
            ypos 0
            lighten
        
        ha "Sounds good. I'll put the men to work on the equipment as soon as they arrive and send it to your village as it comes out."
        ha "Looking forward to working with you and your father, Frederick."

        show ha base happy:
            xcenter 0.15
            ypos 0
            darken

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "Thank you, Lord Annot. We will not let you down."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        show ha talking happy:
            xcenter 0.15
            ypos 0
            lighten

        ha "I sure hope so, we need to both do our best."
        ha "But enough with this negotiation, what say we have dinner?  I'd like to have you meet my daughter, Emilia."

        show ha base happy:
            xcenter 0.15
            ypos 0
            darken

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "It'll be my pleasure."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        
        hide ha base happy with dissolve
        hide fc base happy with dissolve


        ##----------------
        ## Lord Annot Dinning Room Scene
        ##----------------
        scene lord_annot_dinning_room with scene_fade

        show ed base happy:
            xcenter 0.15
            ypos 0
            lighten
        with dissolve
        
        $ textbox = "Narration"

        "They left the main hall and Constantine Appius guided them to the dining table where there was a young woman sitting. She brushed her hair behind her ear and smiled at them as they entered the room."

        show ha base happy:
            xcenter 0.40
            ypos 0
            lighten
        with dissolve

        show fc base happy:
            xcenter 0.85
            ypos 0
            lighten
        with dissolve

        show ha base happy:
            xcenter 0.40
            ypos 0
            darken
        
        show ed base happy:
            xcenter 0.15
            ypos 0
            darken

        show fc shy:
            xcenter 0.85
            ypos 0
            lighten

        $ textbox = "Dialogue"
        fm "…!"

        show fc shy:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Frederick was at a loss for words. She was stunningly beautiful to his eyes."

        show ed base happy:
            xcenter 0.15
            ypos 0
            lighten
        
        $ textbox = "Dialogue"

        ea "…?"

        show ed base happy:
            xcenter 0.15
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Emilia stood up, a bit confused by Fredrick's reaction, but still approached him in a dignified, confident manner while meeting his eyes directly."
        "As she arrived at Lord Horace's side, she bowed her head to greet Frederick."

        show ed happy talking:
            xcenter 0.15
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ea "It is a pleasure to meet you, kind knight."

        show ed base happy:
            xcenter 0.15
            ypos 0
            darken
        
        show ha happy talking:
            xcenter 0.40
            ypos 0
            lighten
        
        ha "This is my daughter Emilia."

        show ha base happy:
            xcenter 0.40
            ypos 0
            darken

        show fc shy:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "..."

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "O-Oh! Forgive me, milady! The pleasure is mine. I am Frederick Marcus, at your service."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Frederick kneeled down to reach for Emilia's hand, and lifted it to kiss it."
        "Emilia gave what felt like a very genuine smile at the gesture and gave a second bow with her head."
        "After introductions were done, they all sat on the dining table, and Lord Annot's cooks soon brought them fish covered in a red sauce, and to the side some vegetables."
        "Fredrick struggled on deciding where to start eating, but eventually just went for the fish, and…"

        show fc ate hot food:
            xcenter 0.85
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        fm "...!"

        show fc ate hot food:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Frederick went red. Drops began to sweat from his forehead, and he could swear there was a fire brewing in his mouth…"

        show ha talking happy:
            xcenter 0.40
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ha "What do you think of the meal? Delicious, isn't it?"

        show ha base happy:
            xcenter 0.40
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Fredrick gulped." 

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        fm "Y- Yes! It has… a unique flavor, yes."

        show fc ate hot food:
            xcenter 0.85
            ypos 0
            lighten
        
        $ textbox = "Thought"
        fm "(A HEALER! SOMEBODY GET ME A HEALER!!!)"

        show fc ate hot food:
            xcenter 0.85
            ypos 0
            darken

        show ha laughing:
            xcenter 0.40
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ha "HAHAHAHAHA! You are not used to spicy food, are you, boy? We love it around here!"

        show ha base happy:
            xcenter 0.40
            ypos 0
            darken
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Oh no, this much spice is no trouble! I can… I could handle it any day of the week."

        show fc ate hot food:
            xcenter 0.85
            ypos 0
            lighten
        
        $ textbox = "Thought"
        fm "(I could handle it… IF ONLY SOMEONE HAD GIVEN ME A WARNING! THIS STUFF BURNS!)"
        fm "(No, focus! Focus, Frederick. You can't make a bad impression on Emilia and Lord Horace…!)"

        show fc ate hot food:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Frederick steeled himself mid-struggle, trying his best attempt to make his mind a fortress and his expression a solemn one."

        show ed talking happy:
            xcenter 0.15
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ea "Your credibility crumbles with all that sweat in your forehead, Marcus."

        show ed base happy:
            xcenter 0.15
            ypos 0
            darken
        
        show ha talking happy:
            xcenter 0.40
            ypos 0
            lighten
        
        ha "Hahahaha, sorry about that, my bad. Your father had a hard time eating our food too."

        show ha base happy:
            xcenter 0.40
            ypos 0
            darken
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Well, I have been caught… I admit it is quite hot— but I like it! I'll just have to get used to it."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "He hoped."

        show ha talking happy:
            xcenter 0.40
            ypos 0
            lighten

        $ textbox = "Dialogue"
        ha "Oh, alright. Then next time, I won't ask my cook to hold back on the spice."

        show ha base happy:
            xcenter 0.40
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Frederick visibly swallowed out of nervousness and took a drink of wine to numb his tongue from the heat."

        show fc grunting pained:
            xcenter 0.85
            ypos 0
            lighten
        
        $ textbox = "Thought"
        fm "(I am done for.)"

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "He somehow managed to finish his food by taking small bites, followed by a drink of wine as they all kept talking about different topics during the dinner."

        show ed base serious:
            xcenter 0.15
            ypos 0

        show ha talking serious:
            xcenter 0.40
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        ha " I was meaning to ask… What do you think of this city, Frederick?"

        show ha base serious:
            xcenter 0.40
            ypos 0
            darken

        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Oh, ahem."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken
        
        $ textbox = "Narration"
        "Fredrick took another sip of the wine to clear his throat and quench the remaining heat."

        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        fm "Well, when I first arrived, I was quite impressed to be honest. It's an incredibly large city with great walls to protect it, but as I walked its streets, I couldn't help but notice how few people there are for its size."
        fm "I believe that to exploit this city to its full potential it should take in people from outside to work for the city… maybe you should consider taking in people from other villages."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken
        
        show ha talking serious:
            xcenter 0.40
            ypos 0
            lighten
        
        ha "Ah… Your father has told me the same before."

        show ha base serious:
            xcenter 0.40
            ypos 0
            darken
        
        show ed talking serious:
            xcenter 0.15
            ypos 0
            lighten

        ea "And so have I!"
        ea "We should accept people from the outside! We can't have our doors closed to everyone forever, there's lots of people that would benefit our city just by living in it."

        show ed base serious:
            xcenter 0.15
            ypos 0
            darken
        
        show ha talking serious:
            xcenter 0.40
            ypos 0
            lighten
        
        ha "Yes, but we can't take just anyone. There are dangerous people outside the city, people that would betray us once they're inside our walls."

        show ha base serious:
            xcenter 0.40
            ypos 0
            darken
        
        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "Well, I can't deny what you're saying, milord, but with proper security, there would be no danger of just taking in a few people into the city. With talks of war, everyone wants a place to shelter themselves in. If you offer them that, I'm sure a great deal of people would offer their hard work for that protection."

        show fc base serious:
            xcenter 0.85
            ypos 0
            darken

        show ha talking serious:
            xcenter 0.40
            ypos 0
            lighten

        ha "Well, I guess I can keep it in mind… but I think it's getting rather late. Let's call it a day for now, I need to get some rest."
        ha "Captain Appius will lead you to our guest room where you can rest for your trip tomorrow."

        show ha base serious:
            xcenter 0.40
            ypos 0
            darken
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "I thank you for the dinner, milord, have a good night."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        show ed base happy:
            xcenter 0.15
            ypos 0

        show ha talking happy:
            xcenter 0.40
            ypos 0
            lighten

        ha "Same to you, make yourself comfortable."

        show ha base happy:
            xcenter 0.40
            ypos 0
            darken

        show ed talking happy:
            xcenter 0.15
            ypos 0
            lighten
        
        ea "I shall take my leave too, a pleasure meeting you, Frederick Marcus."

        show ed base happy:
            xcenter 0.15
            ypos 0
            darken
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten
        
        fm "The pleasure is all mine, milady. I hope to see you again."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        hide ha base happy with dissolve
        hide ed base happy with dissolve
        hide fc base happy with dissolve

        ##----------------
        ## Oase City Scene
        ##----------------
        scene oase_city with scene_fade

        $ textbox = "Narration"
        "The night passed, and the next day Frederick left the city to return to his hometown of Libertis."
        
        ##----------------
        ## Libertis Forest Road Daylight Scene
        ##----------------
        scene libertis_forest_road_daylight with scene_fade

        "It was not that far from the city, just a few hours for a one-way trip. Soon enough, he returned before noon and saw his father and brother, along with more townsfolk arriving at the same time to the gates, all carrying dead animals."

        ##----------------
        ## Libertis Village Daylight Scene
        ##----------------
        scene libertis_village_daylight with scene_fade

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        with dissolve

        show fc happy talking:
            xcenter 0.85
            ypos 0
            lighten

        $ textbox = "Dialogue"
        fm "Arriving from a hunt, everyone?"

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        $ textbox = "Narration"
        "As soon as Frederick said that, a younger boy in his teens came running towards him, carrying rabbits in both hands."

        show um base serious:
            xcenter 0.15
            ypos 0
            flip
            darken
        with dissolve

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten
        
        $ textbox = "Dialogue"
        fm "Did you finally manage to hunt the rabbits, Ulrick?"

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        
        show um happy:
            xcenter 0.15
            ypos 0
            flip
            lighten
        
        um "You should have seen it, bro! I got them both by shooting through their eyes, they didn't even see it coming! Their important meat wasn't hurt, so I'm sure they'll taste great!"

        show um happy:
            xcenter 0.15
            ypos 0
            flip
            darken

        $ textbox = "Narration"
        "As Ulrick was bragging around, practically jumping in excitement."
        "Frederick got off his horse and chuckled, going to pat his little brother in the head."

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        $ textbox = "Dialogue"
        fm "Good job, but don't get too excited and crush their ears, or your shot will go to waste."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        hide um happy with dissolve
        hide fc base happy with dissolve

        $ textbox = "Narration"
        "Then, Frederick turned up, and his father, a man with a big mustache, approached to hug him."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        with dissolve

        show va base serious:
            xcenter 0.15
            ypos 0
            flip
            darken
        with dissolve

        show va happy:
            xcenter 0.15
            ypos 0
            flip
            lighten

        $ textbox = "Dialogue"
        vm "Welcome back Frederick, things on my end went well. We are going to ally ourselves with the nearby villages, and it was decided that in case a fight does erupt, you and I would both serve as commander and captain of the forces respectively."
        vm "What about you? I trust everything went well with Lord Annot?"

        show va base serious:
            xcenter 0.15
            ypos 0
            flip
            darken

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "Yes, Father, the negotiations were easier than I expected. We broke a deal to form an alliance too, and I made him aware of our alliance with the other settlements too, so your agreement works out perfectly."
        fm "On another topic, I also met his daughter and couldn't believe my eyes…"
        fm "She's way too beautiful! A pity I couldn't speak to her alone… how come you didn't tell me about her before?"

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        show va happy:
            xcenter 0.15
            ypos 0
            flip
            lighten

        vm "Hahaha, the guy would probably cut your hand if you laid a finger on his daughter, so I don't advise going after her. He is one overprotective father, let me tell you that."

        show va talking serious:
            xcenter 0.15
            ypos 0
            flip
        
        vm "Now I hate to break this moment, but we should go inside, the townsfolk are waiting for the food to start cooking the quarry."
        vm "While they cook, tell me about the terms you reached with Lord Annot. I want the weapons and armor to arrive as soon as possible so that the town is at its full potential."

        show va base serious:
            xcenter 0.15
            ypos 0
            flip
            darken

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "Of course."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        hide va base serious with dissolve
        hide fc base happy with dissolve

        $ textbox = "Narration"
        "After Frederick informed his father of the deal, he agreed with the proposal and both went to select the warriors and workers that would be sent off to the City of Oase. Then, they prepared the carriages, food, and horses so they would be able to leave early the next morning."

        ##----------------
        ## Libertis Wall Rampart Night Scene
        ##----------------
        scene libertis_wall_rampart_night with scene_fade

        "By the end of preparations, the sun was already hiding, and the smell of food was getting stronger, so they hurried over to get dinner."

        ##----------------
        ## Libertis Interior House Scene
        ##----------------
        scene interior_house with scene_fade

        show ak base happy:
            xcenter 0.50
            ypos 0
            lighten
        with dissolve

        "Subsequently, Frederick's mother, Anja Klein, a beautiful woman with ivory skin and long, wavy golden hair, served them a bowl of beef stew with vegetables, and both started eating immediately."

        show ak base happy:
            xcenter 0.15
            ypos 0
            lighten
            flip
        with easeinleft

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken
        with dissolve

        show ak talking happy:
            xcenter 0.15
            ypos 0
            flip
        
        $ textbox = "Dialogue"

        ak "I prepared your favorite today Frederick, to celebrate you coming back without any incidents."
            
        show ak base happy:
            xcenter 0.15
            ypos 0
            darken
            flip
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "Thank you, mother, this is amazing, especially after what I had the other day."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        hide ak base happy with dissolve

        show va base serious:
            xcenter 0.15
            ypos 0
            flip
            darken

        show va talking serious:
            xcenter 0.15
            ypos 0
            flip
            lighten

        vm "That crazy old man! He gave you one of those spicy, poisonous meals of his, didn't he?"

        show va base serious:
            xcenter 0.15
            ypos 0
            flip
            darken

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "And he seemed to enjoy every second of it! I felt my stomach screaming during my whole trip because of that."

        show fc frustrated:
            xcenter 0.85
            ypos 0
            
        $ textbox = "Thought"
        fm "(I could still use that healer, to be honest…)"

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        show um base serious:
            xcenter 0.50
            ypos 0
            flip
            darken
        with dissolve
        
        show um talking serious:
            xcenter 0.50
            ypos 0
            flip
            lighten

        $ textbox = "Dialogue"
        um "Why? What did he give you?"

        show um base serious:
            xcenter 0.50
            ypos 0
            flip
            darken

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "Hmmm, a red fish of some kind. I swear, my mouth was burning while eating it."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        hide um base serious with dissolve

        show ak base happy:
            xcenter 0.50
            ypos 0
            flip
            darken
        with dissolve

        show ak talking happy:
            xcenter 0.50
            ypos 0
            flip
            lighten

        ak "You are exaggerating, he's served me that too and it tasted great! You need to be open to eating more types of food, or you'll never get married to a good woman."

        show ak base happy:
            xcenter 0.50
            ypos 0
            flip
            darken

        hide ak base happy with dissolve

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "All right, all right, I'll try."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        $ textbox = "Narration"
        "Then, Volker leaned over to Fredrick for a whisper."

        show va happy:
            xcenter 0.15
            ypos 0
            flip
            lighten

        $ textbox = "Dialogue"
        vm "Hey. If you need a healer, I got one ready…"

        show va base serious:
            xcenter 0.15
            ypos 0
            flip
            darken

        show fc frustrated:
            xcenter 0.85
            ypos 0
            lighten

        fm "Dad… "

        show fc frustrated:
            xcenter 0.85
            ypos 0
            darken

        $ textbox = "Narration"
        "He could almost feel a tear coming down his cheek."

        show fc base happy:
            xcenter 0.85
            ypos 0

        show um base serious:
            xcenter 0.50
            ypos 0
            darken
        with dissolve

        show um questioning:
            xcenter 0.50
            ypos 0
            lighten

        $ textbox = "Dialogue"
        um "Hey Dad, did you send Fredrick to Oase just so you could avoid eating that spicy food?"

        show um questioning:
            xcenter 0.50
            ypos 0
            darken

        hide um questioning with dissolve

        show fc angry:
            xcenter 0.85
            ypos 0

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            lighten

        vm "…!"

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            darken


        $ textbox = "Narration"
        "Volker's face contorted in horror, while Fredrick's wore down to that of a man betrayed by whom he trusted most."

        show fc angry:
            xcenter 0.85
            ypos 0
            lighten

        $ textbox = "Dialogue"
        fm "…"

        show fc angry:
            xcenter 0.85
            ypos 0
            darken

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            lighten

        vm "Hey, uhm… Listen, there's a reasonable explanation for all this. I just wanted you to… erm…"

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            darken

        show fc talking serious:
            xcenter 0.85
            ypos 0
            lighten

        fm "Hey Mom, Dad says he doesn't like vegetables in his stew."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        show va shouting:
            xcenter 0.15
            ypos 0
            flip
            lighten

        vm "Why, you little—!"

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            darken

        show ak angry assassin:
            xcenter 0.50
            ypos 0
            lighten
        with dissolve

        ak "Darling… What was that about vegetables?"

        show ak angry assassin:
            xcenter 0.50
            ypos 0
            darken

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            lighten

        vm "What!? Err, I mean, I LIKE them, but in beef stew…"

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            darken

        show ak angry assassin:
            xcenter 0.50
            ypos 0
            lighten
        
        ak "What about the beef stew?"

        show ak angry assassin:
            xcenter 0.50
            ypos 0
            darken

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            lighten

        vm "Well, I just…"

        show va scared:
            xcenter 0.15
            ypos 0
            flip
            darken

        $ textbox = "Narration"
        "Volker leaned back to Frederick."

        show va shouting:
            xcenter 0.15
            ypos 0
            flip
            lighten

        $ textbox = "Dialogue"
        vm "Brat— Are you trying to kill me?!"

        show va base serious:
            xcenter 0.15
            ypos 0
            flip
            darken
        
        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "You did this to yourself, old man. Sorry."

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        show va scared:
            xcenter 0.15
            ypos 0
            flip

        show ak angry assassin:
            xcenter 0.50
            ypos 0
            lighten

        ak "Get over here, darling. I need to talk to you about your diet. You like meat WAY too much, and that won't be…"

        show ak angry assassin:
            xcenter 0.50
            ypos 0
            darken

        show fc talking happy:
            xcenter 0.85
            ypos 0
            lighten

        fm "Heh…"

        show fc base happy:
            xcenter 0.85
            ypos 0
            darken

        hide va scared with dissolve
        hide ak angry assasin with dissolve
        hide fc base happy with dissolve

        $ textbox = "Narration"
        "And so, Fredrick had his vengeance, much to his and Ulrick's entertainment."
        "After dinner, Frederick spent the rest of the night talking with his younger brother about Oase City and his trips until both went to sleep."
        "The next day was a calm one. The selected people just left for the city, and the rest of the townsfolk continued with their daily lives. Frederick trained with his father and Ulrick. They even had a duel between Frederick and Volker, but ended up going to eat without declaring a victor."

        jump ch2_s00_transition
