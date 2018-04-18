from django.conf.urls import url
from application import views

app_name = 'application'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^testpage/$', views.testpage, name='testpage'),
    url(r'^products/$', views.products, name='products'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^tile/$', views.tile, name='tile'),
    url(r'^board/$', views.board, name='board'),
    url(r'^accessories/$', views.accessories, name='accessories'),
    url(r'^drainage/$', views.drainage, name='drainage'),
    url(r'^rollout/$', views.rollout, name='rollout'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]