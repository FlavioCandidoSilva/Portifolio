from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
import logging

def index(request):
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('comment')

        subject = f'New Contact Form Submission from {name}'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

        try:
            sent_count = send_mail(subject, body, email, ['recipient@example.com'])  # Replace with the recipient's email
            logger.debug(f"Email sent successfully: {sent_count}")
            if sent_count > 0:
                message = 'Message sent successfully.'
            else:
                message = 'Message could not be sent.'
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            message = 'An error occurred while sending the message.'

    else:
        message = None

    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/index.html', {'posts': posts, 'message': message})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def contact_form(request):
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('comment')

        subject = f'New Contact Form Submission from {name}'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

        print(f"Name: {name}", flush=True)
        print(f"Email: {email}", flush=True)
        print(f"Message: {message}", flush=True)

        try:
            sent_count = send_mail(subject, body, email, ['recipient@example.com'])  # Replace with the recipient's email
            logger.debug(f"Email sent successfully: {sent_count}")
            if sent_count > 0:
                return JsonResponse({'message': 'Message sent successfully.'})
            else:
                return JsonResponse({'message': 'Message could not be sent.'})
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return JsonResponse({'message': 'An error occurred while sending the message.'})

    return render(request, 'index.html')
