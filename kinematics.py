#Take in user data for a user defined amount of interval to calculate: ∆Position, ∆Time, Velocity, Time of Velocity, ∆Velocity, Acceleration, ∆Time of Acceleration

import methods


#How many intervals will the user use and how long each interval is

intervals = input("Please input how many intervals were used: ")
intervalLength = float(input("Please input how long each interval was (meters): "))

#lists

position = [0]
time = [0]
changeInPosition = [0]
changeInTime = [0]
velocity = [0]
timeOfVelocity = [0]
changeInVelocity = [0]
acceleration = [0]


for x in range(int(intervals)):

    #append values the user inputs

    position.append(intervalLength + position[x])
    changeInPosition.append(intervalLength)

    #input each time at each interval
    time.append(float(input(f"Time at interval {x+1}: ")))

#appending each calculation to its own list
for y in range(int(len(position))):

    #first value is already 0
    if y>0:

        #invoking each calculation from methods.py
        changeInTime.append(methods.changeInTime(time[y], time[y-1]))
        velocity.append(methods.velocity(changeInPosition[y], changeInTime[y]))
        timeOfVelocity.append(methods.timeOfVelcoity(time[y], time[y-1]))
        changeInVelocity.append(methods.changeInVelocity(velocity[y], velocity[y-1]))
        acceleration.append(methods.acceleration(changeInVelocity[y], changeInTime[y]))

#cleaning up and rounding number
#just for practicing methods
for z in range(int(len(position))):

    #invokes method clean up to every number in the list
    changeInTime[z] = methods.cleanUp(changeInTime[z])
    velocity[z] = methods.cleanUp(velocity[z])
    timeOfVelocity[z] = methods.cleanUp(timeOfVelocity[z])
    changeInVelocity[z] = methods.cleanUp(changeInVelocity[z])
    acceleration[z] = methods.cleanUp(acceleration[z])



#printing
print(f"Change in Position: {changeInPosition}")
print(f"Change in Time: {changeInTime}")
print(f"Acceleration: {acceleration}")
    





    


    