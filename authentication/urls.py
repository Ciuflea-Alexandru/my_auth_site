from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('verify_code/', views.verify_code, name='verify_code'),
    path('account/', views.account_page, name='account_page'),
    path('forgot_password/link/', views.forgot_password_link, name='forgot_password_link'),
    path('forgot_password/reset/<uidb64>/<token>/', views.forgot_password_reset, name='forgot_password_reset'),
]
