from prompt_toolkit.buffer import Buffer
from prompt_toolkit.filters import Condition

class CypherBuffer(Buffer):

    def __init__(self, *args, **kwargs):

        @Condition
        def is_multiline():
            text = self.document.text
            return not self.user_wants_out(text)

        super(self.__class__, self).__init__(*args, is_multiline=is_multiline, **kwargs)

    def user_wants_out(self, text):
        return any(
            [
                text.endswith(";"),
                text == "quit",
                text == "exit"
            ]
        )