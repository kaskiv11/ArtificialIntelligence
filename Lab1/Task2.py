import numpy as np
import matplotlib.pyplot as plt
import math

# Task 2 Lab1

#  %%-----------------------------------------
p = np.linspace(start=-5, stop=5, num=100)


#  %%-----------------------------------------
def hardlim(n):
    return np.where(n >= 0.0, 1, -1)


def dhardlim(n):
    return np.where(n >= 0.0, 0, 0)


# np.where(n >= 0.0, 0, 0)

t_hardlim = hardlim(p)

plt.plot(p, t_hardlim, ls='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Hardlims Function')
plt.show()
#  %%-----------------------------------------

t_dhardlim = dhardlim(p)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Dhardlims Function')
plt.show()


#  %%-----------------------------------------


def writeToFileHardlim():
    print('Hardlims Func')
    with open('D:\\learn\\semester 3\\штучний інтелект\\Lab1\\Lab1\\file\\Readme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = hardlim(i)
            print("x= ", i, "y=", t, file=f1)
            print("x=", i, "y=", t)


writeToFileHardlim()


def writeToFileDHardlim():
    print('Dhardlim Function')
    with open('D:\\learn\\semester 3\\штучний інтелект\\Lab1\\Lab1\\file\\DReadme.txt', 'w') as f1:
        for i in np.arange(-5, 5, 0.1):
            t = dhardlim(i)
            print("x= ", i, "y=", t, file=f1)
            print("x= ", i, "y=", t)


writeToFileDHardlim()
