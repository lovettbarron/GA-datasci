from __future__ import division
from collections import Counter, defaultdict
from functools import partial
import math, random, csv
import matplotlib.pyplot as plt
import dateutil.parser as dateparse
import datetime
#
#
# My stuff
#
#

def count_like(rowName,reader):
    return list(Counter(row[rowName] if row[rowName] is not None else None
        for row in reader).items())

# def difference_time(open,close):
    # return datetime.fromTimestam

def mean(x):
    return sum(x)/ len(x)

if __name__ == "__main__":
    random.seed()

    data = []

    with open("data/90_Day_Cases_by_Neighborhood.csv", "rb") as f:
        reader = csv.DictReader(f)
        # Put all closed cases into the data
        data = [row if row["Status"] is not "Open" else None for row in reader]

    difference = [dateparse.parse(x["Closed"])-dateparse.parse(x["Opened"]) for x in data]

    # cleaned = [x if x > 0 else None for x in difference]
    # print [x.total_seconds()//3600 for x in difference]
    # [x[1].days for x in difference]

    category_count = count_like("Category", data)
    number_of_supers = count_like("Supervisor District",data)
    # print number_of_supers
    # crime_count = data
    # print [x[1] for x in data]
    # max_value = max([x[1] for x in data])

    bucket = lambda hour: int(hour // 10 * 10) 
    times_in_hours = [bucket(x.total_seconds()//3600) if bucket(x.total_seconds()//3600) < 90*24 else 0 for x in difference]
    max_time = max(times_in_hours)
    min_time = min(times_in_hours)

    counter = Counter(times_in_hours)

    xs = [x for x in counter.values()]
    ys = range(max_time)

    plt.bar([x for x in counter.keys()],[x for x in counter.values()],1)
    plt.axis([0, len(counter), 0, max([x for x in counter.values()])])
    plt.title("Crimes")
    plt.xlabel("Time taken for a given case")
    plt.ylabel("Total hours")
    plt.show()