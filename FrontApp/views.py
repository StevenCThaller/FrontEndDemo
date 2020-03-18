from django.shortcuts import render

# Create your views here.
def index(request):
    somedata = [
        { "id": 1, "name": "John Doe", "email": "jdoe@gmail.com" },
        { "id": 2, "name": "Jane Doe", "email": "jane-doe@gmail.com" },
        { "id": 3, "name": "Billy Bob", "email": "bbob@hotmail.com" },
        { "id": 4, "name": "Jill Personman", "email": "jpman@aol.net" },
        { "id": 5, "name": "Johnny Applenotseed", "email": "fooledyou@haha.com" }
    ]


    context = {
        # Anything inside of here
        # can be referenced in HTML
        # by just {{}} with the key name
        # inside of the jinja stuff
        "list_of_things": somedata,
        "one_name": "toenail clippings"
    }
    return render(request, "index.html", context)
