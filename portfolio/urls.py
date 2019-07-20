from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.views import password_change as pwd_change, password_change_done as pwd_change_done, password_reset as reset, password_reset_done as reset_done, password_reset_confirm as reset_confirm, password_reset_complete as reset_complete


app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('customer/<int:pk>/summary/', views.summary, name='summary'),
    #url(r'^customer/<int:pk>/pdf/$',GeneratePDF.as_view(),name='report'),
    path('customer/<int:pk>/pdf/', views.admin_summary_pdf, name='admin_summary_pdf'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    url(r'^customers_json/', views.CustomerList.as_view()),
    #path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    #url(r'^customer/<int:pk>/pdf/$',GeneratePDF.as_view(),name='report'),
    path('customer/<int:pk>/portfoliopdf/', views.admin_portfolio_pdf, name='admin_portfolio_pdf'),
    #login signup and registration
    #url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url('^password-change/done/$', pwd_change_done, name='password_change_done'),
    url('^password-change/$', pwd_change, {'post_change_redirect': '/password-change/done/'}, name='password_change'),
    url(r'^password-reset/complete/$', reset_complete, name='password_reset_complete'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', reset_confirm,
        {'post_reset_redirect': '/password-reset/complete/'}, name='password_reset_confirm'),
    url(r'^password-reset/done/$', reset_done, name='password_reset_done'),
    url(r'^password-reset/$', reset, {'post_reset_redirect': '/password-reset/done/',
                                      'email_template_name': 'registration/password_reset_email.html'},
        name='password_reset'),
]
urlpatterns = format_suffix_patterns(urlpatterns)