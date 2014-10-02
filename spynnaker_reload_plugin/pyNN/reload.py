
class Reload(object):

    def __init__(self, file_path_to_reload_script):
        self._path_to_reload_script = file_path_to_reload_script

    def run_reload_script(self):
        execfile(self._path_to_reload_script)