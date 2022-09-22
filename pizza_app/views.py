from distutils.util import convert_path
from http.client import ACCEPTED
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from pizza_app.models import MyCart
from pizza_app.models import Cart
from pizza_app.models import Order
from pizza_app.models import Menu
from pizza_app.models import Customer

from pizza_app.models import CountNum
import re ,os
# Create your views here.


# def home(request):
#    count = CountNum.objects.get(id=1)
#    return render(request, 'home.html', {'count':count})


# def increment(request):

#    count=CountNum.objects.get(id=1)
#    count.countnum=int(count.countnum)+1
#    count.save()
#    return redirect(request.META['HTTP_REFERER'])



# def reset(request):
#     count=CountNum.objects.get(id=1)
#     count.countnum=0
#     count.save()
#     return redirect(request.META['HTTP_REFERER'])



# def decrement(request):
#     count=CountNum.objects.get(id=1)
#     count.countnum=int(count.countnum)-1
#     count.save()
#     return redirect(request.META['HTTP_REFERER'])


def customer_registration(request):
       if request.method=='POST':
            username=request.POST['username']
            f_name=request.POST['firstname']
            l_name=request.POST['lastname']
            email=request.POST['email']
            mobileno=request.POST['mobileno']
            password=request.POST['password']
            repeat_password=request.POST['repeatpassword']
                
            regex = r'\b[A-Za-z0-9._%+-]+@gmail.com\b'

            if(re.fullmatch(regex, email)):
                pass   
            else:
                e_msg="Invalid Username"
                # print("Invalid Email")
                return render(request,"registration.html",{'e_msg':e_msg})

            #  mobile no:
            
            if mobileno.isdigit():
                if len(mobileno)== 10:
                    pass
                else:
                    m_msg="Mobile no Invalid"
                    return render(request,"registration.html",{'m_msg':m_msg})
            else:
                print("invalid data")
                return render(request,"registration.html")

            # password 

            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pat = re.compile(reg)
            if len(password)>=8 :
                if(re.fullmatch(pat, password)):
                    pass   
                else:
                    p_msg="Invalid Password"
                    # print("Invalid Email")
                    return render(request,"registration.html",{'p_msg':p_msg}) 
            else:
                p_msg="Password too Short"
                return render(request,"registration.html",{'p_msg':p_msg}) 


            if password == repeat_password :
                pass
            else:
                rp_msg="Password does not match"
                return render(request,"registration.html",{'rp_msg':rp_msg}) 

            cid= Customer.objects.create(    
                                             username= username,
                                             email=email,
                                             password=password,
                                             first_name=f_name,
                                             last_name=l_name,
                                             mobile_no=mobileno,
                                             role="customer"
                                          )

            context={
                      'cid':cid
            }
            print("sucessfully registerd ")
            return render(request,"login.html",context)
       else: 
            return render(request,"registration.html")


def login(request):
    if 'username' in request.session:
        uid = Customer.objects.filter( username= request.session['username'])
        # u_id = Customer.objects.filter( username= request.session['id'])
        if uid[0].role == 'admin':
           return redirect('adminhome')
                       
        elif uid[0].role == 'customer':
            return redirect('customer_wlc')
        
    else:
        try:
            if request.POST:
                username = request.POST['username']
                password = request.POST['password']
                print("---username ,",username)
                                
                uid = Customer.objects.filter( username= username)
                if len(uid)==0:
                    e_msg=" Invalid username "
                    return render(request,"login.html",{'e_msg':e_msg})
                                            
                elif uid[0].password == password:
                    print("sucessfully")
                    request.session['username']=username
                    
                    print(uid[0].role)
                    if uid[0].role == 'admin':
                        return render(request,"adminhome.html")
                       
                    elif uid[0].role == 'customer':
                        return render(request,"customerwlc.html")
                   

                else:
                    e_msg=" invalid password"
                    return render(request,"login.html",{'e_msg':e_msg})
            else:
                return render(request,"login.html")
        except Exception as e:
                print(e,"---------------------------------------------------------login")
                e_msg="404 page not found"
                return redirect('login')   


def logout(request):
    del request.session['username']
    return redirect('login')

def adminhome(request):
    # y=0
    if 'username' in  request.session:
        cid = Customer.objects.get(username = request.session['username'])    
        mid_all=Menu.objects.all()
        all_ord=Order.objects.all()
        y=len(all_ord)
        return render (request,"adminhome.html",{'mid_all':mid_all,'cid':cid,'y':y}) 
    else :
        return redirect('login')
def add_pizza(request):
    if request.method=="POST":
        if request.FILES:
            
            pizzapic= request.FILES['pizza_pic']
            pizzaname=request.POST['pizzaname']
            pizzaprice=request.POST['pizzaprice']
        
        
            handle_uploaded_file(request.FILES['pizza_pic'])
            print(pizzapic)
            mid=Menu.objects.create(
                pizza_name=pizzaname,
                pizza_price=pizzaprice,
                pizza_image=pizzapic
            )
            return redirect('adminhome')
        else:
            print("sucessfully added")
            return redirect('adminhome')
    else:
        return render(request,"adminhome.html")   

def delete(request,pk):
    print("in delete")
    pizza_del= Menu.objects.get(id = pk)
    pizza_del.delete()

    return redirect('adminhome')
        
        
       
def handle_uploaded_file(f):  
    with open('pizza_app/static/images/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def edit_pizza (request,pk):
    print("in edit")
    edit_pizza= Menu.objects.get(id = pk)
    
    if request.method == "POST":
        mid_all=Menu.objects.all()
        edit_pizza.pizza_name=request.POST['pizzaname']
        edit_pizza.pizza_price=request.POST['pizzaprice']
        try:
            edit_pizza.pizza_image=request.FILES['pizza_pic']
            edit_pizza.save()
        except:
            pass
        edit_pizza.save()
        return render (request,"adminhome.html",{'mid_all':mid_all})

    else:
        print(edit_pizza.pizza_name)
        print(edit_pizza.pizza_price)
        return render(request,"edit.html",{'edit_pizza':edit_pizza})




def customer_wlc(request):
    # x=0
    if 'username' in  request.session:
        cid = Customer.objects.get(username = request.session['username'])
        carts=MyCart.objects.filter(user=cid)
        x=len(carts)
        menu_all=Menu.objects.all()
        return render(request,"customerwlc.html",{'menu_all':menu_all,'cid':cid,'carts':carts,'x':x})
    else :
        return redirect('login')


       
def add_to_cart(request,pk):
   
    menu=Menu.objects.get(id=pk)
    customer = Customer.objects.get(username=request.session['username'])
    price=menu.pizza_price
    # print(price)
    totalprice=menu.pizza_price
    cart=MyCart.objects.filter(menu_id=menu)
    # print(len(cart))
    if len(cart)!=0:
        obj = MyCart.objects.get(menu_id=menu)
        obj.quantity=int(obj.quantity)+1
        
        obj.save()
    else:
        MyCart.objects.create(user=customer,menu_id=menu,price=price,total_price=totalprice)
    
    
    return redirect('customer_wlc')
    

def checkout(request):
    net_price=0
    
    customer=Customer.objects.get(username=request.session['username'])
    carts=MyCart.objects.filter(user=customer)
    
        # print("carts = ", carts)

    
    for i in carts:

            # print("i = ",i, type(i))
        y = i.menu_id.pizza_price
        x = int(i.quantity)

        data = x*int(y)
        i.total_price = data
        net_price=net_price+i.total_price
            # print(data)
        # print("carts of total_price = ",data,type(x),y,carts[0].total_price)
        i.save()
            
    
        

        request.session['cart_count']=len(carts)
        # print(carts[2].total_price)
    return render (request,"checkout.html",{'carts':carts,'net_price':net_price})

def pizza_delete_checkout(request,pk):
    pizza_del_check= MyCart.objects.get(id = pk)
    pizza_del_check.delete()
    
    return redirect('checkout')
def increment(request,pk):
  
   count=MyCart.objects.get(id=pk)
   count.quantity=int(count.quantity)+1
  
   count.save()


   return redirect(checkout)


def decrement(request,pk):
    
    count=MyCart.objects.get(id=pk)
    print(type(count))
    count.quantity=int(count.quantity)-1

    for i in  range(count.quantity):
        
        if i < 1 :
            pass
        count.save()

    return redirect(checkout)

def order(request):
    if request.POST:
    
        customer = Customer.objects.get(username=request.session['username'])
        carts=MyCart.objects.filter(user=customer)
        

      
        for i in carts:
        
             
            a = i.menu_id_id
            print("a",a)
            b = int(i.quantity)
            c= i.price
            d=i.total_price
            print(a)
            
            Order.objects.create(customer_id=customer,menu_id_id=a,quantity=b,price=c,total_price=d)
        MyCart.objects.filter(user=customer).delete()
       
    
    
    return redirect('customer_wlc')

def myorder(request):
    total=0
    status ="PENDING"
    customer = Customer.objects.get(username=request.session['username'])
    myord=Order.objects.filter(customer_id=customer)
    # print(myord[0].status)
    for i in myord:
        total=total+int(i.total_price)
           
        

    return render(request,"myorder.html",{'myord' :myord,'total':total,'status':status})

def adminshoworder(request):
    total=0
   
    all_ord=Order.objects.all()
  
    for i in all_ord:
    
        total=total+int(i.total_price)
        i.save()

    return render (request,"adminorders.html",{'all_ord':all_ord,'total':total
    })

def accept_order(request, pk):
    o = Order.objects.get(id=pk)
    o.status = "Accepted"
    o.save()
    return redirect(adminshoworder)

def reject_order(request, pk):
    o = Order.objects.get(id=pk)
    o.status = "Rejected" 
    o.save()
    
    return redirect(adminshoworder)



