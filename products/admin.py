from django.contrib import admin
from .models import Product, Variation, ProductImage, Category, ProductFeatured, Wish, WishItem
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import ImageField

class ProductImageAdmin(AdminImageMixin, admin.ModelAdmin):
	list_display = ['product', 'image_img']

	class Meta:
		model = ProductImage

class ProductImageInline(AdminImageMixin, admin.TabularInline):
	model = ProductImage
	extra = 1
	max_num = 5
    

class VariationAdmin(admin.TabularInline):
	model = Variation
	extra = 0
	max_num = 10

class ProductAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'price', 'active']
	inlines = [
		VariationAdmin,
		ProductImageInline,
	]
	class Meta:
		model = Product

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model =  Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductFeatured)
admin.site.register(Wish)
admin.site.register(WishItem)
