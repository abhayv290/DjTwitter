from django.urls import path
from .views import tweet_list,tweet_create,tweetDelete,tweetEdit,register
urlpatterns = [
    #  path('',tweetHome , name= 'tweethome'),
    path('',tweet_list,name='tweet_list'),
     path('create/', tweet_create, name='tweet_create'),
     path('<int:tweet_id>/edit/',tweetEdit,name='tweetEdit'),
     path('<int:tweet_id>/delete/',tweetDelete,name='tweetDelete'),
     path('register/',register ,name='register')
]
