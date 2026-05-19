from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Product, StockEntry, StockEntryItem
from .forms import StockEntryForm, ProductForm, StockEntryItemFormSet
from decimal import Decimal
# Create your views here.
def product_list(request):
    products = Product.objects.all().order_by('product_name')
    
    context = {
        'products': products
        }
    return render(request, 'manager/product_list.html', context)





def register_stock(request):

    if request.method == 'POST':

        form = StockEntryForm(request.POST)

        formset = StockEntryItemFormSet(request.POST)

        if form.is_valid() and formset.is_valid():

            stock_entry = form.save(commit=False)

            stock_entry.added_by = request.user

            stock_entry.save()

            total_cost = 0

            items = formset.save(commit=False)

            for item in items:

                item.stock_entry = stock_entry

                item.subtotal = (
                    item.quantity * item.unit_cost
                )

                total_cost += item.subtotal

                item.save()
            for deleted_form in formset.deleted_forms:

                    if deleted_form.instance.pk:

                       deleted_form.instance.delete()

            product = item.product

            product.quantity += item.quantity

            product.unit_cost = item.unit_cost

            wholesale_markup = formset.cleaned_data[
                    items.index(item)
                ]['wholesale_markup']

            normal_markup = formset.cleaned_data[
                     items.index(item)
                ]['normal_markup']

            retail_markup = formset.cleaned_data[
                    items.index(item)
                ]['retail_markup']

            product.wholesale_price = (
                    item.unit_cost *
                    (1 + (wholesale_markup / 100))
                )

            product.normal_price = (
                    item.unit_cost *
                    (1 + (normal_markup / 100))
                )

            product.retail_price = (
                    item.unit_cost *
                    (1 + (retail_markup / 100))
                )

            product.save()

            stock_entry.total_cost = total_cost

            stock_entry.save()

            if stock_entry.supplied_on_credit:

                supplier = stock_entry.supplier

                supplier.balance_due += total_cost

                supplier.save()

            return redirect('product_list')

    else:

        form = StockEntryForm()

        formset = StockEntryItemFormSet()

    context = {
        'form': form,
        'formset': formset
    }

    return render(
        request,
        'manager/register_stock.html',
        context
    )

def add_product(request):

    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('product_list')

    else:
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, 'manager/add_product.html', context)

def edit_product(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':

        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            return redirect('product_list')

    else:
        form = ProductForm(instance=product)

    context = {
        'form': form
    }

    return render(request, 'manager/edit_product.html', context)

def delete_product(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':

        product.delete()

        return redirect('product_list')

    context = {
        'product': product
    }

    return render(request, 'manager/delete_product.html', context)