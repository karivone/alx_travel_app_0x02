from django.core.management.base import BaseCommand
from listings.models import Listing
from django.utils.crypto import get_random_string
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_locations = ['Paris', 'London', 'New York', 'Tokyo', 'Nairobi', 'Madrid']
        Listing.objects.all().delete()
        for _ in range(10):
            title = f"{get_random_string(5)} House"
            description = f"A lovely place in {random.choice(sample_locations)}"
            location = random.choice(sample_locations)
            price = round(random.uniform(50, 300), 2)
            Listing.objects.create(
                title=title,
                description=description,
                location=location,
                price_per_night=price,
                available=random.choice([True, False])
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded listings."))
