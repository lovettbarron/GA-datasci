import matplotlib.pyplot as plt
import random, math
from collections import Counter

def drawBar(plt):
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [random.random() for _ in range(len(years))]

    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    plt.title("A graph title")

    # add a label to the y-axis
    plt.ylabel("Random Value")
    plt.show()

def Flip():
	return 1 if random.random() < .5 else 0

def CountFlip(times):
	count = 0
	for _ in range(times):
		count += Flip()
	print "Flipped ", count, " heads of ", times, "flips"

def testExtreme():


def TestManyTimes(tests,flips)
	count = 0
	for _ in range(tests):
		CountFlip(flips)

def read_csv(path):
	with open(path,"rb") as f:
		



if __name__ == "__main__":
    random.seed()
    CountFlip(10000)