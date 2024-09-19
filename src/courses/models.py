from django.db import models






class AccessReq(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email Required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMMING_SOON = "soon", "Comming Soon"
    DRAFT = "draft", "Draft"
class Course(models.Model):

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
   
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices, 
        default=PublishStatus.DRAFT
        )
    access = models.CharField(
        max_length=10, 
        choices=AccessReq.choices, 
        default=AccessReq.DRAFT
        )

    @property

    def is_publised(self):
        return self.status == PublishStatus.PUBLISHED
