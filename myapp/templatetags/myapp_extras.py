from django import template
from myapp.models import Blog

register = template.Library()

# @register.inclusion_tag('base.html')
@register.simple_tag
def show_latest_blogs(count=5):
    return Blog.objects.order_by('-created_on')[:count]