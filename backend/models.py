# backend/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom User model extending Django's AbstractUser"""
    # Add any additional fields you might need later
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'users'

class AdCategory(models.Model):
    """Categories for music ads (e.g., Vinyl, CDs, Rock, Pop)"""
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'ad_categories'
        verbose_name_plural = "Ad Categories"
    
    def __str__(self):
        return self.category_name

class MusicAd(models.Model):
    """Music products being sold"""
    CONDITION_CHOICES = [
        ('M', 'Mint'),
        ('NM', 'Near Mint'),
        ('VG', 'Very Good'),
        ('G', 'Good'),
        ('F', 'Fair'),
        ('P', 'Poor'),
    ]
    
    ad_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=2, choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False)
    
    # Foreign key to User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='music_ads')
    
    # Many-to-many relationship with categories
    categories = models.ManyToManyField(AdCategory, through='AdCategoryLink', related_name='music_ads')
    
    class Meta:
        db_table = 'music_ads'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - ${self.price}"

class AdCategoryLink(models.Model):
    """Junction table for MusicAd and AdCategory many-to-many relationship"""
    ad = models.ForeignKey(MusicAd, on_delete=models.CASCADE)
    category = models.ForeignKey(AdCategory, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'ad_category_link'
        unique_together = ['ad', 'category']
    
    def __str__(self):
        return f"{self.ad.title} - {self.category.category_name}"

class Watchlist(models.Model):
    """User's watchlist/saved ads"""
    watchlist_id = models.AutoField(primary_key=True)
    
    # One-to-one relationship with User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='watchlist')
    
    # Many-to-many relationship with MusicAd through WatchlistItem
    ads = models.ManyToManyField(MusicAd, through='WatchlistItem', related_name='watchlists')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'watchlists'
    
    def __str__(self):
        return f"{self.user.username}'s Watchlist"

class WatchlistItem(models.Model):
    """Junction table for Watchlist and MusicAd many-to-many relationship"""
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    ad = models.ForeignKey(MusicAd, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'watchlist_items'
        unique_together = ['watchlist', 'ad']
    
    def __str__(self):
        return f"{self.watchlist.user.username} - {self.ad.title}"