from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType


class Jewelry(models.Model):

    name = models.CharField(max_length=250, default='null')
    length = models.CharField(max_length=250, default='null')
    width = models.CharField(max_length=250, default='null')
    thickness = models.CharField(max_length=250, default='null')
    weight = models.CharField(max_length=250, default='null')
    category = models.CharField(max_length=250, default='null')
    image = models.ImageField(upload_to='upload/%Y/%m/%d', default='null')

    def __str__(self):
        return self.name


class Collection(models.Model):

    name = models.CharField(max_length=250, default='null')
    image = models.ImageField(upload_to='collection/%Y/%m/%d', default='null')

    def __str__(self):
        return self.name


class Production(models.Model):

    name = models.CharField(max_length=250, default='null')
    content = models.CharField(max_length=250, default='null')
    idea = models.TextField(max_length=1000, default='null')
    image1 = models.ImageField(upload_to='production/%Y/%m/%d', default='null')
    image2 = models.ImageField(upload_to='production/%Y/%m/%d', default='null')
    background = models.ImageField(upload_to='production/%Y/%m/%d', default='null')
    remark = models.TextField(max_length=1000, default='null')

    def __str__(self):
        return self.name


class Sketch(models.Model):

    image = models.ImageField(upload_to='production/%Y/%m/%d', default='null')


class About(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField(max_length=1000, default='null')
    image = models.ImageField(upload_to='production/%Y/%m/%d', default='null')

    def __str__(self):
        return self.title


class Order(models.Model):

    title = models.CharField(max_length=250, blank=True, default='null')
    content = models.TextField(max_length=1000, default='null')

    def __str__(self):
        return self.title


class QA(models.Model):

    title = models.CharField(max_length=250, default='null')
    content = models.TextField(max_length=1000, default='null')

    def __str__(self):
        return self.title


class Contact(models.Model):

    image = models.ImageField(upload_to='production/%Y/%m/%d', default='null')
    serviceEmail = models.CharField(max_length=250, default='null')
    servicePhone = models.CharField(max_length=250, default='null')

    def __str__(self):
        return self.serviceEmail


class Goods(models.Model):

    name = models.CharField(max_length=250, blank=True, default='')
    price = models.IntegerField(blank=True, default=0)
    originalPrice = models.IntegerField(blank=True, default=0)
    image = models.ImageField(upload_to='production/%Y/%m/%d', default='', blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name


class MyAccount(models.Model):

    clothes_ids = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='clothes_goods', blank=True, default=1)
    hoodies_ids = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='hoodies_goods', blank=True, default=1)
    Tshirts_ids = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='Tshirts_goods', blank=True, default=1)
    music_ids = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='music_goods', blank=True, default=1)
    posters_ids = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='posters_goods', blank=True, default=1)
    uncategorized_ids = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='uncategorized_goods', blank=True, default=1)


class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-creation_date',)

    def __unicode__(self):
        return unicode(self.creation_date)


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_('cart'), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='content_type')
    object_id = models.PositiveIntegerField()
    image = models.ImageField(upload_to='production/%Y/%m/%d', default='', blank=True)


    objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)
