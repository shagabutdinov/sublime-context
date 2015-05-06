import sublime
import sublime_plugin

from Context.base import Base

class Selection(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.substr(sel)
    return self._check_sel('selection', callback, *args)

class LineB(Base):
  def on_query_context(self, *args):
    callback = lambda view, sel: view.substr(view.line(sel.b))
    return self._check_sel('line', callback, *args)

class FollowingTextA(Base):

  def on_query_context(self, *args):
    return self._check_sel('following_text_a', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(sel.a, view.line(sel.a).b))

class FollowingTextB(Base):

  def on_query_context(self, *args):
    return self._check_sel('following_text_b', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(sel.b, view.line(sel.b).b))

class FollowingTextBegin(Base):

  def on_query_context(self, *args):
    return self._check_sel('following_text_begin', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(sel.begin(), view.line(sel.begin()).b))

class FollowingTextEnd(Base):

  def on_query_context(self, *args):
    return self._check_sel('following_text_end', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(sel.end(), view.line(sel.end()).b))

class PrecedingTextA(Base):

  def on_query_context(self, *args):
    return self._check_sel('preceding_text_a', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(view.line(sel.a).a, sel.a))

class PrecedingTextB(Base):

  def on_query_context(self, *args):
    return self._check_sel('preceding_text_b', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(view.line(sel.b).a, sel.b))

class PrecedingTextBegin(Base):

  def on_query_context(self, *args):
    return self._check_sel('preceding_text_begin', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(view.line(sel.begin()).a, sel.begin()))

class PrecedingTextEnd(Base):

  def on_query_context(self, *args):
    return self._check_sel('preceding_text_end', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(view.line(sel.end()).a, sel.end()))

class Preceding128CharsBegin(Base):

  def on_query_context(self, *args):
    return self._check_sel('preceding_128_chars_begin', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(max(0, sel.begin() - 128), sel.begin()))

class Preceding512CharsBegin(Base):

  def on_query_context(self, *args):
    return self._check_sel('preceding_512_chars_begin', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(max(0, sel.begin() - 512), sel.begin()))

class Following128CharsEnd(Base):

  def on_query_context(self, *args):
    return self._check_sel('following_128_chars_end', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(sel.begin(), min(view.size(), sel.end() + 128)))

class Following512CharsEnd(Base):

  def on_query_context(self, *args):
    return self._check_sel('following_512_chars_end', self._callback, *args)

  def _callback(self, view, sel):
    return view.substr(sublime.Region(sel.begin(), min(view.size(), sel.end() + 512)))