from django import forms


class ContactForm(forms.Form):
    """
    The ContactForm model is used inside of the contact page to receive emails.

    Those emails must come for the contact page on the site.

    Attributes
    ----------
    name    : CharField
        The name variable is used to get the name of the sender
    email   : EmailField
        The email field is used to get the senders email address
    subject : CharField
        The subject field is the subject of the email
    message : CharField
        The message field is used to gather the body of the email.
    """

    name = forms.CharField(widget=forms.TextInput(
                                    attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(
                                    attrs={'placeholder': 'Email'}))
    subject = forms.CharField(widget=forms.TextInput(
                                    attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(
                                    attrs={'placeholder': 'Your message...'}))
