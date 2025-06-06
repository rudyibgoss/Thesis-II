from django.apps import AppConfig #importing AppConfig to configure this app's settings

#this class configures the 'transportation' app for the Django project
class TransportationConfig(AppConfig):

    #specifies the default type of primary key to use for models in this app
    default_auto_field = 'django.db.models.BigAutoField'

    #the name of the app this configuration belongs to
    name = 'transportation'
