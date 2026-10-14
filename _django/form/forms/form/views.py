from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def result(request):
    if request.method == "POST":
        request.session["name"] = request.POST["name"]
        request.session["location"] = request.POST["location"]
        request.session["language"] = request.POST["language"]
        request.session["comment"] = request.POST["comment"]
    context = {
        "name": request.session["name"],
        "location": request.session["location"],
        "language": request.session["language"],
        "comment": request.session["comment"],
    }

    return render(request, "result.html", context=context)
