__author__ = 'lucyliu'
def main():
    #checks how many lines are in the acceptance tests
    file = open("RunCollatz.in", "r")
    count = 0
    for line in file:
        count +=1
    print(count)
main()