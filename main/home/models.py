from django.db import models
from django.contrib.gis.db import models
from django import forms
import datetime
import os

# Create your models here.
class Contactrole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'projectdb_contactrole'

class Organizationtype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abr = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'projectdb_organizationtype'

class Contacttype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    orgtype_id = models.ForeignKey(Organizationtype, db_column='orgType_id', null=True, blank=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'projectdb_contacttype'

class Statustype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'projectdb_statustype'

    def __str__(self):
        return (self.name)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    fiscalyear = models.IntegerField()
    publish = models.BooleanField()
    grmw_id = models.IntegerField()
    description = models.CharField(max_length=10000)
    notes = models.CharField(max_length=10000, blank=True, null=True)
    flickr = models.CharField(max_length=100, blank=True, null=True)
    status_id = models.ForeignKey(Statustype, blank=True, null=True)

    def __str__(self):
        return self.name

    def sponsorlist(self):
        sponsors = Organization.objects.filter(project=self,orgRole=1)
        return sponsors

    class Meta:
        managed = True
        ordering = ('name', 'fiscalyear')
        db_table = 'projectdb_project'

class Contact(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    contactrole_id = models.ForeignKey(Contactrole, db_column='contactRole_id', null=True, blank=True)  # Field name made lowercase.
    contacttype_id = models.ForeignKey(Contacttype, db_column='contactType_id', null=True, blank=True)  # Field name made lowercase.
    project_id = models.ForeignKey(Project, db_column='project_id', null=True, blank=True)

    class Meta:
        db_table = 'projectdb_contact'

class Organizationrole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'projectdb_organizationrole'

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    orgrole_id = models.ForeignKey(Organizationrole, db_column='orgRole_id', null=True, blank=True)  # Field name made lowercase.
    orgtype_id = models.ForeignKey(Organizationtype, db_column='orgType_id')  # Field name made lowercase.
    project_id = models.ForeignKey(Project, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'projectdb_organization'

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    contractnumber = models.CharField(db_column='contractNumber', max_length=50)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    fundingorg_id = models.ForeignKey(Organizationtype, db_column='fundingOrg_id', null=True, blank=True)  # Field name made lowercase.
    project_id = models.ForeignKey(Project, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'projectdb_contract'

    def __unicode__(self):
        return '%s - %s (%s)' % (self.fundingOrg, self.project, self.contractNumber)


class DateType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = "projectdb_datetype"

class Date(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project)
    type = models.ForeignKey(DateType)
    date = models.DateField()

    def __unicode__(self):
        return self.date.isoformat()

    class Meta:
        managed = True
        db_table = "projectdb_date"

class DocumentType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'projectdb_documenttype'

    def __str__(self):
        return (self.name)

def get_upload_path(instance, filename):
    return os.path.join( "static", "documents", "data", "project_documents", str(instance.project_id.id), filename)

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=get_upload_path, max_length=200)
    url = models.CharField(max_length=200, blank=True)
    note = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    project_id = models.ForeignKey(Project, null=True)
    type_id = models.ForeignKey(DocumentType)

    class Meta:
        managed = True
        db_table = 'projectdb_document'

    def __str__(self):
        return (self.type_id.name+" - "+self.project_id.name+" - "+str(self.date))

def get_image_path(instance, filename):
    return os.path.join( "static", "images", "data", "project_images", str(instance.project_id.id), filename)

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to=get_image_path, max_length=200)
    project_id = models.ForeignKey(Project, null=True)
    date = models.DateField()

    class Meta:
        managed = True
        db_table = 'projectdb_image'

    def __str__(self):
        return (self.project_id.name+" - "+self.name+" - "+str(self.date))

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    youtubeURL = models.CharField(max_length=200)
    project_id = models.ForeignKey(Project, null=True)
    date = models.DateField()

    class Meta:
        managed = True
        db_table = 'projectdb_video'

    def __str__(self):
        return (self.name+" - "+self.youtubeURL)

def get_ortho_path(instance, filename):
    return os.path.join( "static", "orthos", "data", "project_orthos", str(instance.project_id.id), filename)

class Ortho(models.Model):
    id = models.AutoField(primary_key=True)
    thumbFile = models.FileField(upload_to=get_ortho_path, max_length=200)
    downloadURL = models.CharField(max_length=200)
    project_id = models.ForeignKey(Project, null=True)
    date = models.DateField()

    class Meta:
        managed = True
        db_table = 'projectdb_ortho'

    def __str__(self):
        return (self.project_id.name+" - "+str(self.id))


class Gps(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    description = models.CharField(max_length=300)
    project_id = models.ForeignKey(Project, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'projectdb_gps'

class List(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()

    class Meta:
        managed = True
        db_table = 'projectdb_list'

class ProjectList(models.Model):
    id = models.AutoField(primary_key=True)
    note = models.TextField()
    list_id = models.ForeignKey(List, related_name='plList')
    project_id = models.ForeignKey(Project, null=True, blank=True)

    def __str__(self):
        return '%s: %s' % (self.project.name, self.list.title)

    class Meta:
        managed = True
        db_table = 'projectdb_projectlist'

"""class Piscesmetrics(models.Model):
    id = models.AutoField(primary_key=True)
    project_number = models.CharField(max_length=20)
    project_title = models.CharField(max_length=200)
    contract_number = models.CharField(max_length=50)
    we_id = models.CharField(max_length=4)
    wse_id = models.CharField(max_length=20, blank=True, null=True)
    wse_title = models.CharField(max_length=200, blank=True, null=True)
    wse_progress = models.CharField(max_length=50, blank=True, null=True)
    measures = models.CharField(max_length=200, blank=True, null=True)
    hli = models.CharField(max_length=50, blank=True, null=True)
    metric_id = models.CharField(max_length=10, blank=True, null=True)
    metric = models.CharField(max_length=200, blank=True, null=True)
    actual = models.FloatField(blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'projectdb_piscesmetrics'"""

class Projectboundary(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    geom = models.PolygonField(srid=4326)  # This field type is a guess.
    project_id = models.ForeignKey(Project, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'projectdb_projectboundary'


class Site(models.Model):
    project = models.ForeignKey(Project)
    description = models.CharField(max_length=100)
    mpoint = models.MultiPointField(srid=32611)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s - %s' % (self.project, self.description)

    def getLat(self):
        self.mpoint.transform(4269)
        return self.mpoint.coords[0][1]

    def getLong(self):
        self.mpoint.transform(4269)
        return self.mpoint.coords[0][0]

    class Meta:
        managed = True
        db_table = 'projectdb_site'


class Species(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    scientific = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'projectdb_species'


class SpeciesRel(models.Model):
    id = models.AutoField(primary_key=True)
    primary = models.BooleanField()
    project_id = models.ForeignKey(Project, null=True, blank=True)
    species_id = models.ForeignKey(Species)

    class Meta:
        managed = True
        db_table = 'projectdb_speciesrel'

class Tasktype(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'projectdb_tasktype'

class Tasksubtype(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    tasktype_id = models.IntegerField(db_column='taskType_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'projectdb_tasksubtype'

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    unit = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000, blank=True, null=True)
    project_id = models.ForeignKey(Project, null=True, blank=True)
    task_id = models.ForeignKey(Tasksubtype, related_name='sub_task_type')

    class Meta:
        managed = True
        db_table = 'projectdb_task'

class Ripplesedition(models.Model):
    id = models.AutoField(primary_key=True)
    editionname = models.CharField(db_column='editionName', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'publications_ripplesedition'
        managed = True

    def __str__(self):
    	return self.editionname

class Ripples(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=4)
    url = models.CharField(max_length=200)
    size = models.CharField(max_length=7)
    pub_date = models.DateField()
    edition_id = models.ForeignKey(Ripplesedition, db_column="edition_id")

    class Meta:
        db_table = 'publications_ripples'
        managed = True

    def __str__(self):
    	return (self.edition_id.editionname + " " +self.year)

class Ripplesarticle(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.CharField(max_length=300)
    ripples_id = models.ForeignKey(Ripples, db_column="ripples_id")

    class Meta:
        db_table = 'publications_ripplesarticle'
        managed = True

    def __str__(self):
        return (self.article)

