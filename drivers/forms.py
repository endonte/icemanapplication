from django import forms
from .models import Drivers
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset


class DriverForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = (
                'full_name',
                'nick_name',
                'designation',
                'wechat_id',
                'delivery_areas',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Add Driver'))
        super(DriverForm, self).__init__(*args, **kwargs)
