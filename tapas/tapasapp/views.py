from django.shortcuts import render, redirect, get_object_or_404
from .models import Account 
from django.contrib import messages
# Create your views here.

"""
def better_menu(request):
    dish_objects = Dish.objects.all()
    return render(request, 'tapasapp/better_list.html', {'dishes':dish_objects})

def add_menu(request):
    if(request.method=="POST"):
        dishname = request.POST.get('dname')
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.create(name=dishname, cook_time=cooktime, prep_time=preptime)
        return redirect('better_menu')
    else:
        return render(request, 'tapasapp/add_menu.html')
    

    
def view_detail(request, pk):
    d = get_object_or_404(Dish, pk=pk)
    return render(request, 'tapasapp/view_detail.html', {'d': d})

def delete_dish(request, pk):
    Dish.objects.filter(pk=pk).delete()
    return redirect('better_menu')

def update_dish(request, pk):
    if(request.method=="POST"):
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.filter(pk=pk).update(cook_time=cooktime, prep_time=preptime)
        return redirect('view_detail', pk=pk)
    else:
        d = get_object_or_404(Dish, pk=pk)
        return render(request, 'tapasapp/update_menu.html', {'d':d})
    
"""
def basic_list(request):
    acct_objects = Account.objects.all()
    print(acct_objects)
    return render(request, 'tapasapp/basic_list.html', {'Account':acct_objects})

def login(request):
    if(request.method=="POST"):
        varname = request.POST.get('dname')
        varpassword = request.POST.get('dpassword')
        #if it filters for specific values and the queryset is zero length then loads an error
        if len(Account.objects.filter(name=varname,password=varpassword)) == 0:
            messages.error(request, 'No such Account and Password')
            return redirect('login')
        #else it sends you to basiclist
        else:
            return redirect('basic_list')
        
    else:
        return render(request, 'tapasapp/login.html')
    
def signup(request):
    if(request.method=="POST"):
        varname = request.POST.get('dname')
        varpassword = request.POST.get('dpassword')
        Account.objects.create(name=varname,password=varpassword)
        return redirect('login')
    else:
        return render(request, 'tapasapp/signup.html')
    
def manage_account(request,pk):
    d = get_object_or_404(Account, pk=pk)
    return render(request, 'tapasapp/manage_account.html', {'d': d})

def change_password(request,pk):
    if(request.method=="POST"):
        varname = request.POST.get('dname')
        newpassword = request.POST.get('dnewpassword')
        oldpassword = request.POST.get('dpassword')
        if Account.objects.filter(name=varname,password=oldpassword) == '':
            messages.error(request, 'Wrong old password')
            redirect('change_password', pk=pk)
        else:
            Account.objects.filter(pk=pk).update(password = newpassword)
            redirect('manage_account', pk=pk)
    else:
        d = get_object_or_404(Account,pk=pk)
        return render(request, 'tapasapp/signup.html', {'d':d})
    
def yehey(request):
    return render(request,'tapasapp/yehey.html')

