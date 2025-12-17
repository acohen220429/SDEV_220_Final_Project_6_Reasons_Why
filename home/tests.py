from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class LoginRedirectTests(TestCase):
	def setUp(self):
		User = get_user_model()
		self.user = User.objects.create_user(username='alice', password='pass')

	def test_login_redirects_to_index(self):
		login_url = reverse('login')
		resp = self.client.post(login_url, {'username': 'alice', 'password': 'pass'}, follow=True)
		# final path should be index (/)
		self.assertEqual(resp.request['PATH_INFO'], reverse('index'))

	def test_login_ignores_next_and_redirects_to_index(self):
		login_url = reverse('login') + '?next=' + reverse('appointments_list')
		# perform post including the next param
		resp = self.client.post(login_url, {'username': 'alice', 'password': 'pass', 'next': reverse('appointments_list')}, follow=True)
		self.assertEqual(resp.request['PATH_INFO'], reverse('index'))

class IndexIconsTest(TestCase):
	def test_index_contains_svg_icons(self):
		resp = self.client.get(reverse('index'))
		self.assertContains(resp, '<svg', status_code=200)

# Create your tests here.
