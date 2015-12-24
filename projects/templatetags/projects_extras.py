from django import template
from django.utils.safestring import mark_safe

# The register object
register = template.Library()

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

	value = "<pre><div>" + value + "</div></pre>"
	
	# wrap keywords in span.keyword
	for keyword in keywords:
		markedup = '<span class="keyw">{}</span>'.format(keyword)
		value = value.replace(keyword, markedup)
	
	return mark_safe(value)


register.filter('formatpython', formatpython)