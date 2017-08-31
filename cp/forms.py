from django import forms
from drivers.models import Drivers
from s11.models import Store
from products.models import Product, Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from drivers.models import Drivers

class DriverEditForm(forms.ModelForm):

    class Meta:
        model = Drivers
        fields = (
                'full_name',
                'nick_name',
                'designation',
                'phone_number',
                'wechat_id',
                'delivery_areas',
                'delivery_restrictions',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'
        self.helper.add_input(Submit('submit', 'Add Driver'))
        super(DriverEditForm, self).__init__(*args, **kwargs)

class S11EditStoreForm(forms.ModelForm):
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
        super(S11EditStoreForm, self).__init__(*args, **kwargs)


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
                'product_name',
                'category',
                'uom',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Add Product'))
        super(ProductEditForm, self).__init__(*args, **kwargs)

class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
                'category_name',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Add Category'))
        super(CategoryEditForm, self).__init__(*args, **kwargs)
