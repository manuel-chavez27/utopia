screen view_background_book(background, book):
    tag menu
    add im.Scale(background, 1920,1080)
    imagebutton:
            xalign 0.5
            yalign 0.9
            idle im.Scale("gui/main_menu/Assets/Return.png",212,100)
            hover im.Scale("gui/main_menu/Assets/Return_2.png",212,100)
            action ShowMenu(book)