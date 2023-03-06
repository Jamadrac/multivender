from django.shortcuts import render

from store.models import Product, Category

def frontpage(request):
      #return httpresponse(dfghjklkjhgfd)
  #  products = Product.objects.filter(status=Product.ACTIVE)[0:6]
    products = Product.objects.all()
    category = Category.objects.all()

    return render(request, 'core/frontpage.html', {
        'products': products,'categories':category
    })

def about(request):
    #return httpresponse(dfghjklkjhgfd)
    return render(request, 'core/about.html')