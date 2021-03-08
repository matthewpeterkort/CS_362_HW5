def FizzBuzz():
    i=0
    j=[None]*101
    while(i<101):
        if(i%5==0 and i%3==0):
            print("FizzBuzz")
            j[i]="FizzBuzz"
	elif (i%5==0):
            print("Buzz")
            j[i]="Buzz"
            if(i==100):
                return j
	elif (i%3==0):
	    print("Fizz")
            j[i]="Fizz"

      
        else:
            print(i)
            j[i]=i
            
        i=i+1
  
    
