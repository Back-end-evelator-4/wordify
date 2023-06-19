from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if request.user.is_authenticated:
                full_name = []
                if request.user.first_name:
                    full_name.append(request.user.first_name.title())
                if request.user.last_name:
                    full_name.append(request.user.last_name.title())
                if full_name:
                    name_full = " ".join(full_name)
                else:
                    name_full = request.user.username
                obj.name = name_full
                if request.user.email:
                    obj.email = request.user.email
            obj.save()
            messages.success(request, 'your message was successfully accepted')
            return redirect('contact:contact')
        messages.info(request, 'your message was not accepted')
        return redirect('.')
    ctx = {
        'form': form
    }
    return render(request, 'contact/contact.html', ctx)
