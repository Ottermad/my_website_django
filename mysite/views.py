from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from mysitedjango.settings import SENDGRID_PASSWORD, SENDGRID_USERNAME
from .models import Post, Project
from .forms import Contact
from markdown import markdown

import sendgrid

SENDGRID = sendgrid.SendGridClient(SENDGRID_USERNAME, SENDGRID_PASSWORD)

def posts_listing(request):
    posts = Post.objects.all()
    return render(request, 'mysite/posts_listing.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    html_body = mark_safe(markdown(post.body))
    return render(request, 'mysite/post_detail.html', {'post': post, 'html_body': html_body})


def projects_listing(request):
    projects = Project.objects.all()
    return render(request, 'mysite/projects_listings.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    html_description = mark_safe(markdown(project.description))
    return render(request, 'mysite/project_detail.html', {'project': project, 'html_description': html_description})


def about(request):
    return render(request, 'mysite/about.html')


def contact(request):
    if request.POST:
        message = sendgrid.Mail()
        message.add_to('charlie.thomas@attwoodthomas.net')
        message.set_subject(request.POST['name'])
        message.set_text(request.POST['body'])
        message.set_from(request.POST['email'])

        try:
            SENDGRID.send(message)
            print("Sent")
        except sendgrid.SendGridClientError:
            print("Client Error")
        except sendgrid.SendGridServerError:
            print("Server Error")

    form = Contact(auto_id='%s')
    return render(request, 'mysite/contact.html', {'form': form})
    pass

