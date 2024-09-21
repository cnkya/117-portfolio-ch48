from django.shortcuts import render

def projects_list(request):
    return render(request, "content/projects_list.html")

def experience_list(request):
    return render(request, "content/experience_list.html")