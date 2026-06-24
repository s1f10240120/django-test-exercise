from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from todo.models import Task

# Create your tests here.
class TodoTestCase(TestCase):
    def test_sample1(self):
        self.assertEqual(1 + 2, 3)

class TaskModelTestCase(TestCase):
    def test_task_creation(self):
        due = timezone.make_aware(datetime(2024, 6, 30, 23, 59, 59))
        task = Task(title="task1", due_at=due, completed=False)
        task.save()

        task = Task.objects.get(pk=task.pk)
        self.assertEqual(task.title, "task1")
        self.assertEqual(task.due_at, due)
        self.assertFalse(task.completed)

def test_create_task2(self):
    task =Task(title='task2')
    task.save()

    task = Task.objects.get(pk=task.pk)
    self.assertEqual(task.title, 'task2')
    self.assertFalse(task.completed)
    self.assertEqual(task.due_at, None)