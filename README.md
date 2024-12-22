# Sopa de Letras Generator

This project is a simple Python-based word search (sopa de letras) generator designed to create custom word search puzzles in PDF format. It is tailored for generating 20x20 grids with randomly selected words and can produce 7 puzzles per execution.

## Features

- Generates 7 unique word search puzzles per execution.
- Each puzzle is a 20x20 grid filled with random letters and words.
- Words are between 2 to 8 characters long.
- No words contain the letter "Ñ".
- Exports the puzzles and their word lists to a well-formatted PDF.

## Prerequisites

To run this project, you need the following:
1. Python 3.x installed on your system.
2. The `fpdf` library for generating PDF files.

## Installation

1. Clone or download this repository.
2. Install the required Python library:
   ```bash
   pip install fpdf
   ```

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `sopas_de_letras.py` file.
3. Run the script:
   ```bash
   python sopas_de_letras.py
   ```
4. After execution, a file named `sopas_de_letras.pdf` will be created in the same directory.

## PDF Output

The generated PDF contains:
1. Seven 20x20 word search puzzles.
2. Each puzzle includes a grid of letters with outer borders and a word list organized in 5 rows and 4 columns.
3. The word list is centered below the grid with an additional space between the grid and the word list.
4. Words are aligned to the left within each cell of the word list for a clean look.

## Customization

You can customize the following:
- **Word Pool**: Modify the `WORDS_POOL` variable in `sopas_de_letras.py` to include more words.
- **Number of Puzzles**: Change the loop in the `main` function to generate a different number of puzzles.
- **Grid Size**: Adjust the `size` parameter in the `generate_word_search` function to create grids of different sizes.

## Example Word Pool

The default word pool includes:
- "MONTANA", "OCEANO", "VALLE", "FULGOR", "HORIZONTE"
- "MIRADOR", "AURORA", "LUZ", "ESTRELLA", "GALAXIA"
- "NEBULOSA", "ESPEJISMO", "CASCADA", "CENIZAS", "RAFAGA"
- "CRISTAL", "DIAMANTE", "ESCARCHA", "SELVATICO", "ABISMO"

Feel free to expand this list as desired.

## License

This project is free to use and modify for personal or educational purposes.