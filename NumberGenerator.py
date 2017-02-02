__author__ = 'lucyliu'
import random
def main():

    start = 0
    end = 1000000
    for x in range(0, 999999, 20000):
        i, j = (x, x + 20000)
        print(i, j)
main()