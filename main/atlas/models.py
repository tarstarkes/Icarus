from django.db import models
from django.contrib.gis.db import models as gisModels
from django import forms
import datetime
import os
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class species(models.Model):
	species_name = models.CharField(max_length=100)
	hard_color = models.CharField(max_length=20, blank=True, null=True)
	soft_color = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.species_name

	class Meta:
		db_table = 'atlas_species'

class limiting_factor(models.Model):
	sub_id = models.FloatField()
	ecological_concern = models.CharField(max_length=100)
	sub_concern = models.CharField(max_length=200)
	definition = models.TextField(blank=True, null=True)

	def __str__(self):
		return str(self.sub_id)+" - "+self.ecological_concern+": "+self.sub_concern

	class Meta:
		db_table = 'atlas_limiting_factor'
		ordering = ["ecological_concern"]

class restoration_actions(models.Model):
 	action_number = models.IntegerField(blank=True, null=True)
 	name = models.CharField(max_length=200, blank=True, null=True)

 	def __str__(self):
 		return str(self.action_number)+". "+self.name

 	class Meta:
 		db_table = 'atlas_restoration_actions'

class future_cond_scoring(models.Model):
	atlas_name = models.CharField(max_length=100)
	poor = models.FloatField(default=0.0)
	good = models.FloatField(default=0.0)
	fair = models.FloatField(default=0.0)
	excellent = models.FloatField(default=0.0)
	tbd = models.FloatField(default=0.0)

	def __str__(self):
		return (self.atlas_name)

	class Meta:
		db_table = 'atlas_future_cond_scoring'

class geomorphic_potential_scoring(models.Model):
	atlas_name = models.CharField(max_length=100)
	low = models.FloatField(default=0.0)
	med = models.FloatField(default=0.0)
	high = models.FloatField(default=0.0)
	tbd = models.FloatField(default=0.0)

	def __str__(self):
		return (self.atlas_name)

	class Meta:
		db_table = 'atlas_geomorphic_potential_scoring'

class current_cond_scoring(models.Model):
	atlas_name = models.CharField(max_length=100)
	poor = models.FloatField(default=0.0)
	good = models.FloatField(default=0.0)
	fair = models.FloatField(default=0.0)
	excellent = models.FloatField(default=0.0)
	tbd = models.FloatField(default=0.0)

	def __str__(self):
		return (self.atlas_name)

	class Meta:
		db_table = 'atlas_current_cond_scoring'

class current_temp_scoring(models.Model):
	atlas_name = models.CharField(max_length=100)
	lethal = models.FloatField(default=0.0)
	ok = models.FloatField(default=0.0)
	poor = models.FloatField(default=0.0)
	good = models.FloatField(default=0.0)
	fair = models.FloatField(default=0.0)
	excellent = models.FloatField(default=0.0)
	tbd = models.FloatField(default=0.0)

	def __str__(self):
		return (self.atlas_name)

	class Meta:
		db_table = 'atlas_current_temp_scoring'

class limiting_factor_scoring(models.Model):
	atlas_name = models.CharField(max_length=100)
	high_direct = models.FloatField(default=0.0)
	high_indirect = models.FloatField(default=0.0)
	med_direct = models.FloatField(default=0.0)
	med_indirect = models.FloatField(default=0.0)
	low_direct = models.FloatField(default=0.0)
	low_indirect = models.FloatField(default=0.0)

	def __str__(self):
		return (self.atlas_name)

	class Meta:
		db_table = 'atlas_limiting_factor_scoring'

class restoration_action_scoring(models.Model):
	atlas_name = models.CharField(max_length=100)
	low = models.FloatField(blank=True, null=True)
	low_immediate = models.FloatField(blank=True, null=True)
	low_long_term = models.FloatField(blank=True, null=True)
	med = models.FloatField(blank=True, null=True)
	med_immediate = models.FloatField(blank=True, null=True)
	med_long_term = models.FloatField(blank=True, null=True)
	high = models.FloatField(blank=True, null=True)
	high_immediate = models.FloatField(blank=True, null=True)
	high_long_term = models.FloatField(blank=True, null=True)
	tbd = models.FloatField(blank=True, null=True)

	def __str__(self):
		return (self.atlas_name)

	class Meta:
		db_table = 'atlas_restoration_action_scoring'

class natural_process_scoring(models.Model):
	atlas_name = models.CharField(max_length=100)
	habitat_creation = models.FloatField(blank=True, null=True)
	partial_restoration = models.FloatField(blank=True, null=True)
	full_restoration = models.FloatField(blank=True, null=True)

	def __str__(self):
		return(self.atlas_name)

	class Meta:
		db_table = 'atlas_natural_process_scoring'

class atlas(models.Model):
	atlas_name = models.CharField(max_length=100)
	atlas_desc = models.TextField(blank=True, null=True)
	p_score_cal_factor = models.FloatField(default=0.0)
	u_score_cal_factor = models.FloatField(default=0.0)
	geomorphic_potential_scoring_id = models.ForeignKey(geomorphic_potential_scoring, blank=True, null=True)
	current_cond_scoring_id = models.ForeignKey(current_cond_scoring, blank=True, null=True)
	current_temp_scoring_id = models.ForeignKey(current_temp_scoring, blank=True, null=True)
	future_cond_scoring_id = models.ForeignKey(future_cond_scoring, blank=True, null=True)
	limiting_factor_scoring_id = models.ForeignKey(limiting_factor_scoring, blank=True, null=True)
	restoration_action_scoring_id = models.ForeignKey(restoration_action_scoring, blank=True, null=True)
	natural_process_scoring_id = models.ForeignKey(natural_process_scoring, blank=True, null=True)
	opp_map_zoom = models.IntegerField(blank=True, null=True)
	opp_map_center = models.TextField(blank=True, null=True)
	CHOICES = ((True, "Single Species"), (False, "Multi Species"))
	p_score_mode = models.BooleanField(choices=CHOICES, default=False)
	def __str__(self):
		return (self.atlas_name)

	class Meta:
		db_table = 'atlas_atlas'

def upload_change_log_path(instance, filename):
	upload_dir = os.path.join("static", "documents",  "atlas", "log")
	if not os.path.exists(upload_dir):
		os.makedirs(upload_dir)
	return os.path.join(upload_dir, filename)

class atlas_change_log(models.Model):
	atlas_id = models.ForeignKey(atlas, blank=True, null=True)
	change_log_file = models.FileField(upload_to=upload_change_log_path, null=True, blank=True)

	def __str__(self):
		return (self.atlas_id.atlas_name)

	class Meta:
		db_table = 'atlas_atlas_change_log'

class p_period(models.Model):
	period = models.CharField(max_length=50)

	def __str__(self):
		return (self.period)

	class Meta:
		db_table = 'atlas_p_period'


class fish_use_scoring(models.Model):
	species = models.ForeignKey(species)
	atlas_id = models.ForeignKey(atlas, blank=True, null=True, related_name="life_stage_atlas_id")
	low = models.FloatField(default=0.0)
	med = models.FloatField(default=0.0)
	high = models.FloatField(default=0.0)
	none_apply = models.FloatField(default=0.0)

	def __str__(self):
		return (self.atlas_id.atlas_name+" - "+self.species.species_name)

	class Meta:
		db_table = 'atlas_fish_use_scoring'


class atlas_bsr_tier(models.Model):
	tier = models.CharField(max_length=50)

	def __str__(self):
		return (self.tier)

	class Meta:
		db_table = 'atlas_bsr_tier'

class atlas_bsr(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField(null=True, blank=True)
	CHOICES = (("Low", "Low"), ("Med", "Med"), ("High", "High"), ("TBD", "TBD"))
	CHOICES_3 = (("Poor", "Poor"), ("Fair", "Fair"), ("Good", "Good"), ("Excellent", "Excellent"), ("TBD", "TBD"), ("Lethal", "Lethal"), ("Ok", "Ok"))
	geomorphic_potential = models.CharField(max_length=50, choices=CHOICES, blank=True, null=True)
	CHOICES_2 = (("Poor", "Poor"), ("Fair", "Fair"), ("Good", "Good"), ("Excellent", "Excellent"), ("TBD", "TBD"))
	current_habitat_cond = models.CharField(max_length=50, choices=CHOICES_2, blank=True, null=True)
	current_temp = models.CharField(max_length=50, choices=CHOICES_3, blank=True, null=True)
	future_cond = models.CharField(max_length=50, choices=CHOICES_2, blank=True, null=True)

	def _calc_geomorphic(self):
		scoring = self.atlas_id.geomorphic_potential_scoring_id
		score = 0
		if scoring != None and scoring != "":
			if(self.geomorphic_potential == "Low"):
				score = scoring.low
			elif(self.geomorphic_potential == "Med"):
				score = scoring.med
			elif(self.geomorphic_potential == "High"):
				score = scoring.high
		score = round(score)
		return score

	def _calc_current_cond(self):
		scoring = self.atlas_id.current_cond_scoring_id
		score = 0
		if scoring != None and scoring != "":
			if(self.current_habitat_cond == "Poor"):
				score = scoring.poor
			elif(self.current_habitat_cond == "Fair"):
				score = scoring.fair
			elif(self.current_habitat_cond == "Good"):
				score = scoring.good
			elif(self.current_habitat_cond == "Excellent"):
				score = scoring.excellent
		score = round(score)
		return score

	def _calc_current_temp(self):
		scoring = self.atlas_id.current_temp_scoring_id
		score = 0
		if scoring != None and scoring != "":
			if(self.current_temp == "Poor"):
				score = scoring.poor
			elif(self.current_temp == "Fair"):
				score = scoring.fair
			elif(self.current_temp == "Good"):
				score = scoring.good
			elif(self.current_temp == "Excellent"):
				score = scoring.excellent
			elif(self.current_temp == "Lethal"):
				score = scoring.lethal
			elif(self.current_temp == "Ok"):
				score = scoring.ok
		score = round(score)
		return score

	def _calc_future_score(self):
		scoring = self.atlas_id.future_cond_scoring_id
		score = 0
		if scoring != None and scoring != "":
			if(self.future_cond == "Poor"):
				score = scoring.poor
			elif(self.future_cond == "Fair"):
				score = scoring.fair
			elif(self.future_cond == "Good"):
				score = scoring.good
			elif(self.future_cond == "Excellent"):
				score = scoring.excellent
		score = round(score)
		return score

	def _calc_p_score(self):
		score = self.raw_p_score*self.atlas_id.p_score_cal_factor
		score = round(score)
		return score

	def _calc_u_score(self):
		score = self.raw_u_score*self.atlas_id.u_score_cal_factor
		score = round(score)
		return score

	def _calc_raw_u_score(self):
		final_score = 0
		all_scores = utilization_score.objects.filter(utilization_id__bsr_id=self.id)
		for score in all_scores:
			final_score = final_score + score.score
		return final_score

	def _calc_raw_p_score(self):
		final_score = 0
		all_scores = life_stage.objects.filter(bsr_id=self.id)
		for stage in all_scores:
			stage_marked = False
			if stage.jan_a.period == 'Partial' or stage.jan_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.feb_a.period == 'Partial' or stage.feb_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.mar_a.period == 'Partial' or stage.mar_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.apr_a.period == 'Partial' or stage.apr_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.may_a.period == 'Partial' or stage.may_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.jun_a.period == 'Partial' or stage.jun_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.jul_a.period == 'Partial' or stage.jul_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.aug_a.period == 'Partial' or stage.aug_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.sep_a.period == 'Partial' or stage.sep_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.oct_a.period == 'Partial' or stage.oct_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.nov_a.period == 'Partial' or stage.nov_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.dec_a.period == 'Partial' or stage.dec_a.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.jan_b.period == 'Partial' or stage.jan_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.feb_b.period == 'Partial' or stage.feb_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.mar_b.period == 'Partial' or stage.mar_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.apr_b.period == 'Partial' or stage.apr_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.may_b.period == 'Partial' or stage.may_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.jun_b.period == 'Partial' or stage.jun_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.jul_b.period == 'Partial' or stage.jul_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.aug_b.period == 'Partial' or stage.aug_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.sep_b.period == 'Partial' or stage.sep_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.oct_b.period == 'Partial' or stage.oct_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.nov_b.period == 'Partial' or stage.nov_b.period == "Full":
				final_score=final_score+1
				stage_marked = True
			elif stage.dec_b.period == 'Partial' or stage.dec_b.period == "Full":
				final_score=final_score+1
				stage_marked = True

			if "chinook" in stage.species.species_name.lower() and stage.bsr_id.atlas_id.p_score_mode == True and stage_marked == True:
				final_score = final_score+2
		return final_score

	def _calc_cumulative_score(self):
		score = 0
		if self.atlas_id.id != 3:
			score = self.u_score+self.p_score+self.geomorphic_score+self.current_cond_score+self.current_temp_score
		elif self.atlas_id == 3:
			score = self.u_score+self.p_score+self.geomorphic_score+self.current_cond_score+self.future_cond_score
		score = round(score)
		return score

	p_score = property(_calc_p_score)
	u_score = property(_calc_u_score)
	raw_u_score = property(_calc_raw_u_score)
	raw_p_score = property(_calc_raw_p_score)
	geomorphic_score = property(_calc_geomorphic)
	current_cond_score = property(_calc_current_cond)
	current_temp_score = property(_calc_current_temp)
	future_score = property(_calc_future_score)
	cumulative_score = property(_calc_cumulative_score)
	tier_id = models.ForeignKey(atlas_bsr_tier, blank=True, null=True)
	atlas_id = models.ForeignKey(atlas, blank=True, null=True)
	periodicity_notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return (self.name)

	class Meta:
		db_table = 'atlas_bsr'

class life_stage(models.Model):
	species = models.ForeignKey(species)
	bsr_id = models.ForeignKey(atlas_bsr)
	life_stage_name = models.CharField(max_length=500)
	jan_a = models.ForeignKey(p_period, blank=True, null=True, related_name="jan_a", default=3)
	jan_b = models.ForeignKey(p_period, blank=True, null=True, related_name="jan_b", default=3)
	feb_a = models.ForeignKey(p_period, blank=True, null=True, related_name="feb_a", default=3)
	feb_b = models.ForeignKey(p_period, blank=True, null=True, related_name="feb_b", default=3)
	mar_a= models.ForeignKey(p_period, blank=True, null=True, related_name="mar_a", default=3)
	mar_b = models.ForeignKey(p_period, blank=True, null=True, related_name="mar_b", default=3)
	apr_a= models.ForeignKey(p_period, blank=True, null=True, related_name="apr_a", default=3)
	apr_b= models.ForeignKey(p_period, blank=True, null=True, related_name="apr_b", default=3)
	may_a= models.ForeignKey(p_period, blank=True, null=True, related_name="may_a", default=3)
	may_b = models.ForeignKey(p_period, blank=True, null=True, related_name="may_b", default=3)
	jun_a = models.ForeignKey(p_period, blank=True, null=True, related_name="jun_a", default=3)
	jun_b = models.ForeignKey(p_period, blank=True, null=True, related_name="jun_b", default=3)
	jul_a = models.ForeignKey(p_period, blank=True, null=True, related_name="jul_a", default=3)
	jul_b = models.ForeignKey(p_period, blank=True, null=True, related_name="jul_b", default=3)
	aug_a = models.ForeignKey(p_period, blank=True, null=True, related_name="aug_a", default=3)
	aug_b = models.ForeignKey(p_period, blank=True, null=True, related_name="aug_b", default=3)
	sep_a = models.ForeignKey(p_period, blank=True, null=True, related_name="sep_a", default=3)
	sep_b = models.ForeignKey(p_period, blank=True, null=True, related_name="sep_b", default=3)
	oct_a = models.ForeignKey(p_period, blank=True, null=True, related_name="oct_a", default=3)
	oct_b = models.ForeignKey(p_period, blank=True, null=True, related_name="oct_b", default=3)
	nov_a = models.ForeignKey(p_period, blank=True, null=True, related_name="nov_a", default=3)
	nov_b = models.ForeignKey(p_period, blank=True, null=True, related_name="nov_b", default=3)
	dec_a = models.ForeignKey(p_period, blank=True, null=True, related_name="dec_a", default=3)
	dec_b = models.ForeignKey(p_period, blank=True, null=True, related_name="dec_b", default=3)

	def __str__(self):
		label = self.bsr_id.name+" - "+self.species.species_name+" - "+self.life_stage_name
		return (label)

	class Meta:
		db_table = 'atlas_life_stage'

class periodicity(models.Model):
	bsr_id = models.ForeignKey(atlas_bsr)
	#notes replaces the need for periodicity_comment, but deleting periodicity_comment causes makemigrations to fail
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return (self.bsr_id.name)

	class Meta:
		db_table = 'atlas_periodicity'

def upload_periodicity_comment(instance, filename):
	upload_dir = os.path.join("static", "documents",  "atlas", "comments", "periodicity")
	if not os.path.exists(upload_dir):
		os.makedirs(upload_dir)
	return os.path.join(upload_dir, filename)

class periodicity_comment(models.Model):
	subject = models.CharField(max_length=200, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	user_id = models.ForeignKey(User, blank=True, null=True)
	attachment = models.FileField(upload_to=upload_periodicity_comment, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	periodicity_id = models.ForeignKey(periodicity, blank=True, null=True)

	def __str__(self):
		rtn = ""
		if self.subject != '' and self.subject != None:
			rtn = self.subject
		rtn = rtn + " - "+str(date_created)
		return rtn

	class Meta:
		db_table = 'atlas_periodicity_comment'

def upload_bsr_comment(instance, filename):
	upload_dir = os.path.join("static", "documents",  "atlas", "comments")
	if not os.path.exists(upload_dir):
		os.makedirs(upload_dir)
	return os.path.join(upload_dir, filename)

class bsr_comment(models.Model):
	subject = models.CharField(max_length=200, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	user_id = models.ForeignKey(User, blank=True, null=True)
	attachment = models.FileField(upload_to=upload_bsr_comment, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	bsr_id = models.ForeignKey(atlas_bsr, blank=True, null=True)

	def __str__(self):
		rtn = ""
		if self.subject != '' and self.subject != None:
			rtn = self.subject
		rtn = rtn + " - "+str(date_created)
		return rtn

	class Meta:
		db_table = 'atlas_bsr_comment'

class utilization(models.Model):
	bsr_id = models.ForeignKey(atlas_bsr)
	utilization_name = models.CharField(max_length=200)
	comment = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.bsr_id.name+" - "+self.utilization_name

	class Meta:
		db_table = 'atlas_utilization'

class utilization_score(models.Model):
	species = models.ForeignKey(species)
	utilization_id = models.ForeignKey(utilization)
	CHOICES = (("Low", "Low"), ("Med", "Med"), ("High", "High"), ("N/A", "N/A"))
	rating = models.CharField(max_length=50, choices=CHOICES, default="N/A", blank=True, null=True)

	def _calc_rating_score(self):
		score = 0
		score_table = fish_use_scoring.objects.filter(atlas_id=self.utilization_id.bsr_id.atlas_id).filter(species=self.species)[0]
		if score_table:
			if self.rating == "Low":
				score = score_table.low
			if self.rating == "Med":
				score = score_table.med
			if self.rating == "High":
				score = score_table.high
			if self.rating == "N/A":
				score = score_table.none_apply
		return score

	score = property(_calc_rating_score)

	def __str__(self):
		return self.utilization_id.bsr_id.name+" - "+self.species.species_name+" - "+self.utilization_id.utilization_name

	class Meta:
		db_table = 'atlas_utilization_score'

class limiting_factor_instance(models.Model):
	bsr_id = models.ForeignKey(atlas_bsr)
	limiting_factor_id = models.ForeignKey(limiting_factor)
	comment = models.TextField(blank=True, null=True)

	def __str__(self):
		return(self.bsr_id.name+" - "+str(self.limiting_factor_id))

	class Meta:
		db_table = 'atlas_limiting_factor_instance'

class limiting_factor_score(models.Model):
	species = models.ForeignKey(species)
	CHOICES = (("Low", "Low"), ("Med", "Med"), ("High", "High"), ("N/A", "N/A"))
	limiting_factor_instance_id = models.ForeignKey(limiting_factor_instance)
	rating = models.CharField(max_length=50, choices=CHOICES, blank=True, null=True, default="N/A")

	# def _calc_rating_score(self):
	# 	score = 0
	# 	score_table = atlas.objects.filter(id=self.limiting_factor_instance_id.bsr_id.atlas_id)[0].limiting_factor_scoring_id
	# 	if score_table != None:
	# 		if self.rating == "Low" && 
	# 	return score

	def __str__(self):
		return(self.limiting_factor_instance_id.bsr_id.name+" - "+str(self.species)+": "+str(self.rating)+" - "+str(self.limiting_factor_instance_id.limiting_factor_id))

	class Meta:
		db_table = 'atlas_limiting_factor_score'

class crosswalk(models.Model):
	atlas_id = models.ForeignKey(atlas)
	rest_action_id = models.ForeignKey(restoration_actions)
	limiting_factor_id = models.ForeignKey(limiting_factor)
	CHOICES = (("Direct", "Direct"), ("Indirect", "Indirect"))
	impact = models.CharField(max_length=50, choices=CHOICES)

	def __str__(self):
		return(str(self.impact)+" - "+str(self.rest_action_id)+" - "+str(self.limiting_factor_id.sub_id))

	class Meta:
		db_table = 'atlas_crosswalk'
		ordering = ["-rest_action_id", "-limiting_factor_id"]

class restoration_actions_score(models.Model):
	bsr_id = models.ForeignKey(atlas_bsr)
	restoration_action_id = models.ForeignKey(restoration_actions)
	CHOICES = (("Low", "Low"), ("Med", "Med"), ("High", "High"), ("N/A", "N/A"))
	immediate = models.CharField(max_length=50, choices=CHOICES, blank=True, null=True, default="N/A")
	long_term = models.CharField(max_length=50, choices=CHOICES, blank=True, null=True, default="N/A")
	priority = models.CharField(max_length=50, choices=CHOICES, blank=True, null=True, default="N/A")
	comment = models.TextField(blank=True, null=True, default="No Comment")
	def _calc_lf_score(self):
		total_score = 0
		score_table = atlas.objects.filter(id=self.bsr_id.atlas_id.id)
		cw = crosswalk.objects.filter(rest_action_id=self.restoration_action_id)
		if score_table != None and cw != None:
			score_table = score_table[0].limiting_factor_scoring_id
			for link in cw:
				lf_score = limiting_factor_score.objects.filter(limiting_factor_instance_id__limiting_factor_id=link.limiting_factor_id).filter(limiting_factor_instance_id__bsr_id=self.bsr_id)
				score = 0
				if lf_score != None:
					i=0
					for lf in lf_score:
						if lf.rating == "Low" and link.impact == "Direct":
							score = score+score_table.low_direct
						elif lf.rating == "Low" and link.impact == "Indirect":
							score = score+score_table.low_indirect
						elif lf.rating == "Med" and link.impact == "Direct":
							score = score+score_table.med_direct
						elif lf.rating == "Med" and link.impact == "Indirect":
							score = score+score_table.med_indirect
						elif lf.rating == "High" and link.impact == "Direct":
							score = score+score_table.high_direct
						elif lf.rating == "High" and link.impact == "Indirect":
							score = score+score_table.high_indirect
						i=i+1
					if i != 0:
						score=score/i
					total_score = round(total_score+score, 1)
		return total_score

	limiting_factor_score = property(_calc_lf_score)
	# immediate_score()
	# long_term_score

	def __str__(self):
		return(str(self.bsr_id)+" - "+str(self.restoration_action_id))

	class Meta:
		db_table = 'atlas_restoration_actions_score'

class opportunity_status(models.Model):
	CHOICES = (("Not Started", "Not Started"), ("Planning & Construction", "Planning & Construction"), ("Completed", "Completed"), ("On Hold", "On Hold"))
	status = models.CharField(choices=CHOICES, max_length=30)
	def _colorize_model(self):
		color = "#FF0000"
		if self.status == "Planning & Construction":
			color="#FFFF00"
		elif self.status == "Completed":
			color="#008000"
		elif self.status == "On Hold":
			color="#4E7DB8"
		return color

	color = property(_colorize_model)

	def __str__(self):
		return(self.status)

	class Meta:
		db_table = 'atlas_opportunity_status'


class bsr_opportunity(models.Model):
	bsr_id = models.ForeignKey(atlas_bsr)
	opportunity_name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	CHOICES = (("Habitat Creation", "Habitat Creation"), ("Partial Restoration", "Partial Restoration"), ("Full Restoration", "Full Restoration"))
	natural_process = models.CharField(max_length=50, choices=CHOICES, default="Habitat Creation")
	location = models.TextField(blank=True, null=True)
	zoom = models.IntegerField(blank=True, null=True)
	center = models.TextField(blank=True, null=True)
	comments = models.TextField(blank=True, null=True)
	WATER_RIGHT_CHOICES = (("N/A", "N/A"), ("1867-1869", "1867-1869"), ("1870-1879", "1870-1879"), ("1880-1889", "1880-1889"), ("1890-1899", "1890-1899"), ("1900-1909", "1900-1909"))
	water_right_date = models.CharField(max_length=20, default="N/A", choices=WATER_RIGHT_CHOICES)
	WATER_FLOW_CHOICES = (("N/A", "N/A"), ("< 0.5", "< 0.5"), ("0.5 - 2.5", "0.5 - 2.5"), ("> 2.5", "> 2.5"))
	water_flow_rate = models.CharField(max_length=20, default="N/A", choices=WATER_FLOW_CHOICES)
	status = models.ForeignKey(opportunity_status, blank=True, null=True)

	FC_CHOICES_YES_NO = (("Yes", "Yes"), ("No", "No"), ("TBD", "TBD"))
	FC_CHOICES_LOW_HIGH = (("Low", "Low"), ("Med", "Med"), ("High", "High"), ("TBD", "TBD"))
	fc_landowner_willingness = models.CharField(max_length=20, choices=FC_CHOICES_YES_NO, default="TBD")
	fc_design_effort = models.CharField(max_length=20, choices=FC_CHOICES_LOW_HIGH, default="TBD")
	fc_constuction_effort = models.CharField(max_length=20, choices=FC_CHOICES_LOW_HIGH, default="TBD")
	fc_site_access_effort = models.CharField(max_length=20, choices=FC_CHOICES_LOW_HIGH, default="TBD")
	fc_sm_dewatering_erosion_ctrl_effort = models.CharField(max_length=20, choices=FC_CHOICES_LOW_HIGH, default="TBD")
	fc_risk_goal_objectives = models.CharField(max_length=20, choices=FC_CHOICES_LOW_HIGH, default="TBD")
	fc_risk_public_safety = models.CharField(max_length=20, choices=FC_CHOICES_LOW_HIGH, default="TBD")
	fc_regulatory_requirements = models.CharField(max_length=20, choices=FC_CHOICES_LOW_HIGH, default="TBD")
	fc_value = models.CharField(max_length=20, choices=FC_CHOICES_LOW_HIGH, default="TBD")

	def _calc_natural_process_score(self):
		final_score = 0
		score_table = self.bsr_id.atlas_id.natural_process_scoring_id
		if score_table != None:
			if self.natural_process == "Habitat Creation":
				final_score = final_score + score_table.habitat_creation
			elif self.natural_process == "Partial Restoration":
				final_score = final_score + score_table.partial_restoration
			elif self.natural_process == "Full Restoration":
				final_score = final_score + score_table.full_restoration
		self.natural_process_score = round(final_score, 1)
		self.save()
		return round(final_score, 1)

	def _calc_restoration_action_priority_score(self):
		final_score = 0
		all_actions = bsr_opportunity_action.objects.filter(opportunity_id=self.id)
		score_table = self.bsr_id.atlas_id.restoration_action_scoring_id
		if score_table != None:
			for action in all_actions:
				if action.action_id.priority == "Low":
					final_score = final_score + score_table.low
				elif action.action_id.priority == "Med":
					final_score = final_score + score_table.med
				elif action.action_id.priority == "High":
					final_score = final_score + score_table.high
		self.restoration_action_priority_score = round(final_score*.10, 1)
		self.save()
		return round(final_score*.10, 1) 

	def _calc_long_term_score(self):
		final_score = 0
		all_actions = bsr_opportunity_action.objects.filter(opportunity_id=self.id)
		score_table = self.bsr_id.atlas_id.restoration_action_scoring_id
		if score_table != None:
			for action in all_actions:
				if action.action_id.long_term == "Low":
					final_score = final_score + score_table.low_long_term
				elif action.action_id.long_term == "Med":
					final_score = final_score + score_table.med_long_term
				elif action.action_id.long_term == "High":
					final_score = final_score + score_table.high_long_term
		self.long_term_score = round(final_score*.10, 1)
		self.save()
		return round(final_score*.10, 1)

	def _calc_immediate_term_score(self):
		final_score = 0
		all_actions = bsr_opportunity_action.objects.filter(opportunity_id=self.id)
		score_table = self.bsr_id.atlas_id.restoration_action_scoring_id
		if score_table != None:
			for action in all_actions:
				if action.action_id.immediate == "Low":
					final_score = final_score + score_table.low_immediate
				elif action.action_id.immediate == "Med":
					final_score = final_score + score_table.med_immediate
				elif action.action_id.immediate == "High":
					final_score = final_score + score_table.high_immediate
		self.immediate_score = round(final_score*.10, 1)
		self.save()
		return round(final_score*.10, 1)

	def _calc_limiting_factor_score(self):
		final_score = 0
		all_actions = bsr_opportunity_action.objects.filter(opportunity_id=self.id)
		score_table = self.bsr_id.atlas_id.restoration_action_scoring_id
		if score_table != None:
			for action in all_actions:
				final_score = final_score + round(action.action_id.limiting_factor_score, 2)
		self.limiting_factor_score = round(final_score*.10, 1)
		self.save()
		return round(final_score*.10, 1)

	def _calc_total_bbs_score(self):
		final_score = 0
		final_score = final_score+self.np_score
		final_score = final_score+self.rap_score
		final_score = final_score+self.lt_score
		final_score = final_score+self.imm_score
		final_score = final_score+self.lf_score
		final_score = final_score+self.wrd_score
		final_score = final_score+self.wfr_score
		self.total_bbs_score = round(final_score, 1)
		self.save()
		return round(final_score, 1)

	def _calc_water_right_score(self):
		score = 0
		if self.water_right_date == "1867-1869":
			score = 50
		elif self.water_right_date == "1870-1879":
			score = 40
		elif self.water_right_date == "1880-1889":
			score = 30
		elif self.water_right_date == "1890-1899":
			score = 20
		elif self.water_right_date == "1900-1909":
			score = 10
		self.water_right_date_score = score
		self.save()
		return score
	def _calc_water_flow_rate_score(self):
		score = 0
		if self.water_flow_rate == "< 0.5":
			score = 2
		elif self.water_flow_rate == "0.5 - 2.5":
			score = 5
		elif self.water_flow_rate == "> 2.5":
			score = 10
		self.water_flow_rate_score = score
		self.save()
		return score

	def _calc_longitudinal_score(self):
		score = 0.0
		score = score+self.wrd_score+self.wfr_score
		self.longitudinal_score = round(score, 1)
		self.save()
		return round(score, 1)

	wrd_score = property(_calc_water_right_score)
	wfr_score = property(_calc_water_flow_rate_score)
	l_score = property(_calc_longitudinal_score)
	np_score = property(_calc_natural_process_score)
	rap_score = property(_calc_restoration_action_priority_score)
	lt_score = property(_calc_long_term_score)
	imm_score = property(_calc_immediate_term_score)
	lf_score = property(_calc_limiting_factor_score)
	tbbs_score = property(_calc_total_bbs_score)

	water_right_date_score = models.FloatField(default=0.0)
	water_flow_rate_score = models.FloatField(default=0.0)
	longitudinal_score = models.FloatField(default=0.0)
	natural_process_score = models.FloatField(default=0.0)
	restoration_action_priority_score = models.FloatField(default=0.0)
	long_term_score = models.FloatField(default=0.0)
	immediate_score = models.FloatField(default=0.0)
	limiting_factor_score = models.FloatField(default=0.0)
	total_bbs_score = models.FloatField(default=0.0)

	def __str__(self):
		return(str(self.bsr_id)+" - "+self.opportunity_name)

	class Meta:
		db_table = 'atlas_bsr_opportunity'

class bsr_opportunity_action(models.Model):
	opportunity_id = models.ForeignKey(bsr_opportunity)
	action_id = models.ForeignKey(restoration_actions_score)

	def __str__(self):
		return(str(self.action_id))

	class Meta:
		db_table = "atlas_bsr_opportunity_action"

