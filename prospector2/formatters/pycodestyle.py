from prospector2.formatters.base import Formatter


__all__ = (
    'PycodestyleFormatter',
)


class PycodestyleFormatter(Formatter):
    """
    Format messages the same way as Python's own exceptions to be
    parseable (such as to navigate to the source line by double-clicking
    the error in Geany and possibly other IDEs).
    """

    def render(self, summary=True, messages=True, profile=False):
        # this formatter will always ignore the summary and profile
        output = []
        for message in sorted(self.messages):
            #   ={path}:{line}: [{msg_id}({symbol}), {obj}] {msg}
            # prospector/configuration.py:65: [missing-docstring(missing-docstring), build_default_sources] \
            # Missing function docstring
            template = '%(path)s:%(line)s:%(col)s: [%(code)s(%(source)s), %(function)s] %(message)s'
            output.append(template % {
                'path': message.location.path,
                'line': message.location.line,
                'col': message.location.character if message.location.character else 0,
                'source': message.source,
                'code': message.code,
                'function': message.location.function,
                'message': message.message.strip()
            })

        return '\n'.join(output)
