from django import urls
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='index.html'),
    path('dashboard', views.admin_dashboard, name='dashboard.html'),
    path('add', views.admin_add, name='form-basic.html'),
    path('admin_add', views.admin_add, name='form-basic.html'),
    path('profile', views.admin_profile, name='profile.html'),
    path('gprofile', views.guard_profile, name='guard_profile.html'),
    path('map', views.admin_map, name='sitemap.html'),
    path('attendance', views.admin_attendance, name='Attendance_Table.html'),
    path('distance', views.admin_distance, name='Distance Calculator.html'),
    path('login', views.login),
    path('logout', views.logout,name='logout.html'),
    path('crossing', views.admin_crossing,name='Level_crossing.html'),
    path('obstacle', views.admin_obstacle,name='Obstacle detection.html'),
    path('human', views.admin_human,name='Human Detection.html'),
    path('distance', views.admin_distance,name='Distance Calculator.html'),
    path('warning', views.admin_warning,name='datatable.html'),
    path('gdashboard', views.guard_dashboard,name='guard_dashboard.html'),
    path('status', views.admin_status,name='form-wizard.html'),
    path('glogout', views.glogout,name='guard_logout.html'),
    path('addcomplain', views.guard_complain,name='guard_form-wizard.html'),
]