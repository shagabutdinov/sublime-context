import sublime
import sublime_plugin

from Context.base import Base

class Clipboard(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: sublime.get_clipboard(256)
    return self._check_sel('clipboard', callback, *args)
