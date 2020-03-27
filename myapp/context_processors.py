import datetime
from .models import Blog

def get_current_year_to_context(request):
    current_datetime = datetime.datetime.now()
    return {
        'current_year': current_datetime.year
    }

def get_latest_blogs(request):
    blog = Blog.objects.order_by('-created_on')[:5]
    return { 'latest_blog' : blog }