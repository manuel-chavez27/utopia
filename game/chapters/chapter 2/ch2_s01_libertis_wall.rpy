##----------------
##  Chapter 2: The War Arrives
##  Scene 01: Libertis Wall
##----------------

# TODO: Add sfx effects
label ch2_s01_libertis_wall:
    scene libertis_wall_rampart_night with scene_fade
    play music gates_of_oase loop

    $ textbox = "Narration"
    "The silent cold struck unseen. Even with little, snowless wind, the chill was still there, taking its hold on the land as mightily as it could before the sun could vanquish it."
    "Prelude to winter, these nights struck with a cold serenity, as if forewarning the times to come. The fireplace gave succor with its warmth for those stuck in guard duty, at least, but it was no replacement for that which was truly missing..."

    $ show_character("cls base serious", 0.15, 0, True, darken, flip=flip)
    $ show_character("cls talking serious", 0.15, 0, True, lighten, flip=flip)
    $ textbox = "Dialogue"
    cls "*sigh* I hope my brother does not take too long, over there in the city..."
    $ show_character("cls base serious", 0.15, 0, True, darken, flip=flip)
    
    $ textbox = "Narration"
    "Just a few days had passed since the workers and the veterans left for Oase, but their absence was already noticeable. Those greatly loved are easy to take for granted, until they are gone."

    $ show_character("cls base serious", 0.15, 0, True, lighten, flip=flip)
    $ textbox = "Dialogue"
    cls "...?"
    $ show_character("cls base serious", 0.15, 0, True, darken, flip=flip)
    
    $ textbox = "Narration"
    "Someone with heavy footsteps approached the guard."

    $ show_character("fa1 base happy", 0.85, 0, True, darken)
    $ show_character("fa1 talking happy v2", 0.85, 0, True, lighten)
    $ textbox = "Dialogue"
    fm "So, you drew the short straw for guard duty tonight too, huh?"
    $ show_character("fa1 base happy", 0.85, 0, True, darken)

    $ show_character("cls talking serious", 0.15, 0, True, lighten, flip=flip)
    $ textbox = "Dialogue"
    cls "No, actually. It would normally be John's shift, but I am covering for him since he is away for now."
    $ show_character("cls base serious", 0.15, 0, True, darken, flip=flip)

    $ show_character("fa1 talking serious", 0.85, 0, True, lighten)
    $ textbox = "Dialogue"
    fm "Oh, sorry to hear that."
    $ show_character("fa1 serious", 0.85, 0, True, darken)

    $ textbox = "Narration"
    "Frederick took a seat by the fire, finally getting the chance to bask in its light and warmth."

    $ show_character("cls talking serious", 0.15, 0, True, lighten, flip=flip)
    $ textbox = "Dialogue"
    cls "So, how did it go with Oase? Are there going to be sending in gear soon?"
    $ show_character("cls base serious", 0.15, 0, True, darken, flip=flip)

    $ show_character("fa1 talking happy v2", 0.85, 0, True, lighten)
    $ textbox = "Dialogue"
    fm "That's the plan. We got word from them a little while ago that they should be sending a carriage with it in some forty days."
    $ show_character("fa1 base happy", 0.85, 0, True, darken)

    $ show_character("cls talking serious", 0.15, 0, True, lighten, flip=flip)
    $ textbox = "Dialogue"
    cls "Glad to hear it. This old thing is already starting to show its age."
    $ show_character("cls base serious", 0.15, 0, True, darken, flip=flip)

    $ textbox = "Narration"
    "The guard smacked the shaft of his spear a couple times, making out the sounds of old, brittle wood."
    "Then, the wind blew mightily, ensnaring all those outside the refuge of a warm home. It was a penetrating cold, making even the fires tremble with temptation to die."

    $ show_character("cls talking serious", 0.15, 0, True, lighten, flip=flip)
    $ textbox = "Dialogue"
    cls "Yikes! What a chill! I don't remember ever trembling this much. We might need to make a bigger fire to survive the night."
    $ show_character("cls base serious", 0.15, 0, True, darken, flip=flip)

    $ show_character("fa1 talking happy v2", 0.85, 0, True, lighten)
    $ textbox = "Dialogue"
    fm "Might not be a bad id-"
    $ show_character("fa1 base happy", 0.85, 0, True, darken)

    # TODO: Add OST Terrors of War
    $ textbox = "Narration"
    "An explosion!"

    $ show_character("fa1 shouting", 0.85, 0, True, lighten)
    $ textbox = "Dialogue"
    fm "What was that?!"
    $ show_character("fa1 scared", 0.85, 0, True, darken)
    $ show_character("cls scared", 0.15, 0, True, darken)

    $ textbox = "Narration"
    "And now, a war horn."
    "Frederick and the guard turned around, seeing a growing blaze by the other gate, and started to hear the sounds of screams and swords clashing."

    $ show_character("fa1 scared", 0.85, 0, True, lighten)
    $ textbox = "Dialogue"
    fm "...!"
    $ show_character("fa1 scared", 0.85, 0, True, darken)

    $ textbox = "Narration"
    "Along with them, there were the distinct screams of women and children, too."
    "Frederick immediately took a horn he had on his waist and blew through it, alarming everyone in the village who might not have heard the first one."

    $ show_character("fa1 shouting", 0.85, 0, True, lighten)
    $ textbox = "Dialogue"
    fm "Open the gate! I'll go organize the evacuation for the townsfolk!"
    #   TODO: Change scared expression to worried expression
    $ show_character("fa1 scared", 0.85, 0, True, lighten)
    $ textbox = "Thought"
    fm "(How in the world did they get inside so fast?! The guards should have blown the horn as soon as they saw the enemy approaching!)"
    $ show_character("fa1 scared", 0.85, 0, True, darken)

    $ show_character("cls scared", 0.15, 0, True, lighten, flip=flip)
    $ textbox = "Dialogue"
    cls "Shouldn't we go help instead?"
    $ show_character("cls scared", 0.15, 0, True, darken, flip=flip)

    $ show_character("fa1 shouting", 0.85, 0, True, lighten)
    $ textbox = "Dialogue"
    fm "My father is likely to head straight to the other gate, he can hold them off. What's important is to keep those unable to fight safe!"
    $ show_character("fa1 scared", 0.85, 0, True, darken)