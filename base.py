import sublime
import sublime_plugin
import re

class Base(sublime_plugin.EventListener):
  def _check_value(self, value, operator, operand):
    if operator == sublime.OP_EQUAL:
      return value == operand
    elif operator == sublime.OP_NOT_EQUAL:
      return value != operand
    elif operator == sublime.OP_REGEX_MATCH:
      return re.match(operand, value) != None
    elif operator == sublime.OP_NOT_REGEX_MATCH:
      return re.match(operand, value) == None
    elif operator == sublime.OP_REGEX_CONTAINS:
      return re.search(operand, value) != None
    elif operator == sublime.OP_NOT_REGEX_CONTAINS:
      return re.search(operand, value) == None
    else:
      raise Exception('Unsupported operator: ' + str(operator))


  def _check_sel(self, name, callback, view, key, operator, operand, match_all):
    if key != name:
      return None

    result = True
    for sel in view.sel():
      value = callback(view, sel)
      result = self._check_value(value, operator, operand)
      if not match_all:
        return result

      if not result:
        return False

    return True

  def _check(self, name, callback, view, key, operator, operand, match_all):
    if key != name:
      return None

    result = True
    value = callback(view)
    return self._check_value(value, operator, operand)