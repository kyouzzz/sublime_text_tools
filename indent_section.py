import sublime
import sublime_plugin
import re

class IndentSection(sublime_plugin.TextCommand):
    def run(self, edit, snap_direction=1):
        view = self.view
        
        lines = []
        for sel in view.sel():
            lines += view.lines(sel)
        lines.reverse()

        for line_region in lines:
            content = view.substr(line_region)
            indent_content = ''

            move_num = abs(snap_direction)
            append_str = ' ' * move_num
            if snap_direction > 0:
                # insert spaces
                indent_content = append_str + content
            else:
                if content.startswith(append_str):
                    # remove spaces
                    indent_content = content[move_num:]
                else:
                    indent_content = content

            replace_region = sublime.Region(line_region.a, line_region.b)
            view.replace(edit, replace_region, indent_content)