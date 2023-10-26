from django.contrib import admin
from django.utils import timezone  # Import the timezone module
from datetime import timedelta
from .models import  Book, BorrowingHistory, UserRecommendation, ForumPost , Comments , Contact , Profile , CartItem


# Register your models here.
# admin.site.register(Profile)

def approve_books(modeladmin, request, queryset):
    for cart_item in queryset:
        if cart_item.user.is_staff:  # Ensure that only admins can approve books
            # Create a new entry in BorrowingHistory for the approved book
            BorrowingHistory.objects.create(
                user=cart_item.user,
                book=cart_item.book,
                borrowed_date=timezone.now(),  # Adjust the date as needed
                due_date=timezone.now() + timedelta(days=30),  # Set a due date
            )
            cart_item.delete()  # Remove the book from the cart

approve_books.short_description = "Approve selected books and move to Borrowing History"

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    actions = [approve_books]  # Add the custom action to the admin interface


@admin.register(Book)
class Book(admin.ModelAdmin):
    search_fields = ['title', 'author', 'genre']

@admin.register(BorrowingHistory)
class BorrowingHistory(admin.ModelAdmin):
    search_fields = ['user', 'book', 'borrowed_date', 'due_date', 'return_date']


@admin.register(ForumPost)
class ForumPost(admin.ModelAdmin):
    search_fields = ['title', 'user', 'contect', 'timestamp', 'topic']


@admin.register(Comments)
class Comments(admin.ModelAdmin):
    search_fields = [ 'user', 'comments']


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    search_fields = [ 'name', 'phone', 'email', 'message']


