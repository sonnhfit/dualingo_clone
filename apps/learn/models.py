from django.db import models

# Create your models here.


class Level(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)


class Chapter(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    img = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)

    def __str__(self):
        return self.title
#

# class SinhVien(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#
#
# class LopHoc(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#
#
# class SinhVienLopHoc(models.Model):
#     sv = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
#     lop = models.ForeignKey(LopHoc, on_delete=models.CASCADE)

