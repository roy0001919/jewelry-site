from django.shortcuts import render
from .models import Jewelry, Collection, Production, Sketch, About, Order, QA, Contact, MyAccount, Goods, Item
from .form import ItemForm
from django.contrib import admin
from taggit.models import Tag
from django.http import HttpResponse
from .cart import Cart
# from cart.models import Item
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



def jewelry_list(request):
    jewelries = Jewelry.objects.all()

    return render(
        request,
        'myweb/jewelry.html',
        {'jewelries': jewelries},
    )


def collection_list(request):
    collections = Collection.objects.all()

    return render(
        request,
        'myweb/collection.html',
        {'collections': collections},
    )


def production_list(request):
    productions = Production.objects.all()

    return render(
        request,
        'myweb/production.html',
        {'productions': productions},
    )


def sketch_list(request):
    sketches = Sketch.objects.all()

    return render(
        request,
        'myweb/sketch.html',
        {'sketches': sketches},
    )


def about_list(request):
    abouts = About.objects.all()

    return render(
        request,
        'myweb/about.html',
        {'abouts': abouts},
    )


def order_list(request):
    orders = Order.objects.all()

    return render(
        request,
        'myweb/order.html',
        {'orders': orders},
    )


def qa_list(request):
    qas = QA.objects.all()

    return render(
        request,
        'myweb/QA.html',
        {'qas': qas},
    )


def contact_list(request):
    contacts = Contact.objects.all()

    return render(
        request,
        'myweb/contact.html',
        {'contacts': contacts},
    )


def myaccount_list(request):
    myaccounts = MyAccount.objects.all()

    return render(
        request,
        'myweb/myaccount.html',
        {'myaccounts': myaccounts},
    )


def clothing_list(request):
    filter = request.GET.get('orderby')
    # tag = Tag.objects.filter(slug='clothing').first()
    # goods = Goods.objects.filter(tags__in=[tag])
    # for good in goods:
    #     if good.discount!=0:
    if filter == 'price':
        tag = Tag.objects.filter(slug='clothing').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('price')
    elif filter == 'price-desc':
        tag = Tag.objects.filter(slug='clothing').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('-price')
    else:
        tag = Tag.objects.filter(slug='clothing').first()
        goods = Goods.objects.filter(tags__in=[tag])

    return render(
        request,
        'myweb/clothing.html',
        {'goods': goods},
    )


def hoodies_list(request):
    filter = request.GET.get('orderby')

    if filter == 'price':
        tag = Tag.objects.filter(slug='hoodies').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('price')
    elif filter == 'price-desc':
        tag = Tag.objects.filter(slug='hoodies').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('-price')
    else:
        tag = Tag.objects.filter(slug='hoodies').first()
        goods = Goods.objects.filter(tags__in=[tag])

    return render(
        request,
        'myweb/hoodies.html',
        {'goods': goods},
    )


def Tshirts_list(request):
    filter = request.GET.get('orderby')

    if filter == 'price':
        tag = Tag.objects.filter(slug='tshirt').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('price')
    elif filter == 'price-desc':
        tag = Tag.objects.filter(slug='tshirt').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('-price')
    else:
        tag = Tag.objects.filter(slug='tshirt').first()
        goods = Goods.objects.filter(tags__in=[tag])

    return render(
        request,
        'myweb/Tshirts.html',
        {'goods': goods},
    )


def music_list(request):
    filter = request.GET.get('orderby')

    if filter == 'price':
        tag = Tag.objects.filter(slug='music').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('price')
    elif filter == 'price-desc':
        tag = Tag.objects.filter(slug='music').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('-price')
    else:
        tag = Tag.objects.filter(slug='music').first()
        goods = Goods.objects.filter(tags__in=[tag])

    return render(
        request,
        'myweb/music.html',
        {'goods': goods},
    )


def posters_list(request):
    filter = request.GET.get('orderby')

    if filter == 'price':
        tag = Tag.objects.filter(slug='posters').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('price')
    elif filter == 'price-desc':
        tag = Tag.objects.filter(slug='posters').first()
        goods = Goods.objects.filter(tags__in=[tag]).order_by('-price')
    else:
        tag = Tag.objects.filter(slug='posters').first()
        goods = Goods.objects.filter(tags__in=[tag])

    return render(
        request,
        'myweb/posters.html',
        {'goods': goods},
    )


# def haystack_search(request):
#     myaccounts = MyAccount.objects.all()
#
#     return render(
#         request,
#         'search/search.html',
#         {'myaccounts': myaccounts},
#     )



# def i18n_javascript(request):
#
#     return admin.site.i18n_javascript(request)

def home(request):


    return render(
        request,
        'myweb/home.html',
        {
         },
    )

def cart(request,good_id=None):


    return render(
        request,
        'myweb/cart.html',
        {
         },
    )

def test(request):


    return render(
        request,
        'myweb/test.html',
        {
         },
    )

def test2(request):


    return render(
        request,
        'myweb/test2.html',
        {
         },
    )


def add_to_cart(request, product_id, quantity):
    goods = Goods.objects.get(id=product_id)
    cart_request = Cart(request)
    cart_request.add(goods, goods.price, quantity, goods.image)
    return redirect(request.META['HTTP_REFERER'])


def remove_from_cart(request, product_id):
    goods = Goods.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(goods)
    return render(request, 'myweb/cart.html', {'cart': Cart(request)})


def get_cart(request):
    items = Item.objects.all()
    goods_num = Goods.objects.count()
    total = 0
    for i in items:
        total += int(i.quantity)*int(i.unit_price)

    if request.method == 'POST':
        total = 0
        for i in range(1, goods_num):
            mess = request.POST.get('quantity'+str(i), False)
            if mess != False:
                items = Item.objects.filter(object_id=i).first()
                items.quantity = mess
                items.save()
                total += int(items.quantity)*int(items.unit_price)

    return render(request, 'myweb/cart.html', {'cart': Cart(request), 'total': total})


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(
                request,
                'myweb/index.html',
                {'new_user': new_user}
            )
    else:
        user_form = UserCreationForm()
    return render(
        request,
        'myweb/register.html',
        {'user_form': user_form}
    )


def index(request):
    return render(
        request,
        'myweb/index.html',
        {},
    )