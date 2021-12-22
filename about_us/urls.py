from django.urls import path
from about_us.views import add_contact_flutter, index

app_name = "about_us"

urlpatterns = [
    path('', index, name='index'),
    path('add-contact-flutter', add_contact_flutter, name='add_contact_flutter')
]