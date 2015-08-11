import sublime
import sublime_plugin

from Statement import statement
from Context.base import Base

class Statement(Base):
  def on_query_context(self, *args):
    return self._check_sel('statement', self._get_text, *args)

  def _get_text(self, view, sel):
    current = statement.get_statement(view, sel.begin())
    region = sublime.Region(*current)
    result = view.substr(region)
    return result