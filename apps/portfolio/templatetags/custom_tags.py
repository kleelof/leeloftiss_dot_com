from django import template
from apps.portfolio.models import Page, Technology

register = template.Library()


@register.simple_tag
def get_menu_info():
    return {
        'pages': Page.objects.all(),
        'technologies': Technology.objects.all()
    }