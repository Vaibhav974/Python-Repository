def Plural(n):
    """
      Helps to Determine Singular or Plural Output based on Input
       If Input is equal to 1, it returns Singular word
       otherwise, it returns Plural Word

      Hence, it expects No. as an argument and returns a String
    """
    if n == 1:
        return "Time"
    else:
        return "Times"

print("  This Program, Finds out Frequency of all the Letters in a String ")
print("    So, Continue Entering any String... \n")

String = input("     ==> ")

Freq = {}

for Char in String:
    if Char.isalpha():
        if Char.lower() not in Freq:
            Freq[Char.lower()] = 0
        Freq[Char.lower()] += 1

print("\n  Frequency Chart follows... ")

for Letter in sorted(Freq, key=lambda a: Freq[a], reverse=True):
    print("    {}  -  {} {}".format(Letter, Freq[Letter], Plural(Freq[Letter])))