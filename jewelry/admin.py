from django.contrib import admin
from .models import Jewelry, Collection, Production, Sketch, About, Order, QA, Contact, MyAccount, Goods

admin.site.register(Jewelry)
admin.site.register(Collection)
admin.site.register(Production)
admin.site.register(Sketch)
admin.site.register(About)
admin.site.register(Order)
admin.site.register(QA)
admin.site.register(Contact)
admin.site.register(Goods)
# admin.site.register(MyAccount)


# class MyModelAdmin(admin.ModelAdmin):
#
#     search_fields = ('name', 'length')
#
#
# admin.site.register(Jewelry, MyModelAdmin)

