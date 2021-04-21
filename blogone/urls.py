from django.conf.urls.static import static
from django.urls import path
from TeckBlog import settings
from .import views
from .views import *

urlpatterns = [
    # path('',PostListView.as_view(),name='home'),
    path('',views.post_listing,name='home'),
    path('add-post/',views.Add_post,name='add_post'),
    path('post_detail/<str:id>',views.post_detail,name='post_detail'),
    path('tech_news/',views.technews,name='tech_news'),
    path('comsec_news/',views.comsecnews,name='comsec_news'),
    path('tips_news/', views.tips_and_trick,name='tips'),
    path('deletepost/<int:id>', views.deletepost, name='deletepost'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('editpost/<int:id>', views.editpost, name='editpost'),
    path('suggestion/', views.give_suggestion,name='suggestion'),
    path('suggestion/view', views.view_suggestion,name='view_suggestion'),
    path('viewer/view', views.view_viewer,name='view_viewer'),
    path('logout/', views.logoutView,name='logout'),
    path('login/', views.loginView,name='login'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)