def function1 (listinput):
    result = 0
    # use the sum 
    return sum(listinput)

    #for number in listinput: 
        #result += number# number is alraedy represent the value in  the list 
   # return result

listinputtest=[1,2,3,4,5,6]
#function1(listinputtest)

def function2 (listinput):
    # use max !!!!!!!
    result = listinput[0]
    for number in listinput: 
        if number>result:
            result=number       
    return result

#function2(listinputtest)

def function3():### NO SPACE 
    listoffruit=[]
    listoffruit.insert(0,"D") 
    listoffruit.insert(1,"C")
    listoffruit.append("E")# use append instead of inser
    listoffruit.append("F")
    listoffruit.sort
    del listoffruit[1]

#function3()


def function4(nulltest): ### NO SPACE !! check style app 
    if len(nulltest)==0: #nulltest.len==0
        return False
    else: 
        return True
listnull=[]
#print(function4(listinputtest))
print(function4(listnull))

def function5(): 
    list5 = [1,2,3,4,5]
    list5.reverse()
    return list5

#print(function5()) 

def function6():
    input1 = input("please give me a world ")
    result = input1[::-1]
    if result != input1:
        return "p"
    else: 
        return "not p"
#print(function6()) 


def function7(): 
    list1 = [1,2,3,4,5]
    return [i **2 for i in list1]

def function8(): 
    number = 1 
    input1 = int(input("please give me a numer "))# the input will be string, need to transfer to integer in user to use
    #list = []
    #if input1 != number: 
        #list.append (input1)# why list result is only input ? 
        #input1 -1 
    #return list
    sum=0
    for num in range(1,input1+1):#add 1 to define the correct range
        sum+=num# sum = sum +num 
    return sum
#print(function8()) 

def function9(): 
    input1 = int(input("please give me a numer "))
    if (input1 % 2) ==0:
        print("is not prime")
    else: 
       print(" is prime")
#print(function9()) 

def function10(): 
    #list = range(0,21)
    #return print(list[1:19:3])
    for i in range(0,21,3):
        print(i)
    
print(function10()) 
