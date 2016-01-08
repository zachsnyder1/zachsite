import re
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

# The register object
register = template.Library()


def no_breaks_or_links(value):
	"""
	Replaces ' |PARAGRAPH-BREAK| ' in value with ' '.
	
	       Then:
	    
	Replaces '|LINK=href%@%link_text|' in value with 
	'<a href="href">link_text</a>'.
	"""
	safe_input = escape(value)
	breaks_removed = safe_input.replace(' |PARAGRAPH-BREAK| ', ' ')
	# Regex search string:
	link_regex = r'\|LINK=[^\|]*[%][@][%](?P<link_text>[^\|]*)\|'
	# Simply strips the preprocessing syntax:
	return mark_safe(re.sub(link_regex, r'\1', breaks_removed))

def breaks_and_links(value):
	"""
	Replaces ' |PARAGRAPH-BREAK| ' in value with '<br><br>'.
	
	        Then:
	
	Replaces '|LINK=href%@%link_text|' in value with 
	'<a href="href">link_text</a>'.
	"""
	breaks_added = escape(value).replace(' |PARAGRAPH-BREAK| ', '<br><br>')
	# Regex search string:
	link_regex = r'\|LINK=(?P<href>[^\|]*)[%][@][%](?P<link_text>[^\|]*)\|'
	# Strip preprocessing sytax, add HTML syntax:
	replacement_regex = r'<a href="\1">\2</a>'
	return mark_safe(re.sub(link_regex, replacement_regex, breaks_added))

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


register.filter('no_breaks_or_links', no_breaks_or_links)
register.filter('breaks_and_links', breaks_and_links)
register.filter('formatpython', formatpython)
