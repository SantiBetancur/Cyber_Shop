from django import forms
from StoreBranch.models import Branch,Product

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = [
            "branchId","address"
        ]

