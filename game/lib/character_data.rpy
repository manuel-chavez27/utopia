init python:


    import json
    import os
    

    def load_json(file_path):
        #   Load and parse the JSON file
        full_path = os.path.join(renpy.config.basedir, file_path)
        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)["characters"]

    
    selected_encyclopedia_list = None
    current_page = 1
    characters_per_page = 10

    characters_en = load_json("game\data\en\characters.json")


    def load_characters():
        global characters_en
        characters_en = load_json("game\data\en\characters.json")
        renpy.show_screen("characters_list")

    def get_total_pages():
        return (len(characters_en) / characters_per_page)

    def get_current_page_characters():
        start_index = (current_page - 1) * characters_per_page
        end_index = start_index + characters_per_page
        return characters_en[start_index:end_index]

    selected_character = None

    def format_character_details(character):
        details = (
            f"Name: {character['name']}[br]"
            f"Age: {character['age']}[br]"
            f"Height: {character['height_m']} meters[br]"
            f"Weight: {character['weight_kg']} kg[br]"
            f"Favorite Food: {character['favorite_food']}[br][br]"
            f"{character.get('description', 'No description available.')}"
        )
        return details

    def split_description(text, max_length=500):
        words = text.split()
        pages = []
        page = ""
        for word in words:
            if len(page) + len(word) + 1 > max_length:
                pages.append(page)
                page = word
            else:
                if page:
                    page += " "
                page += word
        if page:
            pages.append(page)
        return pages



    def load_character_details(character):
        global selected_character, description_pages, description_page_index
        selected_character = character
        combined_text = format_character_details(character)
        description_pages = split_description(combined_text)
        description_page_index = 0

    if selected_character:
        description_pages = split_description(selected_character["age"], selected_character["height_m"], selected_character["weight_kg"], selected_character["favorite_food"], selected_character["description"])
    else:
        description_pages = []
    description_page_index = 0