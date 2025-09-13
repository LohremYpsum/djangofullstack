# backend/management/commands/populate_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from backend.models import AdCategory, MusicAd, Watchlist, WatchlistItem, AdCategoryLink
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Simple database population without external dependencies'

    def handle(self, *args, **options):
        self.stdout.write('Starting simple data population...')
        
        # Get the User model
        User = get_user_model()
        
        # Create some test data
        self.create_test_data(User)
        
        self.stdout.write(self.style.SUCCESS('Simple data population complete!'))

    def create_test_data(self, User):
        # Create a test user
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@example.com',
                'first_name': 'Test',
                'last_name': 'User',
                'password': 'testpass123'
            }
        )
        
        if created:
            self.stdout.write(f'Created test user: {user.username}')
        
        # Create categories
        categories = []
        for cat_name in ['Vinyl', 'CDs', 'Rock', 'Jazz']:
            category, created = AdCategory.objects.get_or_create(
                category_name=cat_name,
                defaults={'description': f'{cat_name} category'}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.category_name}')
        
        # Create a music ad
        ad = MusicAd.objects.create(
            title='The Beatles - Abbey Road (Vinyl)',
            description='Original pressing in excellent condition',
            price=Decimal('49.99'),
            condition='VG',
            user=user
        )
        
        # Add categories to ad
        for category in categories[:2]:  # Add first two categories
            AdCategoryLink.objects.create(ad=ad, category=category)
        
        self.stdout.write(f'Created ad: {ad.title} - ${ad.price}')
        
        # Create watchlist
        watchlist, created = Watchlist.objects.get_or_create(user=user)
        if created:
            self.stdout.write(f'Created watchlist for {user.username}')
        
        # Add ad to watchlist
        WatchlistItem.objects.create(watchlist=watchlist, ad=ad)
        self.stdout.write(f'Added ad to {user.username}\'s watchlist')