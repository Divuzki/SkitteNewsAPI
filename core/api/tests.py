from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.authtoken.models import Token
# automated
# new / blank db
from ..models import Post
User = get_user_model()

class PostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User.objects.create(username='divine', email='divine@gmail.com')
        user_obj.set_password("12341234qq")
        user_obj.save()
        post = Post.objects.create(
            user=user_obj,
            source='newyorkpost', 
            author='divine', 
            title="new title", 
            content='hey ppl'
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = Post.objects.count()
        self.assertEqual(post_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse("api-post:post-listcreate")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print(response.data)

    def test_post_list(self):
        data = {"title":"hello world", "content":"hey my name is david"}
        url = api_reverse("api-post:post-listcreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        post = Post.objects.first()
        data = {}
        url = post.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print(response.data)

    def test_update_item(self):
        post = Post.objects.first()
        url = post.get_api_url()
        data = {"title":"hello world", "content":"hey my name is david"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
   
    def test_update_item_with_user(self):
        post = Post.objects.first()
        print(post.content)
        url = post.get_api_url()
        data = {"title":"hello world", "content":"hey my name is david"}
        user_obj = User.objects.first()
        token = Token.objects.filter(user_id=user_obj.id)
        token_rsp = token.first()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token_rsp}')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_post_list(self):
        user_obj = User.objects.first()
        token = Token.objects.filter(user_id=user_obj.id)
        token_rsp = token.first()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token_rsp}')
        data = {"title":"hello world", "content":"hey my name is david"}
        url = api_reverse("api-post:post-listcreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
