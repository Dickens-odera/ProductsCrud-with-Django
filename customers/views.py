from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customers
from .forms import CustomerForm
#UserRegistration
# Create your views here.
""" def index(request):
    template = 'customers/index.html'
    context = locals()
    return render(request,template, context)
 """
def index(request):
    return HttpResponse("Hello Welcome to Django")


def ListCustomers(request):
    customers  = Customers.objects.all()
    context = {'customers': customers}
    template ='customers/index.html'

    return render(request, template, context)

def AddCustomer(request):
    template = 'customers/index.html'
    form = CustomerForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('list_customers')
    return render(request, template, context)

def UpdateCustomer(request, id):
    template = 'customers/update.html'
    customers = Customers.objects.get(id = id)
    if request.method == 'POST':
            form = CustomerForm(request.POST or None, instance=customers)
            context = {'customers':customers, 'form':form}
            if form.is_valid():
                form.save()
                return redirect('list_customers')
    return render(request, template,context)

""" def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if  form.is_valid():
            new_user = form.save(commit = False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
    else:
        form =  UserRegistration()
        context = {'form':form}
        template = 'customers/register.html'
        return render(request, template, context) """
