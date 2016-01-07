import re
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

# The register object
register = template.Library()

def addlinks(input):
	"""
	Replaces '|LINK=href%@%link_text|' in value with 
	'<a href="href">link_text</a>'.
	"""
	split_text = input.split("|")
	for i in range(len(split_text)):
		if split_text[i].find("LINK=") == -1:
			continue
		else:
			split_text[i] = split_text[i].replace("LINK=", '')
			href_linktext = split_text[i].split("%@%")
			split_text[i] = "<a href=\"{}\">{}</a>".\
				format(href_linktext[0], href_linktext[1])
	return ''.join(split_text)

def nolinks(input):
	"""
	Replaces '|LINK=href%@%link_text|' in value with 
	'<a href="href">link_text</a>'.
	"""
	link_regex = r'\|LINK=[^\|]*[%][@][%](?P<link_text>[^\|]*)\|'
	return re.sub(link_regex, r'\1', input)

# <<<-------- FILTERS -------->>>
def no_breaks_or_links(value):
	"""
	Just adds links...
	"""
	safe_input = escape(value)
	breaks_removed = safe_input.replace(' |PARAGRAPH-BREAK| ', ' ')
	return mark_safe(nolinks(breaks_removed))

def breaks_and_links(value):
	"""
	Replaces ' |PARAGRAPH-BREAK| ' in value with ' '.
	
	        Then:
	
	Replaces '|LINK=href%@%link_text|' in value with 
	'<a href="href">link_text</a>'.
	"""
	breaks_added = escape(value).replace(' |PARAGRAPH-BREAK| ', '<br><br>')
	return mark_safe(addlinks(breaks_added))

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
