import sublime
import sublime_plugin

from Context.base import Base

try:
  from Expression import expression
  from Statement import statement
except ImportError:
  sublime.error_message("Dependency import failed; please read readme for " +
   "SnippetManager plugin for installation instructions; to disable this " +
   "message remove this plugin")


class InArguments(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: statement.is_arguments(view, sel.b)
    return self._check_sel('in_arguments', callback, *args)