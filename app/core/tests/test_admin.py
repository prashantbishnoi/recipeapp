from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Test for Admin page"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@abc.com',
            password='admin123'
        )
        self.user = get_user_model().objects.create_user(
            email='abc@abc.com',
            password='test123',
            name='Test User'
        )

        self.client.force_login(self.admin_user)

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        # generates url -> /admin/core/userlist
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_users_change_page(self):
        """Test that user details page has user details"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # generates url -> /admin/core/user/id#
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_users_add_page(self):
        """Test that user details page has user details"""
        url = reverse('admin:core_user_add')
        # generates url -> /admin/core/user/add
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
