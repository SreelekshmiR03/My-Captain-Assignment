#A python program which accepts the radius of the circle from the user and computes area

radius=int(input("radius of the circle:"))
pi=3.14
Area=pi*radius**2
print("area of the circle:",Area)



#A python program to accept a filename from the user and print the extension of that

filename=input("filename:")
ext=filename.split(".")[-1]
print("ext:",ext)  