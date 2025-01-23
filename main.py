with open("students.txt","w") as file:
    file.write("Lida\nTara\nOliver G\nJoseph\nBram\nLetotlo\nBen\nAlessandro\nLayla\nMarlee\nTao\nSofi\nSelma\nAmelia\nLeila\nOliver M\nHarry\nAxel\nBayne\nMaisie\nJolie\nRafael")
with open("students.txt","a") as file:
    new_line = input("Enter the line you want to add to the file:")
    file.write(new_line + "\n")
with open("students.txt","r") as file:
    for line in file:
        print(line.strip())
        print(line[1])

with open("students.txt","r") as file:
    for line in file:
        if len(line)>6:
            print(line)
    