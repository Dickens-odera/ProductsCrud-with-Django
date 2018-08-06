from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm
#Create your views here.
def list_products(request):
    products = Products.objects.all()
    template = 'products/index.html'
    context = {'products':products}
    return render(request, template, context)

def create_products(request):
    template = 'products/create.html'
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request,template,{'form':form})

def update_products(request, id):
    template = 'products/update.html'
    #context = locals()#should be deleted soe time later
    products = Products.objects.get(id = id)
    form = ProductForm(request.POST or None, instance = products)
    context = {'form':form,'products':products}
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request,template,context)

def delete_products(request, id):
    products = Products.objects.get(id = id)
    template = 'products/delete.html'
    context = locals()
    return render(request, template, context)
