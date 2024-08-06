init python:
    
    import json
    import os

    souls_per_page = 10
    selected_soul = None

    def load_json_souls(file_path):
        #   Load and parse the JSON file
        full_path = os.path.join(renpy.config.basedir, file_path)
        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)["souls"]

    def load_souls():
        global souls_en
        souls_en = load_json_souls("game\data\en\souls.json")
        renpy.show_screen("souls_list")

    def get_total_pages_souls():
        return (len(souls_en) / souls_per_page)

    def get_current_page_souls():
        start_index = (current_page - 1) * souls_per_page
        end_index = start_index + souls_per_page
        return souls_en[start_index:end_index]

    def load_souls_details(soul):
        global selected_soul, description_pages, description_page_index
        selected_soul = soul
        description_pages = split_description(soul['description'])
        description_page_index = 0