import sublime, sublime_plugin
import cson, json

def loadConfig():
    return sublime.load_settings('CSON Converter.sublime-settings');

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
            sublime.error_message("CSON Converter\n\nUnsupported scope, can't toggle object notation automatically")

# Convert CSON to JSON
class CsonToJsonCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # read data from view
        selection = self.view.substr(sublime.Region(0, self.view.size()))

        # interprete and validate data
        try:
            data = cson.loads(selection)
        except:
            sublime.error_message("CSON Converter\n\nInvalid CSON, aborting conversion")
            return

        sort_keys = loadConfig().get("jsonSortKeys") or False
        indent = loadConfig().get("jsonIndent") or 2

        # write converted data to view
        selection = sublime.Region(0, self.view.size())
        self.view.replace(edit, selection, json.dumps(data, sort_keys=sort_keys, indent=indent, separators=(',', ': ')))

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
            sublime.error_message("CSON Converter\n\nInvalid JSON, aborting conversion")
            return

        sort_keys = loadConfig().get("jsonSortKeys") or True
        indent = loadConfig().get("jsonIndent") or 2

        # write converted data to view
        selection = sublime.Region(0, self.view.size())
        self.view.replace(edit, selection, cson.dumps(data, sort_keys=sort_keys, indent=indent))

        # set syntax to CSON, requires supported CoffeeScript package
        package = self.get_package()
        if package is not False:
            self.view.set_syntax_file(package)

    def get_package(self):
        import os

        # package locations
        locations = [sublime.installed_packages_path(), sublime.packages_path()]

        # supported packages
        packages = ["Better CoffeeScript", "CoffeeScript", "IcedCoffeeScript"]

        # iterate over packages locations
        for location in locations:
            # iterate over packages installed with Package Control
            for package in packages:
                if os.path.isfile(location + "/" + package + ".sublime-package") is True:
                    if package is "IcedCoffeeScript":
                        return "Packages/IcedCoffeeScript/Syntaxes/IcedCoffeeScript.tmLanguage"
                    else:
                        return "Packages/" + package + "/CoffeeScript.tmLanguage"

        sublime.error_message("CSON Converter\n\nAutomatic conversion requires a supported CoffeeScript package to be installed. See README.md for details!")
        return False
