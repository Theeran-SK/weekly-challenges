testlist = open("test_file.txt")
estlist = testlist.readlines()
testlist2 = open("test_file2.txt")
estlist2 = testlist2.readlines()

stlist = str(estlist)
stlist2 = str(estlist2)

tsiltset = stlist.split(" ")
tsiltset2 = stlist2.split(" ")

list(tsiltset2)
list(tsiltset)

set_test = set(tsiltset)
set_test2 = set(tsiltset2)

if set_test & set_test2:
    print(set_test & set_test2)
