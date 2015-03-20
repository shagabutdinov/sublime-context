import sublime
import sublime_plugin

from Context.base import Base


class LineB(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.substr(view.line(sel.b))
    return self._check_sel('line', callback, *args)

  def _get_text(self, view, sel):
    return view.substr(view.line(sel.b))

class FollowingTextA(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(sel.a, view.line(sel.a).b))

    return self._check_sel('following_text_a', callback, *args)

class FollowingTextB(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(sel.b, view.line(sel.b).b))

    return self._check_sel('following_text_b', callback, *args)

class FollowingTextBegin(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(sel.begin(), view.line(sel.b).b))

    return self._check_sel('following_text_begin', callback, *args)

class FollowingTextEnd(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(sel.end(), view.line(sel.b).b))

    return self._check_sel('following_text_end', callback, *args)

class PrecedingTextA(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(view.line(sel.a).a, sel.a))

    return self._check_sel('preceding_text_a', callback, *args)

class PrecedingTextB(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(view.line(sel.b).a, sel.b))

    return self._check_sel('preceding_text_b', callback, *args)

class PrecedingTextBegin(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(view.line(sel.b).a, sel.begin()))

    return self._check_sel('preceding_text_begin', callback, *args)

class PrecedingTextEnd(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(view.line(sel.b).a, sel.end()))

    return self._check_sel('preceding_text_end', callback, *args)

class Preceding128CharsBegin(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(max(0, sel.begin() - 128), sel.begin()))

    return self._check_sel('preceding_128_chars_begin', callback, *args)

class Preceding512CharsBegin(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(max(0, sel.begin() - 512), sel.begin()))

    return self._check_sel('preceding_512_chars_begin', callback, *args)

class Following128CharsEnd(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(sel.begin(), min(view.size(), sel.end() + 128)))

    return self._check_sel('following_128_chars_end', callback, *args)

class Following512CharsEnd(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: \
      view.substr(sublime.Region(sel.begin(), min(view.size(), sel.end() + 512)))

    return self._check_sel('following_512_chars_end', callback, *args)

# unused; probably will be handy in future;


# class Preceding128CharsA(Base):
#   def on_query_context(self, *args):
#     callback = lambda view, sel: \
#       view.substr(sublime.Region(max(0, sel.a - 128), sel.a))

#     return self._check_sel('preceding_128_chars_a', callback, *args)

# class Preceding128CharsB(Base):
#   def on_query_context(self, *args):
#     callback = lambda view, sel: \
#       view.substr(sublime.Region(max(0, sel.b - 128), sel.b))

#     return self._check_sel('preceding_128_chars_b', callback, *args)
#