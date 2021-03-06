from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label="Email (optional)")
    message = forms.CharField(widget=forms.Textarea)

    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     numwords= len(message.split())
    #     if numwords <4:
    #         raise forms.ValidationError("Not enough Words!!")
    #     return message
