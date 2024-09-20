# import colorgram

# rgb_colors = []
# colors = colorgram.extract(r'C:\Users\aanand2\Downloads\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
    
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tom = turtle_module.Turtle()

color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]

tom.speed('fastest')
tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots+1):

    tom.dot(20, random.choice(color_list))
    tom.forward(50)
    

    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()

    