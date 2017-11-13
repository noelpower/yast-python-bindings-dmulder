#!/usr/bin/env python
# encoding: utf-8

from yast import *

class AutoShortcut2Client:
    def main(self):
      # Demo for automatically generated shortcuts.
      #
      # This is a more realistic example - it points out how the `autoShortcut
      # option is intended to be used. See 'AutoShortcut1.ycp' for a simpler example.
      #
      # There shouldn't be any complaints about shortcuts in the log file when this is started.


      sw_selections = [
        "Minimum System",
        "Minimum X11 System",
        "Gnome System",
        "Default (KDE)",
        "Office System (KDE Based)",
        "Almost Everything"
      ]

      radio_box = VBox()

      for sel in sw_selections:
          radio_box.add(Left(RadioButton(Opt("autoShortcut"), sel)))

      # TODO fix/implement logging
      #Builtins.y2milestone("radio_box: %1", @radio_box)
      print "radio_box: %s"%radio_box.toString()

      UI.OpenDialog(
        VBox(
          RadioButtonGroup(Frame("Software Selection", HVSquash(radio_box))),
          PushButton("&OK")
        )
      )

      UI.UserInput()
      UI.CloseDialog()


AutoShortcut2Client().main()