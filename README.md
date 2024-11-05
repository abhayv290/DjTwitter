Important Settings configuration for django 
setting permission for media files in cpanel 
 chmod -R 777 ./media   ( 777 for anybody ) (755 only or users) 

 when debug is set to the false so accesssing media and static file using django.views.static import serve and then use re_path  in url patterns
 re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

when debug is set to True
if settings.DEBUG:
   urlpatterns =+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

for static and media folder configuration
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

if DEBUG:

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

else:

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticFiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

for correcting the path to server read our project in cpanel in passenger.wsgi file 
from 'project_name'.wsgi import application

creating a package.json file(similir to nodejs envirnoment  )  pip have freeze command which create a  req.txt file , this file stores all the packages we have used throught the project 
pip freeze > req.txt


