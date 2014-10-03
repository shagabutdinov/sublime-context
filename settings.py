import sublime
import sublime_plugin

from Context.base import Base

class Settings(Base):
  def on_query_context(self, view, key, *args):
    if not key.startswith('settings.'):
      return None

    setting = str(view.settings().get(key.split('.', 2)[1], None))
    if setting == None:
      return False

    return self._check_value(setting, *args[:-1])