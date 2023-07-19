# -*- coding: utf-8 -*-
from prospector2.formatters import (
    json,
    text,
    grouped,
    emacs,
    yaml,
    pylint,
    xunit,
    vscode,
    pycodestyle,
    pythonexception,
)


__all__ = (
    'FORMATTERS',
)


FORMATTERS = {
    'json': json.JsonFormatter,
    'text': text.TextFormatter,
    'grouped': grouped.GroupedFormatter,
    'emacs': emacs.EmacsFormatter,
    'yaml': yaml.YamlFormatter,
    'pycodestyle': pycodestyle.PycodestyleFormatter,
    'pylint': pylint.PylintFormatter,
    'xunit': xunit.XunitFormatter,
    'vscode': vscode.VSCodeFormatter,
    'pythonexception': pythonexception.PythonExceptionFormatter,
}
