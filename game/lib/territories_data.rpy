init python:
    
    import json
    import os

    territories_per_page = 10
    selected_territory = None

    def load_json_territories(file_path):
        #   Load and parse the JSON file
        full_path = os.path.join(renpy.config.basedir, file_path)
        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)["territories"]

    def load_territories():
        global territories_en
        territories_en = load_json_territories("game\data\en\\territories.json")
        renpy.show_screen("territories_list")

    def get_total_pages_territories():
        return (len(territories_en) / territories_per_page)

    def get_current_page_territories():
        start_index = (current_page - 1) * territories_per_page
        end_index = start_index + territories_per_page
        return territories_en[start_index:end_index]

    def load_territory_details(territory):
        global selected_territory, description_pages, description_page_index
        selected_territory = territory
        description_pages = split_description(territory['description'])
        description_page_index = 0