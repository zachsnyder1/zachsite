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
	imports, functions, variables = [], [], []
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
	input_lines = safe_input.split('\n')
	
	for line in range(len(input_lines)):
		# don't process one line comments
		if re.search(r'^[\s]*[#]', input_lines[line]):
			continue
		else:
			pass
		
		# add imported entities to imports list
		isymbol = re.sub(r'from [\w\S]* import ([\w\S]*)[\s]*$',
						r'\1',
						input_lines[line])
		if isymbol != input_lines[line]:
			imports.append(isymbol.replace('\r', ''))
		else:
			pass				
		
		# add function names to symbols list
		fsymbol = re.sub(r'^def ([\w]*)\(.*\):', 
						r'\1', 
						input_lines[line])
		if fsymbol != input_lines[line]:
			functions.append(fsymbol.replace('\r', ''))
		else:
			pass
		
		# add var names to symbols list
		vsymbol = re.sub(r'^([\w]*) = .*',
						r'\1',
						input_lines[line])
		if vsymbol != input_lines[line]:
			variables.append(vsymbol.replace('\r', ''))
		else:
			pass
		
		# decorate symbols:
		for imp in imports:
			markedup = '<span class="imp">{}</span>'.format(imp)
			input_lines[line] = input_lines[line].replace(imp, markedup)
		
		# decorate symbols:
		for func in functions:
			markedup = '<span class="func">{}</span>'.format(func)
			input_lines[line] = input_lines[line].replace(func, markedup)
		
		# decorate symbols:
		for var in variables:
			markedup = '<span class="var">{}</span>'.format(var)
			input_lines[line] = input_lines[line].replace(var, markedup)
		
		# decorate keywords:
		for keyword in keywords:
			markedup = '<span class="keyw">{}</span>'.format(keyword)
			input_lines[line] = input_lines[line].replace(keyword, markedup)
	
	output = "<pre><div>" + '\n'.join(input_lines) + "</div></pre>"
	return mark_safe(output)
		
		
register.filter('no_breaks', no_breaks)
register.filter('add_breaks', add_breaks)
register.filter('formatpython', formatpython)
