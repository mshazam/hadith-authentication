import json
import re

def load_narrators_data(filename="narrators.json"):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

def extract_narrators(hadith_text, narrators_data):
    found_narrators = []
    for narrator in narrators_data:
        if isinstance(narrator, dict) and "full_name" in narrator:
            if narrator["full_name"] in hadith_text or any(alias in hadith_text for alias in narrator.get("aliases", [])):
                found_narrators.append(narrator["full_name"])
        else:
            print(f"Invalid narrator data: {narrator}")  # Debugging line to catch incorrect data
    return found_narrators

def is_narrator_strong(narrator_data):
    if not narrator_data:
        return False
    
    reliability = narrator_data.get("reliability_assessments", {})
    if not any(value == "Thiqa" for value in reliability.values()):
        return False
    
    memory_strength = narrator_data.get("memory_strength_over_time", {})
    if any(strength != "Strong" for strength in memory_strength.values()):
        return False
    
    if narrator_data.get("known_tadlis", False):
        return False
    
    if not narrator_data.get("geospatial_verification_of_isnad", False):
        return False
    
    return True

def validate_hadith(hadith_text, narrators_data):
    narrators = extract_narrators(hadith_text, narrators_data)
    if not narrators:
        return "Weak: No known narrators found."
    
    for narrator in narrators:
        narrator_info = next((n for n in narrators_data if n["full_name"] == narrator), None)
        if not is_narrator_strong(narrator_info):
            return f"Weak: {narrator} has weaknesses in the chain."
    
    return "Strong: All narrators are reliable."

def main():
    narrators_data = load_narrators_data()
    
    while True:
        hadith_text = input("Enter Hadith (or type 'stop' to exit): ")
        if hadith_text.lower() == "stop":
            break
        
        result = validate_hadith(hadith_text, narrators_data)
        print(result)

if __name__ == "__main__":
    main()
