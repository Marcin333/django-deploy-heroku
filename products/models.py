from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from sorl.thumbnail import ImageField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify

class ProductQuerySet(models.query.QuerySet): # define which product queryset is True, is active.
    def active(self):
		return self.filter(active=True)

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self, *args, **kwargs):
		return self.get_queryset().active()

	def get_related(self, instance):
		products_one = self.get_queryset().filter(categories__in=instance.categories.all())
		products_two = self.get_queryset().filter(default=instance.default)
		qs = (products_one | products_two).exclude(id=instance.id).distinct()
		return qs

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', blank=True)
    default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)

    objects = ProductManager()

    class Meta:
        ordering = ['-title']

    def __unicode__(self):
        return self.title

    def get_absolute_url(   self):
        return reverse('product_detail', kwargs={'pk':self.pk})

    def get_image_url(self):
        img = self.productimage_set.first()
        if img:
            return img.image.url
        return img

    def product_slug(self):
        slug = slugify(self.title)
        return slug

class Variation(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True) # -1 means unlimited

    def __unicode__(self):
        return self.title

    def get_html_price(self):
        if self.sale_price is not None:
        	html_text = "<h4 id='price-home'><span>&pound;%s</span><span class='sale-price'>&nbsp;&pound;%s</span></h4>\
             " %(self.sale_price, self.price)
        else:
        	html_text = "<h4 id='price'><span>&pound;%s</span></h4>" %(self.price)
        return mark_safe(html_text)
        # return mark_safe(html_text)

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def add_to_cart(self):
        return '{0}?item={1}&qty=1'.format(reverse('cart', self.id))

    def remove_form_cart(self):
        return '{0}?item={1}&qty=1&delete=true'.format(reverse('cart'), self.id)

    def get_title(self):
        return '{0} - {1}'.format(self.product.title, self.title)

    def add_to_wish_list(self):
        return '{0}?item={1}&add_to_wish_list=true'.format(reverse('cart'), self.id)

def product_post_save_receiver(sender, instance, created, *args, **kwargs):
    # print sender -->  <class 'products.models.Product'>
    # print instance --> T-shirt
    # print created --> True
    product = instance
    variation = product.variation_set.all()
    # variation = Variation.objects.filter(product=product) # Equivalent of variation above
    if variation.count() == 0:
        new_variation = Variation()
        new_variation.product = product
        new_variation.title = 'Default'
        new_variation.price = product.price
        new_variation.save()
        # print new_variation

post_save.connect(product_post_save_receiver, sender=Product)

def image_upload(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    file_extension = filename.split('.')[1]
    new_image_name = '{0}.{1}'.format(instance.id, file_extension)
    return "products/{0}/{1}".format(slug, new_image_name)

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=image_upload)

    def __unicode__(self):
        return self.product.title

    def image_img(self):
	    if self.image:
	        return u'<img src="%s" height="125" width="125"/>' % self.image.url
	    else:
	        return '(Image is not available)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

def image_upload_featured(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    file_extenction = filename.split('.')[1]
    new_image_name = '{0}/{1}.{2}'.format(slug, instance.id, file_extenction)
    return 'products/{0}/featured/{1}'.format(slug, new_image_name)

class ProductFeatured(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to=image_upload_featured)
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.CharField(max_length=120, null=True, blank=True)
    text_css_color = models.CharField(max_length=12, null=True, blank=True)
    text_right = models.BooleanField(default=False)
    make_image_background = models.BooleanField(default=False)
    show_price = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.product.title
    
class WishItem(models.Model):
    wish = models.ForeignKey("Wish")
    item = models.ForeignKey(Variation)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return str(self.item.product)

class Wish(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    items = models.ManyToManyField(Variation, through=WishItem)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return str(self.id)