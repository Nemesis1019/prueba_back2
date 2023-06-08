from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import view

router =  routers.DefaultRouter()
router.register(r'client',view,'clients' )


urlpatterns =[
    
    path("",include(router.urls)),
    path("docs/",include_docs_urls("Client API")),
   
    
]