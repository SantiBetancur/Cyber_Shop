from django import forms
from StoreBranch.models import Branch, Stock

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

