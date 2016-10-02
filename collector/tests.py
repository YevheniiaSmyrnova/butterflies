# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.utils import timezone

from collector.models import Collector
from exhibition.models import Exhibition, Collection
from sponsors.models import Sponsor


def insert_exhibitions():
	new_user_1 = User.objects.create(username='user_1')
	new_collector_1 = Collector.objects.create(
							name='new_user_1',
							surname='new_user_1',
							date_of_birth='1985-11-26',
							email='new_user_1@ukr.net',
							phone='222 22 55 896',
							address='г. Харьков',
							skype='user_1')
	new_sponsor_1 = Sponsor.objects.create(
							user=new_user_1,
							date_of_birth='1985-11-27',
							gender='M',
							phone='778 95 45 785',
							address='г. Харьков',
							skype='user_2',
							description='Руководитель')
	new_collection_1 = Collection.objects.create(
							name='collection_1',
							description='Some info',
							collector=new_collector_1)
	new_collection_2 = Collection.objects.create(
							name='collection_2')
	new_exhibition_1 = Exhibition.objects.create(
							name='new_exhibition_1',
							date='2016-01-12',
							short_description='Some info',
							collection=new_collection_1)
	new_exhibition_2 = Exhibition.objects.create(
							name='new_exhibition_2',
							date=timezone.now(),
							short_description='Some info',
							collection=[new_collection_2])


class CoursesListTest(TestCase):
	def setUp(self):
		self.client = Client()
		insert_exhibitions()

	def test_new_course(self):
		self.assertEqual(Exhibition.objects.all().count(), 2)

	def test_page_course(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'new_exhibition_2')
		self.assertTemplateUsed(response, 'index.html')
    
	def test_link_add_edit_remove_course(self):
		response = self.client.get('/')
		self.assertContains(response, '/exhibition/add/')
		for i in range(1, 3):
			self.assertContains(response, '/exhibition/edit/{}/'.format(i))
			self.assertContains(response, '/exhibition/remove/{}/'.format(i))
