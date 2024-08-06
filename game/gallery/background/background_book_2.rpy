screen background_book_2():
    tag menu
    add im.Scale("gui/gallery/background/background_open_book_empty.png",1920,1080)
    hbox:
        imagebutton:
            left_margin 0.12
            idle im.Scale("gui/gallery/background/previous_button.png", 200, 108)
            action ShowMenu("background_book")
        imagebutton:
            left_margin 0.72
            idle im.Scale("gui/gallery/background/next_button.png", 200, 108)
            action ShowMenu("gallery")
    hbox:
        xpos 0.15
        ypos 0.1
        vbox:      
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.lord_annot_throne_room_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Lord_Annot_Throne_Room.png', 'background_book_2'):
                        idle im.Scale("Backgrounds/Lord_Annot_Throne_Room.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.lord_annot_dinning_room_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Lord_Annot_Dinning_Room.png', 'background_book_2'):
                        idle im.Scale("Backgrounds/Lord_Annot_Dinning_Room.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.libertis_forest_road_daylight_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Libertis_Forest_Road_Daylight.png', 'background_book_2'):
                        idle im.Scale("Backgrounds/Libertis_Forest_Road_Daylight.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.libertis_village_daylight_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Libertis_Village_Daylight.png', 'background_book_2'):
                        idle im.Scale("Backgrounds/Libertis_Village_Daylight.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
        vbox:
            xpos 0.15
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.libertis_wall_rampart_night_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Libertis_Wall_Rampart_Night.png', 'background_book_2'):
                        idle im.Scale("Backgrounds/Libertis_Wall_Rampart_Night.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.interior_house_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Interior_House.png', 'background_book_2'):
                        idle im.Scale("Backgrounds/Interior_House.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.sandstorm_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Abandoned_Houses.png', 'background_book_2'):
                        idle im.Scale("Backgrounds/Abandoned_Houses.png", 590, 117)
                        xpos 0.042
                        ypos 0.12
            fixed xsize 650 ysize 195:
                add im.Scale("gui/gallery/background/image_frame_locked.png", 650, 195)
                if persistent.sandstorm_scene:
                    imagebutton action ShowMenu('view_background_book', 'Backgrounds/Oase_Smithery.png', 'background_book_2'):
                        idle im.Scale("Backgrounds/Oase_Smithery.png", 590, 117)
                        xpos 0.042
                        ypos 0.12