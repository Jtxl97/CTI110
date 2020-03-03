#This program will calculate the area of two rectangles
#based on user input and tell which rectangle has the greater
#area
#3/3/2020
#CTI-1100 P3T1 - Areas of Rectangles
#Jonathan Lopresto

#Input the length and width of rectangle 1
#Input the length and width of rectangle 2
#Calculate the area of rectangle 1
#Calculate the area of rectangle 2
#if area1 > area2
        #Display "The first rectangle has the greatest area."
#else if area2 > area1
        #Display "The second rectangle has the greatest area."
#else
        #Display "Both rectangles have the same area."

#Get the dimensions of rectangle 1
length_1 = int(input('Enter the length of the first rectangle: '))
width_1 = int(input('Enter the width of the first rectangle: '))

#Get the dimensions of rectangle 2
length_2 = int(input('Enter the length of the second rectangle: '))
width_2 = int(input('Enter the width of the second rectangle: '))

#Calculate the areas of the rectangles
area_1 = length_1 * width_1
area_2 = length_2 * width_2

#Display which area is greater using if-elif-else
if area_1 > area_2:
    print('The first rectangle has the greater area.')
elif area_2 > area_1:
    print('The second rectangle has the greater area.')
else:
    print('Both rectangles have the same area.')
