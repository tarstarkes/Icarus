# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountsOrganization(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'accounts_organization'


class AccountsProject(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    organization_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_project'


class AccountsUserprofile(models.Model):
    id = models.AutoField()
    organization_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_userprofile'


class AccountsUserprofileProjects(models.Model):
    id = models.AutoField()
    userprofile_id = models.IntegerField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_userprofile_projects'


class ActivitiesActivity(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=200)
    flickr = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activities_activity'


class AtlasAtlas(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atlas_atlas'


class AtlasBsr(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500, blank=True, null=True)
    atlas_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_bsr'


class AtlasBsrTier(models.Model):
    id = models.AutoField()
    bsr_id = models.IntegerField()
    tier_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_bsr_tier'


class AtlasCacheOpScore(models.Model):
    id = models.AutoField()
    lf = models.DecimalField(max_digits=10, decimal_places=2)
    imm = models.DecimalField(max_digits=10, decimal_places=2)
    lon = models.DecimalField(max_digits=10, decimal_places=2)
    np = models.DecimalField(max_digits=10, decimal_places=2)
    wrd = models.DecimalField(max_digits=10, decimal_places=2)
    wrr = models.DecimalField(max_digits=10, decimal_places=2)
    tot_hab = models.DecimalField(max_digits=10, decimal_places=2)
    tot_long = models.DecimalField(max_digits=10, decimal_places=2)
    bio_ben = models.DecimalField(max_digits=10, decimal_places=2)
    op_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_cache_op_score'


class AtlasComment(models.Model):
    id = models.AutoField()
    comment = models.CharField(max_length=5000)
    date = models.DateTimeField()
    deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'atlas_comment'


class AtlasFu(models.Model):
    id = models.AutoField()
    current = models.BooleanField()
    bsr_id = models.IntegerField()
    fu_name_id = models.IntegerField()
    fu_score_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_fu'


class AtlasFuComment(models.Model):
    id = models.AutoField()
    fu_id = models.IntegerField()
    comment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_fu_comment'


class AtlasFuName(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'atlas_fu_name'


class AtlasFuScore(models.Model):
    id = models.AutoField()
    score = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'atlas_fu_score'


class AtlasImpact(models.Model):
    id = models.AutoField()
    impact_name_id = models.IntegerField()
    lf_name_id = models.IntegerField()
    ra_name_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_impact'


class AtlasImpactName(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'atlas_impact_name'


class AtlasItmeetings(models.Model):
    id = models.AutoField()
    date = models.DateField()
    agenda = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'atlas_itmeetings'


class AtlasItmeetingsAtlas(models.Model):
    id = models.AutoField()
    itmeetings_id = models.IntegerField()
    atlas_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_itmeetings_atlas'


class AtlasItmeetingsOpportunities(models.Model):
    id = models.AutoField()
    itmeetings_id = models.IntegerField()
    op_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_itmeetings_opportunities'


class AtlasLf(models.Model):
    id = models.AutoField()
    expert_panel = models.IntegerField()
    current = models.BooleanField()
    bsr_id = models.IntegerField()
    lf_name_id = models.IntegerField()
    lf_score_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_lf'


class AtlasLfComment(models.Model):
    id = models.AutoField()
    lf_id = models.IntegerField()
    comment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_lf_comment'


class AtlasLfName(models.Model):
    id = models.AutoField()
    number = models.CharField(max_length=4)
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'atlas_lf_name'


class AtlasLfScore(models.Model):
    id = models.AutoField()
    score = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'atlas_lf_score'


class AtlasLimitingfactorsscore(models.Model):
    id = models.AutoField()
    scorevalue = models.DecimalField(max_digits=10, decimal_places=2)
    limitingfactorsactivityimpactoptions_id = models.IntegerField()
    limitingfactorscoreoption_id = models.IntegerField()
    restorationatlas_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_limitingfactorsscore'


class AtlasNaturalprocessoptionsscorevalue(models.Model):
    id = models.AutoField()
    scorevalue = models.DecimalField(max_digits=10, decimal_places=2)
    naturalprocessoptions_id = models.IntegerField()
    restorationatlas_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_naturalprocessoptionsscorevalue'


class AtlasNp(models.Model):
    id = models.AutoField()
    np_name_id = models.IntegerField()
    op_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_np'


class AtlasNpName(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'atlas_np_name'


class AtlasOp(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=200)
    bsr_id = models.IntegerField()
    op_lead_id = models.IntegerField(blank=True, null=True)
    op_status_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atlas_op'


class AtlasOpComment(models.Model):
    id = models.AutoField()
    op_id = models.IntegerField()
    comment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_op_comment'


class AtlasOpLead(models.Model):
    id = models.AutoField()
    name = models.TextField()
    accr = models.TextField()

    class Meta:
        managed = False
        db_table = 'atlas_op_lead'


class AtlasOpMapping(models.Model):
    id = models.AutoField()
    description = models.TextField()
    poly = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'atlas_op_mapping'


class AtlasOpOpMapping(models.Model):
    id = models.AutoField()
    op_id = models.IntegerField()
    op_mapping_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_op_op_mapping'


class AtlasOpRa(models.Model):
    id = models.AutoField()
    activity_id = models.IntegerField()
    op_id = models.IntegerField()
    ra_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_op_ra'


class AtlasOpRaActivitytype(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'atlas_op_ra_activitytype'


class AtlasOpStatus(models.Model):
    id = models.AutoField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'atlas_op_status'


class AtlasRa(models.Model):
    id = models.AutoField()
    current = models.BooleanField()
    bsr_id = models.IntegerField()
    immediate_id = models.IntegerField()
    long_id = models.IntegerField()
    ra_name_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_ra'


class AtlasRaComment(models.Model):
    id = models.AutoField()
    ra_id = models.IntegerField()
    comment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_ra_comment'


class AtlasRaName(models.Model):
    id = models.AutoField()
    number = models.CharField(max_length=4)
    name = models.CharField(max_length=500)
    ra_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_ra_name'


class AtlasRaNameGroup(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=500)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_ra_name_group'


class AtlasRaScore(models.Model):
    id = models.AutoField()
    score = models.CharField(max_length=50)
    ra_score_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_ra_score'


class AtlasRaScoreType(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'atlas_ra_score_type'


class AtlasRestorationactivityscorevalue(models.Model):
    id = models.AutoField()
    scorevalue = models.DecimalField(max_digits=10, decimal_places=2)
    restorationactivityscore_id = models.IntegerField()
    restorationatlas_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_restorationactivityscorevalue'


class AtlasScoringLf(models.Model):
    id = models.AutoField()
    atlas_id = models.IntegerField()
    score = models.DecimalField(max_digits=10, decimal_places=2)
    lf_score_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_scoring_lf'


class AtlasTier(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'atlas_tier'


class AtlasWaterrightdatesscorevalue(models.Model):
    id = models.AutoField()
    scorevalue = models.DecimalField(max_digits=10, decimal_places=2)
    restorationatlas_id = models.IntegerField()
    waterrightdates_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_waterrightdatesscorevalue'


class AtlasWaterrightratesscorevalue(models.Model):
    id = models.AutoField()
    scorevalue = models.DecimalField(max_digits=10, decimal_places=2)
    restorationatlas_id = models.IntegerField()
    waterrightrates_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_waterrightratesscorevalue'


class AtlasWr(models.Model):
    id = models.AutoField()
    op_id = models.IntegerField()
    wr_date_id = models.IntegerField()
    wr_rate_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_wr'


class AtlasWrDate(models.Model):
    id = models.AutoField()
    range = models.CharField(max_length=50)
    reliability = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atlas_wr_date'


class AtlasWrRate(models.Model):
    id = models.AutoField()
    range = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'atlas_wr_rate'


class AuthGroup(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.AutoField()
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.AutoField()
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.AutoField()
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.AutoField()
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.AutoField()
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.AutoField()
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class EventsBoardmeeting(models.Model):
    id = models.AutoField()
    date = models.DateTimeField()
    agenda_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField()
    minutes_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_boardmeeting'


class EventsDocument(models.Model):
    id = models.AutoField()
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=200)
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'events_document'


class EventsDocumenttype(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'events_documenttype'


class EventsMeetinglocation(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'events_meetinglocation'


class GeositeExtent(models.Model):
    id = models.AutoField()
    extent_name = models.CharField(max_length=25)
    extent_path = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'geosite_extent'


class GeositeFile(models.Model):
    id = models.AutoField()
    theme_id = models.IntegerField()
    extent_id = models.IntegerField()
    file_name = models.CharField(max_length=100)
    metadata_path = models.CharField(max_length=60)
    file_path = models.CharField(max_length=100)
    size = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'geosite_file'


class GeositeTheme(models.Model):
    id = models.AutoField()
    theme_name = models.CharField(max_length=30)
    theme_path = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'geosite_theme'


class GrbasinChinookEsuReaches(models.Model):
    id = models.AutoField()
    objectid = models.IntegerField()
    reach = models.CharField(max_length=5)
    source = models.CharField(max_length=50)
    oldreach = models.CharField(max_length=6)
    miles = models.FloatField()
    shape_leng = models.FloatField()
    shape_le_1 = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_chinook_esu_reaches'


class GrbasinChinookMegalayer(models.Model):
    id = models.AutoField()
    gridcode = models.FloatField()
    reach = models.CharField(max_length=5)
    label = models.CharField(max_length=16)
    basin_name = models.CharField(max_length=75)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_chinook_megalayer'


class GrbasinChinookReaches(models.Model):
    id = models.AutoField()
    reach = models.CharField(max_length=5)
    source = models.CharField(max_length=50)
    oldreach = models.CharField(max_length=6)
    miles = models.FloatField()
    updated_re = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_le_1 = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_chinook_reaches'


class GrbasinFishpassageBarriers(models.Model):
    id = models.AutoField()
    objectid = models.IntegerField()
    fpbftrid = models.IntegerField()
    fpblong = models.FloatField()
    fpblat = models.FloatField()
    fpbsiteid = models.IntegerField()
    fpbrevdt = models.CharField(max_length=8)
    fpboftrid = models.CharField(max_length=40)
    fpbonm = models.CharField(max_length=30)
    fpbositeid = models.CharField(max_length=40)
    fpblocmd = models.CharField(max_length=15)
    fpblocaccu = models.IntegerField()
    fpblocdt = models.CharField(max_length=8)
    fpbftrty = models.CharField(max_length=25)
    fpbftrnm = models.CharField(max_length=50)
    fpbrmvdt = models.CharField(max_length=8)
    fpbmltftr = models.CharField(max_length=7)
    fpbfpassta = models.CharField(max_length=8)
    fpbstaevdt = models.CharField(max_length=8)
    fpbstaevmd = models.CharField(max_length=20)
    fpbfysta = models.CharField(max_length=20)
    fpbfycrit = models.CharField(max_length=7)
    fpbcrddesc = models.CharField(max_length=254)
    permanent_field = models.CharField(max_length=40)
    reachcode = models.CharField(max_length=14)
    measure = models.FloatField()
    eventdate = models.DateField()
    reachsmdat = models.DateField()
    reachresol = models.IntegerField()
    fpbstrnm = models.CharField(max_length=50)
    fpbrdid = models.CharField(max_length=13)
    fpbrdmile = models.FloatField()
    fpbrdnm = models.CharField(max_length=50)
    fpbloconm = models.CharField(max_length=30)
    fpbftrsty = models.CharField(max_length=30)
    fpbftrnmsr = models.CharField(max_length=5)
    fpbheight = models.FloatField()
    fpblength = models.FloatField()
    fpbwidth = models.FloatField()
    fpbslope = models.FloatField()
    fpbdrop = models.FloatField()
    fpboryr = models.CharField(max_length=4)
    fpbmoddt = models.CharField(max_length=8)
    fpbmodty = models.CharField(max_length=10)
    fpbmoddesc = models.CharField(max_length=254)
    fpbdesonm = models.CharField(max_length=30)
    fpbown = models.CharField(max_length=60)
    fpblown = models.CharField(max_length=60)
    fpboperate = models.CharField(max_length=60)
    fpbfyown = models.CharField(max_length=60)
    fpbownty = models.CharField(max_length=15)
    fpblownty = models.CharField(max_length=15)
    fpbownonm = models.CharField(max_length=30)
    fpbfyty = models.CharField(max_length=15)
    fpbfysty = models.CharField(max_length=20)
    fpbfyoryr = models.CharField(max_length=4)
    fpbfpasonm = models.CharField(max_length=30)
    fpblocmdd = models.CharField(max_length=100)
    fpbftrtyd = models.CharField(max_length=100)
    fpbftrstyd = models.CharField(max_length=100)
    fpbevmdfad = models.CharField(max_length=100)
    fpbevmdpad = models.CharField(max_length=100)
    fpbfytyd = models.CharField(max_length=100)
    fpbowntyd = models.CharField(max_length=100)
    fpblowntyd = models.CharField(max_length=100)
    fpbcomment = models.CharField(max_length=254)
    fpbstrid = models.CharField(max_length=13)
    fpbstrmeas = models.FloatField()
    comid = models.IntegerField()
    featurecla = models.IntegerField()
    offset = models.FloatField()
    eventtype = models.IntegerField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_fishpassage_barriers'


class GrbasinGrSsBasins(models.Model):
    id = models.AutoField()
    label = models.CharField(max_length=16)
    basin_name = models.CharField(max_length=75)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_gr_ss_basins'


class GrbasinGranderondechinookpopulations(models.Model):
    id = models.AutoField()
    objectid = models.IntegerField()
    label = models.CharField(max_length=16)
    basin_name = models.CharField(max_length=75)
    ruleid = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_granderondechinookpopulations'


class GrbasinGranderondesteelheadpopulations(models.Model):
    id = models.AutoField()
    label = models.CharField(max_length=16)
    basin_name = models.CharField(max_length=75)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    sq_mileage = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_granderondesteelheadpopulations'


class GrbasinGrgeology(models.Model):
    id = models.AutoField()
    ref_id_cod = models.CharField(max_length=25)
    map_unit_l = models.CharField(max_length=12)
    map_unit_n = models.CharField(max_length=100)
    g_mrg_u_l = models.CharField(max_length=60)
    geo_genl_u = models.CharField(max_length=50)
    age_name = models.CharField(max_length=50)
    terrane_gr = models.CharField(max_length=50)
    formation = models.CharField(max_length=200)
    member = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    g_rock_typ = models.CharField(max_length=50)
    lith_m_u_l = models.CharField(max_length=50)
    lith_gen_u = models.CharField(max_length=75)
    lth_rk_typ = models.CharField(max_length=50)
    layering = models.CharField(max_length=50)
    cr_grn_siz = models.CharField(max_length=50)
    getec_prop = models.CharField(max_length=50)
    gn_lith_ty = models.CharField(max_length=50)
    arcjoinkey = models.CharField(max_length=37)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_grgeology'


class GrbasinGrmwwatershedborders(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    abr = models.CharField(max_length=10)
    description = models.TextField()
    poly = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_grmwwatershedborders'


class GrbasinGrmwwatershedboundaries(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    atr = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    poly = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_grmwwatershedboundaries'


class GrbasinGrmwwatersheds(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    abr = models.CharField(max_length=10)
    description = models.TextField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_grmwwatersheds'


class GrbasinHuc12Grbasin(models.Model):
    id = models.AutoField()
    objectid = models.IntegerField()
    tnmid = models.CharField(max_length=40)
    metasource = models.CharField(max_length=40)
    sourcedata = models.CharField(max_length=100)
    sourceorig = models.CharField(max_length=130)
    sourcefeat = models.CharField(max_length=40)
    loaddate = models.DateField()
    gnis_id = models.IntegerField()
    areaacres = models.FloatField()
    areasqkm = models.FloatField()
    states = models.CharField(max_length=50)
    huc12 = models.CharField(max_length=12)
    name = models.CharField(max_length=120)
    hutype = models.CharField(max_length=254)
    humod = models.CharField(max_length=30)
    tohuc = models.CharField(max_length=16)
    noncontrib = models.FloatField()
    noncontr_1 = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_huc12grbasin'


class GrbasinHuc5(models.Model):
    id = models.AutoField()
    area = models.FloatField()
    perimeter = models.FloatField()
    huc5_field = models.IntegerField()
    huc5_id = models.IntegerField()
    acres = models.FloatField()
    huc_type = models.CharField(max_length=8)
    region_nam = models.CharField(max_length=30)
    subregion_field = models.CharField(max_length=30)
    basin_name = models.CharField(max_length=30)
    subbasin_n = models.CharField(max_length=30)
    watershed_field = models.CharField(max_length=80)
    old_hucnum = models.CharField(max_length=16)
    states = models.CharField(max_length=12)
    ncontrib_d = models.FloatField()
    ds_huc5 = models.CharField(max_length=10)
    ds_huc6 = models.CharField(max_length=12)
    huc_mod = models.CharField(max_length=80)
    comment = models.CharField(max_length=100)
    region = models.CharField(max_length=2)
    subregion = models.CharField(max_length=4)
    basin = models.CharField(max_length=6)
    subbasin = models.CharField(max_length=8)
    first_fiel = models.CharField(max_length=2)
    second_fie = models.CharField(max_length=2)
    third_fiel = models.CharField(max_length=2)
    fourth_fie = models.CharField(max_length=2)
    fifth_fiel = models.CharField(max_length=2)
    watershed = models.CharField(max_length=10)
    mpoly = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_huc5'


class GrbasinLandmanagement(models.Model):
    id = models.AutoField()
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    land_mgmt_field = models.IntegerField()
    land_mgmt1 = models.IntegerField()
    site_nm = models.CharField(max_length=60)
    owner = models.CharField(max_length=25)
    pub_land = models.CharField(max_length=14)
    gap_code = models.IntegerField()
    sma_nm = models.CharField(max_length=60)
    sma_own = models.CharField(max_length=25)
    sma_code = models.FloatField()
    km2 = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_landmanagement'


class GrbasinOdfwhabitat(models.Model):
    id = models.AutoField()
    fnode_field = models.IntegerField()
    tnode_field = models.IntegerField()
    lpoly_field = models.IntegerField()
    rpoly_field = models.IntegerField()
    length = models.FloatField()
    grnd10hab_field = models.IntegerField()
    grnd10hab1 = models.IntegerField()
    basin = models.CharField(max_length=30)
    stream = models.CharField(max_length=30)
    sampl_date = models.DateField()
    location = models.CharField(max_length=15)
    reach_numb = models.IntegerField()
    reach_new = models.IntegerField()
    chan_form = models.CharField(max_length=2)
    valley_fm = models.CharField(max_length=2)
    veg_cl_dom = models.CharField(max_length=5)
    veg_cl_sub = models.CharField(max_length=5)
    land_dom = models.CharField(max_length=5)
    land_sub = models.CharField(max_length=5)
    water_temp = models.FloatField()
    unit_numb = models.IntegerField()
    unit_type = models.CharField(max_length=2)
    unit_name = models.CharField(max_length=20)
    chanl_type = models.CharField(max_length=2)
    per_flow = models.IntegerField()
    cor_length = models.FloatField()
    cor_width = models.FloatField()
    cor_area = models.FloatField()
    fromdist = models.FloatField()
    todist = models.FloatField()
    slope = models.FloatField()
    shade = models.FloatField()
    ac_width = models.FloatField()
    ac_height = models.FloatField()
    fp_width = models.FloatField()
    fp_height = models.FloatField()
    terr_width = models.FloatField()
    terr_heigh = models.FloatField()
    vwi = models.FloatField()
    depth = models.FloatField()
    depth_ptc = models.FloatField()
    so_adj = models.FloatField()
    snd_adj = models.FloatField()
    grv_adj = models.FloatField()
    cbl_adj = models.FloatField()
    bld_adj = models.FloatField()
    brk_adj = models.FloatField()
    bldr_count = models.IntegerField()
    ac_erosion = models.IntegerField()
    undercut = models.IntegerField()
    wood_class = models.IntegerField()
    npieces = models.IntegerField()
    wvolume = models.FloatField()
    keypieces = models.IntegerField()
    comm_code = models.CharField(max_length=10)
    note_1 = models.CharField(max_length=30)
    note_2 = models.CharField(max_length=30)
    canopy_cl = models.IntegerField()
    smallcon = models.FloatField()
    c_50 = models.IntegerField()
    c_90 = models.IntegerField()
    tothwood = models.FloatField()
    llid = models.CharField(max_length=13)
    habrch = models.CharField(max_length=15)
    habunt = models.CharField(max_length=19)
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_odfwhabitat'


class GrbasinOregoncounties(models.Model):
    id = models.AutoField()
    cnty_code = models.CharField(max_length=2)
    unitid = models.CharField(max_length=17)
    instname = models.CharField(max_length=99)
    altname = models.CharField(max_length=99)
    descriptn = models.CharField(max_length=254)
    instcode = models.CharField(max_length=9)
    coderef = models.CharField(max_length=25)
    effdate = models.CharField(max_length=8)
    unitowner = models.CharField(max_length=8)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_oregoncounties'


class GrbasinSteelheadMegalayer(models.Model):
    id = models.AutoField()
    label = models.CharField(max_length=16)
    basin_name = models.CharField(max_length=75)
    megaid = models.FloatField()
    gridcode = models.FloatField()
    reach = models.CharField(max_length=5)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_steelhead_megalayer'


class GrbasinSteelheadReaches(models.Model):
    id = models.AutoField()
    lifehistor = models.IntegerField()
    usetypeid = models.IntegerField()
    comments25 = models.CharField(max_length=254)
    reachname = models.CharField(max_length=5)
    source = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_le_1 = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_steelhead_reaches'


class GrbasinWatershedborders(models.Model):
    id = models.AutoField()
    area = models.FloatField()
    perimeter = models.FloatField()
    huc6_id = models.IntegerField()
    acres = models.IntegerField()
    huc_num = models.CharField(max_length=16)
    huc_type = models.CharField(max_length=8)
    region_name = models.CharField(max_length=30)
    subregian_name = models.CharField(max_length=30)
    basin_name = models.CharField(max_length=30)
    subbasin_name = models.CharField(max_length=30)
    watershed_name = models.CharField(max_length=80)
    subwatershed_name = models.CharField(max_length=80)
    old_huc_num = models.CharField(max_length=16)
    states = models.CharField(max_length=12)
    ncontrib_id = models.FloatField()
    huc5 = models.CharField(max_length=10)
    huc6 = models.CharField(max_length=12)
    hucmod = models.CharField(max_length=80)
    comment = models.CharField(max_length=100)
    region = models.CharField(max_length=2)
    subregion = models.CharField(max_length=4)
    basin = models.CharField(max_length=6)
    subbasin = models.CharField(max_length=8)
    watershed = models.CharField(max_length=10)
    subwatershed = models.CharField(max_length=12)
    first_field = models.CharField(max_length=2)
    second_field = models.CharField(max_length=2)
    third_field = models.CharField(max_length=2)
    fourth_field = models.CharField(max_length=2)
    fifth_field = models.CharField(max_length=2)
    sixth_field = models.CharField(max_length=2)
    shape_length = models.FloatField()
    shape_area = models.FloatField()
    assignment = models.CharField(max_length=50)
    mpoly = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grbasin_watershedborders'


class Layer(models.Model):
    topology = models.ForeignKey('Topology', models.DO_NOTHING)
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=-1)
    table_name = models.CharField(max_length=-1)
    feature_column = models.CharField(max_length=-1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('schema_name', 'table_name', 'feature_column'), ('topology', 'layer_id'),)


class ProjectdbContact(models.Model):
    id = models.AutoField()
    contactrole_id = models.IntegerField(db_column='contactRole_id')  # Field name made lowercase.
    contacttype_id = models.IntegerField(db_column='contactType_id')  # Field name made lowercase.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_contact'


class ProjectdbContactrole(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projectdb_contactrole'


class ProjectdbContacttype(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    orgtype_id = models.IntegerField(db_column='orgType_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'projectdb_contacttype'


class ProjectdbContract(models.Model):
    id = models.AutoField()
    contractnumber = models.CharField(db_column='contractNumber', max_length=50)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    fundingorg_id = models.IntegerField(db_column='fundingOrg_id')  # Field name made lowercase.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_contract'


class ProjectdbDate(models.Model):
    id = models.AutoField()
    date = models.DateField()
    project_id = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_date'


class ProjectdbDatetype(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'projectdb_datetype'


class ProjectdbDocument(models.Model):
    id = models.AutoField()
    url = models.CharField(max_length=200)
    note = models.CharField(max_length=100)
    date = models.DateField()
    project_id = models.IntegerField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_document'


class ProjectdbDocumenttype(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projectdb_documenttype'


class ProjectdbGps(models.Model):
    id = models.AutoField()
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    description = models.CharField(max_length=300)
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_gps'


class ProjectdbGrmwdatabase(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    collection = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'projectdb_grmwdatabase'


class ProjectdbGrmwdatabasepolygon(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    mpoly = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'projectdb_grmwdatabasepolygon'


class ProjectdbList(models.Model):
    id = models.AutoField()
    title = models.TextField()

    class Meta:
        managed = False
        db_table = 'projectdb_list'


class ProjectdbOrganization(models.Model):
    id = models.AutoField()
    orgrole_id = models.IntegerField(db_column='orgRole_id')  # Field name made lowercase.
    orgtype_id = models.IntegerField(db_column='orgType_id')  # Field name made lowercase.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_organization'


class ProjectdbOrganizationrole(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projectdb_organizationrole'


class ProjectdbOrganizationtype(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    abr = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'projectdb_organizationtype'


class ProjectdbPiscesmetrics(models.Model):
    id = models.AutoField()
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
    id = models.AutoField()
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


class ProjectdbProjectboundary(models.Model):
    id = models.AutoField()
    description = models.CharField(max_length=100)
    geom = models.TextField()  # This field type is a guess.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_projectboundary'


class ProjectdbProjectlist(models.Model):
    id = models.AutoField()
    note = models.TextField()
    list_id = models.IntegerField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_projectlist'


class ProjectdbProjectreporting(models.Model):
    id = models.AutoField()
    reporting_completed = models.BooleanField()
    reporting_name = models.CharField(max_length=50)
    reporting_date = models.DateField()
    reporting_project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_projectreporting'


class ProjectdbSite(models.Model):
    id = models.AutoField()
    description = models.CharField(max_length=100)
    mpoint = models.TextField()  # This field type is a guess.
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_site'


class ProjectdbSpecies(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    scientific = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'projectdb_species'


class ProjectdbSpeciesrel(models.Model):
    id = models.AutoField()
    primary = models.BooleanField()
    project_id = models.IntegerField()
    species_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_speciesrel'


class ProjectdbStatustype(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'projectdb_statustype'


class ProjectdbTask(models.Model):
    id = models.AutoField()
    unit = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000, blank=True, null=True)
    project_id = models.IntegerField()
    task_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'projectdb_task'


class ProjectdbTasksubtype(models.Model):
    id = models.AutoField()
    description = models.CharField(max_length=100)
    tasktype_id = models.IntegerField(db_column='taskType_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'projectdb_tasksubtype'


class ProjectdbTasktype(models.Model):
    id = models.AutoField()
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'projectdb_tasktype'


class ProjectdbTestpoly(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    mpoly = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'projectdb_testpoly'


class ProjectdbUnittype(models.Model):
    id = models.AutoField()
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'projectdb_unittype'


class PublicationsNewsarticle(models.Model):
    id = models.AutoField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    date = models.DateField()
    glimps = models.CharField(max_length=400)
    graphic = models.CharField(max_length=200, blank=True, null=True)
    publisher_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publications_newsarticle'


class PublicationsNewspublisher(models.Model):
    id = models.AutoField()
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'publications_newspublisher'


class PublicationsRipples(models.Model):
    year = models.CharField(max_length=4)
    url = models.CharField(max_length=200)
    size = models.CharField(max_length=7)
    pub_date = models.DateField()
    edition = models.ForeignKey('PublicationsRipplesedition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'publications_ripples'


class PublicationsRipplesarticle(models.Model):
    article = models.CharField(max_length=300)
    ripples = models.ForeignKey(PublicationsRipples, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'publications_ripplesarticle'


class PublicationsRipplesedition(models.Model):
    editionname = models.CharField(db_column='editionName', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publications_ripplesedition'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class StepwisedbFlags(models.Model):
    id = models.AutoField()
    date = models.DateField()
    description = models.CharField(max_length=100)
    complete = models.BooleanField()
    flagtype_id = models.IntegerField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stepwisedb_flags'


class StepwisedbFlagtype(models.Model):
    id = models.AutoField()
    description = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'stepwisedb_flagtype'


class StepwisedbPhase(models.Model):
    id = models.AutoField()
    order = models.IntegerField()
    description = models.CharField(max_length=50)
    step_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stepwisedb_phase'


class StepwisedbPhasetype(models.Model):
    id = models.AutoField()
    complete = models.BooleanField()
    date = models.DateField()
    description = models.CharField(max_length=100)
    phase_id = models.IntegerField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stepwisedb_phasetype'


class StepwisedbStep(models.Model):
    id = models.AutoField()
    name = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stepwisedb_step'


class StepwisedbStepwiselist(models.Model):
    id = models.AutoField()
    complete = models.BooleanField()
    active = models.BooleanField()
    publish = models.BooleanField()
    current = models.BooleanField()
    project_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stepwisedb_stepwiselist'


class StepwisedbStepwiselistTasks(models.Model):
    id = models.AutoField()
    stepwiselist_id = models.IntegerField()
    tasktype_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stepwisedb_stepwiselist_tasks'


class TaxlotdbContact(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'taxlotdb_contact'


class TaxlotdbPhone(models.Model):
    id = models.AutoField()
    contact_id = models.IntegerField()
    phone = models.CharField(max_length=20)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxlotdb_phone'


class TaxlotdbPhonecall(models.Model):
    id = models.AutoField()
    taxlot_id = models.IntegerField()
    date = models.DateField()
    who_id = models.IntegerField()
    whom_id = models.IntegerField()
    description = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'taxlotdb_phonecall'


class TaxlotdbRelationship(models.Model):
    id = models.AutoField()
    contact_id = models.IntegerField()
    taxlot_id = models.IntegerField()
    rel = models.IntegerField()
    description = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'taxlotdb_relationship'


class TaxlotdbRiver(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'taxlotdb_river'


class TaxlotdbSurvey(models.Model):
    id = models.AutoField()
    survey_crew_id = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxlotdb_survey'


class TaxlotdbSurveycrew(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    organization_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxlotdb_surveycrew'


class TaxlotdbSurveysections(models.Model):
    id = models.AutoField()
    survey_id = models.IntegerField()
    rm_start = models.DecimalField(max_digits=5, decimal_places=1)
    rm_end = models.DecimalField(max_digits=5, decimal_places=1)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'taxlotdb_surveysections'


class TaxlotdbTaxlot(models.Model):
    id = models.AutoField()
    number = models.CharField(max_length=30)
    map = models.IntegerField()
    river_mile_start = models.DecimalField(max_digits=5, decimal_places=1)
    river_mile_end = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'taxlotdb_taxlot'


class TaxlotdbTaxlots(models.Model):
    id = models.AutoField()
    river_id = models.IntegerField()
    maptaxlot = models.CharField(max_length=25)
    property = models.CharField(max_length=254)
    apn = models.CharField(max_length=30)
    map = models.CharField(max_length=12)
    taxlot = models.CharField(max_length=15)
    refnum = models.FloatField()
    address1 = models.CharField(max_length=50)
    ctyst = models.CharField(max_length=50)
    zip = models.CharField(max_length=12)
    alndv = models.FloatField()
    aimpv = models.FloatField()
    mlndv = models.FloatField()
    mimpv = models.FloatField()
    pcl = models.FloatField()
    code = models.FloatField()
    var = models.CharField(max_length=10)
    zoning = models.CharField(max_length=10)
    acres = models.FloatField()
    lotsf = models.FloatField()
    num = models.FloatField()
    road = models.CharField(max_length=50)
    rdext = models.CharField(max_length=25)
    city = models.CharField(max_length=30)
    link_map = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'taxlotdb_taxlots'


class TaxlotdbTaxlotstatus(models.Model):
    id = models.AutoField()
    taxlot_id = models.IntegerField()
    survey_id = models.IntegerField()
    status = models.IntegerField()
    comment = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'taxlotdb_taxlotstatus'


class TemperatureLoggerinfo(models.Model):
    id = models.AutoField()
    programsiteid = models.IntegerField(db_column='ProgramSiteID')  # Field name made lowercase.
    sitename = models.CharField(db_column='SiteName', max_length=100)  # Field name made lowercase.
    watershedid = models.IntegerField(db_column='WatershedID')  # Field name made lowercase.
    watershedname = models.CharField(db_column='WatershedName', max_length=100)  # Field name made lowercase.
    sampledate = models.DateTimeField(db_column='SampleDate')  # Field name made lowercase.
    hitchname = models.CharField(db_column='HitchName', max_length=100)  # Field name made lowercase.
    crewname = models.CharField(db_column='CrewName', max_length=100)  # Field name made lowercase.
    visityear = models.CharField(db_column='VisitYear', max_length=100)  # Field name made lowercase.
    iterationid = models.IntegerField(db_column='IterationID', blank=True, null=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=100)  # Field name made lowercase.
    panelname = models.CharField(db_column='PanelName', max_length=100)  # Field name made lowercase.
    visitid = models.IntegerField(db_column='VisitID', blank=True, null=True)  # Field name made lowercase.
    visitdate = models.DateTimeField(db_column='VisitDate')  # Field name made lowercase.
    aem = models.CharField(db_column='AEM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bugvalidation = models.CharField(db_column='BugValidation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    champ10previsit = models.CharField(db_column='CHaMP10PRevisit', max_length=100, blank=True, null=True)  # Field name made lowercase.
    champcore = models.CharField(db_column='CHaMPCore', max_length=100, blank=True, null=True)  # Field name made lowercase.
    champpibocomparison = models.CharField(db_column='CHaMPPiBOComparison', max_length=100, blank=True, null=True)  # Field name made lowercase.
    effectiveness = models.CharField(db_column='Effectiveness', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hasfishdata = models.CharField(db_column='HasFishData', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imw = models.CharField(db_column='IMW', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remove = models.CharField(db_column='Remove', max_length=100, blank=True, null=True)  # Field name made lowercase.
    velocityvalidation = models.CharField(db_column='VelocityValidation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    primaryvisit = models.CharField(db_column='PrimaryVisit', max_length=100, blank=True, null=True)  # Field name made lowercase.
    qcvisit = models.CharField(db_column='QCVisit', max_length=100, blank=True, null=True)  # Field name made lowercase.
    error = models.CharField(db_column='Error', max_length=100, blank=True, null=True)  # Field name made lowercase.
    no = models.CharField(db_column='No', max_length=100, blank=True, null=True)  # Field name made lowercase.
    yes = models.CharField(db_column='Yes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    measurementid = models.IntegerField(db_column='MeasurementID', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dataupdatenotes = models.CharField(db_column='DataUpdateNotes', max_length=500, blank=True, null=True)  # Field name made lowercase.
    loggerid = models.CharField(db_column='LoggerID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    utmzone = models.IntegerField(db_column='UTMZone', blank=True, null=True)  # Field name made lowercase.
    utmnorthing = models.IntegerField(db_column='UTMNorthing', blank=True, null=True)  # Field name made lowercase.
    utmeasting = models.IntegerField(db_column='UTMEasting', blank=True, null=True)  # Field name made lowercase.
    gpsaccuracy = models.FloatField(db_column='GPSAccuracy', blank=True, null=True)  # Field name made lowercase.
    gpsaccuracytype = models.CharField(db_column='GPSAccuracyType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dateinstalled = models.DateTimeField(db_column='DateInstalled', blank=True, null=True)  # Field name made lowercase.
    dateremoved = models.DateTimeField(db_column='DateRemoved', blank=True, null=True)  # Field name made lowercase.
    elevation = models.IntegerField(db_column='Elevation', blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distancefrombank = models.FloatField(db_column='DistanceFromBank', blank=True, null=True)  # Field name made lowercase.
    attachmentmethod = models.CharField(db_column='AttachmentMethod', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photofilename = models.CharField(db_column='PhotoFileName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    placementlocation = models.CharField(db_column='PlacementLocation', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temperature_loggerinfo'


class TemperatureSiteinfo(models.Model):
    id = models.AutoField()
    watershed = models.CharField(max_length=254, blank=True, null=True)
    siteid = models.CharField(max_length=254, blank=True, null=True)
    streamname = models.CharField(max_length=254, blank=True, null=True)
    panel = models.CharField(max_length=254, blank=True, null=True)
    category = models.CharField(max_length=254, blank=True, null=True)
    boseasting = models.FloatField(blank=True, null=True)
    bosnorthin = models.IntegerField(blank=True, null=True)
    specialcat = models.CharField(max_length=254, blank=True, null=True)
    borassmtre = models.CharField(max_length=254, blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'temperature_siteinfo'


class TemperatureStreamtempmeasurements(models.Model):
    id = models.AutoField()
    programsiteid = models.IntegerField(db_column='ProgramSiteID', blank=True, null=True)  # Field name made lowercase.
    sitename = models.CharField(db_column='SiteName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    watershedid = models.IntegerField(db_column='WatershedID', blank=True, null=True)  # Field name made lowercase.
    watershedname = models.CharField(db_column='WatershedName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    countmeasurements = models.IntegerField(db_column='CountMeasurements', blank=True, null=True)  # Field name made lowercase.
    countdifferentdates = models.IntegerField(db_column='CountDifferentDates', blank=True, null=True)  # Field name made lowercase.
    eventdatehour = models.DateTimeField(db_column='EventDateHour', blank=True, null=True)  # Field name made lowercase.
    eventdateday = models.DateTimeField(db_column='EventDateDay', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.IntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    hour = models.IntegerField(db_column='Hour', blank=True, null=True)  # Field name made lowercase.
    tempmin = models.FloatField(db_column='TempMin', blank=True, null=True)  # Field name made lowercase.
    tempavg = models.FloatField(db_column='TempAvg', blank=True, null=True)  # Field name made lowercase.
    tempmax = models.FloatField(db_column='TempMax', blank=True, null=True)  # Field name made lowercase.
    temprange = models.FloatField(db_column='TempRange', blank=True, null=True)  # Field name made lowercase.
    decisionid = models.IntegerField(db_column='DecisionID', blank=True, null=True)  # Field name made lowercase.
    notetext = models.CharField(db_column='NoteText', max_length=500, blank=True, null=True)  # Field name made lowercase.
    severitylevel = models.CharField(db_column='SeverityLevel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userdisplayname = models.CharField(db_column='UserDisplayName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eventdate = models.DateTimeField(db_column='EventDate', blank=True, null=True)  # Field name made lowercase.
    asdf = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temperature_streamtempmeasurements'


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'
