init python:
    def show_character(image, xcenter, ypos, use_dissolve=False, transform1=None, flip=None):

        base_transform = Transform(xcenter=xcenter, ypos=ypos)
        
        transforms = [base_transform]

        if transform1:
            transforms.append(transform1)

        if flip:
            transforms.append(flip)

        # Show the image with the desired transforms and position
        renpy.show(image, at_list=transforms)

        if use_dissolve:
            renpy.with_statement(dissolve)
