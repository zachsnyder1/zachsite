from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

# The register object
register = template.Library()

def addbreaks(value):
	"""
	Replaces ' |PARAGRAPH-BREAK| ' in value with '<br><br>'.
	"""
	output = escape(value)
	return mark_safe(output.replace(' |PARAGRAPH-BREAK| ', '<br><br>'))

def nobreaks(value):
	"""
	Replaces ' |PARAGRAPH-BREAK| ' in value with ' '.
	"""
	output = escape(value)
	return mark_safe(output.replace(' |PARAGRAPH-BREAK| ', ' '))

def addlinks(value):
	"""
	Replaces '|LINK=href%@%link_text|' in value with 
	'<a href="href">link_text</a>'.
	"""
	output = escape(value)
	split_text = output.split("|")
	for i in range(len(split_text)):
		if split_text[i].find("LINK=") == -1:
			continue
		else:
			split_text[i] = split_text[i].replace("LINK=", '')
			href_linktext = split_text[i].split("%@%")
			split_text[i] = "<a href=\"{}\">{}</a>".format(href_linktext[0], href_linktext[1])
	processed = ''.join(split_text)
	return mark_safe(processed)

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

	value = "<pre><div>" + escape(value) + "</div></pre>"
	
	# wrap keywords in span.keyword
	for keyword in keywords:
		markedup = '<span class="keyw">{}</span>'.format(keyword)
		value = value.replace(keyword, markedup)
	
	return mark_safe(value)


register.filter('addbreaks', addbreaks)
register.filter('nobreaks', nobreaks)
register.filter('addlinks', addlinks)
register.filter('formatpython', formatpython)
