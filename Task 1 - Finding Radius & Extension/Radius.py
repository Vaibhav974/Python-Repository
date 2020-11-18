import math

def Is_Float(k):
    """ 
      Checks, if a String is Convertible to float type or Not and Returns corresponding Boolean Value
      It expects a String as Argument
    """
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