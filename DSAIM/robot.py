string="UDDLLRUUUDUURUDDUULLDRRRR"
rows=5
columns=5
ob1=[2,2]
ob2=[3,3]
left,right=0,0
for char in string:
    if left==ob1[0] or left ==ob2[0] or left==rows or left==-1:
        continue
    if right==ob1[1] or right==ob2[1] or right==columns or right==-1:
        continue
    if char =="U":
        left+=1
    if char=="L":
        right-=1
    if char=="R":
        right+=1
    if char=="D":
        left-=1
print("left",left,"right",right)
    
