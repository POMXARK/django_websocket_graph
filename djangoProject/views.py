from django.forms import  formset_factory
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
import requests
from app.forms import  AddPostFormAi1, AddPostFormAi2
from app.models import Ai1, Ai2


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    """
    Render a template. Pass keyword arguments from the URLconf to the context.
    """
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        global form, data, tables
        username = self.request.user.username

        if username == 'user1':
            data = Ai1.objects.values()
            table_form_set = formset_factory(AddPostFormAi1, extra=0)
            form = table_form_set(initial=data)
            tables = requests.get('http://127.0.0.1:8000/api/tables-1').json()
        if username == 'user2':
            data = Ai2.objects.values()
            table_form_set = formset_factory(AddPostFormAi2, extra=0)
            form = table_form_set(initial=Ai2.objects.values())
            tables = requests.get('http://127.0.0.1:8000/api/tables-2').json()

        if len(data) == 0:
            return self.render_to_response(context=[])
        data = {
            "title_page": "Api",
            "title": f"Welcome, {username}! Thanks for logging in.",
            "table_title": ["id", "current", "sts"],
            "qs": data,
            "form": form,
            "tables": tables,
            "username": username,
        }
        return self.render_to_response(context=data)
