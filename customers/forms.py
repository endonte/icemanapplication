from django import forms
from .models import Customer, Billing_Details
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
                'contact_name',
                'contact_number',
                'contact_email',
                'company_name',
                'company_reg_no',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(CustomerForm, self).__init__(*args, **kwargs)

class CustomerBillingForm(forms.ModelForm):
    class Meta:
        model = Billing_Details
        fields = (
                'billing_address_line1',
                'billing_address_line2',
                'billing_postal',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(CustomerBillingForm, self).__init__(*args, **kwargs)
