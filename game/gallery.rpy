## Gallery screen ##############################################################
##
## This is a screen that displays the gallery menu. 
##

screen gallery:
    tag menu
    add "gui/gallery/Gallery_Background.png"
    imagebutton:
        idle "gui/gallery/Return_Button.png"
        action Return()
    hbox:
        yalign 0.4
        imagebutton:
            left_margin 0.08
            idle "gui/gallery/Character/character_Book.png"
            hover "gui/gallery/Character/character_Book_2.png"
            action ShowMenu("character_main")
        imagebutton:
            left_margin 0.07
            idle "gui/gallery/Background/Background_Book.png"
            hover "gui/gallery/Background/Background_Book_2.png"
            action ShowMenu("background_book")
        imagebutton:
            left_margin 0.2
            idle "gui/gallery/Story/Story_Book.png"
            hover "gui/gallery/Story/Story_Book_2.png"
            action ShowMenu("story_book")

screen character_main():
    tag menu
    add "gui/gallery/Character/character_first_page_2.png"
    hbox:
        imagebutton:
            left_margin 0.09
            top_margin 0.02
            idle "gui/gallery/Character/return_button.png"
            action ShowMenu("gallery")
        imagebutton:
            left_margin 0.72
            top_margin 0.055
            idle im.Scale("gui/gallery/Character/next_button.png", 200, 108)
            action ShowMenu("character_book_frederick")