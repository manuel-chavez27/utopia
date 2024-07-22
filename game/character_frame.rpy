$ outfits = ["Casual", "Armor"]
$ outfits_length = array_length(outfits)

screen character_frame(character, character_book):
    #add im.Scale("gui/gallery/Gallery_Dirt_Background.png", 1920,1080)
    #add im.Scale("gui/gallery/Gallery_Dirt_Background_2.png", 1920,1080)
    #add im.Scale("gui/gallery/Background_Green.png", 1920,1080)
    #add im.Scale("gui/gallery/Background_Yellow.png", 1920,1080)
    add im.Scale("gui/gallery/Background_Cyan.png", 1920,1080)
    #add im.Scale("gui/gallery/Background_Red.png", 1920,1080)

    tag menu
    vbox:
        xsize 1920
        hbox:
            xalign 0.5
            textbutton "Change Outfit" yoffset 200:
                action ToggleScreen("menu_option")
            spacing 500
            add im.Scale(character,599,950)
            
        imagebutton:
            xalign 0.5
            idle im.Scale("gui/main_menu/Assets/Return.png",212,100)
            hover im.Scale("gui/main_menu/Assets/Return_2.png",212,100)
            action ShowMenu(character_book)

screen menu_option():
    $ outfits = ["Casual", "Armor"]
    for i, outfit in enumerate(outfits):
        textbutton "[outfit]" yoffset (250+(50*i)):
            xalign 0.2
            action Return()