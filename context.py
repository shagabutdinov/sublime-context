import sublime
import sublime_plugin
import importlib
import os
import re

ignore = ['Package Control', 'SublimeLinter', 'Default']
class Context():
  def __init__(self):
    self.listeners, self.files = self._create_listeners()

    self.operators = {
      'equal': sublime.OP_EQUAL,
      'not_equal': sublime.OP_NOT_EQUAL,
      'regex_match': sublime.OP_REGEX_MATCH,
      'not_regex_match': sublime.OP_NOT_REGEX_MATCH,
      'regex_contains': sublime.OP_REGEX_CONTAINS,
      'not_regex_contains': sublime.OP_NOT_REGEX_CONTAINS,
    }

  def _create_listeners(self):
    result, files = [], []

    resources = sublime.find_resources('*.py')
    for resource in resources:
      full_path = os.path.join(sublime.packages_path(), '..', resource)
      full_path = os.path.normpath(full_path)

      _, resource = resource.split('/', 1) # remove Packages/ from path

      resource, _ = os.path.splitext(resource)
      resource = resource.replace('/', '.')

      ignored = False
      for ignore_regexp in ignore:
        if re.search(ignore_regexp, resource):
          ignored = True

      if ignored:
        continue

      try:
        module = importlib.import_module(resource)
      except :
        continue

      for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        is_event_listener = (isinstance(attribute, type) and
          issubclass(attribute, sublime_plugin.EventListener) and
          hasattr(attribute, 'on_query_context'))

        if not is_event_listener:
          continue

        result.append(attribute())
        files.append(full_path)

    return result, files

  def check(self, view, context):
    for item in context:
      found = False
      key, operator, operand, match_all = self._prepare_context_item(item)
      for listener in self.listeners:
        query_result = listener.on_query_context(view, key, operator, operand,
          match_all)

        if query_result == None:
          continue

        if not query_result:
          return False

        found = True
        break

      if not found:
        raise Exception('Context "' + key + '" not found')

    return True

  def _prepare_context_item(self, item):
    key = item['key']
    operator = self.operators[item['operator']]
    operand = item['operand']
    match_all = item.get('match_all', False)

    return key, operator, operand, match_all

context_object = None
def check(view, context):
  global context_object
  if context_object == None:
    context_object = Context()

  return context_object.check(view, context)

class ReloadContextListeners(sublime_plugin.TextCommand):
  def run(self, edit):
    global context_object
    context_object = None

class ReloadContextListener(sublime_plugin.EventListener):
  def on_post_save_async(self, view):
    global context_object
    if context_object == None:
      return

    if view.file_name() in context_object.files:
      view.run_command('reload_context_listeners')