from decimal import Decimal

# User data
USERS_DATA = [
    {'username': 'testuser', 'email': 'test@example.com', 'first_name': 'Test', 'last_name': 'User'},
    {'username': 'jane.doe', 'email': 'jane.doe@example.com', 'first_name': 'Jane', 'last_name': 'Doe'},
    {'username': 'john.smith', 'email': 'john.smith@example.com', 'first_name': 'John', 'last_name': 'Smith'},
    {'username': 'susan.b', 'email': 'susan.b@example.com', 'first_name': 'Susan', 'last_name': 'Bates'},
    {'username': 'mike.jones', 'email': 'mike.jones@example.com', 'first_name': 'Mike', 'last_name': 'Jones'},
]

# Category data
CATEGORIES_DATA = [
    'Vinyl', 'CDs', 'Rock', 'Jazz', 'Pop', 'Hip-Hop', 'Electronic'
]

# Music Ad data
ADS_DATA = [
    {'title': 'The Beatles - Abbey Road (Vinyl)', 'description': 'Original pressing in excellent condition', 'price': Decimal('49.99'), 'condition': 'VG'},
    {'title': 'Pink Floyd - The Dark Side of the Moon (Vinyl)', 'description': 'Classic rock masterpiece on vinyl', 'price': Decimal('35.50'), 'condition': 'NM'},
    {'title': 'Michael Jackson - Thriller (CD)', 'description': 'The best-selling album of all time', 'price': Decimal('15.00'), 'condition': 'EX'},
    {'title': 'Miles Davis - Kind of Blue (Vinyl)', 'description': 'Essential jazz record, great condition', 'price': Decimal('25.75'), 'condition': 'NM'},
    {'title': 'Radiohead - OK Computer (CD)', 'description': 'Includes all original liner notes', 'price': Decimal('12.99'), 'condition': 'G'},
    {'title': 'Taylor Swift - 1989 (Vinyl)', 'description': 'Sealed copy of the pop hit album', 'price': Decimal('29.99'), 'condition': 'M'},
    {'title': 'Kendrick Lamar - To Pimp a Butterfly (Vinyl)', 'description': 'Critically acclaimed hip-hop album', 'price': Decimal('38.00'), 'condition': 'VG'},
    {'title': 'Daft Punk - Discovery (CD)', 'description': 'Iconic electronic music album', 'price': Decimal('19.99'), 'condition': 'EX'},
    {'title': 'Queen - A Night at the Opera (Vinyl)', 'description': 'Bohemian Rhapsody and more!', 'price': Decimal('45.00'), 'condition': 'VG'},
    {'title': 'Nirvana - Nevermind (CD)', 'description': 'Grunge classic', 'price': Decimal('10.50'), 'condition': 'EX'},
]