import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from tasks.models import Task

# task = Task.objects.create(
#     title="Test",
#     description="",
#     creator_id=1
# ).save

# task = Task.objects.get(id=1)
# print(task.title)

# task_update = Task.objects.get(id=1)
# task_update.title = "Do my homework"
# task_update.save()
# print(task.title)

# task_update = Task.objects.get(id=1)
# task_update.status = "DONE"
# task_update.save()
# print(task_update.status)

# task_delete = Task.objects.get(id=1)
# task_delete.delete()