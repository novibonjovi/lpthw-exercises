#  1) [X] True and True  ->  True
#  2) [X] False and True  ->  False
#  3) [X] 1 == 1 and 2 == 1  ->  False
#  4) [X] "test" == "test"  ->  True
#  5) [X] 1 == 1 or 2 != 1  ->  True
#  6) [X] True and 1 == 1  ->  True
#  7) [X] False and 0 != 0  ->  False
#  8) [X] True or 1 == 1  ->  True
#  9) [X] "test" == "testing"  -> False
# 10) [X] 1 != 0 and 2 == 1  ->  False
# 11) [X] "test" != "testing"  ->  True
# 12) [X] "test" == 1  ->  False
# 13) [X] not (True and False)  ->  True
# 14) [X] not (1 == 1 and 0 != 1)  ->  False
# 15) [X] not (10 == 1 or 1000 == 1000)  ->  False
# 16) [X] not (1 != 10 or 3 == 4)  ->  False
# 17) [X] not ("testing" == "testing" and "Zed" == "Cool Guy")  ->  True
# 18) [X] 1 == 1 and (not ("testing" == 1 or 1 == 0))  ->  True
# 19) [x] "chunky" == "bacon" and (not (3 == 4 or 3 == 3))  ->  False
# 20) [x] 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))  ->  False

print("01", True and True)
print("02", False and True)
print("03", 1 == 1 and 2 == 1)
print("04", "test" == "test")
print("05", 1 == 1 or 2 != 1)
print("06", True and 1 == 1)
print("07", False and 0 != 0)
print("08", True or 1 == 1)
print("09", "test" == "testing")
print("10", 1 != 0 and 2 == 1)
print("11", "test" != "testing")
print("12", "test" == 1)
print("13", not (True and False))
print("14", not (1 == 1 and 0 != 1))
print("15", not (10 == 1 or 1000 == 1000))
print("16", not (1 != 10 or 3 == 4))
print("17", not ("testing" == "testing" and "Zed" == "Cool Guy"))
print("18", 1 == 1 and (not ("testing" == 1 or 1 == 0)))
print("19", "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print("20", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))
