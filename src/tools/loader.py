import importlib
import pkgutil
import tools


def load_plugins():
    for _, module_name, _ in pkgutil.iter_modules(tools.__path__):

        if module_name in (
            "decorator",
            "loader",
            "manager",
            "prompt",
            "registry",
        ):
            continue

        importlib.import_module(f"tools.{module_name}")