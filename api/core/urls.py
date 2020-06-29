from django.urls import path, include
from rest_framework import routers
from . import views

# from .viewsets import DocumentViewSet

router = routers.SimpleRouter()
router.register('documents',views.DocumentView)

# urlpatterns = router.urls

urlpatterns = [
	# path('form/', views.myform, name='myform'),
    # path('api/', include(router.urls)),
    path('prueba/', views.prueba),
 
] 

# router = routers.DefaultRouter()

# router.register('MyAPI', views.ApprovalsView)
# urlpatterns = [
# 	path('form/', views.myform, name='myform'),
#     path('api/', include(router.urls)),
#     path('status/', views.approvereject),
 
# ] 
