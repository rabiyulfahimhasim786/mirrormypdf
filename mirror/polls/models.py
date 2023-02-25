from django.db import models

class Pdf(models.Model):
    link = models.CharField(max_length=255)
    data = models.FileField(null=False, blank=False,  upload_to='pdf')
    description = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s %s" % (self.link, self.data, self.description)

    

class Pdfurl(models.Model):
    documentname = models.CharField(max_length=255)
    documenturl = models.URLField(null=False, blank=False, max_length=255)
    documenttype = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s %s" % (self.documentname, self.documenturl, self.documenttype)
 
