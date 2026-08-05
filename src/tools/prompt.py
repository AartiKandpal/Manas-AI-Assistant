def generate_tool_prompt():

    return """
open_notepad()
open_calculator()
open_chrome()

google_search(query)
youtube_search(query)
search_maps(location)

current_time()
current_date()

remember(key, value)
recall(key)

create_folder(path)
create_file(path)

write_file(path, content)
append_file(path, content)
read_file(path)

delete_file(path)
delete_folder(path)

list_directory(path)
"""