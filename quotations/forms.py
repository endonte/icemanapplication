from django import forms
from .models import Quote, Quote_Products
from customers.models import Shipping_Details
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div

class QuoteCreateForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = (
                'customer',
                'quote_type',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        #self.helper.form_class = 'form-inline'
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        #self.helper.form_action = ''
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Next - Shipping Details'))
        super(QuoteCreateForm, self).__init__(*args, **kwargs)

class QuoteShippingNewForm(forms.ModelForm):

    class Meta:
        model = Shipping_Details
        fields = (
                'shipping_address_line1',
                'shipping_address_line2',
                'shipping_postal',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        #self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        #self.helper.form_action = ''
        self.helper.help_text_inline = True
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit New Address'))
        super(QuoteShippingNewForm, self).__init__(*args, **kwargs)

class QuoteShippingExistingForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = (
                'shipping_address',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.help_text_inline = True
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Next - Add Products'))
        super(QuoteShippingExistingForm, self).__init__(*args, **kwargs)

class QuoteProductNoTotalForm(forms.ModelForm):
    class Meta:
        model = Quote_Products
        fields = (
                'quote_product',
                'quote_product_price',
                'quote_product_description',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.form_action = ''
        self.helper.help_text_inline = True
        self.helper.form_error_title = 'Form Errors'
        self.helper.layout = Layout(
            Div(
                Div('quote_product', css_class = "col-sm-3"),
                Div('quote_product_price', css_class = "col-sm-3"),
                Div('quote_product_description', css_class = "col-sm-6 "),
                css_class = 'row'
            )
        )

        self.helper.add_input(Submit('submit', 'Add Product'))
        super(QuoteProductNoTotalForm, self).__init__(*args, **kwargs)

class QuoteProductTotalForm(forms.ModelForm):
    class Meta:
        model = Quote_Products
        fields = (
                'quote_product',
                'quote_product_price',
                'quote_product_qty',
                'quote_product_description',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = True
        self.helper.form_error_title = 'Form Errors'
        self.helper.layout = Layout(
            Div(
                Div('quote_product', css_class = "col-sm-3"),
                Div('quote_product_price', css_class = "col-sm-2"),
                Div('quote_product_qty', css_class = "col-sm-2"),
                Div('quote_product_description', css_class = "col-sm-5"),
                css_class = 'row'
            )
        )

        self.helper.add_input(Submit('submit', 'Add Product'))
        super(QuoteProductTotalForm, self).__init__(*args, **kwargs)

class QuoteConfirmForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = (
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.help_text_inline = True
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Confirm Quote', css_class='btn-block btn-primary'))
        super(QuoteConfirmForm, self).__init__(*args, **kwargs)
