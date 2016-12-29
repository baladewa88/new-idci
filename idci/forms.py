from django import forms
from .models import MergingAffiliasi, MergingAuthor
from django.forms import ModelForm, TextInput
#from haystack.forms import SearchForm

class NameForm(forms.Form):
    your_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

class AuthorForm(forms.Form):
    author_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

class AfiliasiForm(forms.Form):
    aff_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

class AfiliasiMerging(forms.ModelForm):
    #author = forms.CharField(label='Author\'s Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    #paper= forms.CharField(label='Article\'s Title ',widget=forms.TextInput(attrs={'class': 'form-control'}))
    #afiliasi = forms.CharField(label='Affiliation\'s Name',widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MergingAffiliasi
        fields = ('namapenulis', 'namaaffiliasi',)
        widgets = {
            'namapenulis': TextInput(attrs={'class': 'form-control'}),
            'namaaffiliasi': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'namapenulis': ('Author\'s Name'),
            'namaaffiliasi': ('Affiliation'),
        }

class AuthorMerging(forms.ModelForm):
    #author = forms.CharField(label='Author\'s Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    #paper= forms.CharField(label='Article\'s Title ',widget=forms.TextInput(attrs={'class': 'form-control'}))
    #afiliasi = forms.CharField(label='Affiliation\'s Name',widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MergingAuthor
        fields = ('namapenulis','email','penulisbasedata',)
        widgets = {
            'namapenulis': TextInput(attrs={'class': 'form-control'}),
			'email': TextInput(attrs={'class': 'form-control'}),
			'penulisbasedata': TextInput(attrs={'class': 'form-control'}),
        }
		
        labels = {
            'namapenulis': ('Author\'s Name in Paper'),
			'email': ('Author\'s Email in Paper'),
			'penulisbasedata': ('Author\'s Fullname'),
        }

#class AdvancedSearchForm(forms.Form):
 #   aff_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

#class PaperAdvancedSearchForm(SearchForm):

 #   def no_query_found(self):
  #      return self.searchqueryset.all()

class PaperAdvancedSearchForm2(forms.Form):
    papers_name = forms.CharField(label='Article\'s Title',widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    papers_year = forms.IntegerField(label='Year',widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    author = forms.CharField(label='Author',widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    source = forms.CharField(label='Source Title',widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    publisher = forms.CharField(label='Publisher',widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Keyword = forms.CharField(label='Keyword',widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

