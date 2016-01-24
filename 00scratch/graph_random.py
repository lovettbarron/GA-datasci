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



if __name__ == "__main__":
    random.seed()
    drawBar(plt)