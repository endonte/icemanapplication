from django import forms
from .models import Orders_Adhoc, OrderItems, CustomerItems
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div

class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Orders_Adhoc
        fields = (
                'customer',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        #self.helper.form_class = 'form-inline'
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        #self.helper.form_action = ''
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Next - Add Products'))
        super(OrderCreateForm, self).__init__(*args, **kwargs)

class OrderProductForm(forms.ModelForm):

    class Meta:
        model = OrderItems
        fields = (
                'order_product',
                'order_product_qty',
                'additional_details',
        )

    def __init__(self, *args, **kwargs):
        orderid = kwargs.pop('pk')
        print(orderid)
        order = Orders_Adhoc.objects.get(pk=orderid)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = True
        self.helper.form_error_title = 'Form Errors'
        self.helper.layout = Layout(
            Div(
                Div('order_product', css_class = "col-sm-4"),
                Div('order_product_qty', css_class = "col-sm-2"),
                Div('additional_details', css_class = "col-sm-6 "),
                css_class = 'row'
            )
        )

        self.helper.add_input(Submit('submit', 'Add Product'))
        super(OrderProductForm, self).__init__(*args, **kwargs)

class OrderConfirmForm(forms.ModelForm):

    class Meta:
        model = Orders_Adhoc
        fields = (
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'post'
        self.helper.help_text_inline = True
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Confirm Order', css_class='btn-block btn-primary'))
        super(OrderConfirmForm, self).__init__(*args, **kwargs)