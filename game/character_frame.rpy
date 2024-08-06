#$ outfits = ["Casual", "Armor"]
#$ outfits_length = array_length(outfits) 

screen character_frame(character_book, images, outfits):
    #add im.Scale("gui/gallery/Background_Green.png", 1920,1080)
    add im.Scale("gui/gallery/Background_Yellow.png", 1920,1080)
    #add im.Scale("gui/gallery/Background_Cyan.png", 1920,1080)
    #add im.Scale("gui/gallery/Background_Red.png", 1920,1080

    tag menu
    vbox:
        xsize 1920
        hbox:
            xalign 0.1
            textbutton "Change Outfit" yoffset 200:
                action ToggleScreen("menu_option", outfits = outfits)
            spacing 400
            add im.Scale(images[current],599,950)
            
        imagebutton:
            xalign 0.5
            idle im.Scale("gui/main_menu/Assets/Return.png",212,100)
            hover im.Scale("gui/main_menu/Assets/Return_2.png",212,100)
            action Function(returnMenu, book = character_book)

screen menu_option(outfits):
    for i, outfit in enumerate(outfits):
        textbutton "[outfit]" yoffset (250+(50*i)):
            xalign 0.1
            action SetVariable("current", i)
            #action ()

init python:
    def returnMenu(book):
        renpy.hide_screen('menu_option')
        renpy.show_screen(book)