import colorgram
import turtle as t
import random

#colors = colorgram.extract("hirst_painting.jpg", 40)       # picture file name, no. of pictures
#list_of_colors = []            # Create empty list so i can append r,g,b tuple
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    color_as_tuple = (r, g, b)
#    list_of_colors.append(color_as_tuple)       # append each tuple for every iteration
#print(list_of_colors)            # copy paste the output into a list of colors, comment out the above

list_of_colors = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189),
                  (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16),
                  (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),
                  (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
                  (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40),
                  (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223),
                  (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]

def hirst_painting(number_of_dots):
    t.setheading(225)                    # so that i can fit the painting on the screen
    t.penup()
    t.forward(300)
    t.setheading(0)

    for dot in range(1, number_of_dots + 1):      # from 1 to number of dots
        random_color = random.choice(list_of_colors)
        t.penup()
        t.colormode(255)               # need to change to 255 since using rgb values that are between 0-255
        t.dot(20, random_color)
        t.forward(50)
        t.pendown()
        if dot % 10 == 0:             # multiples of 10, reach the end of the line/row, will change direction
            t.setheading(90)
            t.penup()             # so i won't draw lines connected
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)
        if dot == number_of_dots:
            t.hideturtle()              # so that cursor will disappear at the end 


hirst_painting(number_of_dots=100)
screen = t.Screen()       # Create screen object from turtle module
screen.exitonclick()      # Won't disappear until we click on it