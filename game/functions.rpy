init python:
    def show_character(image, xcenter, ypos, use_dissolve=False, transform1=None, transform2=None):

        base_transform = Transform(xcenter=xcenter, ypos=ypos)

        transforms = [base_transform]

        #Transform 1 checks for lighten or darken
        if transform1:
            transforms.append(transform1)
        
        #Transform 2 checks for flip
        if transform2:
            transforms.append(transform2)

        renpy.show(image, at_list=transforms)

        if use_dissolve:
            renpy.with_statement(dissolve)