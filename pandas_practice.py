import pandas as pd 
import numpy as np

print("pandas version is :", pd.__version__)
print("Numpy version is : ",np.__version__)
print("\n")

#convertin a list into padas series (series is a data type in pandas)

my_list = [  6, 7, 9, 3.23, 4.23]
my_series = pd.Series(my_list)

print(my_series)
print("\n")

#convertin a dictionary to pandas series
dict_a = {"Paris" : 234222, "France" : 432345, "India" : 14034583, "UK" : 323432, "Europe" : 232343}
dict_series = pd.Series(dict_a)
print(dict_series)
print("\n")

#creatin series from numpy list 
numpy_list = np.array([1, 2, 4, 3])
numpy_pandas_series = pd.Series(numpy_list)
print(numpy_pandas_series)
print("\n")

#from scalar, assinging same value for all the variable it's usefull
grade = "B"
index_position = ["Ravi", "Tukku", "Gnanu", "Anil", "Vamshi"]
scalar_series = pd.Series(grade, index=index_position)
print(scalar_series)
print("\n")

#NaN type data, for missing data values we add NaN type
score = [143, 342, 543, 321, 345, np.nan]
player_name = ["Ravi", "Tukku", "Gnanu", "Anil", "Vamshi", "kiran"]
nan_series = pd.Series(score, index=player_name)
print(nan_series)
print("\n")

# filter the data using boolean 
mask = nan_series > 300 
print(nan_series[mask])
print("\n")

#re indexing 
chars = ["a", "b", 'C', 'd', 'e']
nums = [1, 2, 3, 4, 5]
nums_series = pd.Series(nums, index=chars)
re_chars = ["w", 'x', 'y', 'z', 't']
new_Series = nums_series.reindex(re_chars)
print(new_Series)
print("\n")


# resetting the index 
reset_seris = new_Series.reset_index()
print(reset_seris)

# slicing the series to get a portion, it like a list slicing 
a = [22, 34, 43, 53, 63, 73, 83]
b = pd.Series(a)
print(b)

#to get first three 
c = b[:3]
#to get last three 
d = b[-3 : ]

print(c)
print(d)