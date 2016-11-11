from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^adsearch/?$', views.search, name='search'),
    url(r'^report/?$', views.analisa, name='analisa'),
    url(r'^titlesearch/?$', views.get_name, name='name'),
    url(r'^result/(?P<data>.+)/$', views.paperlist, name='result'),
    url(r'^authorsearch/?$', views.get_authorname, name='authorname'),
    url(r'^resulta/(?P<data>.+)/$', views.listauthor, name='resulta'),
    url(r'^affsearch/?$', views.get_publisher, name='publisher'),
    url(r'^resultaff/(?P<data>.+)/$', views.publisherlist, name='resultpub'),
    url(r'^paper/(?P<pk>\S+)/(?P<judul>.+)/$', views.paperdetail, name='paperdetail'),
    url(r'^mergeaff/(?P<judul>.+)/$', views.merge_aff, name='merge_aff'),
    url(r'^mergeaut/(?P<judul>.+)/$', views.merge_aut, name='merge_aut'),
    url(r'^mergeaffhasil/$', views.mergeaffhasil, name='mergeaffhasil'),
    url(r'^author/(?P<nama>.+)/$', views.authorlist, name='authorlist'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^contact/?$', views.contact, name='contact'),
]
