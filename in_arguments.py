import sublime
import sublime_plugin

from Context.base import Base
from Expression import expression
from Statement import statement

class InArguments(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: statement.is_arguments(view, sel.b)
    return self._check_sel('in_arguments', callback, *args)