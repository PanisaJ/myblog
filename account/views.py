from django.shortcuts import render

# Create your views here.
def test_templatetags(request):
    return render(request, 'account/test.html')