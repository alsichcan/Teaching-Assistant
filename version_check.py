import os

src_path = os.path.dirname("./001/HW8/")
#dst_path = os.path.dirname("./001/HW/")

assignment = dict()
with open("./001/assignment.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split('\t')
        assignment[data[0]] = data[-1][0]

for filename in os.listdir(src_path):
    elems = filename.split("_")
    if elems[5][-1] != assignment[elems[1]]:
        print(elems[0], elems[1],  assignment[elems[1]], elems[5][-1])