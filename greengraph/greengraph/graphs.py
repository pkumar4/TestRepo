from graph import Greengraph
def greengraph(fromLocation, toLocation, steps):
    greenGraphObject = Greengraph(arguments.fromLocation,arguments.toLocation)
    #print(greenGraphObject.geolocate(arguments.fromLocation))
    #print(arguments.fromLocation)
    #greenGraphObject = Greengraph(arguments)
    data = greenGraphObject.green_between(arguments.steps)
    return data