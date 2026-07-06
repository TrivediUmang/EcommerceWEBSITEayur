from django.core.management.base import BaseCommand
from products.models import Product
from django.core.files import File
import os


class Command(BaseCommand):
    help = "Assign images to products"

    def handle(self, *args, **kwargs):

        media_path = "media/products"

        products = Product.objects.all().order_by("id")

        for index, product in enumerate(products, start=1):

            image_name = f"product_{index:02}.png"

            image_path = os.path.join(media_path, image_name)

            if os.path.exists(image_path):

                with open(image_path, "rb") as img:

                    product.image.save(image_name, File(img), save=True)

                    self.stdout.write(f"✅ {product.name} -> {image_name}")

            else:

                self.stdout.write(f"❌ {image_name} not found")

        self.stdout.write(
            self.style.SUCCESS("🎉 All Images Assigned Successfully")
        )