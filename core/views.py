from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'

class AllProjectsView(TemplateView):
    template_name = 'all-projects.html'