import sublime
import sublime_plugin
import re
from Expression import expression

class Base(sublime_plugin.EventListener):

  def _check_value(self, value, operator, operand):
    try:
      if operator == sublime.OP_EQUAL:
        return value == operand
      elif operator == sublime.OP_NOT_EQUAL:
        return value != operand
      elif operator == sublime.OP_REGEX_MATCH:
        return value != None and re.match(operand, value) != None
      elif operator == sublime.OP_NOT_REGEX_MATCH:
        return value == None or re.match(operand, value) == None
      elif operator == sublime.OP_REGEX_CONTAINS:
        return value != None and re.search(operand, value) != None
      elif operator == sublime.OP_NOT_REGEX_CONTAINS:
        return value == None or re.search(operand, value) == None
      else:
        raise Exception('Unsupported operator: ' + str(operator))
    except Exception as error:
      print('Failed to check context', operand, value, error)
      raise error

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