from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import NameForm, AuthorForm, AfiliasiForm, AfiliasiMerging, AuthorMerging, ContactForm

from .models import Papers, Authors, Keywords, Citations, Urls, Affiliations, MergingAffiliasi, AuthorBasedata, Venues, AffiliasiRelasi

# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from .forms import PaperAdvancedSearchForm2


# Create your views here.
hitung =0

def index(request):
    form = NameForm()
    forma = AuthorForm()
    formaf = AfiliasiForm()
    countPaper = Papers.objects.all().count();
    countAuthor = Authors.objects.all().count();
    countSource = Venues.objects.all().count();

    citedPaper = Papers.objects.order_by('-ncites')[:5]

    return render(request, 'idci/index.html', {'form':form,'forma':forma,'formaf':formaf,'paperSum':countPaper, 'authorSum':countAuthor, 'journalSum':countSource, 'citedPaper':citedPaper})

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
        
    paperLists = Papers.objects.select_related('venue').filter(title__icontains=data)
    listAuthorTemp = []


    for a in paperLists:
        AuthorList = Authors.objects.select_related('paperid').filter(paperid=a.id)
        listAuthorTemp.append(AuthorList)
        print(listAuthorTemp)
        #print("Authorrrr")
        #print(AuthorList)
    #print(paperLists.query)
    #arraypaper = []
    #for r in paperLists:
    #    arraypaper.append(paperLists)
    #authorLists=[]
   
    #i = 0
    #for i in range(len(arraypaper)):
    #    arraypaper.append([])
    #    for idpenulis in paperLists:
    #        arraypaper = Authors.objects.select_related('paperid').filter(paperid=idpenulis.pk)
    #        print(arraypaper)
    #        print("ASASA => "+str(idpenulis.pk))
   
    return render(request, 'idci/title.html', {'list': paperLists, 'form':form, 'penulis':listAuthorTemp})

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
    
    hitung = []
    for cPub in pubLists:
        
        hitung.append(AffiliasiRelasi.objects.filter(idaffiliasi=cPub.id).count())
        #print (hitung)

    return render(request, 'idci/publisher.html', {'publisher': pubLists, 'form':form, 'pap':hitung })

def afflist(request, nama):
    #aff = Affiliations.objects.filter(name=nama).order_by('ndocs')
                                         
   # for a in aff:
    affs = AffiliasiRelasi.objects.select_related('idpaper').filter(idaffiliasi=nama)
    #print(affs)


    return render(request, 'idci/publisherlist.html', {'lists': affs})

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

def listauthor(request, data):
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
    #authorLists.append([])
    i = 0

    authorListsCount = []
    for cAut in authorLists:
        authorListsCount.append(Authors.objects.filter(name__icontains=cAut.name).select_related('paperid').count())
        i= i+1
    
   
    print(authorListsCount)

    return render(request, 'idci/author.html', {'author': authorLists, 'form':form, 'sum':authorListsCount })

def paperdetail(request, pk, judul):
    #detailPaper = get_object_or_404(Papers,pk=pk)
    forma = AuthorForm()
    detailPaper = Papers.objects.select_related('venue').get(pk=pk)
    key = Keywords.objects.filter(paperid=pk).order_by('id')

    ref = Citations.objects.filter(paperid=pk).order_by('id')
    author = Authors.objects.filter(paperid=pk).order_by('id')
    citedd = Citations.objects.filter(title=judul).order_by('id')
    venueType = detailPaper.venue.type

    for c in citedd:
        cited = Papers.objects.filter(id=c.paperid).order_by('id')
                                                             
    #for a in key:
     #   cite = Papers.objects.filter(id=a.paperid).order_by('id')
        
            
    dl = Urls.objects.get(paperid=pk)
    
    return render(request, 'idci/detail.html', {'forma':forma, 'paperdetail': detailPaper, 'keyword':key, 'ref':ref, 'author':author, 'cited':citedd, 'url':dl, 'venueType':venueType})

def merge_aff(request, judul):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
      
        forma = AfiliasiMerging (request.POST)
        # check whether it's valid:
        
        if forma.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = forma.save(commit=False)
            post.namapenulis = forma.cleaned_data['namapenulis']
            post.namaaffiliasi = forma.cleaned_data['namaaffiliasi']
            post.judulpaper = judul
            post.status = "Sedang di Proses"
            post.save()

            #return HttpResponseRedirect('/index.html/')
            return HttpResponseRedirect('/mergeaffhasil/')

    else:
        forma = AfiliasiMerging()

    return render(request, 'idci/merge_aff.html', {'forma':forma, 'judul':judul})

def merge_aut(request, judul):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
      
        formas = AuthorMerging (request.POST)
        # check whether it's valid:
        
        if formas.is_valid():
            post = formas.save(commit=False)
            post.namapenulis = formas.cleaned_data['namapenulis']
            post.penulisbasedata = formas.cleaned_data['penulisbasedata']
            post.email = formas.cleaned_data['email']
            post.judulpaper = judul
            post.status = "Sedang di Proses"
            post.save()

            #return HttpResponseRedirect('/index.html/')
            return HttpResponseRedirect('/mergeaffhasil/')

    else:
        formas = AuthorMerging()

    return render(request, 'idci/merge_aut.html', {'formas':formas, 'judul':judul})

def mergeaffhasil(request):
    #new_entry = MergingAffiliasi(judulpaper=judul, namapenulis=penulis, namaaffiliasi=affiliasi, status="Sedang diproses")
    #new_entry.save()

    return render(request, 'idci/thanks.html', {})

def authorlist(request, nama):
    author = Authors.objects.select_related('paperid').filter(id=nama)
    dataAuthor = Authors.objects.get(id=nama)
    totalPaper = Authors.objects.select_related('paperid').filter(id=nama).count()

    totalSitasi = 0
    totalDokSitasi = 0

    for sum in author:
        totalSitasi += sum.paperid.ncites 
        if sum.paperid.ncites>0:
            totalDokSitasi +=1


    print("Total sitasi => "+str(totalSitasi))

    #for a in author:
     #   jumlahPaper = AuthorsRelasi.objects.filter(idbasedata=a.id).count()

    return render(request, 'idci/authorlist.html', {'lists': author, 'penulis': dataAuthor, 'totalPaper': totalPaper, 'totalSitasi':totalSitasi, 'totalDokSitasi':totalDokSitasi})

def about (request):
    return render(request, 'idci/about.html', {})

def contact(request):
    form_class = ContactForm
    

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['sutadi.triputra@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'idci/contact.html', {
        'form': form_class,
    })

def notes(request):
    #form = PaperAdvancedSearchForm(request.GET)
    #notes = form.search()
    #return render_to_response('search/search.html',{'notes':form})

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
      
        forma =PaperAdvancedSearchForm2 (request.POST)
        # check whether it's valid:
        
        if forma.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = forma.save(commit=False)
            post.namapenulis = forma.cleaned_data['namapenulis']
            post.namaaffiliasi = forma.cleaned_data['namaaffiliasi']
            post.judulpaper = judul
            post.status = "Sedang di Proses"
            post.save()

            #return HttpResponseRedirect('/index.html/')
            return HttpResponseRedirect('/mergeaffhasil/')

    else:
        forma = PaperAdvancedSearchForm2()

    return render(request, 'idci/search.html', {'forma':forma,})