from django import forms
from .models import Store, StoreRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
                'store_no',
                'store_address1',
                'store_address2',
                'store_postal',
                'store_contact_no',
                'store_district_area',
                'assigned_driver',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(StoreForm, self).__init__(*args, **kwargs)


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

        self.helper.add_input(Submit('submit', 'Submit'))
        super(StoreRequestForm, self).__init__(*args, **kwargs)

class StoreConfirmForm(forms.ModelForm):

    class Meta:
        model = StoreRequest
        fields = (
                'request_invoice_no',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(StoreConfirmForm, self).__init__(*args, **kwargs)
