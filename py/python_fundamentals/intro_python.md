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