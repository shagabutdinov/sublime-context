import sublime
import sublime_plugin

from Context.base import Base
from Expression import expression
from IndentationNavigation import indentation_navigation
import re

class InClassDefinition(Base):
  def on_query_context(self, view, *args):
    return self._check_sel('in_class_definition', self._check_point,
        view, *args)

  def _check_point(self, view, sel):
    nesting = expression.get_nesting(view, sel.a, None, {}, r'[\(]')
    if nesting != None:
      return False

    point = sel.a

    point = indentation_navigation.get_point(view, point, alignment = "left",
      backward = True, before = 1, type = "lesser")
    if point == 0:
      text = view.substr(view.line(0))
    else:
      text = view.substr(sublime.Region(max(point - 512, 0), point))

    expr = r'(\n|^)\s*(class|module|interface|trait).*(\s*\{\s*)?$'
    return re.search(expr, text, re.IGNORECASE) != None

class ClassName(Base):
  def on_query_context(self, view, *args):
    return self._check_sel('class_name', self._get_class_name, view, *args)

  def _get_class_name(self, view, point):
    expr = r'(?:\n|^)\s*((class|module|interface).*)\n'
    text = view.substr(sublime.Region(0, view.size()))
    match = expression.find_match(view, point.begin(), expr, {
        'backward': True,
        'nesting': True,
        'options': re.IGNORECASE,
    })

    if match == None:
      return None

    return match.group(1)