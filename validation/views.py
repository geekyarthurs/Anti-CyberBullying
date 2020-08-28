from django.shortcuts import render, redirect
from django.contrib import messages

import time

message_obj_list = []


def home(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        print(name, email, message)
        if not message == "offensive text":
            message_obj = {"name": name, "email": email, "message": message}
            message_obj_list.append(message_obj)
        else:
            messages.error(
                request, f"Your post was detected as offensive and has been removed by our system")
            redirect("/")
    return render(request, 'index.html', context={"posts": message_obj_list})
