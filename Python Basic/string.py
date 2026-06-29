#Concatenation
str1 = "Hello guys this is Shaurya"
str2 = "i'm learing python today"
finalstr = str1 + " " + str2
print(finalstr)

#Length of str
len(str1)
print(len(str1))

#indexing
str = "Shauryaa Singh"
print(str[9])

#Slicing (Accessing parts of  string)
str = "ABES Engineering College"
print(str[5:16])
print(str[5:len(str)])
print(str[-7:-1])

"""String Function"""
str = "i'm studying python from kaggle and youtube"
print(str.endswith("tube"))
print(str.capitalize())                    #Capitalize first letter
print(str.replace("python","javascript"))
print(str.find("from"))                    #find 1st occurence
print(str.count("o"))