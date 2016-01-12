import re
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

# The register object
register = template.Library()


def no_breaks(value):
	"""
	Replaces ' |PARAGRAPH-BREAK| ' in value with ' '.
	"""
	safe_input = escape(value)
	return mark_safe(safe_input.replace(' |PARAGRAPH-BREAK| ', ' '))

def add_breaks(value):
	"""
	Replaces ' |PARAGRAPH-BREAK| ' in value with '<br><br>'.
	"""
	safe_input = escape(value)
	return mark_safe(safe_input.replace(' |PARAGRAPH-BREAK| ', '<br><br>'))

def formatpython(value):
	"""
	Formats a code string for proper styling.
	"""
	output = None
	keywords = [
		'and ',
		'as ',
		'assert',
		'break',
		'class ',
		'continue',
		'def ',
		'del ',
		'elif',
		'else',
		'except',
		'finally',
		'for ',
		'from',
		'global',
		'if ',
		'import',
		'in ',
		'is ',
		'lambda',
		'nonlocal',
		'not ',
		'or ',
		'pass',
		'raise',
		'return',
		'try',
		'while',
		'with ',
		'yield'
	]
	
	safe_input = escape(value)
	value = "<pre><div>" + safe_input + "</div></pre>"
	
	# wrap keywords in span.keyword
	for keyword in keywords:
		markedup = '<span class="keyw">{}</span>'.format(keyword)
		value = value.replace(keyword, markedup)
	
	return mark_safe(value)


register.filter('no_breaks', no_breaks)
register.filter('add_breaks', add_breaks)
register.filter('formatpython', formatpython)
