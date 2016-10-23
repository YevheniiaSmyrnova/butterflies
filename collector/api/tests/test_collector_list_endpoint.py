"""
Collector list endpoint tests module
"""
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_dynamic_fixture import G
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, \
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase

from collector.models import Collector


class CollectorListEndpointTests(APITestCase):
    """
    Test for collector list endpoint
    """
    def setUp(self):
        """
        Setup params
        """
        self.url = reverse("collector_api_urls:collectors_list")

    def test_get_successful(self):
        """
        Test get successful collector list
        """
        G(Collector)
        response = self.client.get(self.url)
        self.assertEqual(HTTP_200_OK, response.status_code)
        expected_key = {
            "id",
            "name",
            "surname",
            "date_of_birth",
            "email",
            "photo",
            "phone",
            "address",
            "skype"
        }
        self.assertEqual(expected_key,
                         set(response.data.get("results")[0].keys()))

    def test_post_fail(self):
        """
        Test unauthorized case
        """
        response = self.client.post(self.url)
        self.assertEqual(HTTP_401_UNAUTHORIZED, response.status_code)

    def test_post_successful(self):
        """
        Test success case
        """
        user = User.objects.create()
        token, is_created = Token.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION="Token {}".format(token.key))
        post_data = {
            "phone": 1,
            "email": "test@example.com",
            "name": "test",
            "surname": "test",
            "date_of_birth": "2016-02-01"
        }
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(HTTP_201_CREATED, response.status_code)
        expected_keys = {
            "id",
            "name",
            "surname",
            "date_of_birth",
            "email",
            "photo",
            "phone",
            "address",
            "skype"
        }
        self.assertEqual(expected_keys, set(response.data.keys()))

    def test_post_fail_bad_request(self):
        """
        Test bad request case
        """
        user = User.objects.create()
        token, is_created = Token.objects.get_or_create(user=user)
        self.client.credentials(
         HTTP_AUTHORIZATION="Token {}".format(token.key))
        response = self.client.post(self.url)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)
        expected_keys = {
            "name",
            "surname",
            "date_of_birth",
            "email",
            "phone",
        }
        self.assertEqual(expected_keys, set(response.data.keys()))
