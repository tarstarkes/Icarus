from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='stepwise_home'),
    url(r'^stepwise_portal/$', views.stepwise_portal, name="stepwise_portal"),
    url(r'^stepwise_detail/(?P<process_id>[0-9]*)/$', views.stepwise_detail, name="stepwise_detail"),
    url(r'^edit_prospectus/(?P<process_id>[0-9]*)/$', views.stepwise_edit_prospectus, name="stepwise_edit_prospectus"),
    url(r'^stepwise_prospectus/(?P<step>[0-9]*)/$', views.stepwise_prospectus, name="stepwise_prospectus"),
    url(r'^stepwise_prospectus/clean/(?P<step>[0-9]*)/$', views.stepwise_prospectus_clean_model, name="stepwise_prospectus_clean_model"),
    url(r'^stepwise_prospectus/(?P<step>add_landowner)/$', views.stepwise_prospectus, name="add_landowner"),
    url(r'^stepwise_prospectus/delete_landowner/(?P<landowner_id>[0-9]*)/$', views.stepwise_delete_landowner, name="delete_landowner"),
    url(r'^generate_prospectus/(?P<process_id>[0-9]*)/$', views.stepwise_generate_prospectus, name="stepwise_generate_prospectus"),
    url(r'^stepwise_comment/(?P<process_id>[0-9]*)/$', views.stepwise_comment, name="stepwise_comment"),
    url(r'^stepwise_comment_admin/(?P<process_id>[0-9]*)/$', views.stepwise_comment_admin, name="stepwise_comment_admin"),
    url(r'^upload_draft/(?P<process_id>[0-9]*)/$', views.stepwise_upload_draft, name="stepwise_upload_draft"),
    url(r'^stepwise_portal_admin/$', views.stepwise_portal_admin, name="stepwise_portal_admin"),
	url(r'^stepwise_portal_admin/stepwise_project_delete/(?P<process_id>[0-9]*)/$', views.stepwise_project_delete, name="stepwise_project_delete"),
	url(r'^stepwise_portal_admin/stepwise_project_detail_admin/(?P<process_id>[0-9]*)/$', views.stepwise_project_detail_admin, name="stepwise_project_detail_admin"),
	url(r'^stepwise_portal_admin/review_prospectus_approve/(?P<process_id>[0-9]*)/$', views.review_prospectus_approve, name="review_prospectus_approve"),
	url(r'^stepwise_portal_admin/review_prospectus_deny/(?P<process_id>[0-9]*)/$', views.review_prospectus_deny, name="review_prospectus_deny"),
	url(r'^stepwise_portal_admin/oweb_app_submitted/(?P<process_id>[0-9]*)/$', views.oweb_app_submitted, name="oweb_app_submitted"),
	url(r'^stepwise_portal_admin/evaluate_draft_approve/(?P<process_id>[0-9]*)/$', views.evaluate_draft_approve, name="evaluate_draft_approve"),
	url(r'^stepwise_portal_admin/evaluate_draft_deny/(?P<process_id>[0-9]*)/$', views.evaluate_draft_deny, name="evaluate_draft_deny"),
	url(r'^stepwise_portal_admin/final_approval_approve/(?P<process_id>[0-9]*)/$', views.final_approval_approve, name="final_approval_approve"),
	url(r'^stepwise_portal_admin/final_approval_deny/(?P<process_id>[0-9]*)/$', views.final_approval_deny, name="final_approval_deny"),
	url(r'^upload_final/(?P<process_id>[0-9]*)/$', views.stepwise_upload_final, name="stepwise_upload_final"),

]