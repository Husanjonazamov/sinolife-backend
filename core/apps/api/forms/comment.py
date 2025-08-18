from django import forms

from core.apps.api.models import CommentModel


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = "__all__"
