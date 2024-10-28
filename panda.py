from pandas import Series, DataFrame
import pandas as pandas
import numpy as np



#SERIESE

obj = Series([4,2,7,-5,3])
# print(obj)

# obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print(obj2)

# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# OBJ3 = Series(sdata)
# print(OBJ3)

#DATAFRAME
# obj = Series([4,2,7,-5,3])
# dataframe = DataFrame(obj,columns = ['values'],index = [1,2,3,4,5])
# print(dataframe)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
 'year': [2000, 2001, 2002, 2001, 2002],
 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
#OR
frame1 = DataFrame(data, columns=['year', 'state', 'pop'],index=['one', 'two', 'three', 'four', 'five'])
# print(frame)
# print(frame1)

# #           ACCESS COLUMN
# print(frame1['state'])
# print(frame1.year)

# #           ACCESS ROW
# print(frame1.loc['two'])

#       Assign value to a column
# frame1['debt'] = 16.5
# print(frame1)

# pop = {
#     'Nevada': {2001: 2.4, 2002: 2.9},
#     'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
#   }
# frame3 = DataFrame(pop)
# print(frame3.T)

              ###################
              #   indexing      #
              ###################
# obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# print(obj['b'])
# print(obj['b':'e'])
# data = DataFrame(np.arange(16).reshape((4, 4)),
#  index=['Ohio', 'Colorado', 'Utah', 'New York'],
#  columns=['one', 'two', 'three', 'four'])
# frame = DataFrame(data)
# print(frame['one'])
# print(frame[['three','four']])

              ###############################
              #   Arithmatic operation      #
              ###############################

# s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
# s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

# print(s1+s2) 
# ->
'''
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64

'''
#       USE DEFAULT VALUE

# df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
#     index=['Ohio', 'Texas', 'Colorado'])
# df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
#     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

# print(df1+df2)
# print(df1.add(df2, fill_value=0))

              ###########################################
              #   Function application and mapping      #
              ###########################################
# frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
#         index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# print(frame)
# print(np.abs(frame))

# f = lambda x: x.max() - x.min()
# print(frame.apply(f,axis=1))

# format = lambda x: '%.2f' % x
# print(frame.map(format))

              ###########################################
              #         Sorting and Ranking             #
              ###########################################
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
        index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
# print(frame.sort_index(axis=1,ascending=False))
print(frame.sort_values(by=['d', 'b']))