print("Enter DOB in such manner","Date: x","Month:y ","Year: z",sep="\n")
y=int(input("Date: "))
x=int(input("Month:"))
z=int(input("Year: "))
days=0;
for i in range(1,(x+1)):
        if i==1 or i== 3 or i==5 or i==7 or i==8 or i==10 or i==12:
                month=31;
        elif i==4 or i==6 or i==9 or i==11:
                month=30;
        elif i==2 and z%4==0:
                month=29;
        elif i==2 and z%4!=0:
                month=28;
        days= days + month;
if x==1 or x== 3 or x==5 or x==7 or x==8 or x==10 or x==12:
                month=31;
elif x==4 or x==6 or x==9 or x==11:
                month=30;
elif x==2 and z%4==0:
                month=29;
else:
        month=28;
days= days + y - month;
if z%4==0:
 q=366 - days;
else:
 q=365 - days;        
#print(q);

days1=0;
y1=int(input("Today's Date: "));
x1=int(input("Ongoing Month: "));
z1=int(input("Ongoing Year: "));
for j in range(1,x1+1):
        if j==1 or j== 3 or j==5 or j==7 or j==8 or j==10 or j==12:
                month=31;
        elif j==4 or j==6 or j==9 or j==11:
                month=30;
        elif j==2 and z1%4==0:
                month=29;
        elif j==2 and z1%4!=0:
                month=28;
        days1= days1 + month;
if x1==1 or x1== 3 or x1==5 or x1==7 or x1==8 or x1==10 or x1==12:
                month=31;
elif x1==4 or x1==6 or x1==9 or x1==11:
                month=30;
elif x1==2 and z1%4==0:
                month=29;
else:
        month=28;
days1= days1 + y1 - month;
for h in range((z+1),z1):
        if h%4==0:
                days1= days1 + 366;
        else:
                days1= days1 + 365;
t=q +days1;
if ((x==2 and y==29 and z%4!=0)) or ((x1==2 and y1==29 and (z1)%4!=0)) or (z1<z) or y>31 or y1>31 or x>12 or x1>12 :
        print("Invalid Input.")
elif ((y>28 and x==2) or (y1>28 and x1==2)):
        print("Invalid Input.")        
else:
        print("Total Days:",t);
        print(eval("t//365"),"Year",eval("(t%365)//30"),"Month",eval("(t%365)%30"),"Days")
