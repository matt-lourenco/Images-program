# Created by: Matthew Lourenco
# Created on: 19 Sept 2016
# This program is a program that shows two images

import ui

my_pic = ui.Image.named('./sprite/MT_crest.jpg')
my_image = ui.ImageView(frame=(250,150,200,300))
my_image.image = my_pic

view = ui.load_view()
view.add_subview(my_image)
view.present('full_screen')
