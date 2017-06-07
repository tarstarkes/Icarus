"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='atlas_home'),
    url(r'^go_to_atlas/(?P<atlas_id>.*)/$', views.BSR_view, name='atlas_BSR_view'),
    url(r'^get_access/(?P<atlas>.*)/$', views.get_access, name='atlas_get_access'),
    url(r'^add_new_bsr/(?P<atlas_id>.*)/$', views.add_new_bsr, name='add_new_bsr'),
    url(r'^go_to_bsr/(?P<bsr_id>.*)/$', views.BSR_detail, name='BSR_detail'),
    url(r'^bsr_comment/(?P<bsr_id>.*)/$', views.bsr_create_comment, name='bsr_create_comment'),
    url(r'^go_to_opportunity/(?P<opp_id>.*)/$', views.opportunity_detail, name='opportunity_detail'),
    url(r'^edit_bsr/(?P<bsr_id>.*)/$', views.edit_bsr, name='edit_bsr'),
    url(r'^update_tier/(?P<bsr_id>.*)/$', views.update_tier, name='update_tier'),
    url(r'^add_new_life_stage/(?P<bsr_id>.*)/$', views.add_new_life_stage, name='add_new_life_stage'),
    url(r'^delete_life_stage/(?P<life_stage_id>.*)/$', views.delete_life_stage, name='delete_life_stage'),
    url(r'^update_fish_use/(?P<bsr_id>.*)/$', views.update_fish_use, name='update_fish_use'),
    url(r'^add_new_fish_use/(?P<bsr_id>.*)/$', views.add_new_fish_use, name='add_new_fish_use'),
    url(r'^delete_fish_use/(?P<util_id>.*)/$', views.delete_fish_use, name='delete_fish_use'),
    url(r'^add_new_limiting_factor/(?P<bsr_id>.*)/$', views.add_new_limiting_factor, name='add_new_limiting_factor'),
    url(r'^update_limiting_factors/(?P<bsr_id>.*)/$', views.update_limiting_factors, name='update_limiting_factors'),
    url(r'^delete_limiting_factor/(?P<lf_id>.*)/$', views.delete_limiting_factor, name='delete_limiting_factor'),
    url(r'^update_rest_actions/(?P<bsr_id>.*)/$', views.update_rest_actions, name='update_rest_actions'),
    url(r'^add_new_opp/(?P<bsr_id>.*)/$', views.add_new_opp, name='add_new_opp'),
    url(r'^edit_opp/(?P<opp_id>.*)/$', views.edit_opp, name='edit_opp'),
    url(r'^update_opp_map/(?P<opp_id>.*)/$', views.update_opp_map, name='update_opp_map'),
    url(r'^add_opp_limiting_factor/(?P<opp_id>.*)/$', views.add_opp_limiting_factor, name='add_opp_limiting_factor'),
    url(r'^update_opp_np/(?P<opp_id>.*)/$', views.update_opp_np, name='update_opp_np'),
    url(r'^update_longitudinal_score/(?P<opp_id>.*)/$', views.update_longitudinal_score, name='update_longitudinal_score'),
    url(r'^update_fc/(?P<opp_id>.*)/$', views.update_fc, name='update_fc'),
    url(r'^update_opp_comment/(?P<opp_id>.*)/$', views.update_opp_comment, name='update_opp_comment'),
    url(r'^update_opp_desc/(?P<opp_id>.*)/$', views.update_opp_desc, name='update_opp_desc'),
    url(r'^delete_lf_score/(?P<lf_id>.*)/$', views.delete_lf_score, name='delete_lf_score'),
    url(r'^go_to_opp_map/(?P<atlas_id>.*)/$', views.atlas_opp_map, name='atlas_opp_map'),

]

