import sublime
import sublime_plugin
import re

from Context.base import Base

try:
  from Expression import expression
  from Statement import statement
except ImportError:
  sublime.error_message("Dependency import failed; please read readme for " +
   "Context plugin for installation instructions; to disable this " +
   "message remove this plugin")

class CalledMethod(Base):

  def _get_value(self, view, sel):
    nesting = expression.get_nesting(view, sel.begin(), 2048, {}, r'\(')
    if nesting == None:
      return None

    start, end = nesting[0], nesting[1]

    previous_text = view.substr(sublime.Region(0, start - 1))
    matches = re.search(r'([\w?!]+)\s*$', previous_text)
    if matches == None:
      return None

    return matches.group(1)

  def on_query_context(self, *args):
    return self._check_sel('called_method', self._get_value, *args)
