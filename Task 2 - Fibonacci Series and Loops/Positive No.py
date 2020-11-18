def Is_Int(k):
    """ 
      Checks, if a String is Convertible to Int type or Not and Returns corresponding Boolean Value
      It expects a String as Argument
    """
    try:
        int(k)
        return True
    except:
        return False

print("\n Aim of this Program is to Filter out Negative Elements of an Array")
print("   Enter No.s to Add into the List, once you are done hit 'Enter' again to end Input")

Number = " "
No_List = []

while Number != "":
    Number = input("     ")
    if(Is_Int(Number)):
        No_List.append(int(Number))
    else:
        if Number != "":
            print("       That was not a Number! So, didn't consider that... \n")

Max = len(No_List)
i = 0
while i < Max:
    if No_List[i] < 0:
        No_List.pop(i)
        Max -= 1
    else:
        i += 1

print(" List of Positive Elements Follows... ")
print("  ", No_List, "\n")