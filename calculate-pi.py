import random  #imports random library

points = 100  #number of points  (the more points the more acurate)

circlePoint = 0  #resets points
totalPoints = 0  #resets points
for i in range(points):  #loops for each point
    xPos = random.uniform(0,1)  #random x position
    yPos = random.uniform(0,1)  #random y position
    distance = xPos**2 + yPos**2  #finds the distance of the point from 0,0 point
    if distance <= 1:  #checks if the distance is inside a 1/4 circle (distance is less than one from 0,0 point)
        circlePoint += 1  #adds a point as inside circle
    totalPoints += 1  #adds a total point

pi = 4*circlePoint/totalPoints  #calculates pi by checking how many dots are inside the circle compared to the total and multiplying that with 4 to make a whole circle  
print(pi)  #prints the pi output to the console
