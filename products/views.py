from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required

# ১. হোম পেজ - পণ্য দেখা এবং নতুন পণ্য যোগ করা (Read & Create)
@login_required
def index(request):
    if request.method == "POST":
        p_name = request.POST.get('name')
        p_price = request.POST.get('price')
        p_desc = request.POST.get('description')
        
        # ডাটাবেজে সেভ করা
        Product.objects.create(name=p_name, price=p_price, description=p_desc)
        return redirect('home')

    # সব পণ্য নতুন থেকে পুরাতন ক্রমে সাজিয়ে আনা
    all_products = Product.objects.all().order_by('-id')
    return render(request, 'index.html', {'products': all_products})

# ২. পণ্য মুছে ফেলার ফাংশন (Delete)
@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('home')

# ৩. পণ্য এডিট করার ফাংশন (Update)
@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    
    if request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.save() # পরিবর্তনগুলো সেভ করা
        return redirect('home')

    return render(request, 'edit.html', {'product': product})