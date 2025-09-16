from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from backend.models import AdCategory, MusicAd, Watchlist, WatchlistItem, AdCategoryLink
import random
from decimal import Decimal
from faker import Faker
import hashlib

# Import the CATEGORIES_DATA from your data file
from backend.management.data.data import CATEGORIES_DATA

class Command(BaseCommand):
    help = 'Populates the database with a specified number of randomly generated entries, clearing old data first.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            help='Number of users to create',
            default=5
        )
        parser.add_argument(
            '--ads',
            type=int,
            help='Number of ads to create',
            default=10
        )
        parser.add_argument(
            '--no-clear',
            action='store_true',
            help='Do not clear existing data before populating.'
        )

    def handle(self, *args, **options):
        self.stdout.write('Starting data population...')
        
        # Check if the --no-clear flag is present
        if not options['no_clear']:
            self.stdout.write('Clearing old data...')
            self.clear_old_data()
            self.stdout.write('Old data cleared.')

        # Get command-line arguments
        num_users = options['users']
        num_ads = options['ads']

        # Get the User model
        User = get_user_model()
        
        # Initialize Faker
        fake = Faker()

        # Create test data
        self.create_test_data(User, fake, num_users, num_ads)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully populated with {num_users} users and {num_ads} ads!'))

    def clear_old_data(self):
        """
        Deletes all existing data from the models.
        """
        # Deleting dependent models first to avoid integrity errors
        WatchlistItem.objects.all().delete()
        Watchlist.objects.all().delete()
        AdCategoryLink.objects.all().delete()
        MusicAd.objects.all().delete()
        AdCategory.objects.all().delete()
        # Delete users, but exclude the superuser if one exists
        User = get_user_model()
        User.objects.filter(is_superuser=False).delete()

    def create_test_data(self, User, fake, num_users, num_ads):
        # Create users
        self.stdout.write(f'Creating {num_users} users...')
        users = []
        for i in range(num_users):
            first_name = fake.first_name()
            last_name = fake.last_name()
            # Add a unique hash to prevent username collisions from Faker
            username = f"{first_name.lower()}.{last_name.lower()}{random.randint(1000, 9999)}"
            email = f"{username}@example.com"
            
            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password('testpass123')
            user.save()
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')
        
        # Create categories (using the list from data.py)
        self.stdout.write('Creating categories...')
        categories = []
        for cat_name in CATEGORIES_DATA:
            category = AdCategory.objects.create(
                category_name=cat_name,
                description=f'{cat_name} category'
            )
            categories.append(category)
            self.stdout.write(f'Created category: {category.category_name}')
        
        # Create music ads
        self.stdout.write(f'Creating {num_ads} ads...')
        ads = []
        conditions = ['M', 'NM', 'EX', 'VG', 'G', 'P']
        for i in range(num_ads):
            ad_user = random.choice(users)
            
            title = fake.sentence(nb_words=5).rstrip('.')
            description = fake.paragraph(nb_sentences=3)
            price = Decimal(random.randint(5, 200)) + Decimal(random.randint(0, 99)) / 100
            condition = random.choice(conditions)

            ad = MusicAd.objects.create(
                title=title,
                description=description,
                price=price,
                condition=condition,
                user=ad_user
            )
            ads.append(ad)
            
            random_categories = random.sample(categories, random.randint(1, 3))
            for category in random_categories:
                AdCategoryLink.objects.create(ad=ad, category=category)
            
        self.stdout.write('Ads created successfully.')
        
        # Create watchlists for each user and add some ads
        self.stdout.write('Creating watchlists and populating them...')
        for user in users:
            watchlist = Watchlist.objects.create(user=user)
            
            ads_to_add = random.sample(ads, random.randint(1, min(len(ads), 5)))
            for ad in ads_to_add:
                WatchlistItem.objects.create(watchlist=watchlist, ad=ad)
            
        self.stdout.write('Watchlists populated successfully.')