from django.conf.urls import url, include
from django.conf.urls import patterns
from django.contrib import admin
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    # para /app_restaurantes/index
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^like_category/$', views.like_category, name='like_category'),
    url(r'^api/restaurantes/$', views.restauranteCollection, name='restauranteCollection'),
    url(r'^api/restaurante/(?P<pk>[0-9]+)/$', views.restauranteElement,name='restauranteElement'),
   


    url(r'^ap/(?P<nombre>[\w\- ]+)/$', views.add_plato, name ='add_plato'),
    url(r'^ng-test/$', TemplateView.as_view(template_name='ng_test.html')),
]
