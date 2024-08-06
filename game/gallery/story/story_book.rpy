screen story_book:
    tag menu
    add im.Scale("gui/gallery/Story/story_open_book_empty.png",1920,1080)
    hbox:
        ypos 0.03
        xpos 0.02
        imagebutton:
            left_margin 0.125
            idle im.Scale("gui/gallery/Story/previous_button.png",200,110)
            action ShowMenu("gallery")
        imagebutton:
            left_margin 0.70
            idle im.Scale("gui/gallery/Story/next_button.png",200,110)
            action ShowMenu("gallery")
    
    hbox:
        xpos 0.17
        ypos 0.13
        vbox:      
            fixed xsize 600 ysize 180:
                add im.Scale("gui/gallery/Story/image_frame_locked.png", 600, 180)
                if persistent.sandstorm_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Sandstorm_Scene.png', 'background_book'):
                        idle im.Scale("Backgrounds/Sandstorm_Scene.png", 507, 100)
                        xpos 0.066
                        ypos 0.125
            fixed xsize 600 ysize 180:
                add im.Scale("gui/gallery/Story/image_frame_locked.png", 600, 180)
                if persistent.room_with_beed_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Room_With_Bed.png', 'background_book'):
                        idle im.Scale("Backgrounds/Room_With_Bed.png", 507, 100)
                        xpos 0.066
                        ypos 0.125
            fixed xsize 600 ysize 180:
                add im.Scale("gui/gallery/Story/image_frame_locked.png", 600, 180)
                if persistent.oase_city_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_City.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_City.png", 507, 100)
                        xpos 0.066
                        ypos 0.125
            fixed xsize 600 ysize 180:
                add im.Scale("gui/gallery/Story/image_frame_locked.png", 600, 180)
                if persistent.oase_wall_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Front_Gate_Daylight.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_Front_Gate_Daylight.png", 507, 100)
                        xpos 0.066
                        ypos 0.125
        vbox:
            xpos 0.2
            fixed xsize 600 ysize 180:
                add im.Scale("gui/gallery/Story/image_frame_locked.png", 600, 180)
                if persistent.oase_training_daylight_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Training_Grounds_Daylight.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_Training_Grounds_Daylight.png", 507, 100)
                        xpos 0.066
                        ypos 0.125
            fixed xsize 600 ysize 180:
                add im.Scale("gui/gallery/Story/image_frame_locked.png", 600, 180)
                if persistent.oase_market_daylight_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Market_Daylight.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_Market_Daylight.png", 507, 100)
                        xpos 0.066
                        ypos 0.125
            fixed xsize 600 ysize 180:
                add im.Scale("gui/gallery/Story/image_frame_locked.png", 600, 180)
                if persistent.abandoned_houses_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Abandoned_Houses.png', 'background_book'):
                        idle im.Scale("Backgrounds/Abandoned_Houses.png", 507, 100)
                        xpos 0.066
                        ypos 0.125
            fixed xsize 600 ysize 180:
                add im.Scale("gui/gallery/Story/image_frame_locked.png", 600, 180)
                if persistent.oase_smithery_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Smithery.png', 'background_book'):
                        idle im.Scale("Backgrounds/Oase_Smithery.png", 507, 100)
                        xpos 0.066
                        ypos 0.125