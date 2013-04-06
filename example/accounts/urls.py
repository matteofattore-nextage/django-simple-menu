from django.conf.urls.defaults import *

urlpatterns = patterns(
    'accounts.views',

    url(r'profile/', 'profile', name="profile"),
    url(r'one/', 'one', name="one"),
    url(r'two/', 'two', name="two"),
    url(r'three/', 'three', name="three"),
    url(r'four/', 'four', name="four"),
    url(r'', 'index')
)
