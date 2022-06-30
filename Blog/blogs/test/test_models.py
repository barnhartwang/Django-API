from django.test import TestCase
from blogs.models import Blog
from django.contrib.auth.models import User

class BlogModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
       #Create a User
       test_user = User.objects.create_user(username = 'testuser', password = 'password') 
       test_user.save()

       #create a blog post
       test_post = Blog.objects.create(author = test_user, title = 'title', body = 'body')
       test_post.save()

    def test_blog_content(self):
        blog = Blog.objects.get(id=1)
        author = f'{blog.author}'
        title = f'{blog.title}'
        body = f'{blog.body}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'title')
        self.assertEqual(body,'body')