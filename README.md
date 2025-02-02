# Hadith Authentication Program

This program helps in authenticating the chain of narrators in a Hadith based on a provided Hadith text. It verifies if the narrators in the chain are reliable and checks if they meet specific criteria such as memory strength and geospatial verification.

## Features
- Load a JSON file containing data about narrators.
- Extract narrators mentioned in the Hadith text.
- Verify the authenticity of the narrators based on their reliability and memory strength.
- Validate if the Hadith is strong based on the narrators' assessments.

## Prerequisites
- Python 3.x
- JSON file containing narrators' data (e.g., `narrators.json`).

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hadith-authentication.git
   ```

2. Navigate to the project directory:

   ```bash
   cd hadith-authentication
   ```

3. Install the required Python libraries (if any):

   ```bash
   pip install -r requirements.txt
   ```

   **Note**: This program uses Python's built-in libraries (`json`, `re`), so there are no external dependencies required.

## Usage

### Loading Narrators Data

The narrators' data is loaded from a JSON file (`narrators.json`). Ensure that the file is structured as follows:

```json
{
  "narrators": [
    {
      "full_name": "Malik ibn Anas",
      "aliases": ["Abu Abdullah Malik"],
      "birth_year_AH": 93,
      "death_year_AH": 179,
      "birthplace": "Medina",
      "reliability_assessments": {
        "Al-Bukhari": "Thiqa",
        "Ibn Hajar": "Thiqa"
      },
      "memory_strength_over_time": {
        "before_150_AH": "Strong",
        "after_160_AH": "Strong"
      },
      "known_tadlis": false
    },
    ...
  ]
}
```

### Running the Program

1. Ensure the `narrators.json` file is in the same directory as the Python script.
2. Run the Python script:

   ```bash
   python authenticator.py
   ```

3. Enter the Hadith text when prompted. The program will check the narrators mentioned in the text and verify their authenticity based on the data provided in the `narrators.json` file.

   Example input:
   ```text
   Imam Malik ibn Anas reported from Abu Huraira (may Allah be pleased with him), who said:"The Messenger of Allah (ﷺ) said: 'The best of your deeds is prayer. Whoever is diligent in it will enter Paradise.'
   ```

   Example output:
   ```text
   Strong: All narrators are reliable.
   ```

### Stopping the Program

To exit the program, type `stop` when prompted to enter a Hadith.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues and submit pull requests to improve this program.

## Author

This program was developed by **Muhammad Shazam**.
```

### Key Sections of the README:
- **Features**: Highlights the core functionality of the program.
- **Prerequisites**: Specifies Python 3.x and the required JSON file for narrators.
- **Setup**: Details how to set up the project, clone the repo, and install any necessary dependencies.
- **Usage**: Explains how to use the program, including how to load narrators and validate Hadiths.
- **License and Contributing**: Mentions the project's license and invites contributions.

Feel free to update the links and any specific information based on your actual repository and project details.