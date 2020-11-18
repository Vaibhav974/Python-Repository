"""
  Credits to Java Version of Same Problem...
"""

curr_col = 0
Ready = False
n = 0

def Num_Width(BigNo):
    """
     Returns No. of Digits Present in a Number... Hence, expects a No. as Argument
    """
    return len(str(BigNo))



def No_Show(n, w):
    """
      Formats a No. to occupy a particular width, with extra space filled with ' '
      Expects No, and the Width as Arguments
      Returns formatted String, ready to be displayed on Screen
    """
    n = str(n)
    Print = ""

    if w < len(n):
        return " { }".format(int(n))

    for i in range(0, w - len(n)):
        Print += " "
    Print += n
    return Print



def Reset(NewL = True):
    """
     Brings Column count back to Zero, when Output Number width moves from one category to other
     Generally, it has tendency to move into a new line, 
       except when transition happens from 0th to 1st Category of Width
    """
    if NewL:
        print("\n\n  ", end="")
    global curr_col
    curr_col = 0



def Hell():
    """
      Adds adjective to final Output statement, representing frustration of Program to Calculate
       huge or super huge values
    """
    A = ""
    Dictionary = ["'Difficult'", ", 'Insane'", ", 'Draculous'", ", 'Unrealistic'", ""] # n = 300, 900, 27000, 810000

    global n
    if n < 150:
        return ""

    if n >= 300:
        Dictionary[0] = "'Hell'"

    i = 1
    while 30**i <= n:
        if Dictionary[i-1] == "":
            return A
        else:
            A += Dictionary[i-1]
        i += 1

    A += " "
    return A



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



def Input(Print=True):
    """
      Takes Input for Processing Output, In OOP concept taking Input is possible without giving output
      So, anyway, an option is provided
    """
    global Ready
    Buffer = input("\n  Enter No. of Elements to be Displayed from the Fibonacci Series  : ")

    if not Is_Int(Buffer):
        print("   This is not a Number... Please Try Again!")
        Ready = False
        return Ready

    global n 
    n = int(Buffer)
    Ready = True
    if Print:
        Output()
    return Ready



def Output():
    """
     Responsible for Main Output of the Program
    """
    (a, b, c, max_col, width) = -1, 1, 0, 0, 0

    if Ready == False:
        print("\n No Number to Print upto... ! Sorry... ")
        return

    print("\n  ", end="")

    for i in range(n):
        c = a + b
        a = b
        b = c

        global curr_col
        curr_col += 1
        N_Width = [5, 8, 13, 17, 21, 27, 37, 57]
        T_Width = [8, 10, 15, 20, 24, 30, 40, 60]

        for i in range(8):
            if Num_Width(c) < N_Width[i]:
                if width != T_Width[i]:
                    if i == 0:
                        Reset(False)
                    else:
                        Reset()
                width = T_Width[i]
                max_col = 120//T_Width[i]
                break

        if Num_Width(c) >= 57:
            k = 60
            while(True):
                if Num_Width(c) < k-3: # Speed Improvement Possible
                    if width != k:
                        Reset()
                    width = k
                    max_col = 1
                    break
                k += 5

        if curr_col % max_col == 0 and curr_col != 0:
            print("\n  ", end="")

        print(No_Show(c, width), end="")

    print("\n\n  As Per {}Requirements, Fibonacci Series has been Printed !!".format(Hell()))


print("\n  Here, we are going to Print Out, Fibonacci Series upto 'n' Terms ", end="")
while(not Input()):
    pass