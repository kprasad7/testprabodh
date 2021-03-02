from django.shortcuts import render
from django.template import Context, Template
from django.template import RequestContext


def handler404(request, exception, template_name="404/index.html"):
    response = render("quiz/404.html")
    response.status_code = 404
    return response