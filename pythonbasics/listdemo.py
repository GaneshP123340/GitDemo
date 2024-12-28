from selenium.webdriver.common.print_page_options import PrintOptions

values = [4,4,4,'@','Ganesh']
print(values[0:10])
print(values[0:3])
values.insert(3,4)
print(values[0:5])
values.append('kumar')
values[4] = '#'
del values [2]
print(values)
print(values.count(4))



# TUPPLE = same as list data type but immutable
val = (1,2,'ganesh',2.4)
print(val[2])
# val[2] = 'revathi' ; TypeError: 'tuple' object does not support item assignment

# dictionary
dic = {'a':2 , 2:'bgv' , 'c':'My dict'}
print(dic[2])
print(dic['c'])

dict = {}
dict['firstname'] = "ganesh"
dict['lastname'] = "prajapati"
dict['age'] = 27
print(dict)
print("***************************************************************************************************************")
# classes are user defined blueprint or prototype
# CLASS will have methods , class variable , instance variables , cunstructor etc .
# self keyword is mandatory for calling variable names into method .
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object
# 

class calculator:
    num =100 #class variable

    #defolt constructor
    def __init__(self , a , b):
        self.firstNumber = a
        self.secondNumber = b
        print('i am called automatically when object is create')

    def getdata(self):
        print(' i am now executing as method in class')

    def summation(self):
        return self.firstNumber + self.secondNumber + calculator.num


obj = calculator(2,3) #syntax to create object in python
obj.getdata()
print(obj.num)

obj1 = calculator(4,8) #syntax to create object in python
obj1.getdata()
print(obj1.num)

