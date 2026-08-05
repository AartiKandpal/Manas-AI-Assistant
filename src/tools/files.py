from pathlib import Path
import shutil


class FileTools:

    # -------------------------------------------------
    # CREATE FOLDER
    # -------------------------------------------------

    @staticmethod
    def create_folder(
        path: str = None,
        folder_name: str = None,
        name: str = None
    ):
        path = path or folder_name or name

        if not path:
            return "❌ No folder name provided."

        Path(path).mkdir(parents=True, exist_ok=True)

        return f"📁 Folder created: {path}"

    # -------------------------------------------------
    # CREATE FILE
    # -------------------------------------------------

    @staticmethod
    def create_file(
        path: str = None,
        file_name: str = None,
        file_path: str = None,
        name: str = None
    ):
        path = path or file_name or file_path or name

        if not path:
            return "❌ No file name provided."

        Path(path).touch(exist_ok=True)

        return f"📄 File created: {path}"

    # -------------------------------------------------
    # WRITE FILE
    # -------------------------------------------------

    @staticmethod
    def write_file(
        path: str = None,
        file_path: str = None,
        content: str = ""
    ):
        path = path or file_path

        if not path:
            return "❌ No file path provided."

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"✍️ Written to {path}"

    # -------------------------------------------------
    # APPEND FILE
    # -------------------------------------------------

    @staticmethod
    def append_file(
        path: str = None,
        file_path: str = None,
        content: str = ""
    ):
        path = path or file_path

        if not path:
            return "❌ No file path provided."

        with open(path, "a", encoding="utf-8") as f:
            f.write(content)

        return f"➕ Appended to {path}"

    # -------------------------------------------------
    # READ FILE
    # -------------------------------------------------

    @staticmethod
    def read_file(
        path: str = None,
        file_path: str = None
    ):
        path = path or file_path

        if not path:
            return "❌ No file path provided."

        if not Path(path).exists():
            return f"❌ File '{path}' not found."

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    # -------------------------------------------------
    # DELETE FILE
    # -------------------------------------------------

    @staticmethod
    def delete_file(
        path: str = None,
        file_path: str = None
    ):
        path = path or file_path

        if not path:
            return "❌ No file path provided."

        p = Path(path)

        if not p.exists():
            return f"❌ File '{path}' not found."

        p.unlink()

        return f"🗑️ Deleted file: {path}"

    # -------------------------------------------------
    # DELETE FOLDER
    # -------------------------------------------------

    @staticmethod
    def delete_folder(
        path: str = None,
        folder_name: str = None
    ):
        path = path or folder_name

        if not path:
            return "❌ No folder name provided."

        p = Path(path)

        if not p.exists():
            return f"❌ Folder '{path}' not found."

        shutil.rmtree(path)

        return f"🗑️ Deleted folder: {path}"

    # -------------------------------------------------
    # LIST DIRECTORY
    # -------------------------------------------------

    @staticmethod
    def list_directory(path: str = "."):

        p = Path(path)

        if not p.exists():
            return f"❌ Directory '{path}' not found."

        files = list(p.iterdir())

        if not files:
            return "📂 Directory is empty."

        return "\n".join(f.name for f in files)