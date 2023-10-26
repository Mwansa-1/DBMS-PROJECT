from django.shortcuts import render , redirect , get_object_or_404
from .models import Book , ForumPost , User , Comments , Contact , CartItem ,BorrowingHistory , Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms
from django.utils import timezone
from .forms import SearchForm





# Create your views here.
def index(request):
    return render(request , "library/index.html",{
        "books" : Book.objects.all(),
        "forums" : ForumPost.objects.all()
    })

def about(request):
    return render(request , "library/about.html")

def books(request):
    return render(request , "library/books.html" ,{
        "books" : Book.objects.all()
    })

def book_details(request , id):
    
    return render(request , "library/book_details.html" ,{
        "book" : Book.objects.get(pk=id),
    })

def forum(request):
    return render(request , "library/forum.html",{
        "forums" : ForumPost.objects.all()
    })

@login_required(login_url='/accounts/login/')
def addforum(request):
     if request.method == 'POST' :
        form = forms.AddPost(request.POST)
        if form.is_valid():
            #save comment to db
            #get the id for the post and post on that id 
            
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            
            return redirect('forum') 
     else:
        form = forms.AddPost()
     return render(request , "library/addforum.html",{
        "form" : form   
    })

def contact_view(request):
     if request.method == 'POST' :
        form = forms.Contact(request.POST)
        if form.is_valid():
            #save comment to db
            #get the id for the post and post on that id 
            
            instance = form.save(commit=False)
            instance.save()
            
            return redirect('index') 
     else:
        form = forms.Contact()
     return render(request , "library/contact.html",{
        "form" : form
       
    })


def forum_details(request , id):
    if request.method == 'POST' :
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            #save comment to db
            #get the id for the post and post on that id 
            
            instance = form.save(commit=False)
            instance.user = request.user
            instance.forumid = ForumPost.objects.get(pk=id)
            instance.save()
            
            return redirect('forum_details', id=id)
       
    else:
        form = forms.CommentForm()
    return render(request , "library/forum_details.html",{
        "forum":ForumPost.objects.get(pk=id),
        "forums" : ForumPost.objects.all(),
        "comment" : Comments.objects.filter(forumid=id),
        "form" : form
       
    })

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comments, pk=comment_id)

    # Check if the user is the owner of the comment (optional)
    if request.user == comment.user:
        comment.delete()

    # Redirect back to the post details page or any other appropriate page
    return redirect('library/forum_details', id=comment.forumid.id)  # Redirect to the post details page

def delete_post(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)

    # Check if the user is the owner of the post (optional)
    if request.user == post.user:
        post.delete()

    # Redirect back to the post details page or any other appropriate page
    return redirect('library/forum')  # Redirect to the post details page

@login_required(login_url='/accounts/login/')
def profile(request ):
    borrowing_history = BorrowingHistory.objects.filter(user=request.user).order_by('-borrowed_date')

    # Render the borrowing history in a template
    return render(request, 'library/profile.html',{
        'borrowing_history': borrowing_history,
        'profile': Profile.objects.all()
        })
  
        
   

###Cart Items
@login_required(login_url='/accounts/login/')
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'library/cart.html', {'cart_items': cart_items})

@login_required(login_url='/accounts/login/')
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart_item = CartItem(user=request.user, book=book)
    cart_item.save()
    return redirect('view_cart')

@login_required(login_url='/accounts/login/')
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

###### Borrowing books


@login_required(login_url='/accounts/login/')
def borrow_books(request):
    cart_items = CartItem.objects.filter(user=request.user)
    current_date = timezone.now().date()
    due_date = current_date + timezone.timedelta(days=14)  # You can adjust the due date as needed.

    for cart_item in cart_items:
        book = cart_item.book
        BorrowingHistory.objects.create(user=request.user, book=book, borrowed_date=current_date, due_date=due_date)
        book.availability = False
        book.save()

    # Clear the user's cart after borrowing.
    cart_items.delete()

    return redirect('view_borrowing_history')  # You can create a view for viewing borrowing history.

###### Borrowing History
@login_required(login_url='/accounts/login/')
def view_borrowing_history(request):
    # Retrieve the borrowing history for the current user
    borrowing_history = BorrowingHistory.objects.filter(user=request.user).order_by('-borrowed_date')

    # Render the borrowing history in a template
    return render(request, 'library/borrowing_history.html',{'borrowing_history': borrowing_history})


### Search View 


def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.filter(title__icontains=query)  # Example search by book title
        else:
            results = []
    else:
        form = SearchForm()
        results = []

    return render(request, 'library/search_results.html', {'form': form, 'results': results})


def search_forum(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = ForumPost.objects.filter(title__icontains=query)  # Example search by book title
        else:
            results = []
    else:
        form = SearchForm()
        results = []

    return render(request, 'library/search_results_forum.html', {'form': form, 'results': results})