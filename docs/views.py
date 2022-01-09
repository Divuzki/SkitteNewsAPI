
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from core.models import Post
from core.api.serializers import PostSerializer

# Third Party
from rest_framework import generics
from rest_framework.reverse import reverse as api_reverse
from rest_framework.authtoken.models import Token
# Function based views to Class Based Views

def docs_view(request, *args, **kwargs):
    context = {
        "nav": "nav"
    }
    return render(request, "docs.html", context)

def docs_usage_installation_view(request, *args, **kwargs):
    user = request.user
    user_id = user.id
    data = Token.objects.filter(user_id=user_id)
    data = data.first()
    context = {
        "key": data,
        "nav": "nav"
    }
    return render(request, "usage.html", context)

def token_api_view(request):
    user = request.user
    user_id = user.id
    data = Token.objects.filter(user_id=user_id)
    data = data.first()
    context = {
        "key": data,
        "nav": "nav"
    }
    return render(request, 'yourAPIkey.html', context)

class DevAPIView(generics.ListAPIView):
    """
    CONSUME BY JAVASCRIPT | SWIFT | JAVA | IOS | ANDRIOD | PYTHON | Go and so on...
    Note: YOUR ```API KEY``` IS ```NOT``` MENT TO BE SHARED BY OTHERS
    """
    lookup_field = 'pk' #slug or id # url(r'?P<pk>\d+')
    serializer_class = PostSerializer

    def get_queryset(self):
        data = 'Loading...'
        apikey = self.request.GET.get("key")
        if apikey == None:
            data = 'You will need to insert api key into "?key=<yourapikey>" in url'
        else:
            data = Token.objects.filter(key=apikey)
            # if data == None:
            #     data = 'WRONG API KEY'
            #     print(data)
            if data.exists():
                data = Token.objects.get(key=apikey)
                if data:
                    data = Post.objects.all()
            else:
                data = {
                "message":"wrong api key",
                "help":"you will need to insert api key into '?key=<yourapikey>' in url",
                "status":"No User With Api Key `status =>`401"
                }
                # data = 'WRONG API KEY'
        return data
