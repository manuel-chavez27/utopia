screen background_book():
    tag menu
    add im.Scale("gui/gallery/background/background_open_book_empty.png",1920,1080)
    hbox:
        imagebutton:
            left_margin 0.12
            idle im.Scale("gui/gallery/background/previous_button.png", 200, 108)
            action ShowMenu("gallery")
        imagebutton:
            left_margin 0.72
            idle im.Scale("gui/gallery/background/next_button.png", 200, 108)
            action ShowMenu("background_book_2")
    hbox:
        xpos 0.15
        ypos 0.1
        vbox:      
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.sandstorm_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Sandstorm_Scene.png', 'background_book'):
                        idle im.Scale("Backgrounds/Sandstorm_Scene.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.room_with_beed_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Room_With_Bed.png', 'background_book'):
                        idle im.Scale("Backgrounds/Room_With_Bed.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.oase_city_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_City.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_City.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.oase_wall_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Front_Gate_Daylight.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_Front_Gate_Daylight.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
        vbox:
            xpos 0.15
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.oase_training_daylight_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Training_Grounds_Daylight.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_Training_Grounds_Daylight.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.oase_market_daylight_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Market_Daylight.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_Market_Daylight.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.abandoned_houses_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Abandoned_Houses.png', 'background_book'):
                        idle im.Scale("Backgrounds/Abandoned_Houses.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.oase_smithery_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Smithery.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_Smithery.png", 590, 117)
                        xpos 0.042
                        ypos 0.12