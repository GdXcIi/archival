from django.test import TestCase
from users.models import User
from .models import ContentBlock

# Create your tests here.
class ContentBlockTest(TestCase):
    def test_image_without_source_fails(self):
        user = User.objects.create(username="test", role="student")
        block = ContentBlock.objects.create(
            author=user,
            content_type="image"
        )
        self.assertEqual(block.sources.count(), 0)