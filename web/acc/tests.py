from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomerTests(TestCase):
    def tesr_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username="mamad",email="my@gmail.com",password="qwe1!"
        )
        self.assertEqual(user.username,"mamad")
        self.assertEqual(user.email,"my@gmail.com")
        self.assertTrue(user.is_Active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username="sup",email="sup@gmail.com",password="sup@gmail.com"
        )
        self.assertEqual(admin_user,"sup")
        self.assertEqual(admin_user.email,"sup@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
        