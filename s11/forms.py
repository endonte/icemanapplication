from django import forms
from .models import Store, StoreRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout


class StoreRequestForm(forms.ModelForm):

    class Meta:
        model = StoreRequest
        fields = (
                'requesting_store',
                'assigned_driver',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit Request', css_class='btn-block btn primary'))
        super(StoreRequestForm, self).__init__(*args, **kwargs)

class StoreConfirmForm(forms.ModelForm):

    class Meta:
        model = StoreRequest
        fields = (
                'request_invoice_no',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Confirm Delivery', css_class='btn-block btn primary'))
        super(StoreConfirmForm, self).__init__(*args, **kwargs)
