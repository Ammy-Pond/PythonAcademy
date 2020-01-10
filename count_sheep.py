array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

def count_sheeps(arrayOfSheeps):
    n=0
    for sheep in arrayOfSheeps:
        if sheep:
            n=n+1
    return n

count_sheeps(array1)