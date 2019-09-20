from django.shortcuts import render
from django.http import HttpResponse
from math import sqrt


def home(request):
    return render(request,"home.html")

def output(request):
    number_1=request.GET.get("nm_1","default")
    number_2=request.GET.get("nm_2","default")
    add=request.GET.get("s","default")
    mul=request.GET.get("s","default")
    division=request.GET.get("s","default")
    subtraction=request.GET.get("s","default")
    modulation=request.GET.get("s","default")
    double_div=request.GET.get("s","default")
    powar=request.GET.get("s","default")
    percentage=request.GET.get("s","default")
    root=request.GET.get("s","default")


    if add=="sm":
        s=int(number_1)+int(number_2)
        parameter={"first_Number":number_1,"Second_Number":number_2,"first Number":number_1,"Second Number":number_2,"action":"Finding Addition","result":s}
        return render(request,"output.html",parameter)

    elif mul == "pr" :
        s=int(number_1)*int(number_2)
        parameter={"first_Number":number_1,"Second_Number":number_2,"action":"Finding Multipication","result":s}
        return render(request,"output.html",parameter)

    elif division=="div" :
        s=int(number_1)/int(number_2)
        parameter={"first_Number":number_1,"Second_Number":number_2,"action":"Finding Division","result":s}
        return render(request,"output.html",parameter)
    
    elif subtraction=="sub" :
        s=int(number_1)-int(number_2)
        parameter={"first_Number":number_1,"Second_Number":number_2,"action":"Finding Subtraction","result":s}
        return render(request,"output.html",parameter)
    
    elif modulation=="mod" :
        s=int(number_1)%int(number_2)
        parameter={"first_Number":number_1,"Second_Number":number_2,"action":"Finding Modulo","result":s}
        return render(request,"output.html",parameter)

    elif double_div=="d_div" :
        s=int(number_1)//int(number_2)
        parameter={"first_Number":number_1,"Second_Number":number_2,"action":"Finding Double Division","result":s}
        return render(request,"output.html",parameter)
    
    elif powar=="pow" :
        s=int(number_1)**int(number_2)
        parameter={"first_Number":number_1,"Second_Number":number_2,"action":"Finding To The Powar","result":s}
        return render(request,"output.html",parameter)
    
    elif percentage == "per":
        s=(int(number_1)/int(number_2))*100
        t=f"First number is {s}  % of Second number"
        parameter={"first_Number":number_1,"Second_Number":number_2,"action":"Finding percentege","result":t}
        return render(request,"output.html",parameter)
    elif root == "rt":
        s=sqrt(int(number_1))
        t=sqrt(int(number_2))
        
        parameter={"first_Number":number_1,"Second_Number":number_2,"action":"Finding square root of two number","result":[s,t]}
        return render(request,"output.html",parameter)
    else:
        a=int(number_1)+int(number_2)
        b=int(number_1)*int(number_2)
        c=int(number_1)/int(number_2)
        d=int(number_1)-int(number_2)
        e=int(number_1)%int(number_2)
        f=int(number_1)//int(number_2)
        g=int(number_1)**int(number_2)
        h=(int(number_1)/int(number_2))*100

        parameter={"first_Number":number_1,"Second_Number":number_2,"Addition":a,"Multipication":b,"Division":c,"Subtraction":d,"Modulo":e,"Double_Division":f,"Powar":g,"precentege":h}
        return render(request,"all.html",parameter)







    

