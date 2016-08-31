from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

class AuthorForm(forms.Form):
    author_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

class AfiliasiForm(forms.Form):
    aff_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))

class AfiliasiMerging(forms.Form):
    author = forms.CharField(label='Author\'s Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    paper= forms.CharField(label='Article\'s Title ',widget=forms.TextInput(attrs={'class': 'form-control'}))
    afiliasi = forms.CharField(label='Affiliation\'s Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    
