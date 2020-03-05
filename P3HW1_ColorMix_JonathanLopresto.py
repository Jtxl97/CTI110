#CTI-110
#P3HW1 - Color Mixer
#Jonathan Lopresto
#2/5/2020

#Input first and second primary colors
#if color1 is red and color2 is blue
    #Display "The resulting color is purple"
#else if color1 is red and color2 is yellow
    #Display "The resulting color is orange"
#else if color1 is blue and color1 is yellow
    #Display "The resulting color is green"
#else if color1 is blue and color 2 is red
    #Display "The resulting color is purple"
#else if color1 is yellow and color2 is red
    #Display "The resulting color is orange"
#else if color1 is yellow and color2 is blue
    #Display "The resulting color is green"
#else
    #Display "Entry error"

color1 = input('Enter first primary color: ')
color2 = input('Enter second primary color: ')

if color1 == "red" and color2 == "blue":
    print('The resulting color is purple')
elif color1 == "red" and color2 == "yellow":
    print('The resulting color is orange')

elif color1 == "blue" and color2 == "yellow":
    print('The resulting color is green')
elif color1 == "blue" and color2 == "red":
    print('The resulting color is purple')

elif color1 == "yellow" and color2 == "red":
    print('The resulting color is orange')
elif color1 == "yellow" and color2 == "blue":
    print('The resulting color is green')
else:
    print('Entry error')
