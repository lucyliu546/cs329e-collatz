__author__ = 'lucyliu'
import random
def main():

    start = 0
    end = 150
    for i in range(0, 150):
        i, j = random.randrange(0, 100, 1), random.randrange(0, 100, 1)
        print(i, j)
main()