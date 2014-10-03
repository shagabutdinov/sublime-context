import sublime
import sublime_plugin

from Context.base import Base

class FileName(Base):
  def on_query_context(self, *args):
    callback = lambda view: view.file_name() or ''
    return self._check('filename', callback, *args)