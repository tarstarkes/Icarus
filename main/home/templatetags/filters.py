from django import template
from django.contrib.auth.models import Group
from jinja2 import Environment

register = template.Library()

@register.filter(is_safe=True)
def has_group(user, group):
	get_group = Group.objects.get(name=group)
	return get_group in user.groups.all()