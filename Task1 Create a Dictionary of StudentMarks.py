dict={'Alice':85,'Asha':90,'Fig':75,'Anil':100}
student = input("Enter the  student's name : ")
if (student in dict):
    print("{}'s marks:".format(student),dict[student])
else:
    print("Student not found.")

