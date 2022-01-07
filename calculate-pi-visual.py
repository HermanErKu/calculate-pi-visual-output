import random  #imports random library
import pygame  #imports pygame library

pointsAsk = input("How many points...  ")  #number of points  (the more points the more acurate)
points = int(pointsAsk)  #turns the points to an integer

screen = pygame.display.set_mode((500, 500))  #creates 500x500px window
pygame.display.set_caption('Visual Dots')  #titles the window "visual dots"
screen.fill((234,212,252)) #creates background color for the window
pygame.init()  #initiates pygame (for text)

circlePoint = 0  #resets points
totalPoints = 0  #resets points
for i in range(points):  #loops for each point
    xPos = random.uniform(0,1)  #random x position
    yPos = random.uniform(0,1)  #random y position
    xPosPoint = xPos * 500  #multiplies by 500 so we can display on the 500x500px window
    yPosPoint = yPos * 500  #multiplies by 500 so we can display on the 500x500px window
    distance = xPos**2 + yPos**2  #finds the distance of the point from 0,0 point
    if distance <= 1:  #checks if the distance is inside the 1/4 circle (distance is less than one from 0,0 point)
        circlePoint += 1  #adds a point as inside circle
        pygame.draw.line(screen, (255, 0, 0), (xPosPoint, yPosPoint), (xPosPoint, yPosPoint))  #draws the point as red
        pygame.display.flip()  #updates the 500x500px window
        totalPoints += 1  #adds a total point
    elif distance >= 1:  #if the distance is outside of the 1/4 circle (distance is more than one from 0,0 point)
        totalPoints += 1  #adds a total point
        pygame.draw.line(screen, (0, 0, 255), (xPosPoint, yPosPoint), (xPosPoint, yPosPoint))  #draws the point as red
        pygame.display.flip()  #updates the 500x500px window

pi = 4*circlePoint/totalPoints  #calculates pi by checking how many dots are inside the circle compared to the total and multiplying that with 4 to make a whole circle

pygame.draw.circle(screen, (0,0,0), (0,0), 500, 1)  #draws 1/4 circle to see the separation of the dots
myfont = pygame.font.SysFont('Comic Sans MS', 23)  #gets a font
points = myfont.render('Placed  '+str(points)+'  dots', True, (0, 0, 0))  #writes how many dots it places
screen.blit(points,(0,0))  #places the text
pi = myfont.render('Pi is:  '+str(pi), True, (0, 0, 0))  #writes the pi output
screen.blit(pi,(0,25))  #places the text
pygame.display.update()  #updates the window to show the text

print(pi)  #prints the pi output to the console

running = True  #is the pygame 500x500px window running
while running:  #if running is true and the window is running
    for event in pygame.event.get():  #checks for events
        if event.type == pygame.QUIT:  #if you quit the window
            running = False  #running is false
