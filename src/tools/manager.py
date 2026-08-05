from tools.system import SystemTools
from tools.browser import BrowserTools
from tools.files import FileTools
from tools.memory_tools import MemoryTools
from tools.datetime_tools import DateTimeTools


class ToolManager:

    def __init__(self):

        self.tools = {

            # =========================
            # SYSTEM
            # =========================

            "open_notepad": SystemTools.open_notepad,
            "open_calculator": SystemTools.open_calculator,
            "open_vscode": SystemTools.open_vscode,
            "open_chrome": SystemTools.open_chrome,

            # =========================
            # BROWSER
            # =========================

            "open_google": BrowserTools.open_google,
            "google_search": BrowserTools.google_search,
            "youtube_search": BrowserTools.youtube_search,
            "search_maps": BrowserTools.search_maps,

            # =========================
            # FILES
            # =========================

            "create_folder": FileTools.create_folder,
            "create_file": FileTools.create_file,
            "write_file": FileTools.write_file,
            "append_file": FileTools.append_file,
            "read_file": FileTools.read_file,
            "delete_file": FileTools.delete_file,
            "delete_folder": FileTools.delete_folder,
            "list_directory": FileTools.list_directory,

            # =========================
            # MEMORY
            # =========================

            "remember": MemoryTools.remember,
            "recall": MemoryTools.recall,
            "forget": MemoryTools.forget,
            "show_memory": MemoryTools.show_memory,

            # =========================
            # DATE & TIME
            # =========================

            "current_time": DateTimeTools.current_time,
            "current_date": DateTimeTools.current_date,
        }

    def get_tool_names(self):
        return sorted(self.tools.keys())

    def has_tool(self, name: str) -> bool:
        return name in self.tools

    def execute(self, tool_call):

        tool = self.tools.get(tool_call.tool)

        if tool is None:
            return f"❌ Unknown tool: {tool_call.tool}"

        try:

            result = tool(**tool_call.arguments)

            if result is None:
                return f"✅ {tool_call.tool} executed."

            return str(result)

        except TypeError as e:
            return f"❌ Argument Error ({tool_call.tool}): {e}"

        except Exception as e:
            return f"❌ Execution Error ({tool_call.tool}): {e}"