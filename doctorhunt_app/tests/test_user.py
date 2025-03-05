from django.test import TestCase
from ..models.user_model import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", password="testpass")
        self.assertEqual(user.email, "test@example.com")
