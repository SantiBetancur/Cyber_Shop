from django import forms
from StoreBranch.models import Branch,Product

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

