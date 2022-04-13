from django import forms
from ..models import Books


class Book(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('name', 'author', 'description', 'price', 'amount')
        labels = {
            'name': 'Full Name',
        }

    def __init__(self, *args, **kwargs):
        super(Book, self).__init__(*args, **kwargs)
