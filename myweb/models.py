from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('living', 'Living Room Furniture'),
        ('office', 'Office Furniture'),
        ('bedroom', 'Bedroom Furniture'),
        ('kitchen', 'Kitchen Furniture'),
        ('other', 'Other products'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    in_stock = models.BooleanField(default=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    main_image = models.ImageField(upload_to='products/main/')
    preview_image1 = models.ImageField(upload_to='products/previews/', blank=True, null=True)
    preview_image2 = models.ImageField(upload_to='products/previews/', blank=True, null=True)
    preview_image3 = models.ImageField(upload_to='products/previews/', blank=True, null=True)
    preview_image4 = models.ImageField(upload_to='products/previews/', blank=True, null=True)

    def __str__(self):
        return self.name

class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.product.name} at {self.created_at.strftime('%Y-%m-%d %H:%M')}"



from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
