"""
Tags and other extras for use in zachsite app's templates
"""

import re
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape


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


class AbstractSymbolType():
    """
    Abstract class for symbol type.
    """
    pattern = r''
    repl = r''
    decoration = ''

    def __init__(self):
        """
        Initialize with empty list to store found symbols.
        """
        self.found_symbols = []

    def find_symbol(self, search_string):
        """
        Find symbol in string.
        """
        symbol = re.sub(self.pattern, self.repl, search_string)
        if symbol != search_string:
            self.found_symbols.append(symbol.replace('\r', ''))
        else:
            pass


class PythonImportSymbolType(AbstractSymbolType):
    """
    Concrete class for import symbols in Python.
    """
    pattern = r'from [\w\S]* import ([\w\S]*)[\s]*$'
    repl = r'\1'
    decoration = '<span class="imp">{}</span>'


class PythonFunctionSymbolType(AbstractSymbolType):
    """
    Concrete class for function symbols in Python.
    """
    pattern = r'^def ([\w]*)\(.*\):'
    repl = r'\1'
    decoration = '<span class="func">{}</span>'


class PythonVarSymbolType(AbstractSymbolType):
    """
    Concrete class for var symbols in Python.
    """
    pattern = r'^([\w]*) = .*'
    repl = r'\1'
    decoration = '<span class="var">{}</span>'


class AbstractFormatter():
    """
    Abstract code formatter class.
    """
    comment_line_regex = r''  # override!
    keywords = []

    def __init__(self, raw_input):
        """
        Escape and store input.
        """
        self.symbol_types = []
        self.input = escape(raw_input).split('\n')

    def identify_symbols(self):
        """
        Indentify symbols for formatting.
        """
        for line in enumerate(self.input):
            # don't process comment lines
            if re.search(self.comment_line_regex, self.input[line[0]]):
                continue
            else:
                pass
            # generate lists of symbols to format
            for symbol_type in self.symbol_types:
                symbol_type.find_symbol(self.input[line[0]])

    def decorate_symbols(self):
        """
        Wrap symbols with HTML elements.
        """
        # decorate symbols:
        for line in enumerate(self.input):
            # don't process comment lines
            if re.search(self.comment_line_regex, self.input[line[0]]):
                continue
            else:
                pass
            for symbol_type in self.symbol_types:
                for symbol in symbol_type.found_symbols:
                    decorated = symbol_type.decoration.format(symbol)
                    self.input[line[0]] = self.input[line[0]].replace(symbol, decorated)
            for keyword in self.keywords:
                decorated = '<span class="keyw">{}</span>'.format(keyword)
                self.input[line[0]] = self.input[line[0]].replace(keyword, decorated)

    def get_output(self):
        """
        Return output after marking safe.
        """
        output = "<pre><div>" + '\n'.join(self.input) + "</div></pre>"
        return mark_safe(output)


class PythonFormatter(AbstractFormatter):
    """
    Concrete formatter class for Python code.
    """
    comment_line_regex = r'^[\s]*[#]'  # override!
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

    def __init__(self, raw_input):
        """
        Initialize.
        """
        super().__init__(raw_input)
        self.symbol_types = [
            PythonImportSymbolType(),
            PythonFunctionSymbolType(),
            PythonVarSymbolType()
        ]


def formatpython(value):
    """
    Formats a code string for proper styling.
    """
    py_formatter = PythonFormatter(value)
    py_formatter.identify_symbols()
    py_formatter.decorate_symbols()
    return py_formatter.get_output()


# The register object
register = template.Library()
register.filter('no_breaks', no_breaks)
register.filter('add_breaks', add_breaks)
register.filter('formatpython', formatpython)
