from django.db import models

# Create your models here.

class MyModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.title}"
    

class NewModel(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    file = models.FileField(upload_to='uploads/')
    # file_path = models.FilePathField(path='/first_app/')

    float_val = models.FloatField()
    # foreign_key = models.ForeignKey(MyModel, on_delete=models.CASCADE)

    ipVal = models.GenericIPAddressField()
    file = models.FileField()

    # int_val = models.IntegerField()

    pos_int = models.PositiveBigIntegerField()
    pos_big_int = models.PositiveBigIntegerField()
    pos_small_int = models.PositiveSmallIntegerField()

    slug_text = models.SlugField()
    small_int = models.SmallIntegerField()

    text = models.TextField()
    time = models.TimeField()

    # uuid = models.UUIDField()
    

    # auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    # big_integer_field = models.BigIntegerField()
    # text = models.CharField(max_length=255)

    date = models.DateField()
    appointment = models.DateTimeField()

    value = models.DecimalField(max_digits = 5, decimal_places=2)
    duration = models.DurationField()

