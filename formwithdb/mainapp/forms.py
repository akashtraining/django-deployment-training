from mainapp.models import User
from django.forms import ModelForm, fields

class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
