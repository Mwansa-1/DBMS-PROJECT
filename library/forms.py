# forms.py
from django import forms
from . import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['comments']
        
        #Compare this snippet from BookNest/library/templates/library/forum_details.html:
class AddPost(forms.ModelForm):
    class Meta:
        model = models.ForumPost
        fields = ['title','topic','content']

#Contact Form

class Contact(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name','phone','email','message' ]
        
#Search Form
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
        