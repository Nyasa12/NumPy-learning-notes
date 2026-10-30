import numpy as np
#Q1.Create a NumPy array containing 10, 20, 30, 40, 50.
'''
array = np.array([10,20,30,40,50 ])
print(array)
'''
#Q2.Create an array of numbers from 1 to 20 using NumPy.
'''
array1 = np.arange(1, 21)
print(array1)
'''
#Q3.Create a 1D array with 6 elements and print its shape.
'''
array2 = np.array([1,3,5,7,9,11 ])
print(array2.shape)
'''
#Q4.Create an array [5, 10, 15, 20, 25] and print the third element.
'''
array3 = np.array([5,10,15,20,25 ])
print(array3[2])
'''
#Q5.From the array [10, 20, 30, 40, 50, 60], print the last three elements.
'''
array4 = np.array([10, 20, 30, 40, 50, 60 ])
print(array4[-3:])
'''
#Q6.Create two arrays [1, 2, 3] and [4, 5, 6]. Add them element by element.
'''
array5 = np.array([1,2,3 ])
array6 = np.array([4,5,6 ])
print(array5 + array6)
'''
#Q7.Create an array [2, 4, 6, 8] and multiply every element by 3.
'''
array7 = np.array([2,4,6,8 ])
print(array7* 3)
'''
#Q8.Create an array [10, 20, 30, 40, 50]. Print its sum and mean.
'''
array8 = np.array([10, 20, 30, 40, 50 ])
sum = np.sum(array8)
mean = np.mean(array8)
print(sum)
print(mean)
'''
#Q9.Create a 2D array with 3 rows and 2 columns. Print its shape.
'''
array9 = np.array([[1,2 ],
                   [3,4 ],
                   [5,6 ]])
print(array9.shape)
'''
#Q10.Given array [12, 5, 18, 7, 20, 3], print only the elements greater than 10.
'''
array10 = np.array([12, 5, 18, 7, 20, 3])

elements = array10[array10> 10]
print(elements)
'''
#11 Get 5 evenly spaced numbers from 0 to 1, both ends included.
'''
print(np.linspace(0, 1 ,5))
'''
#12 m = np.arange(1, 10).reshape(3, 3). Get the middle column and the bottom-right 2x2 block.
'''
m = np.arange(1, 10).reshape(3, 3)
print(m[:, 1])
print(m[1:, 1:])
'''
#13 Turn np.arange(12) into 3x4, then into 2 rows without typing the column count.
'''
print(np.arange(12).reshape(3,4))
print(np.arange(12).reshape(2,-1))
'''
#14 a = [1,2,3], b = [4,5,6] as arrays. Build [[1,2,3],[4,5,6]] and also [[1,4],[2,5],[3,6]].



#15 Does np.ones((3, 2)) + np.array([1, 2, 3]) work? If not, fix it so each row gets 1, 2, 3.
'''
num = np.ones((3, 2)) + np.array([1, 2, 3]).reshape(3,1)
print(num)
'''
