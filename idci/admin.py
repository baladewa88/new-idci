from django.contrib import admin

from .models import Affiliations, Urls, Keywords, Papers, Citations, Authors, Venues, AffiliasiRelasi, AuthorBasedata, AuthorsRelasi, MergingAffiliasi, MergingAuthor
from random import randint

import time

class KeywordsInline(admin.TabularInline):
    model = Keywords
    extra = 3
    exclude = ['id']

class UrlInline(admin.TabularInline):
    model = Urls
    extra = 1
    exclude = ['id']

class AuthorInline(admin.StackedInline):
    model = Authors
    extra = 3
    exclude = ['id','cluster']

class AffiliasiRelasiInline(admin.TabularInline):
    model = AffiliasiRelasi
    extra = 2
    exclude = ['id',]
    
class PapersAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['title','abstract','year', 'venue', 'pages', 'volume', 'number','selfcites','publisher','pubaddress']})]
    list_filter = ('crawldate'),('year')
    list_display = ('id','title','ncites')
    ordering = ('-crawldate',)
    search_fields = ['title','id']
    
    def save_model(self, request, obj, form, change):
        currentTime = int(round(time.time() * 1000))+randint(0,99)
        if obj.id == "":
            obj.id = str(currentTime)
            refCount = Citations.objects.filter(title=form.cleaned_data['title']).count()
            obj.ncites = refCount
            print("ID => "+str(currentTime))
            obj.save()
        else :
            obj.save()

    inlines =[KeywordsInline,UrlInline,AuthorInline, AffiliasiRelasiInline]
    
class CitationsAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['title','authors','venue', 'year', 'pages', 'editors', 'volume', 'number', 'paperid', 'self', 'publisher','pubaddress']})]
    #list_filter = ('year'),
    list_display = ('id','title','authors')
    ordering = ('authors',)
    search_fields = ['title', 'authors',]

    def save_model(self, request, obj, form, change):
        print(obj.id)
        paperCount = Papers.objects.filter(title=form.cleaned_data['title']).count()
        print(paperCount)
        if obj.id is None:
            print("Citation > Title : "+form.cleaned_data['title']+" Jumlahnya = "+str(paperCount))
            if paperCount>0 :
                cite = Papers.objects.get(title=form.cleaned_data['title'])
                cite.ncites = cite.ncites + 1
                cite.save()
            obj.save()
        else :
            print("Citation > ID : "+str(obj.id))
            obj.save()
        
class AffiliasiAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['name','address','url']})]
    list_display = ('name','address','url')
    ordering = ('name',)

class AuthorsAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['paperid','name','affil','address', 'email', 'ord', 'parentid']})]
    list_display = ('name','affil', )
    ordering = ('name',)

class AuthorsBasedataAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['namalengkap','affiliasi','alamat_affiliasi']})]
    list_display = ('namalengkap','affiliasi','jumlahdokumen' )
    ordering = ('namalengkap',)

class AuthorRelasiAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['idbasedata','idauthors']})]
    list_display = ('idbasedata','idauthors' )
    ordering = ('idbasedata',)
    
admin.site.register(Papers, PapersAdmin)
admin.site.register(Urls)
admin.site.register(Keywords)
admin.site.register(Affiliations, AffiliasiAdmin)
admin.site.register(Citations, CitationsAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Venues)
admin.site.register(AuthorBasedata, AuthorsBasedataAdmin)
admin.site.register(AuthorsRelasi, AuthorRelasiAdmin)
admin.site.register(MergingAffiliasi )
admin.site.register(MergingAuthor)

