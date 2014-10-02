from spynnaker_reload_plugin.pyNN.reload import Reload
from spynnaker_reload_plugin.pyNN import exceptions

_reload = None

def load_from(file_path_to_reload_file):
    global _reload
    _reload = Reload(file_path_to_reload_file)


def change_runtime_param(new_value):
    raise exceptions.SpynnakerReloadPluginNotImplimentedException(
        "this functionality has not yet been implimented")


def change_neural_param(new_value):
    raise exceptions.SpynnakerReloadPluginNotImplimentedException(
        "this functionality has not yet been implimented")


def change_edge_param(new_value):
    raise exceptions.SpynnakerReloadPluginNotImplimentedException(
        "this functionality has not yet been implimented")


def change_recording_scope(new_scope):
    raise exceptions.SpynnakerReloadPluginNotImplimentedException(
        "this functionality has not yet been implimented")


def change_architecture(definition):
    raise exceptions.SpynnakerReloadPluginNotImplimentedException(
        "this functionality has not yet been implimented")


def reload_script():
    global _reload
    _reload.run_reload_script()