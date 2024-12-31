print("licznik dram!")
text = open("points.txt", "r")
print("dram już było:")
print(text.read())
text.close()

point = input("Drama dzisiaj była? Y/N")
if point == "Y":
     print("dodano!")
     text = open("points.txt", "w")
     text.write(",")
     text.close()



if point == "N":
     print("nie dodano!")