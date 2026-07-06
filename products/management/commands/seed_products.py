from django.core.management.base import BaseCommand
from products.models import Category, Product
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Seed Categories and Products"

    def handle(self, *args, **kwargs):

        categories = {
            "Hair Care": [
                ("Onion Hair Oil", 499),
                ("Bhringraj Hair Oil", 549),
                ("Hair Growth Serum", 699),
            ],

            "Skin Care": [
                ("Aloe Vera Gel", 299),
                ("Neem Face Wash", 249),
                ("Herbal Face Pack", 399),
            ],

            "Immunity": [
                ("Giloy Juice", 349),
                ("Tulsi Drops", 199),
                ("Chyawanprash", 599),
            ],

            "Wellness": [
                ("Herbal Tea", 299),
                ("Organic Turmeric Powder", 399),
                ("Ashwagandha Capsules", 699),
            ],

            "Digestive Care": [
                ("Triphala Powder", 299),
                ("Digestive Tea", 249),
            ],

            "Personal Care": [
                ("Neem Soap", 199),
                ("Charcoal Soap", 229),
                ("Herbal Tooth Powder", 179),
            ],

            "Essential Oils": [
                ("Lavender Essential Oil", 599),
                ("Tea Tree Oil", 649),
            ],

            "Men's Care": [
                ("Beard Growth Oil", 449),
                ("Energy Booster", 799),
            ],

            "Women's Care": [
                ("PCOS Herbal Tea", 499),
                ("Iron Tonic", 399),
            ],

            "Kids Care": [
                ("Kids Immunity Syrup", 349),
                ("Baby Massage Oil", 299),
            ],
        }

        for category_name, products in categories.items():

            # Category create karega agar nahi hai
            category, created = Category.objects.get_or_create(
                name=category_name,
                defaults={
                    "slug": slugify(category_name)
                }
            )

            for name, price in products:

                Product.objects.get_or_create(
                    name=name,
                    defaults={
                        "category": category,
                        "price": price,
                        "description": f"{name} made with premium Ayurvedic ingredients."
                    }
                )

        self.stdout.write(
            self.style.SUCCESS("✅ Categories & Products Added Successfully")
        )