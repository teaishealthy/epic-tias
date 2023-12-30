import importlib.util
import sys


def load_module(file_path: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, file_path)

    assert spec, f"Failed to load module {module_name} from {file_path}"
    assert spec.loader, f"Failed to load module {module_name} from {file_path}"

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module


file1 = load_module("file1.py", "file1")
file1.show_sys()

old_sys = sys.modules["sys"]

try:
    print("Loading other_sys.py")
    other_sys = load_module("other_sys.py", "other_sys")
    old_sys.modules["sys"] = other_sys

    file2 = load_module("file2.py", "file2")
    file1.show_sys()
    file2.show_sys()
finally:
    print("Restoring sys module")
    old_sys.modules["sys"] = old_sys

file1.show_sys()
file2.show_sys()
