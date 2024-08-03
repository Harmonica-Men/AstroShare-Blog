from django import forms
from .models import Post, Category, Comment, Subscriber


# Hardcode the list
# choices = [('coding', 'coding'), ('sports', 'sports'), ('voetbal', 'voetbal')]
choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'image')
# widgits are magic
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name', 'id': 'js_id', 'type': 'hidden'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control','placeholder': 'choice'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        # fields = ('title', 'title_tag', 'author', 'category', 'body', 'image')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'placeholder test'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }


def subscribe(request):
    email = request.GET.get('email')
    if email:
        subscriber, created = Subscriber.objects.get_or_create(email=email)
        if created:
            send_confirmation_email(subscriber)
            return HttpResponse("Subscription successful! Please check your email to confirm.")
        else:
            return HttpResponse("This email is already subscribed.")
    return HttpResponse("Please provide an email address.")

def confirm_email(request, confirmation_code):
    try:
        subscriber = Subscriber.objects.get(confirmation_code=confirmation_code)
        subscriber.is_confirmed = True
        subscriber.save()
        return HttpResponse("Email confirmed successfully!")
    except Subscriber.DoesNotExist:
        return HttpResponse("Invalid confirmation code.")

def send_confirmation_email(subscriber):
    confirmation_link = f"{settings.SITE_URL}/confirm/{subscriber.confirmation_code}/"
    send_mail(
        'Confirm your subscription',
        f'Please confirm your subscription by clicking the following link: {confirmation_link}',
        settings.DEFAULT_FROM_EMAIL,
        [subscriber.email],
        fail_silently=False,
    )
