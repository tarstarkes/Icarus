from django.db import models

# Create your models here.
class ProjectdbContact(models.Model):
    contactrole_id = models.IntegerField(db_column='contactRole_id')  # Field name made lowercase.
    contacttype_id = models.IntegerField(db_column='contactType_id')  # Field name made lowercase.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_contact'


class ProjectdbContactrole(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projectdb_contactrole'


class ProjectdbContacttype(models.Model):
    name = models.CharField(max_length=50)
    orgtype_id = models.IntegerField(db_column='orgType_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'projectdb_contacttype'


class ProjectdbContract(models.Model):
    contractnumber = models.CharField(db_column='contractNumber', max_length=50)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    fundingorg_id = models.IntegerField(db_column='fundingOrg_id')  # Field name made lowercase.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_contract'


class ProjectdbDate(models.Model):
    date = models.DateField()
    project_id = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_date'


class ProjectdbDatetype(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'projectdb_datetype'


class ProjectdbDocument(models.Model):
    url = models.CharField(max_length=200)
    note = models.CharField(max_length=100)
    date = models.DateField()
    project_id = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_document'


class ProjectdbDocumenttype(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projectdb_documenttype'


class ProjectdbGps(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    description = models.CharField(max_length=300)
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_gps'


class ProjectdbGrmwdatabase(models.Model):
    name = models.CharField(max_length=100)
    collection = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'projectdb_grmwdatabase'


class ProjectdbGrmwdatabasepolygon(models.Model):
    name = models.CharField(max_length=100)
    mpoly = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'projectdb_grmwdatabasepolygon'


class ProjectdbList(models.Model):
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'projectdb_list'


class ProjectdbOrganization(models.Model):
    orgrole_id = models.IntegerField(db_column='orgRole_id')  # Field name made lowercase.
    orgtype_id = models.IntegerField(db_column='orgType_id')  # Field name made lowercase.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_organization'


class ProjectdbOrganizationrole(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projectdb_organizationrole'


class ProjectdbOrganizationtype(models.Model):
    name = models.CharField(max_length=100)
    abr = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'projectdb_organizationtype'


class ProjectdbPiscesmetrics(models.Model):
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
        managed = False
        db_table = 'projectdb_piscesmetrics'


class ProjectdbProject(models.Model):
    name = models.CharField(max_length=100)
    fiscalyear = models.IntegerField()
    publish = models.BooleanField()
    grmw_id = models.IntegerField()
    description = models.CharField(max_length=10000)
    notes = models.CharField(max_length=10000, blank=True, null=True)
    flickr = models.CharField(max_length=100, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projectdb_project'

    def __str__(self):
    	return self.name


class ProjectdbProjectboundary(models.Model):
    description = models.CharField(max_length=100)
    geom = models.TextField()  # This field type is a guess.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_projectboundary'


class ProjectdbProjectlist(models.Model):
    note = models.TextField()
    list_id = models.IntegerField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_projectlist'


class ProjectdbProjectreporting(models.Model):
    reporting_completed = models.BooleanField()
    reporting_name = models.CharField(max_length=50)
    reporting_date = models.DateField()
    reporting_project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_projectreporting'


class ProjectdbSite(models.Model):
    description = models.CharField(max_length=100)
    mpoint = models.TextField()  # This field type is a guess.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_site'


class ProjectdbSpecies(models.Model):
    name = models.CharField(max_length=50)
    scientific = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'projectdb_species'


class ProjectdbSpeciesrel(models.Model):
    primary = models.BooleanField()
    project_id = models.IntegerField()
    species_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_speciesrel'


class ProjectdbStatustype(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projectdb_statustype'


class ProjectdbTask(models.Model):
    unit = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000, blank=True, null=True)
    project_id = models.IntegerField()
    task_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_task'


class ProjectdbTasksubtype(models.Model):
    description = models.CharField(max_length=100)
    tasktype_id = models.IntegerField(db_column='taskType_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'projectdb_tasksubtype'


class ProjectdbTasktype(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'projectdb_tasktype'


class ProjectdbTestpoly(models.Model):
    name = models.CharField(max_length=100)
    mpoly = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'projectdb_testpoly'


class ProjectdbUnittype(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'projectdb_unittype'


class PublicationsRipples(models.Model):
    year = models.CharField(max_length=4)
    url = models.CharField(max_length=200)
    size = models.CharField(max_length=7)
    pub_date = models.DateField()
    edition_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publications_ripples'

    def __str__(self):
    	term = ""
    	if (self.edition_id == 1):
    		term = "Winter"
    	elif (self.edition_id == 2):
    		term = "Spring"
    	elif (self.edition_id == 3):
    		term = "Summer"
    	else:
    		term = "Fall"
    	return (term+" "+self.year)


class PublicationsRipplesarticle(models.Model):
    article = models.CharField(max_length=300)
    ripples_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publications_ripplesarticle'


class PublicationsRipplesedition(models.Model):
    editionname = models.CharField(db_column='editionName', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_ripplesedition'

    def __str__(self):
    	return self.editionName

