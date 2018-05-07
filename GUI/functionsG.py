import motion_control_scriptG

index = 0
x = None
y = None
z = None
wait = None


def input(text):
    global index
    if(index == 0):
        output = "x-coordinate: "+text+"!"
        global x
        x = text
        index = index+1
        return output
    elif(index == 1):
        output = "y-coordinate: " + text +"!"
        global y
        y = text
        index = index + 1
        return output
    elif (index == 2):
        output = "z-coordinate: " + text + "!"
        global z
        z = text
        index = index + 1
        return output
    elif (index == 3):
        output = "time to wait: " + text + " sec!\n print script"
        global wait
        wait = text
        motion_control_scriptG.saveCoordinates(x,y,z,wait)
        motion_control_scriptG.saveCoordinates(x,y,z,wait)
        motion_control_scriptG.printScript1(x,y,z,wait)
        index = 0
        return output