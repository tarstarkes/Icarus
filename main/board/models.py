from django.db import models
import datetime
# Create your models here.
class EventsMeetinglocation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'events_meetinglocation'
    def __str__(self):
    	return self.name

class EventsDocumenttype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'events_documenttype'
    def __str__(self):
    	return self.name

class EventsDocument(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    url = models.FileField(upload_to="static/documents/board/uploaded/minutes&agenda/", null=True)
    type_id = models.ForeignKey(EventsDocumenttype)

    class Meta:
        managed = True
        db_table = 'events_document'
    def __str__(self):
    	return self.title

class EventsBoardmeeting(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    agenda_id = models.ForeignKey(EventsDocument, null=True, blank=True, related_name="agenda_id")
    location_id = models.ForeignKey(EventsMeetinglocation)
    minutes_id = models.ForeignKey(EventsDocument, null=True, blank=True, related_name="minutes_id")

    class Meta:
        managed = True
        db_table = 'events_boardmeeting'
    def __str__(self):
    	return self.location_id.name