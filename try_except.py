if 0: 
    x=-1
    if x<0:
        raise Exception('raised for no reason')

try:
    if n>0:
        print('n>0')
except TypeError:
    print('raised when two diff types are combined')
except NameError:
    print('error because variable doesnt exist') # outputs only this because only one except touched
except:
    print('n doesnt exist, hence entering except()')
    #raise Exception('raising exception for it')