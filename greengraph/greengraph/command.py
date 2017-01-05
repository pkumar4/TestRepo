from argparse import ArgumentParser
from graph import Greengraph
from matplotlib import pyplot as plt

#%matplotlib qt

def process():
	#get_ipython().magic('matplotlib inline')
	parser = ArgumentParser(description = "Generate appropriate green counts")
	#parser.add_argument('--title', '-t')
	#parser.add_argument('--polite', '-p', action="store_true")
	parser.add_argument('fromLocation')
	parser.add_argument('toLocation')
	parser.add_argument('steps')

	arguments= parser.parse_args()
	print(arguments.fromLocation)
	greenGraphObject = Greengraph(arguments.fromLocation,arguments.toLocation)
	#print(greenGraphObject.geolocate(arguments.fromLocation))
	#print(arguments.fromLocation)
	#greenGraphObject = Greengraph(arguments)
	data = greenGraphObject.green_between(arguments.steps)
	print(data)
	#print(Greengraph(arguments.fromLocation,arguments.toLocation))
	plt.show(data)

if __name__ == "__main__":
	process()



