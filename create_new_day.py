import os

x = input("Enter day number: ")

fpath = "Day" + x
os.mkdir(fpath)
with open(fpath + "/day" + x + "a.py", "w+") as f:
    with open("template.py") as g:
        lines = g.readlines()
        for line in lines:
            f.write(line.replace("rep_DAY_CODE", fpath + "/day" + x + ".txt"))

with open(fpath + "/day" + x + "b.py", "w+") as f:
    with open("template.py") as g:
        lines = g.readlines()
        for line in lines:
            f.write(line.replace("rep_DAY_CODE", fpath + "/day" + x + ".txt"))

with open(fpath + "/day" + x + ".txt", "w+"):
    pass

yn = input("Configure runtime? y/n ")
if yn == "y":
    with open("RUN_A.py", "w+") as f:
        f.write("from " + fpath + " import day" + x + "a as prog\n")
        f.write("print('Running day " + x + " A')\n")
        f.write("prog.main()\n")

    with open("RUN_B.py", "w+") as f:
        f.write("from " + fpath + " import day" + x + "b as prog\n")
        f.write("print('Running day " + x + " B')\n")
        f.write("prog.main()\n")
    os.system("git add Day" + x)
