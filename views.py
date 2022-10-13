from django.shortcuts import render
from django.views.generic import TemplateView
from backend.chat import chat


class mainpage(TemplateView):
    Template_view = "index.html"

    def get(self, request):
        return render(request, self.Template_view)

    def post(self, request):
        if request.method == 'POST':
            user = request.POST.get('input', False)
            context = {"user": user, "bot": chat(request)}

        return render(request, self.Template_view, context)
