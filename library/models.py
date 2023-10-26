from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User Model
# class User(models.Model):
#     computerNumber = models.CharField(max_length=50 , unique=True)
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=255)  # Store hashed and salted passwords
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
   

#     def __str__(self):
#         return self.username
    
# #Genre
# class Genre(models.Model):
#     genre = models.CharField(max_length=50, blank=True, null=True)
#     topic = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         name = self.genre
#         return name
    

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)
    book_picture = models.ImageField(upload_to='static/images', blank= True , null= True)



    def __str__(self):
        return self.title

# BorrowingHistory Model
class BorrowingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}  borrowed  {self.book}  on  {self.borrowed_date}"

# UserRecommendation Model
class UserRecommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)



# ForumPost Model
class ForumPost(models.Model):
    forumid = models.AutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=50, blank=True, null=True)
    # comment = models.CharField(max_length=255 , blank= True , null= True )

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"Name : {self.name} ,  Phone : {self.phone},  Email : {self.phone},  Message : {self.message}"

class Comments(models.Model):
    comments = models.CharField(max_length=255)
    forumid= models.ForeignKey(ForumPost ,on_delete=models.CASCADE , blank = True , null = True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.comments} by {self.user.username}"
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart Item: {self.book.title}"

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    computerNumber = models.CharField(max_length=50 , unique=True)
    

    def __str__(self):
        return f"{self.comments} by {self.user.username}"