from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vlans import views
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'vlans', views.VlansViewSet)
router.register(r'coresubnets', views.CoreSubnetsViewSet)  # Register the new viewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vlans_data/', views.vlans_data, name='vlans_data'),
    path('api/coresubnets_data/', views.coresubnets_data, name='coresubnets_data'),  # New route for CoreSubnets data
    path('api/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('vlans/', views.index, name='vlans'),  # Ensure this exists
    path('coresubnets/', views.coresubnets, name='coresubnets'),  # Corrected path for CoreSubnets
    path('redirect_to_vlans/', views.redirect_to_vlans, name='redirect_to_vlans'),
    path('redirect_to_coresubnets/', views.redirect_to_coresubnets, name='redirect_to_coresubnets'),  # New redirect path
    path('', views.home, name='home'),  # Set home.html as the default landing page
]
