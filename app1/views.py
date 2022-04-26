from django.shortcuts import render, redirect
from django.shortcuts import get_list_or_404
from app1.models import PasswordModel


def add_userpassword(request):
    if request.method == 'POST':
            title= request.POST['title']
            username= request.POST['username']
            password= request.POST['password']
            p = PasswordModel(title= title, username= username, password= password)
            p.save()
            return redirect('list')
        
    return render(request, 'app1/add-edit.html')



def password_list(request):
    context = {
        'passwords': PasswordModel.objects.all(),
    }
    return render(request, 'app1/list.html', context)


def details_userpassword(request, pk):
    context = {
        'details': get_list_or_404(PasswordModel, id=pk),
    }
    return render(request, 'app1/details.html', context)



def edit_userpassword(request, pk):
    if request.method == 'POST':
        obj = PasswordModel.objects.get(id=pk)
        obj.title= request.POST['title']
        obj.username= request.POST['username']
        obj.password= request.POST['password']
        obj.save()
        return redirect('list')
        
    context = {
        'edit': get_list_or_404(PasswordModel, id=pk),
    }
    return render(request, 'app1/add-edit.html', context)


def delete_userpassword(request, pk):
    if request.method == 'POST':
        obj = emp = Employee.objects.get(pk = id)
        obj.delete()
        return redirect('list')
    
    context = {
        'delete': get_list_or_404(PasswordModel, id=pk),
    }
    return render(request, 'app1/delete.html', context)

