# Python lists

## List slicing
 ```py
 fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
 ```

 ```py
 fam[3:5]
 ```
 >[1.68, 'mom']

 ```py
 fam[1:4]
 ```
>[1.73, 'emma', 1.68]

 ![](https://telegra.ph/file/575e1ed3d79a8e7c8f9ea.png)

 ## List Manipulation
* Change list elements
* Add list elements
* Remove list elements

 ```py
 fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]

 fam[7] = 1.86
 ```
 >['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.86]

  ```py
 fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]

fam[0:2] = ["lisa", 1.74]
 ```
 >['lisa', 1.74, 'emma', 1.68, 'mom', 1.71, 'dad', 1.86]

<br>

## Adding and removing elements

```py
fam = ['lisa', 1.74,'emma', 1.68,'mom', 1.71,'dad', 1.86]

fam_add = fam + ["me", 1.79]

print(fam)
print(fam_add)
```
>['lisa', 1.74,'emma', 1.68, 'mom', 1.71, 'dad', 1.86] <br>
>['lisa', 1.74,'emma', 1.68, 'mom', 1.71, 'dad', 1.86, 'me', 1.79]

```py
fam = ['lisa', 1.74,'emma', 1.68,'mom', 1.71,'dad', 1.86]


del(fam[2])

print(fam)
```
>['lisa', 1.74, 1.68, 'mom', 1.71,'dad', 1.86] <br>

<br>

# Behind the scenes (1)
```py
x = ["a", "b", "c"]
```
![](https://telegra.ph/file/6165f4e2cdfd271fe6264.png)

```py
x = ["a", "b", "c"]
y = x
```
![](https://telegra.ph/file/d604a20c991db94ba258b.png)

```py
x = ["a", "b", "c"]
y = x

y[1] = "z"
print(y)
print(x)
```
> ['a', 'z', 'c'] <br>
> ['a', 'z', 'c']

![](https://telegra.ph/file/4ce634e9db3b5af82c63f.png)

<br>

# Behind the scenes (2)
```py
x = ["a", "b", "c"]
y = list(x)
 # or 
y = x[:]
```
![](https://telegra.ph/file/95deccfb69e5a6455aa0b.png)

# Methods

**Methods:** Functions that belong to objects
![](https://telegra.ph/file/6c0fa2ca803219198892d.png)

```py
fam = ['lisa', 1.74,'emma', 1.68,'mom', 1.71,'dad', 1.86]


print(fam.index("mom"))

sister = 'liz'

print(sister.capitalize())

print(sister.replace("z", "sa"))
```
>4 <br>
Liz<br>
lisa<br>

# Packages
* Directory of Python Scripts
* Each script = module
* Specify functions, methods, types
* Thousands of packages available
    * NumPy
    * Matplotlib
    * scikit-learn

## import package
```py
import numpy # numpy.array()
# or
import numpy as np # np.array()
# or
from numpy import array # array()
```

# NumPy
* Powerful
* Collection of values
* Hold different types
* Change, add, remove
* Need for Data Science
    * Mathematical operations over collections
    * Speed

```py
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height) #array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array(weight) #array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2 # array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])
```

```py
np.array([1.0, "is", True])

# > array(['1.0', 'is', 'True'], dtype='<U32')
```
* NumPy arrays: contain only one type

### remarks

```py
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

python_list + python_list # [1, 2, 3, 1, 2, 3]

numpy_array + numpy_array # array([2, 4, 6])
```

* Different types: different behavior!

```py
print(bmi)
# array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])

print(bmi[1])
# 20.975

print(bmi > 23)
# array([False, False, False, True, False])

print(bmi[bmi > 23])
#array([24.7473475])
```

## 2D NumPy Arrays

```py
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d)
# array([[ 1.73, 1.68, 1.71, 1.89, 1.79], 
#       [65.4 , 59.2 , 63.6 , 88.4 , 68.7 ]])  

print(np_2d.shape)
# (2, 5) -> here 2 is number of rows, 5 is number of columns


print(np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
        [65.4, 59.2, 63.6, 88.4, "68.7"]]))

# array([['1.73','1.68','1.71','1.89','1.79'],
#        ['65.4','59.2','63.6','88.4','68.7']], dtype='<U32')
```

## Subsetting

```py
          0     1     2     3     4
array([[ 1.73, 1.68, 1.71, 1.89, 1.79],  0
       [ 65.4, 59.2, 63.6, 88.4, 68.7]]) 1
```

```py
np_2d[0] > array([1.73, 1.68, 1.71, 1.89, 1.79])

np_2d[0][2] > 1.71

np_2d[0, 2] > 1.71

np_2d[:, 1:3] > array([[ 1.68, 1.71],
                       [59.2 , 63.6 ]])

np_2d[1, :] > array([65.4, 59.2, 63.6, 88.4, 68.7])

```

```py
print(np_city)

array([[1.64, 71.78],
       [1.37, 63.35],
       [1.6 , 55.09],
       ...,
       [2.04, 74.85],
       [2.04, 68.72],
       [2.01, 73.57]])
```

```py
print(np.mean(np_city[:, 0])) > 1.7472

print(np.median(np_city[:, 0])) > 1.75

print(np.corrcoef(np_city[:, 0], np_city[:, 1]))

array([[ 1. ,   -0.01802],
       [-0.01803, 1.    ]])

print(np.std(np_city[:, 0])) > 0.1992
```

* `sum()`, `sort()`, ...
* Enforce single data type: speed!

## Generate data
* Arguments for `np.random.normal()`
    * distribution mean
    * distribution standard deviation
    * number of samples
```py
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))
```