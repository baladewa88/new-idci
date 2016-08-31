from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect

from .forms import NameForm, AuthorForm, AfiliasiForm, AfiliasiMerging

from .models import Papers, Authors, Keywords, Citations, Urls, Affiliations, MergingAffiliasi

# Create your views here.
def index(request):
    form = NameForm()
    forma = AuthorForm()
    formaf = AfiliasiForm()
    return render(request, 'idci/index.html', {'form':form,'forma':forma,'formaf':formaf,})

def analisa(request):
  
    return render(request, 'idci/report.html', {})

def search (request):
    formw = PaperForm()
    return render(request, 'idciapp/adsearch.html', {'forme':formw})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/result/'+form.cleaned_data['your_name'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'idci/index.html', {'form': form})

def paperlist(request, data):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/result/'+form.cleaned_data['your_name'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        
    paperLists = Papers.objects.filter(title__icontains=data)
          
    return render(request, 'idci/title.html', {'list': paperLists, 'form':form })

def get_publisher(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AfiliasiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/resultaff/'+form.cleaned_data['aff_name'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AfiliasiForm()

    return render(request, 'idci/index.html', {'form': form})

def publisherlist(request, data):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AfiliasiForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/resultaff/'+form.cleaned_data['aff_name'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AfiliasiForm()
        
    pubLists = Affiliations.objects.filter(name__icontains=data)
    for cPub in pubLists:
        count = Affiliations.objects.filter(pk=cPub.id).count()
        
          
    return render(request, 'idci/publisher.html', {'publisher': pubLists, 'form':form, 'pap':count })


def get_authorname(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        forma = AuthorForm (request.POST)
        # check whether it's valid:
        
        if forma.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/resulta/'+forma.cleaned_data['author_name'])

    else:
        forma = AuthorForm()

    return render(request, 'idci/index.html', {'forma':forma})

def authorlist(request, data):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/resulta/'+form.cleaned_data['author_name'])

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthorForm()
        
    authorLists = Authors.objects.filter(name__icontains=data)
          
    return render(request, 'idci/author.html', {'author': authorLists, 'form':form })

def paperdetail(request, pk, judul):
    detailPaper = get_object_or_404(Papers,pk=pk)
    key = Keywords.objects.filter(paperid=pk).order_by('id')
    ref = Citations.objects.filter(paperid=pk).order_by('id')
    author = Authors.objects.filter(paperid=pk).order_by('id')
    citedd = Citations.objects.filter(title=judul).order_by('id')
    cite = ""
    
    for c in citedd:
        cited = Papers.ea.filter(id=c.paperid).order_by('id')
                                                             
    for a in key:
        cite = Papers.ea.filter(title__icontains=a.keyword).order_by('id')
            
    dl = Urls.objects.get(paperid=pk)
    
    return render(request, 'idci/detail.html', {'paperdetail': detailPaper, 'keyword':key, 'ref':ref, 'author':author, 'title':cite, 'cited':citedd, 'url':dl})

def merge_aff(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        forma = AfiliasiMerging (request.POST)
        # check whether it's valid:
        
        if forma.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/mergeaffhasil/'+forma.cleaned_data['author']+"/"+forma.cleaned_data['afiliasi']+forma.cleaned_data['paper'])

    else:
        forma = AfiliasiMerging()

    return render(request, 'idci/merge_aff.html', {'forma':forma})

def mergeaffhasil(request, penulis, affiliasi, judul):
    new_entry = MergingAffiliasi(judulpaper=judul, namapenulis=penulis, namaaffiliasi=affiliasi, status="Sedang diproses")
    new_entry.save()
