import sublime
import sublime_plugin

from Context.base import Base

class SelectionEmpty(Base):
  def on_query_context(self, *args):
    callback = lambda _, sel: sel.empty()
    return self._check_sel('selection_empty', callback, *args)

class SelectionBGreaterOrEqualA(Base):
  def on_query_context(self, *args):
    callback = lambda _, sel: sel.b >= sel.a
    return self._check_sel('selection_b_greater_or_equal_a', callback, *args)

class SelectionBGreaterA(Base):
  def on_query_context(self, *args):
    callback = lambda _, sel: sel.b > sel.a
    return self._check_sel('selection_b_greater_a', callback, *args)

class SelectionBLesserOrEqualA(Base):
  def on_query_context(self, *args):
    callback = lambda _, sel: sel.b <= sel.a
    return self._check_sel('selection_b_lesser_or_equal_a', callback, *args)

class SelectionBLesserA(Base):
  def on_query_context(self, *args):
    callback = lambda _, sel: sel.b < sel.a
    return self._check_sel('selection_b_lesser_a', callback, *args)