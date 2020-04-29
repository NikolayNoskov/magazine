from django.forms import ModelForm
from .models import *

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        #fields = ('fio', 'phoneinternal', 'phone496', 'phone495', 'mail', 'contactdepartament')
        exclude = [""]

