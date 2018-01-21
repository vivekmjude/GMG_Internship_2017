from django import forms
from .models import Order
from django.utils import timezone
from django_select2.forms import Select2MultipleWidget
from django.forms.widgets import SelectMultiple

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # super(OrderForm, self).__init__(*args, **kwargs)
        # self.fields['price_'] = forms.IntegerField()
        super(OrderForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        # if not(instance and instance.pk):
        #     self.instance.patient="Miss Chanandler Bong"
        if instance and instance.pk:
            self.fields['provider'].widget.attrs['readonly'] = True
            # self.fields['casenum'].widget.attrs['readonly'] = True
            s=self.instance.status
            if s=='Processing' or s=='Shipped from Lab' or s=='Arriving Today' or s=='Received by Provider' or s=='Completed':
                self.fields['patient'].widget.attrs['readonly'] = True
                self.fields['teethnum'].widget.attrs['readonly'] = True
                self.fields['product'].widget.attrs['readonly'] = True
                self.fields['expecteddate'].widget.attrs['readonly'] = True
                self.fields['location'].widget.attrs['readonly'] = True
                self.fields['remarks'].widget.attrs['readonly'] = True
    class Meta:
        model=Order
        # fields=['casenum','provider','patient','product','teethnum','location','expecteddate','status','remarks']
        fields=['provider','patient','product','teethnum','location','expecteddate','remarks']
        casenum =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
        provider =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))

    def clean_expecteddate(self):
        expecteddate=self.cleaned_data.get('expecteddate')
        if expecteddate<timezone.now().date():
            raise forms.ValidationError("Please enter a valid expected date")
        return expecteddate
    teethnum=forms.MultipleChoiceField(
    choices=[(x, x) for x in range(1, 33)],
    widget=Select2MultipleWidget,
    required=True,
    label='Tooth No.'
    )


    # def pricing(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         if instance.product == 'PFM High Noble':
    #             instance.price=123
