from django.shortcuts import render

from django.shortcuts import render
from .models import Product
from .models import Product
from django.shortcuts import render, get_object_or_404
from .models import Product

from django.shortcuts import render
from .models import Product, ContactMessage

def home(request):
    new_products = Product.objects.all()
    more_products = Product.objects.all()[:12]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

    return render(request, 'index.html', {
        'new_products': new_products,
        'more_products': more_products
    })


from .models import Product, ProductComment  # Make sure ProductComment is imported

def product(request, id):
    product = get_object_or_404(Product, pk=id)
    image_url = request.build_absolute_uri(product.main_image.url)

    if request.method == 'POST':
        comment_content = request.POST.get('comment')
        if comment_content:
            ProductComment.objects.create(
                product=product,
                content=comment_content
            )

    comments = product.comments.order_by('-created_at') 

    return render(request, 'product.html', {
        'product': product,
        'image_url': image_url,
        'comments': comments,
    })



def store(request): 
    products = Product.objects.all()
    return render(request, 'store.html',{'products': products}) 


# select where product category = bedroom
def Bedroom_Furniture(request): 
    products = Product.objects.filter(category='bedroom')
    return render(request, 'Bedroom_Furniture.html', {'products': products}) 

# select where product category = kitchen
def Kitchen_Furniture(request): 
    products = Product.objects.filter(category='kitchen')
    return render(request, 'Kitchen_Furniture.html', {'products': products}) 

# select where product category = living
def Living_Room_Furniture(request): 
    products = Product.objects.filter(category='living')
    return render(request, 'Living_Room_Furniture.html', {'products': products}) 

# select where product category = office
def office_furnitures(request): 
    products = Product.objects.filter(category='office')
    return render(request, 'office_furnitures.html', {'products': products}) 


from .models import Product

def dashboald(request): 
    products = Product.objects.all()
    return render(request, 'dashboald/dashboald.html', {'products': products})

def campany(request): 
    products = Product.objects.all()
    return render(request, 'campany.html', {'products': products})


# campany
