#Q1 --

try:
    f1=open(r"C:\Users\HP\PythonBy tutedude\Python_Assignments\sample.txt","r")
    f2=open("sample.txt","r")
except Exception as e:
    # print("The file {} does not Found.".format(e))
    print(e)
print()
print(f1.read())
f1.close()

# with open(r"C:\Users\HP\PythonBy tutedude\Python_Assignments\sample.txt", "r") as f1:
#     # Read the entire file
#     content = f1.read()
#     print(content)

print()

#Q2-- 
s=input("Enter text to write to the file : ")

try:
    f3=open(r"C:\Users\HP\PythonBy tutedude\Python_Assignments\output.txt","w+")
    f3.write(s)
    print("Data Successfully written to output.txt file .")
except Exception as e:
    print(e)
f3.seek(0)
print(f3.read())

print()

s1=input("Enter additional text to append : ")
try:
    f3.write("\n"+s1)
    print("Data successfully Appended.")
except Exception as e:
    print(e)
f3.seek(0)
A
print()

print("Final content of output.txt file is : ")
print(f3.read())