from django.test import TestCase
from todos.models import Todo

class TestTodoModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='my title', body='my body')

    def test_todo_title_content(self):
        todo = Todo.objects.get(id=1)
        data = f'{todo.title}'
        self.assertEqual(data, 'my title')

    def test_todo_body_content(self):
        todo = Todo.objects.get(id=1)
        data = f'{todo.body}'
        self.assertEqual(data, 'my body')
