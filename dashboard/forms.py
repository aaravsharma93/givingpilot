from django import forms


class CommentForm(forms.Form):
    message = forms.Textarea()
