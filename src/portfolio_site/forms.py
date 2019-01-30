from django import forms

class ContactForm(forms.Form):
    # nput type="text" placeholder="Name" id="name" name="name" class="form-control" required
    # type="email" placeholder="Email" id="email" name="email" class="form-control"
    # type="text" placeholder="Subject" id="subject" name="subject" class="form-control" 
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message...'}))
