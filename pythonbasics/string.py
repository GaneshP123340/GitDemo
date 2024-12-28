str = " i am Revathi And i Hate ganesh When He Speak anything "
str2 = " i insult him all the time"
str3 = " but if he insult me i will fight with him "
str4 = "Revathi"
str5 = " ganesh "
str6 = "Revathi.Ganesh"

print(str[1])
print(str[5:22]) # substring in python
print(str+str2+str3) # concatenating string
print(str4 in str , str5 in str) # substring check
var = str6.split(".") # split method , split into two different string
print(var)
print(str5.strip()) # strip the white spaces
print(str5.lstrip())# strip the left space
print(str5.rsplit())# convert in list
