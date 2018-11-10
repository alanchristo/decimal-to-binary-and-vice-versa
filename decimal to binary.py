def to_binary():
    a= int(input("Enter a number to convert"))
    reminder =0
    b=0
    list = []
    while reminder != 1:
        b=a%2
        print("2",a,"-",b)
        list.append(b)
        a=a//2
        if a==1:
            list.append(a)
            print(" ",a)
            reminder =1
    list.reverse()
    print(*list,sep=' ')
def to_decimal():
    a= int(input("Enter a number to convert"))
    l=len(str(a))-1
    power = ["⁰","ⁱ","²","³","⁴","⁵","⁶","⁷","⁸","⁹"]
    b=0
    c=0
    d= [int(i) for i in str(a)]
    for i in range(l+1):
        b=b+d[i]*(2**l)
        print("2"+power[l],"*",d[i],"=",d[i]*(2**l))
        l=l-1 
    print(b)
while True:
    q = input("do yo want to covert to binary or decimal?")
    if q=="binary":
        to_binary()
        break
    elif q=="decimal":
        to_decimal()
        break
