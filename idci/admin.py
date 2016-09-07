from django.contrib import admin

from .models import Affiliations, Urls, Keywords, Papers, Citations, Authors, Venues

class PapersAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['title','abstract','year', 'venue', 'pages', 'volume', 'number','selfcites']}),
                ('Affiliation',{'fields':['affiliasi','publisher','pubaddress']}),
                 ]
    list_filter = [('crawldate')]
    list_display = ('id','title','affiliasi','ncites','selfcites')
    ordering = ('-crawldate',)
    
admin.site.register(Papers, PapersAdmin)
admin.site.register(Urls)
admin.site.register(Keywords)
admin.site.register(Affiliations)
admin.site.register(Citations)
admin.site.register(Authors)
admin.site.register(Venues)

