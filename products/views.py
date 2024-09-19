from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F


from .models import Product, ProductAttachment, Review, Vendor, CategoryChoices, Cart, CartItem


def index(request):
    products = Product.objects.select_related('vendor').prefetch_related('reviews')
    context = {'products': products}
    return render(request, 'index.html', context=context)


def product_detail(request, handle):
    product = get_object_or_404(Product, handle=handle)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
    could_review = None
    if request.user.is_authenticated:
        could_review = not Review.objects.filter(product=product, owner=request.user.profile).exists()
    context = {'product': product, 'related_products': related_products, 'could_review': could_review}
    return render(request, 'product.html', context=context)


def attachment_download(request, handle, pk):
    attachment = get_object_or_404(ProductAttachment, product__handle=handle, pk=pk)
    image = attachment.image.open(mode='rb')
    filename = attachment.image.name

    response = FileResponse(image)
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = f'attachment;filename={filename}'
    return response

def product_download(request, handle):
    product = get_object_or_404(Product, handle=handle)
    image = product.image    
    filename = image.name

    response = FileResponse(image)
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = f'attachment;filename={filename}'
    return response


@login_required
def cart(request):
    cart = get_object_or_404(Cart, owner=request.user.profile)
    items = CartItem.objects.filter(cart=cart)
    context = {'items': items, 'cart': cart}
    return render(request, 'cart.html', context=context)


def shop(request):
    products = Product.objects.all()
    vendors = Vendor.objects.all()
    categories = CategoryChoices.choices
    context = {'products': products, 'categories': categories, 'vendors': vendors}
    return render(request, 'shop.html', context=context)

def category(request, category):
    category = CategoryChoices(category)
    products = Product.objects.filter(category=category)
    context = {'products': products, 'category': category}
    return render(request, 'category.html', context=context)

def categories_list(request):
    categories = Product.objects.values('category').annotate(num_products=Count('pk'))
    for item in categories:
        item['category_name'] = CategoryChoices(item['category']).label
        item['category_db'] = item['category']
        del item['category']
    context = {'categories': categories}
    return render(request, 'categories-list.html', context=context)

def wishlist(request):
    return render(request, 'wishlist.html')

