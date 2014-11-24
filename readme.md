# Context

Low-level plugin that provides "check context" functionality for other plugins
just like "context" section in .sublime-keymap works.

It also provides several basic contexts that can be used with this library or
in .sublime-keymap files. This conexts are listed below.


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Dependecies

None


### Api

  **context.check(view, context)**

  Check given context in given view. If one of
  contexts passed to array returns false result of call will be false. If no
  context key found, exception will be raised.

  - view - view (sublime.View) where context should be checked

  - context - array of dicts with following format:
    ```
    [
      {
        "key": key,
        "operator": operator,
        "operand": value,
        "match_all" true/false,
      },

      {
        "key": key,
        "operator": operator,
        "operand": value,
      },

      // ...
    ]
    ```

  - key - context key (string) that will be checked by corresponding plugin;
    refer to context providers plugins to see which keys can be passed to
    this parameter

  - operator - string that can one following values: 'equal', 'not_equal',
    'regex_match', 'not_regex_match', 'regex_contains', 'not_regex_contains'

  - operand - value that should be applied to key with operator

  - match_all - match all cursors with provided context or one is enought


### Examples

    from Context import context

    class TestCommand(sublime_plugin.TextCommand):
      def run(self, edit):
        is_python_file = {
          "key": "file_name",
          "operator": "regex_contains",
          "operand": "py$",
        }

        is_file_in_tests = {
          "key": "file_name",
          "operator": "regex_contains",
          "operand": "/tests/",
        }

        if context.check(self.view, [is_python_file, is_file_in_tests]):
          print("This file is python file in tests directory!")


### Provided context keys

- **file_name** - is name of file matches provided regexp
- **selection_empty** - is selection empty
- **selection_b_greater_or_equal_a** - is sel.b >= sel.a
- **selection_b_greater_a** - is sel.b > sel.a
- **selection_b_lesser_or_equal_a** - is sel.b <= sel.a
- **selection_b_lesser_a** - is sel.b < sel.a
- **line_b** - line that contains sel.b: view.substr(view.line(sel.b))
- **following_text_a** - text to EOL after sel.a
- **following_text_b** - text to EOL after sel.b
- **following_text_begin** - text to EOL after min(sel.a, sel.b)
- **following_text_end** - text to EOL after max(sel.a, sel.b)
- **preceding_text_a** - text to BOL before a
- **preceding_text_b** - text to BOL before b
- **preceding_text_begin** - text to BOL before min(sel.a, sel.b)
- **preceding_text_end** - text to BOL before max(sel.a, sel.b)