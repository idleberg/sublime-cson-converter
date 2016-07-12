import sublime, sublime_plugin
import cson, json

# Automatic conversion
class ToggleObjectNotationCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        scope = self.view.scope_name(self.view.sel()[0].a)

        if "source.json" in scope \
        or scope.startswith('source.sublime'):
            self.view.run_command('json_to_cson')
        elif "source.coffee" in scope:
            self.view.run_command('cson_to_json')
        else:
            sublime.error_message("CSON Converter: Unsupported scope, can't toggle object notation automatically")

# Convert CSON to JSON
class CsonToJsonCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # read data from view
        selection = self.view.substr(sublime.Region(0, self.view.size()))

        # interprete and validate data
        try:
            data = cson.loads(selection)
        except:
            sublime.error_message("CSON Converter: Invalid CSON, aborting conversion")
            return

        # write converted data to view
        selection = sublime.Region(0, self.view.size())
        self.view.replace(edit, selection, json.dumps(data, sort_keys=False, indent=2, separators=(',', ': ')))

        # set syntax to JSON
        if sublime.version() >= "3103":
            self.view.set_syntax_file('Packages/JavaScript/JSON.sublime-syntax')
        else:
            self.view.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')

# Convert JSON to CSON
class JsonToCsonCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # read data from view
        selection = self.view.substr(sublime.Region(0, self.view.size()))

        # interprete and validate data
        try:
            data = json.loads(selection)
        except:
            sublime.error_message("CSON Converter: Invalid JSON, aborting conversion")
            return

        # write converted data to view
        selection = sublime.Region(0, self.view.size())
        self.view.replace(edit, selection, cson.dumps(data, sort_keys=False, indent=2))

        # set syntax to CSON, requires supported CoffeeScript package
        package = self.get_package()
        if package is not False:
            self.view.set_syntax_file(package)

    def get_package(self):
        import os

        # supported packages
        packages = ["Better CoffeeScript", "CoffeeScript"]

        # iterate over packages installed with Package Control
        for package in packages:
            if os.path.isfile(sublime.installed_packages_path() + "/" + package + ".sublime-package") is True:
                return "Packages/" + package + "/CoffeeScript.tmLanguage"

        # still found nothing, let's iterate over manually installed packages  
        for package in packages:
            if os.path.isdir(sublime.packages_path() + "/" + package) is True:
                return "Packages/" + package + "/CoffeeScript.tmLanguage"

        sublime.error_message("CSON Converter: Automatic conversion requires a supported CoffeeScript package to be installed. See README.md for details!")
        return False
