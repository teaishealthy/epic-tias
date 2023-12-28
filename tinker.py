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
file1.show_os()

old_os = sys.modules["os"]

try:
    print("Loading other_os.py")
    other_os = load_module("other_os.py", "other_os")
    sys.modules["os"] = other_os

    file2 = load_module("file2.py", "file2")
    file1.show_os()
    file2.show_os()
finally:
    print("Restoring os module")
    sys.modules["os"] = old_os

file1.show_os()
file2.show_os()
