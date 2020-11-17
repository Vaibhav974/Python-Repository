import math

def Is_Float(k):
    try:
        float(k)
        return True
    except:
        return False

r = input(" Enter Radius of the Circle to Calculate Area   : ")

if Is_Float(r):
    print("  Area of the Circle is Found as : {:.3f} ".format(math.pi*float(r)**2))
else:
    print("  Sorry, that was Not a Number")