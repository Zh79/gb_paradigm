# from scipy.stats.stats import pearsonr
import numpy
import statistics

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 65]

print(numpy.corrcoef(list1, list2)[0, 1])
print(statistics.correlation(__x=list1, __y=list2))
