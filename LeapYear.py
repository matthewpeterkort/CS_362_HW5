def leapyear():
    year=False
    leap=1
    while(leap==1):
        val=int(input("enter a year"))
        if((val%4==0) and (val%100!=0):
            print(val,"is a leap year")
            year=True
            leap=0
            return year
    