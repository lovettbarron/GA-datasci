from collections import Counter

def count_unique(x):
	c = Counter(x)
	return dict(c)

if __name__ == "__main__":
	the_list = ['a', 'b', 'a', 'a', 'c', 'c', 'q', 'q']
	print count_unique(the_list)