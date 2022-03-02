while True:
    try:
        a=int(input())
        x="1"
        while(1):
            if int(x)%a==0:break
            x+="1"
        print(len(x))
            
            
    except:
        break
