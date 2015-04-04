import sublime
import sublime_plugin

from Context.base import Base
from Expression import expression

class Nesting(Base):

  def _get_value(self, view, sel):
    begin = expression.get_nesting_type(view, sel.begin(), 2048)

    if sel.begin() != sel.end():
      if begin != expression.get_nesting_type(view, sel.end(), 2048):
        return None

    return begin

  def on_query_context(self, *args):
    return self._check_sel('nesting', self._get_value, *args)

class NestingBegin(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: expression.get_nesting_type(view, sel.begin(),
      2048)
    return self._check_sel('nesting_begin', callback, *args)

class NestingEnd(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: expression.get_nesting_type(view, sel.end(),
      2048)
    return self._check_sel('nesting_end', callback, *args)