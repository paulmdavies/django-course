from django.forms import FileField
from django.forms.forms import Form


class ProfileForm(Form):
    user_image = FileField()