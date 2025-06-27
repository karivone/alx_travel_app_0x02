from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        titles = [
            "Cozy Beach Cottage",
            "Modern Apartment in City Center",
            "Quiet Mountain Cabin",
            "Luxury Downtown Loft",
            "Rustic Farmhouse"
        ]
        locations = ["Mombasa", "Nairobi", "Naivasha", "Nakuru", "Kisumu"]

        for i in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description="This is a sample description for the listing.",
                location=random.choice(locations),
                price_per_night=random.randint(50, 500),
                available=True
            )
        self.stdout.write(self.style.SUCCESS('✅ Sample listings created successfully.'))
