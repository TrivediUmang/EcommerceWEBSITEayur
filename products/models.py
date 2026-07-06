from django.db import models


# ================= CATEGORY MODEL =================

class Category(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


# ================= PRODUCT MODEL =================

class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=200
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# ================= BLOG MODEL =================

class Blog(models.Model):

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True
    )

    image = models.ImageField(
        upload_to="blogs/"
    )

    short_description = models.CharField(
        max_length=300
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
    # ================= CONTACT MODEL =================

class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name