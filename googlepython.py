# a = 6
# print(a)
#
# a = "hello"
# print(a)
#
# print(len(a))
#
# print(A)
#
# print("Hello" + 6)
# print("Hello" + str(6))

import sys


def Hello(name):
    if name == "Alice" or name == "Nick":
        DoesNotExist(name)
        name = name + "???"
    else:
        name = name + "!!!!!"
    print("hello", name)


def main():
    Hello(sys.argv[1])


if __name__ == '__main__':
    main()

# dir(sys)
# help(sys)
#
# help(sys.exit)
#
# help(len)
#
# a = 'Hello'
# a = "isn't"
#
# len(a)
#
# print(a + "yay!")
#
# a = "Hello"
# print(a.lower())
#
# b = "YAY"
# print(b.lower())
#
# print(a.lower())
# print(a)
#
# print(a.find("e"))
#
# print(a[0])
# print(a[100])
#
# print("Hi %s I have %d donuts" % ("Alice", 42))
#
# a = "Hello"
#
# print(a[0])
# print(a[1])
# len(a)
# print(a[1:3])
# print(a[1:5])
# print(a[1:])
# print(a[:])
#
# print(a[-4:-2])
# print(a[:-3])
# print(a[-3:])
