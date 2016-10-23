"""
Collector detail endpoint tests module
"""
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_dynamic_fixture import G
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, \
    HTTP_401_UNAUTHORIZED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
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
        self.inst = G(Collector)
        self.url = reverse("collector_api_urls:collector_detail",
                           kwargs={"pk": self.inst.id})
        self.bad_url = reverse("collector_api_urls:collector_detail",
                               kwargs={"pk": 0})

    def test_get_successful(self):
        """
        Test get successful collector detail
        """
        response = self.client.get(self.url)
        self.assertEqual(HTTP_200_OK, response.status_code)
        # import ipdb;ipdb.set_trace()
        self.assertEqual(self.inst.name, response.data.get('name'))

    def test_get_fail(self):
        """
        Test not found case
        """
        response = self.client.get(self.bad_url)
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code)

    def test_put_fail(self):
        """
        Test not found case
        """
        user = User.objects.create()
        token, is_created = Token.objects.get_or_create(user=user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Token {}".format(token.key))
        put_data = {'name': 'Test'}
        response = self.client.delete(self.bad_url, data=put_data)
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code)

    def test_put_fail_unauthorized(self):
        """
        Test unauthorized case
        """
        put_data = {'name': 'Test'}
        response = self.client.put(self.url, data=put_data)
        self.assertEqual(HTTP_401_UNAUTHORIZED, response.status_code)

    def test_put_successful(self):
        """
        Test success case
        """
        user = User.objects.create()
        token, is_created = Token.objects.get_or_create(user=user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Token {}".format(token.key))
        put_data = {'name': 'Test'}
        response = self.client.put(self.url, data=put_data)
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(response.data.get('name'), 'Test')

    def test_put_fail_bad_request(self):
        """
        Test bad request case
        """
        user = User.objects.create()
        token, is_created = Token.objects.get_or_create(user=user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Token {}".format(token.key))
        put_data = {'date_of_birth': 123}
        response = self.client.put(self.url, data=put_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

    def test_delete_fail(self):
        """
        Test not found case
        """
        user = User.objects.create()
        token, is_created = Token.objects.get_or_create(user=user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Token {}".format(token.key))
        response = self.client.delete(self.bad_url)
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code)

    def test_delete_fail_unauthorized(self):
        """
        Test unauthorized case
        """
        response = self.client.delete(self.url)
        self.assertEqual(HTTP_401_UNAUTHORIZED, response.status_code)

    def test_delete_successful(self):
        """
        Test success case
        """
        user = User.objects.create()
        token, is_created = Token.objects.get_or_create(user=user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Token {}".format(token.key))
        response = self.client.delete(self.url)
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)
