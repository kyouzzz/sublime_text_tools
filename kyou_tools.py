#
import sublime
import sublime_plugin
import subprocess
import webbrowser
import re

# PHP手册
class openWebManualCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ### self.view.insert(edit, 0, "Hello, World!")
        selected = self.view.substr(self.view.sel()[0])
        php_url = "http://php.net/manual-lookup.php?pattern=%s&scope=quickref" % (selected)
        webbrowser.open_new_tab(php_url)

# 百度翻译
class openWebTransCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # 检查中文
        selected = self.view.substr(self.view.sel()[0])
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        has_zh = zhPattern.search(selected)
        if has_zh:
            from urllib.parse import quote
            extend = "#zh/en/" + quote(selected);
        else:
            extend = "#en/zh/" + selected;
        url = "http://fanyi.baidu.com/" + extend
        webbrowser.open_new_tab("http://fanyi.baidu.com/" + extend)
