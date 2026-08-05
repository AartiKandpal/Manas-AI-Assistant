import re


class CommandRouter:

    def route(self, text: str):

        text = text.lower().strip()

        # -----------------------------
        # System
        # -----------------------------

        if text == "open calculator":
            return {
                "tool": "open_calculator",
                "arguments": {}
            }

        if text == "open chrome":
            return {
                "tool": "open_chrome",
                "arguments": {}
            }

        if text == "open vscode":
            return {
                "tool": "open_vscode",
                "arguments": {}
            }

        if text == "open notepad":
            return {
                "tool": "open_notepad",
                "arguments": {}
            }

        if text == "open google":
            return {
                "tool": "open_google",
                "arguments": {}
            }

        # -----------------------------
        # Google
        # -----------------------------

        m = re.match(
            r"search (.+) on google",
            text
        )

        if m:

            return {
                "tool": "google_search",
                "arguments": {
                    "query": m.group(1)
                }
            }

        # -----------------------------
        # YouTube
        # -----------------------------

        m = re.match(
            r"search (.+) on youtube",
            text
        )

        if m:

            return {
                "tool": "youtube_search",
                "arguments": {
                    "query": m.group(1)
                }
            }

        # -----------------------------
        # Maps
        # -----------------------------

        m = re.match(
            r"(find|search|open maps for) (.+)",
            text
        )

        if m:

            return {
                "tool": "search_maps",
                "arguments": {
                    "location": m.group(2)
                }
            }

        # -----------------------------
        # Folder
        # -----------------------------

        m = re.match(
            r"create folder(?: called)? (.+)",
            text
        )

        if m:

            return {
                "tool": "create_folder",
                "arguments": {
                    "path": m.group(1)
                }
            }

        # -----------------------------
        # File
        # -----------------------------

        m = re.match(
            r"create file(?: called)? (.+)",
            text
        )

        if m:

            return {
                "tool": "create_file",
                "arguments": {
                    "path": m.group(1)
                }
            }

        return None