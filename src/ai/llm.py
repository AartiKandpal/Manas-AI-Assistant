from ollama import Client

from core.logger import logger
from tools.manager import ToolManager
from utils.parser import parse_json


class LocalLLM:

    def __init__(
        self,
        model: str = "qwen2.5:7b",      # Change to qwen2.5:7b later if you download it
        host: str = "http://127.0.0.1:11434",
    ):

        self.client = Client(host=host)
        self.model = model
        self.tool_manager = ToolManager()

    def _system_prompt(self):

        tools = "\n".join(
            f"- {tool}"
            for tool in self.tool_manager.get_tool_names()
        )

        return f"""
You are Manas.

You are a LOCAL desktop AI assistant.

You MUST ALWAYS return ONLY valid JSON.

Never return markdown.

Never explain your reasoning.

Never write text outside JSON.

Available tools:

{tools}
IMPORTANT

Use a tool ONLY when the user's request explicitly asks to perform an action.

If the user is asking a question,
explaining something,
asking a definition,
asking for information,
or chatting,

NEVER call a tool.

Return

{{
  "tools": [],
  "response":"..."
}}

Examples

"What is Python?"
→ No tool

"Define iterative"
→ No tool

"Explain recursion"
→ No tool

"Who is Virat Kohli?"
→ No tool

Only call tools for actions like

open
create
delete
search
remember
recall
write
read
append
play
shutdown
restart
etc.

=========================
JSON FORMAT
=========================

If no tool is needed:

{{
    "tools": [],
    "response": "your answer"
}}

If a tool is needed:

{{
    "tools":[
        {{
            "tool":"tool_name",
            "arguments":{{}}
        }}
    ],
    "response":""
}}

=========================
Examples
=========================

User:
Hi

Return

{{
"tools":[],
"response":"Hello! How can I help you today?"
}}

-------------------------

User:
Open notepad

Return

{{
"tools":[
{{
"tool":"open_notepad",
"arguments":{{}}
}}
],
"response":""
}}

-------------------------

User:
Open calculator

Return

{{
"tools":[
{{
"tool":"open_calculator",
"arguments":{{}}
}}
],
"response":""
}}

-------------------------

User:
Search python

Return

{{
"tools":[
{{
"tool":"google_search",
"arguments":{{"query":"python"}}
}}
],
"response":""
}}

-------------------------

User:
Create folder Test

Return

{{
"tools":[
{{
"tool":"create_folder",
"arguments":{{"path":"Test"}}
}}
],
"response":""
}}

-------------------------

User:
Create file hello.txt

Return

{{
"tools":[
{{
"tool":"create_file",
"arguments":{{"path":"hello.txt"}}
}}
],
"response":""
}}

-------------------------

User:
Show files

Return

{{
"tools":[
{{
"tool":"list_directory",
"arguments":{{}}
}}
],
"response":""
}}

-------------------------

User:
What time is it?

Return

{{
"tools":[
{{
"tool":"current_time",
"arguments":{{}}
}}
],
"response":""
}}

-------------------------

User:
Remember my name is Aarti

Return

{{
"tools":[
{{
"tool":"remember",
"arguments":
{{
"key":"name",
"value":"Aarti"
}}
}}
],
"response":""
}}

-------------------------

User:
What is my name?

Return

{{
"tools":[
{{
"tool":"recall",
"arguments":
{{
"key":"name"
}}
}}
],
"response":""
}}

Always use the tools when they exist.

Never invent tool names.

Never invent argument names.

Return ONLY JSON.
"""

    def chat(self, messages):

        # Build conversation
        chat_messages = [
            {
                "role": "system",
                "content": self._system_prompt(),
            }
        ]

        # Skip previous system prompts from memory
        for msg in messages:
            if msg.get("role") == "system":
                continue

            chat_messages.append(
                {
                    "role": msg["role"],
                    "content": msg["content"],
                }
            )

        logger.info("Sending request to Ollama...")

        print("\n======================")
        print("MODEL:", self.model)
        print("======================")

        try:

            response = self.client.chat(
                model=self.model,
                messages=chat_messages,
                options={
                    "temperature": 0,
                    "top_p": 0.9,
                    "num_predict": 1024,
                    "repeat_penalty": 1.05,
                },
            )

        except Exception:
            import traceback
            traceback.print_exc()
            raise

        text = response["message"]["content"]
        print("RAW repr:")
        print(repr(text))

        print("\n========== RAW RESPONSE ==========")
        print(text)
        print("==================================")

        logger.info(
            "Raw model response:\n%s",
            text,
        )

        # Parse JSON
        parsed = parse_json(text)
        print("=" * 60)
        print(type(parsed))
        print(parsed)
        print("=" * 60)
        print("\n========== PARSED ==========")
        print(parsed)
        print("============================\n")

        if not isinstance(parsed, dict):
            return {
                "tools": [],
                "response": "Sorry, I couldn't understand the response."
            }

        # Ensure keys exist
        parsed.setdefault("tools", [])
        parsed.setdefault("response", "")

        # Normalize tool calls
        normalized_tools = []

        for tool in parsed["tools"]:

            if not isinstance(tool, dict):
                continue

            tool.setdefault("arguments", {})

            args = tool["arguments"]

            # ---------- create_file ----------
            if tool["tool"] == "create_file":

                if "filename" in args:
                    args["path"] = args.pop("filename")

                if "file_name" in args:
                    args["path"] = args.pop("file_name")

                if "filePath" in args:
                    args["path"] = args.pop("filePath")

            # ---------- create_folder ----------
            elif tool["tool"] == "create_folder":

                if "folder" in args:
                    args["path"] = args.pop("folder")

                if "folder_name" in args:
                    args["path"] = args.pop("folder_name")

                if "name" in args:
                    args["path"] = args.pop("name")

            # ---------- write_file ----------
            elif tool["tool"] == "write_file":

                if "file_path" in args:
                    args["path"] = args.pop("file_path")

            # ---------- append_file ----------
            elif tool["tool"] == "append_file":

                if "file_path" in args:
                    args["path"] = args.pop("file_path")

            normalized_tools.append(tool)

        parsed["tools"] = normalized_tools

        return parsed