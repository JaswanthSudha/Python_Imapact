def check(string):
    list=[]
    for item in string:
        if item =="{" or item=="[" or item=="(":
            list.append(item)
        if item ==")" or item=="]" or item=="}":
            element=list.pop()
            if element=="(" and item==")" or element=="{" and item=="}" or element=="[" and item=="]":
                pass
            else:
                return "No"
                
    return "YES"
def postfix(string):
    output=""
    list=[]
    for item in string:
        if item.isdigit():
            output=output+item
        if item==")":
            for ch in list:
                if ch=="(":
                    break
                else:
                    output=output+ch
        else:
            list.append(item)
    if len(list)!=0:
        while len(list)==0:
            x=list.pop()
            string=string+x 
    return output


string=input("enter the string")
print(postfix(string))
# print(check(string))
# ptr1=0
# ptr2=0
# for i in range(len(string)):
#     ptr1=i
#     ptr2=(len(string)-1)-i
#     start=string[ptr1]
#     end=string[ptr2]
#     if ptr1>ptr2:
#         break
#     if start=="(" and end==")" or start=="{" and end=="}" or start=="[" and end=="]":
#         pass
#     else:
#         print("no")
#         break
# def infix():
#     pass


    

        
    

# string="1234"