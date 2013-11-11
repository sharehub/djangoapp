from django.db import models

# Create your models here.
class SearchKey(models.Model):
    queryEnc = models.CharField(max_length=512)
    queryExt = models.CharField(max_length=128)
    listNum = models.DecimalField(decimal_places=1, max_digits=10)
    displayNum = models.DecimalField(decimal_places=1, max_digits=10)
    bdFmtDispNum = models.CharField(max_length=64)
    bdSearchTime = models.CharField(max_length=32)
    bdIsClustered = models.CharField(max_length=16)
    
    def __unicode__(self):
        return self.queryExt


class SearchData(models.Model):
    key = models.ForeignKey(SearchKey)
    thumbURL = models.URLField(max_length=512)
    middleURL = models.URLField(max_length=512)
    largeTnImageUrl = models.URLField(max_length=512)
    hasLarge = models.BooleanField()
    hoverURL = models.URLField(max_length=512)
    pageNum = models.DecimalField(decimal_places=1, max_digits=10)
    objURL = models.CharField(max_length=512)
    fromURL = models.CharField(max_length=512)
    fromURLHost = models.URLField()
    currentIndex = models.CharField(max_length=32)
    width = models.DecimalField(decimal_places=1, max_digits=10)
    height = models.DecimalField(decimal_places=1, max_digits=10)
    type = models.CharField(max_length=8)
    filesize = models.CharField(max_length=32)
    bdSrcType = models.BooleanField()
    di = models.CharField(max_length=32)
    bis = models.CharField(max_length=32)
    hasThumbData = models.BooleanField()
    bdSetImgNum = models.BooleanField()
    bdImgnewsDate = models.DateTimeField()
    fromPageTitle = models.CharField(max_length=512)
    fromPageTitleEnc = models.CharField(max_length=512)
    bdSourceName = models.CharField(max_length=512)
    bdFromPageTitlePrefix = models.CharField(max_length=512)
    isAspDianjing = models.BooleanField()
    token = models.CharField(max_length=512)
    imgType = models.CharField(max_length=32)
    source_type = models.CharField(max_length=32)

    def __unicode__(self):
        return self.fromURLHost
