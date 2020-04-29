'''админка landing'''
from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    '''административное представление контакта'''
  #  list_display = ('name', 'email')
    list_display = [field.name for field in Subscriber._meta.fields] # все поля в списке записей
    list_display_links = ['name'] # эти поля показываются как ссылки
    list_filter = ['name', 'email'] # фильтрация по полям в админке
    search_fields = ('name', 'email')
    fields = ['name'] # поля в редакторе текущей записи


admin.site.register(Subscriber, SubscriberAdmin)
