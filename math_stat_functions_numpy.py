import numpy as np

arr = np.array([[4,3,2],[10,1,0],[5,8,24]])

""" printing the minimum numbers in an array 
    on the x and y axis"""
print(np.min(arr))

print(np.amin(arr, axis=0))

print(np.amin(arr,axis=1))


""" Printing the maximum numbers in an array
    on the x and y axis """

print(np.max(arr))

print(np.amax(arr, axis=0))

print(np.amax(arr, axis=1))


""" The functions median, mean, standard
    div, variants """

print(np.median(arr))

print(np.mean(arr))

print(np.std(arr))

print(np.var(arr))

""" Mathematical function that are useful"""

print(np.percentile(arr,50))

deg = np.array([0,30,45,60,90])
print(np.sin(deg*np.pi/180))
print(np.cos(deg*np.pi/180))
print(np.tan(deg*np.pi/180))


"""Need to check into this more!!!!"""
print('''arcsin
arccos
arctan
''')

"""Using floor and ceil on the array"""
arr_one = np.array([0.1,0.8,-2.2,-9.87])

print(np.floor(arr_one))

print(np.ceil(arr_one))






