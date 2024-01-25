##Take in user data for a user defined amount of interval to calculate: ∆Position, ∆Time, Velocity, Time of Velocity, ∆Velocity, Acceleration, ∆Time of Acceleration

##How many intervals will the user use

intervals = input("Please input how many intervals were used: ")
intervalLength = int(input("Please input how long each interval was (meters): "))

##lists

position = [0]
time = [0]
changeInPosition = [0]

for x in range(int(intervals)):

    #append values the user inputs

    position.append(intervalLength + position[x])
    time.append(int(input(f"Time at interval {x+1}: ")))


    