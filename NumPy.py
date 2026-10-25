import numpy as np

#1 Multidimesional Arrays
'''
list = [1,2,3]

array = np.array(list)

print(array)

print(type(array))
'''

#1d array
'''
array1 = np.array([1,2,3,4])

print(array1[2])
'''

#2d array
'''
array3 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(array3)
'''

#3d array
'''
array4 = np.array([[['A' , 'B' , 'C'], ['D' , 'E' , 'F'],['G' , 'H' , 'I']],
                  [['J' , 'K' , 'L'], ['M' , 'N' , 'O'],['P' , 'Q' , 'R']],
                  [['S' , 'T' , 'U'], ['V' , 'W' , 'X'],['Y' , 'Z' , 'N']]])

print(array4)
print(array4[0][1][2])
#or
print(array4[0,1,2])

word = array4[1,1,1] + array4[2,2,0] + array4[0,0,0] + array4[2,0,0] + array4[0,0,0]

print(word)
'''

#2 Slicing And Indexing
'''
array5 = np.array([[2,3,4,5], 
                  [3,4,5,6], 
                  [4,5,6,7], 
                  [5,6,7,8]])
'''

#indexing
'''
print(array5[0])
print(array5[1])
print(array5[2])
print(array5[3])
print()
print(array5[-1])
print(array5[-2])
print(array5[-3])
print(array5[-4])
'''

#slicing
'''
print(array5[0:2])
print(array5[:])
print(array5[2:4])
print(array5[-3:-1])
print(array5[1:3, 1:3])
'''

#step slicing
'''
print(array5[0:4:2])
print(array5[::-2])
print(array5[0:4:2, 0:4:2])
'''

#3 Scalar arithmetic

'''
array6 = np.array([1,2,3 ])
print(array6 + 2)
print(array6 - 1)
print(array6 * 3)
print(array6 / 4)
print(array6 ** 5)
'''

#4 Vectorized arithmetic
'''
array7 = np.array([1.3,2,3,4 ])

print(np.sqrt(array7))
print(np.round(array7))
print(np.ceil (array7))
print(np.pi)
'''

#EXERCISE
'''
radii = np.array([1,2,3 ])
print(np.pi * radii ** 2)
'''

#5 Element wise arithmetic
'''
array8 = np.array([4,5,6 ])
array9 = np.array([1,2,3 ])

print(array8 + array9)
print(array8 - array9)
print(array8 * array9)
print(array8 / array9)
print(array8 ** array9)
'''
#6 Comparison operators
'''
array8 = np.array([4,5,6 ])
array9 = np.array([1,2,3 ])

print(array8 > array9)

marks = np.array([98, 87, 63, 45, 78 ])

print(marks >= 60)
print(marks == 60)
print(marks <= 60)

marks[marks <= 60] = 0
print(marks)
'''

#question from chatgpt

'''
array10 = np.array([5,10,15,20,25 ])
print(array10)

array11 = np.arange(1, 11)
print(array11)

array12 = np.array([2,4,6,8,10 ])
print(np.shape(array12))

array13 = np.array([10, 20, 30, 40, 50 ])
print(array13[0])

array14 = np.array([10, 20, 30, 40, 50 ])
print(array14[2:])

array15 = np.array([[1,2,3 ]])
array16 = np.array([[4,5,6 ]])
print(array15 + array16)

array17 =np.array([[5],[10],[15],[20 ]])
array18 = np.array([2 ])
print(array17 * array18)
 

array19 = np.array([[1,2,3 ], [4,5,6 ]])
print(array19.shape)
'''

#7 Broadcasting
'''
array20 = np.array([[1 ,2 ,3 ,4 ]])
array21 = np.array([[6],[7],[8],[9]])

print(array20.shape)
print(array21.shape)

print(array20* array21)
'''

'''
array22 = np.array([[1] ,[2] ,[3] ,[4] ,[5] ,[6] ,[7] ,[8] ,[9] ,[10] ])
array23 = np.array([[1,2,3,4,5,6,7,8,9,10]])

print(array22.shape)
print(array23.shape)

print(array22* array23)
'''

#8 Aggregate functions

'''
array24 = np.array([[1,2,3,4 ],
                  [5,6,7,8 ]])

print(np.sum(array24))
print(np.var(array24)) #variance
print(np.std(array24)) #standard deviation
print(np.mean(array24)) #mean
print(np.min(array24)) #minimum
print(np.max(array24)) #maximum
print(np.argmin(array24)) #index of minimum
print(np.argmax(array24)) #index of maximum
print(np.median(array24)) #median
print(np.percentile(array24, 50)) #percentile
print(np.sum(array24, axis = 0)) #sum of columns
print(np.sum(array24, axis = 1)) #sum of rows
'''

#9 Filtering (it does not preserve the shape of the array until we use the where function )

'''
ages = np.array([[18, 25,32, 23, 45, 67, 89, 12, 34, 56],
                 [22, 33, 44, 55, 66, 77, 88, 99, 11, 22]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 60)]
different = ages[(ages <= 18) | (ages > 60)]
seniors = ages[ages >= 60]
even = ages[ages % 2 == 0]
odd = ages[ages % 2 != 0]

print(teenagers)
print(adults)
print(different)
print(seniors)
print(even)
print(odd)

#adults = np.where(ages>=18 , ages , 0) #used to preserve the arrays shape
#print(adults)
'''

#10 Random numbers
'''
rng = np.random.default_rng() #seed == using it will give the same random numbers every time we run the code

print(rng.integers(1, 100 , size = (3 )))

np.random.seed(1) #seed == using it will give the same random numbers every time we run the code
rng1 = np.random.uniform( low = -1 , high = 1 , size = (2,1)) #it generates random numbers from a uniform distribution between low and high values also in float numbers
print(rng1)


rng2 = np.random.default_rng()
array00 = np.array([1,2,3,4 ])
np.random.shuffle(array00)
print(array00)

rng3 = np.random.default_rng()
fruits = np.array(["apples", "banana", "coconut", "oranges" ,"strawberry" ])
fruits = rng3.choice(fruits, size = 3)
print(fruits)

rng4 = np.random.default_rng()
fruit = np.array(["apples", "banana", "coconut", "oranges" ,"strawberry" ])
fruit = rng4.choice(fruit)
print(fruit)
'''