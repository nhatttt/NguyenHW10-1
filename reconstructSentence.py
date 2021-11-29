'''this script takes two input text files to parse for words and string them together.
    the first word is taken from the end of file 1, then the end of  file 2.
    this process is repeated until no words are left and an output.txt file is
    generated with the combination of words from both files.
    run the program with command: "python reconstructSentence.py'''

in1 = open("input1.txt", "r")
in2 = open("input2.txt", "r")

list1 = in1.read().split(" ")
list2 = in2.read().split(" ")
in1.close()
in2.close()

outList = []
y = 0
z = 0
for x in range(len(list1)+len(list2)):
    if len(list1) >= len(list2):
        if x % 2 == 0:
            outList.append(list1[y])
            y += 1
        else:
            outList.append(list2[z])
            z += 1
    else:
        if x % 2 == 0:
            outList.append(list2[y])
            y += 1
        else:
            outList.append(list1[z])
            z += 1

output = open("output.txt", "w")
for n in range(-1,-(len(outList)) - 1, -1):
    output.write(outList[n].strip())
    output.write(" ")



