subject={}
s=int(input("enter number of course do you wants:"))
for j in range(0,s):
    a=input("enter course:")
    n=int(input("enter number of subject:"))
    subject[a]={}
    for i in range(0,n): 
        s1=input("enter subject:")
        att=int(input("enter attendence:"))
        subject[a][s1]=att
        
print("\n",subject,"\n")
print("="*21)
print("Get Attendence detail")
print("="*21,"\n")

c=input("enter course:")
s2=input("enter subject:")

print(subject[c][s2])

