TOOL_REGISTRY = {}


def tool(
    name: str,
    description: str,
    parameters: dict | None = None,
):
    def wrapper(func):

        TOOL_REGISTRY[name] = {
            "function": func,
            "description": description,
            "parameters": parameters or {},
        }

        return func

    return wrapper