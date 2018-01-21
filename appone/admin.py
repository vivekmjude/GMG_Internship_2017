# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Order,Product
from .forms import OrderForm
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
# from django_admin_bootstrapped.admin.models import SortableInline

admin.site.site_title='Portal'
admin.site.site_header='Provider Lab Portal'
admin.site.index_title='Home'
# admin.site.index_template = 'admin/index.html'
# admin.autodiscover()
def MarkOrderAsComplete(modeladmin, request, queryset):
    queryset.update(status='Completed')
MarkOrderAsComplete.short_description = "Mark selected order(s) as Completed"

def MarkOrderAsPlaced(modeladmin, request, queryset):
    # if queryset.get('status')=='Saved':
        queryset.update(status='Placed')
MarkOrderAsPlaced.short_description = "Mark selected order(s) as Placed"


class OrderAdmin(admin.ModelAdmin):

    class Media:
        css = {
            'all': ('/css/admin base.css',)
        }

    actions_on_top = False; actions_on_bottom = True
    list_display=('ordernum','casenum','orderdate','provider','patient','product','teethnum','location','expecteddate','daystodelivery','price','status')
    list_display_links=['ordernum']
    list_filter=(('casenum',DropdownFilter),('orderdate',DropdownFilter),('provider',DropdownFilter),
    ('patient',DropdownFilter),('product',DropdownFilter),('location',DropdownFilter),('expecteddate',DropdownFilter),('status',DropdownFilter))
    search_fields=('ordernum','casenum','orderdate','provider','patient','product','location','expecteddate','status')
    ordering = ['-casenum']
    list_per_page = 15
    date_hierarchy = 'expecteddate'
    actions = [MarkOrderAsPlaced,MarkOrderAsComplete]
    empty_value_display = '-empty-'
    form=OrderForm

class ProductAdmin(admin.ModelAdmin):
    list_display=('productname','cost')


admin.site.register(Order,OrderAdmin)
admin.site.register(Product,ProductAdmin)


#Entho Bootstrap Experiment class TestSortable(admin.StackedInline, SortableInline):
#     model = Order
#     extra = 0
