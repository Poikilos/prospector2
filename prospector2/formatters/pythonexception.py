import re
import os

from prospector2.formatters.text import TextFormatter


__all__ = (
    'PythonExceptionFormatter',
)


class PythonExceptionFormatter(TextFormatter):
    """
    Format the location heading above each message the same way as
    Python's own exceptions to be parseable (such as to navigate to the
    source line by double-clicking the error in Geany and possibly
    other IDEs).
    """

    def render_messages(self):
        output = []
        for message in sorted(self.messages):
            # INFO: filename is the *linter* not the target here
            line = message.location.line
            fn_name = message.location.function
            output.append('  File "%s", line %s, in %s'
                          '' % (message.location.path, line, fn_name))
            character = message.location.character
            output.append(
                '    %s: %s / %s%s' % (
                    message.source,
                    message.code,
                    message.message,
                    (' (col %s)' % character) if character else '',
                )
            )

        output.append('')

        return '\n'.join(output)
