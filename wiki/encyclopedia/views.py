from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import util,forms
from random import choice
from django.urls import reverse
form = forms.SearchForm()

def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": form
    })

def get_page(request, title):

    page = util.get_entry(title)   

    if page is None:
         return render(request, "encyclopedia/error404.html", {
            "form": form
        })
    
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content": page,
        "form": form
    })

def new_page(request):
    if request.method == "POST":
        new_form = forms.BaseForm(request.POST)
        if new_form.is_valid():
            title = new_form.cleaned_data["title"]          
            content = new_form.cleaned_data["content"]            
            for entry in util.list_entries():
                if title.lower() == entry.lower(): 
                    return render(request, "encyclopedia/new.html", {
                        "new_form": forms.BaseForm(),
                        "form": form,
                        "error409": entry,
                    })
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("wiki:title", kwargs={'title': title}))   
    return render(request, "encyclopedia/new.html", {
        "new_form": forms.BaseForm(),
        "form": form
    })

def edit_page(request, title):       
    content = util.get_entry(title)
    edit_form = forms.EditForm(initial={'title': title,'content': content})
    if edit_form.is_valid():
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "form": form,
            "edit_form": edit_form,
        })
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "form": form,
            "edit_form": edit_form,
        })

def save_page(request):
    edit_form = forms.EditForm(request.POST)
    if edit_form.is_valid():
        title = edit_form.cleaned_data["title"]
        content = edit_form.cleaned_data["content"]        
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("wiki:title", kwargs={'title': title}))

    else:
        return render(request, "encyclopedia/edit.html",{
            "form":form,
            "edit_form":edit_form
            
        })

def random_page(request):    
    return HttpResponseRedirect(reverse("wiki:title", kwargs={'title': choice(util.list_entries())}))

def search_page(request):
    if request.method == "GET":
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data["search"].lower()
            entries = util.list_entries()

            pages_found = [page for page in entries if search in page.lower()]

            if len(pages_found)==0:
                return render(request, "encyclopedia/search.html", {
                    "error409": True,
                    "form": form
                })
            
            elif len(pages_found) == 1 and pages_found[0].lower() == search:
                
                title = pages_found[0]
                return HttpResponseRedirect(reverse("wiki:title", kwargs={'title': title}))

            else:
                title = [page for page in pages_found if search == page.lower()]
                if len(title)>0:
                    return get_page(request, title[0])
                else:
                    return render(request, "encyclopedia/search.html", {
                    "found": pages_found,
                    "form": form
                })

        else: 
            return index(request)
    
    return index(request)