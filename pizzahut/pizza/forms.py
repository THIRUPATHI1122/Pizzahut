from django import forms

class PizzaForm(forms.Form):     #django form class

    topping1 = forms.CharField(label='Topping1',max_length=100)
    topping2 = forms.CharField(label='Topping2',max_length=100)
    size = forms.ChoiceField(label='size',choices=[('small','small'),
                                                   ('medium','medium'),
                                                   ('large','large')])