from django import forms
from .models import MergingAffiliasi
from django.forms import ModelForm, TextInput

class NameForm(forms.Form):
    your_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

class AuthorForm(forms.Form):
    author_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

class AfiliasiForm(forms.Form):
    aff_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

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
