from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Post

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"

class ImpressumView(TemplateView):
    template_name = "impressum.html"


class DatenschutzView(TemplateView):
    template_name = "datenschutz.html"


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "You received a message from: " + form.cleaned_data["name"]
            from_email = form.cleaned_data["from_email"]
            message = (
                form.cleaned_data["name"]
                + " is interested in a "
                + form.cleaned_data["lessontype"]
                + " lesson."
                + "\n"
                + form.cleaned_data["name"]
                + "'s current language level is: "
                + form.cleaned_data["languagelevel"]
                + ", and he/she wants to book a "
                + form.cleaned_data["lessonduration"]
                + " minute lesson."
                + "\nThe student is interested in booking a "
                + form.cleaned_data["lessonpackage"]
                + "lesson/session package"
                + "\n\nThe senders personal message to you is: \n"
                + form.cleaned_data["message"]
                + "\n\nThe senders email address is: "
                + form.cleaned_data["from_email"]
            )
            try:
                send_mail(subject, message, from_email, ["11morgss@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "contact.html", {"form": form})


def successView(request):
    return HttpResponseRedirect("/")


class BlogPageView(ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 9


class BlogPostView(DetailView):
    model = Post
    template_name = "blogpost.html"

