from django.db import models

# Create your models here.

class Model1(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'model1'


class Model2(models.Model):
    model1 = models.ForeignKey(Model1, on_delete=models.CASCADE, related_name='model2_rn')
    model2_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'model2'
