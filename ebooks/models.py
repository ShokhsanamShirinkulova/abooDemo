from django.db import models


class AbooMain(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    imgUrl = models.CharField(max_length=100)
    fileUrl = models.CharField(max_length=100)

# Create / Insert / Add  => Post
# Retrieve / Fetch => Get
# Update / Edit  => Put
# Delete / Remove  => Delete
    def __set__(self, instance, value):
        return self.title
