from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime


def main(request):
    return render(request, 'main.html',)  # locals()


def testpage(request):
    return render_to_response('testpage.html')


def about(request):
    return render_to_response('about.html')


def contact(request):
    return render_to_response('contact.html')


def products(request):
    return render_to_response('products.html')


def tile(request):
    query = Product.objects.filter(flag=True)
    query_tile = query.filter(category__id=1)
    return render(request, 'prodlist.html', locals())


def board(request):
    query = Product.objects.filter(flag=True)
    query_tile = query.filter(category__id=2)
    return render(request, 'prodlist.html', locals())


def accessories(request):
    query = Product.objects.filter(flag=True)
    query_tile = query.filter(category__id=3)
    return render(request, 'prodlist.html', locals())


def drainage(request):
    query = Product.objects.filter(flag=True)
    query_tile = query.filter(category__id=4)
    return render(request, 'prodlist.html', locals())


def rollout(request):
    query = Product.objects.filter(flag=True)
    query_tile = query.filter(category__id=5)
    return render(request, 'prodlist.html', locals())


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', locals())