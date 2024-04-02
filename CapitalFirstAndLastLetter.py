yourStr = "why are you learning python"
def CapitalWords(yoursVal):
    return " ".join(map(lambda s:s[:-1]+s[-1].upper(),yoursVal.title().split()))
print(CapitalWords(yourStr))

# output = WhY ArE YoU LearninG PythoN
