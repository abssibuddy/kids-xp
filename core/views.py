from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "<h1>kids-xp</h1>"
        "<p>Admin: <a href='/admin/'>/admin/</a></p>"
    )
