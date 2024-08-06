##----------------
## Test Chapter for developer
##----------------

image scene_test = "Backgrounds/Libertis_Village_In_Flames.png"

label test:
    scene scene_test with fade

    $ textboxColor = "Yellow"

    $ textbox = "Dialogue"

    $ show_character("um angry", 0.15, 0, True, lighten, flip)

    $ show_character("fa shouting", 0.85, 0, True, darken)

    um "What's going on, brother? Why are we leaving? We must defend the town, not leave it"

    pause