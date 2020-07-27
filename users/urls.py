from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit-phno',views.edit_phno),
    path('allorders',views.allorders),
    path('edit-address',views.edit_address),
    path('admin-orders',views.admin_view),
    path('delivered/<id>',views.delivered),
    path('login',views.login),
    path('signup',views.signup),
    path('menu',views.home),
    path('logout',views.logout),
    path('cart',views.cart),
    path('menu/<str:rest_name>',views.items),
    path('order',views.order),
    path('cancel',views.cancel),
    path('account',views.account),
    path('allorders',views.allorders),
    path('checkout',views.checkout),
    path('recieved',views.recieved),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='set_password.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name="password_reset_complete"),
]