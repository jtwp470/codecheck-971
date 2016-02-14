from django.db import models


class Projects(models.Model):
    """
    id integer PRIMARY_KEY AUTOINCREMENT,
    url varchar(255) NULL,
    title varchar(255) NOT NULL,
    description text NOT NULL,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
    """
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
