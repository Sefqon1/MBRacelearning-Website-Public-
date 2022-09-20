from django.test import TestCase, SimpleTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import ContactForm
from .models import Post


# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_impressum_page_status(self):
        response = self.client.get("/impressum/")
        self.assertEqual(response.status_code, 200)

    def test_datenschutz_page_status(self):
        response = self.client.get("/datenschutz/")
        self.assertEqual(response.status_code, 200)



class TestForms(SimpleTestCase):
    def test_contact_form_valid(self):
        form = ContactForm(
            data={
                "from_email": "test@test.de",
                "name": "Testiboy",
                "subject": "Testing this",
                "message": "Hello this is a test",
                "languagelevel": "a1",
            }
        )

        self.assertTrue(form.is_valid())

    def test_contact_from_invalid(self):
        form = ContactForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
            cover= SimpleUploadedFile("file.jpeg","file_content", content_type=("image/jpeg"))
        )

    """def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
        self.assertEqual(f'{self.post.cover}', 'file.jpeg')

    def test_blog_page_status(self):
        response = self.client.get("blog/")
        self.assertEqual(response.status_code, 200)
        self.assertContaints(response, 'Nice body conent')
        self.assertTemplateUsed(Response, 'blog.html')

    def test_post_detail_view(self):
        response = self.client.get('/blogpost/1/')
        response = self.client.get('/blogpost/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blogpost.html')"""