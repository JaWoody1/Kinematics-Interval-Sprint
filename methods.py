#methods

def changeInTime (time1, time2):
    t = time1 - time2
    return t

def velocity (meters, time):
    v = meters/time
    return v

def timeOfVelcoity (time1, time2):
    t = (time1 + time2)/2
    return t

def changeInVelocity (velocity1, velocity2):
    cV = velocity1 - velocity2
    return cV

def acceleration (changeInVelocity, changeInTime):
    a = changeInVelocity/changeInTime
    return a

def cleanUp (i):
    i = float(i)
    i = round(i, 2)
    return i