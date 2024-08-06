#Adjust the book element
transform fix_book:
    xpos 0.04
    ypos 0.02

screen character_book_frederick():
    tag menu
    add im.Scale("gui/gallery/Gallery_Dirt_Background_2.png",1920,1080)
    add im.Scale("gui/gallery/Character/character_open_book_empty.png",1840,1039) at fix_book
    hbox:
        ypos 0.05
        imagebutton:
            left_margin 0.12
            idle im.Scale("gui/gallery/Character/previous_button.png", 200, 108)
            action ShowMenu("character_main")
        imagebutton:
            left_margin 0.72
            idle im.Scale("gui/gallery/Character/next_button.png", 200, 108)
            action ShowMenu("gallery")
    
    hbox:
        xpos 0.13
        hbox:
            ypos 0.13
            add im.Scale("gui/gallery/Character/big_image_frame_locked.png", 740, 825)
        hbox:
            ypos 0.17
            xpos 0
            vbox: 
                spacing 65
                if not persistent.frederick_casual_base_happy:
                    add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
                else:
                    imagebutton:
                        idle im.Scale("gui/gallery/Character/character_frames/frederick_marcus/fc_base_happy_frame.png", 225, 203)
                        action ShowMenu("character_frame", character_book = 'character_book_frederick', images = ['Characters/Frederick_Marcus/Casual/FC_Base_Happy_Expression.png', 'Characters/Frederick_Marcus/Armor_FA1/FA1_Base_Happy_Expression.png'], outfits = ['Casual', 'Armor'])
    
                add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
                add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
            vbox:
                spacing 65
                add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
                add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
                add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
            vbox:
                spacing 65
                add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
                add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
                add im.Scale("gui/gallery/Character/image_frame_locked.png", 225, 203)
