# Created by: Kay Lin
# Created on: Sep 25th 2017
# Created for: ICS3U
# This program calculates the circumference of a circle,
#   when you give it the radius

import ui

def calculate_touch_up_inside(sender):
    # calculate circumference
    
    # constants
    PI = 3.14
    
    # input
    radius = int(view['radius_textbox'].text)
    
    # process
    circumference = 2 * PI * radius
    
    # output
    view['answer_label'].text = 'The circumference is: ' + str(circumference) + ' cm'

view = ui.load_view()
view.present('full_screen')
