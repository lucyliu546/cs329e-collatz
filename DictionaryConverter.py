__author__ = 'lucyliu'
def main():

    file = open("dictionary.txt", "r")
    for line in file:

        list = []
        list.append(line.split())


        print("(",list[0][0],"," + list[0][1], ") :", list[0][2], ",")

main()