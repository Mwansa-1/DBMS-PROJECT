from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
import static

urlpatterns = [
    path("", views.index, name = "index"),
    path("books", views.books, name = "books"),
    path("forum", views.forum, name = "forum"),
    path("profile", views.profile, name = "profile"),
    path("addforum", views.addforum, name = "addforum"),
    path("about", views.about, name = "about"),
    path("contact", views.contact_view, name = "contact"),
    path('cart/', views.view_cart, name='view_cart'),
    path('borrow_books/', views.borrow_books, name='borrow_books'),
    path('view_borrowing_history/', views.view_borrowing_history, name='view_borrowing_history'),
    path('search/', views.search, name='search'),
    path('search_forum/', views.search_forum, name='search_forum'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path("book_details/<int:id>", views.book_details, name = "book_details"),
    path("forum_details/<int:id>", views.forum_details, name = "forum_details"),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    
    

    
]