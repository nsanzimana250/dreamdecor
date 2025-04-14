from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductComment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock', 'display_main_image')
    readonly_fields = ['display_main_image', 'display_preview1', 'display_preview2', 'display_preview3', 'display_preview4']
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price', 'old_price', 'in_stock', 'category')
        }),
        ("Main Image", {
            'fields': ('main_image', 'display_main_image')
        }),
        ("Preview Images", {
            'fields': ('preview_image1', 'display_preview1',
                       'preview_image2', 'display_preview2',
                       'preview_image3', 'display_preview3',
                       'preview_image4', 'display_preview4')
        }),
    )

    def display_main_image(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="100" />', obj.main_image.url)
        return "-"
    display_main_image.short_description = 'Main Image'

    def display_preview1(self, obj):
        if obj.preview_image1:
            return format_html('<img src="{}" width="100" />', obj.preview_image1.url)
        return "-"
    display_preview1.short_description = 'Preview 1'

    def display_preview2(self, obj):
        if obj.preview_image2:
            return format_html('<img src="{}" width="100" />', obj.preview_image2.url)
        return "-"
    display_preview2.short_description = 'Preview 2'

    def display_preview3(self, obj):
        if obj.preview_image3:
            return format_html('<img src="{}" width="100" />', obj.preview_image3.url)
        return "-"
    display_preview3.short_description = 'Preview 3'

    def display_preview4(self, obj):
        if obj.preview_image4:
            return format_html('<img src="{}" width="100" />', obj.preview_image4.url)
        return "-"
    display_preview4.short_description = 'Preview 4'

class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at', 'content')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductComment, ProductCommentAdmin)



from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at','message')
    search_fields = ('name', 'email', 'subject', 'message')
