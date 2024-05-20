# The script of the game goes in this file.
# The game starts here.

#Animations
define transition_dissolve = Dissolve(1)
define scene_fade = Fade(1, 1, 1, color="000")

#Music
define audio.facing_uncomfort = "audio/music/Facing_Uncomfort.mp3"
define audio.gates_of_oase = "audio/music/Gates_Of_Oase.mp3"

#Utils
define yellowTextbox = False
define redTextbox = False
define greenTextbox = False

define gui.name_xpos = 65
define gui.name_ypos = 10
define gui.name_text_size = 24

define gui.dialogue_xpos = 30

style textbox:
    spacing 100

#Characters
define ms = Character("Man", window_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), color="#FFF")
image ms_base = im.Scale("Silhouette/Unknown_Man_Silhouette.png", 1390, 2205)

define ws = Character("Woman", window_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), color="#FFF")
image ws_base = im.Scale("Silhouette/Unknown_Woman_Silhouette.png", 1390, 2205)

#Frederick Marcus
define f = Character("Frederick Marcus", window_background=Frame("gui/textbox/Dialogue_Yellow_Box.png"), color="#FFF")
image fc serious = im.Scale("Characters/Frederick_Marcus/FC_Base_Expression_Happy.png", 1390, 2203)
image fc serious talking = im.Scale("Characters/Frederick_Marcus/FC_Talking_Happy_Expression.png", 1390, 2203)

label start:

    #Transition Background Chapter 0
    jump ch0

    # This ends the game.

    return
