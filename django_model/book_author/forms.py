from book_author.models import Author
from .models import Author,Book
from django import forms

class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ("name",)

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)



class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)