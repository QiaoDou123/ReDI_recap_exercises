import string
def def11():
    initial = "thequickbrownfoxjumpsoverthelazydog."
    user = input("please give me a character")
    number = initial.count(user)
    return  number    

def def12():
    user=input("please give me a string ")
    unique = []
    for character in user:
        if character not in unique:
            unique.append(character) # collect one letter only once 
    for char in unique:# each letter content not each position number 
        count = user.count(char)
        return f"'{char}' appears {count} times in the string."

def def13(): 
    user=input("please give me a string")
    userfirst =user[0]
    userlast = user[-1]

    if len(user)%2==0: 
       usermiddle = user[int(len(user)/2) -1 ]
    else: 
        usermiddle = user[int(len(user)/2)]
    return userfirst, usermiddle, userlast 



def def14(): 
    listinput=["Anna", "Bob", "Caroline", "Don", "Ellen","Felix"]
    resultcount =[]
    for name in listinput:
        if len(name)>=4:
            resultcount.append(name)
        else:continue 
    return resultcount


def def15(input): 
   rate = 0,95905482
   result = input*rate
   return result 
euro = 200 
def15(euro)


    