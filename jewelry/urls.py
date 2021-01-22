from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

# def i18n_javascript(request):
#
#     return admin.site.i18n_javascript(request)


app_name = 'jewelry'
urlpatterns = [
    path('jewelry/', views.jewelry_list, name='jewelry_list'),
    path('collection/', views.collection_list, name='collection_list'),
    path('production/', views.production_list, name='production_list'),
    path('sketch/', views.sketch_list, name='sketch_list'),
    path('about/', views.about_list, name='about_list'),
    path('order/', views.order_list, name='order_list'),
    path('qa/', views.qa_list, name='qa_list'),
    path('contact/', views.contact_list, name='contact_list'),
    path('myaccount/', views.myaccount_list, name='myaccount'),
    path('clothing/', views.clothing_list, name='clothing_list'),
    path('hoodies/', views.hoodies_list, name='hoodies_list'),
    path('T-shirts/', views.Tshirts_list, name='Tshirts_list'),
    path('music/', views.music_list, name='music_list'),
    path('posters/', views.posters_list, name='posters_list'),
    # path('search/', include('haystack.urls')),
    # url(r'^admin/jsi18n', i18n_javascript),
    # url(r'^admin/', admin.site.urls),
    # path('filter/<str:tag_slug>/', views.test_list, name='test_list'),
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<str:product_id>/<int:quantity>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('get_cart/', views.get_cart, name='get_cart'),
    path('myaccount/login/', auth_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),
    path('myaccount/logout/', auth_views.LogoutView.as_view(template_name='myweb/myaccount.html'), name='logout'),
    path('myaccount/register/', views.register, name='register'),
    path('myaccount/index/', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


