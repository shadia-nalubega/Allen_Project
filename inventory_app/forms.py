from django import forms
from .models import StockEntry, Product, StockEntryItem
from django.forms import inlineformset_factory


class StockEntryForm(forms.ModelForm):

    class Meta:

        model = StockEntry

        fields = [
            'supplier',
            'supplied_on_credit',
            'stock_date',
            'supplied_on_credit',
            'notes',
        ]
        widgets = {

    'supplier': forms.Select(attrs={
        'class': 'form-control'
    }),

    'invoice_number': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter invoice number'
    }),

    'stock_date': forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }),

    'supplied_on_credit': forms.CheckboxInput(attrs={
        'class': 'checkbox-input'
    }),

    'notes': forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'placeholder': 'Additional notes'
    }),

}
  




class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'category',
            'sku',
            'product_name',
            'unit',
            'unit_cost',
            'retail_price',
            'wholesale_price',
            'normal_price',
            'quantity',
            'reorder_level',
        ]

        widgets = {

            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'sku': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter SKU'
            }),

            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),

            'unit': forms.Select(attrs={
                'class': 'form-control'
            }),

            'unit_cost': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'retail_price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'wholesale_price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'normal_price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'quantity': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'reorder_level': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

        }



class StockEntryForm(forms.ModelForm):

    class Meta:

        model = StockEntry

        fields = [
            'supplier',
            'invoice_number',
            'stock_date',
            'supplied_on_credit',
        ]

class StockEntryItemForm(forms.ModelForm):
    wholesale_markup = forms.DecimalField(
        max_digits=7,
        decimal_places=2,
        initial=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Wholesale %'
            })
    )
    
    retail_markup = forms.DecimalField(
        max_digits=7,
        decimal_places=2,
        initial=25,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Retail %'
            })
    )

    normal_markup = forms.DecimalField(
        max_digits=7,
        decimal_places=2,
        initial=20,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Normal %'
            })
    )

    
    class Meta:

        model = StockEntryItem

        fields = [
            'product',
            'quantity',
            'unit_cost',
            'wholesale_markup',
            'normal_markup',
            'retail_markup',
        ]       
         
StockEntryItemFormSet = inlineformset_factory(

    StockEntry,
    StockEntryItem,

    form=StockEntryItemForm,

    extra=1,

    can_delete=True
)