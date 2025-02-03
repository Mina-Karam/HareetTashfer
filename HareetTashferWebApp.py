from flask import Flask, request, jsonify, render_template
from predefined_codes import *
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/convert', methods=['POST'])
def convert_arabic_to_code():
    data = request.json
    arabic_text = data.get('text', '')
    key_mapping = data.get('mappings', {})

    non_convertible_chars = '،'
    non_convertible_found = [char for char in arabic_text if char in non_convertible_chars]

    # Check for characters not in the base key mapping
    for char in arabic_text:
        if char not in MAPPING_FIELDS:
            non_convertible_found.append(char)

    # Check optional characters and add them to non_convertible_found if their mappings are empty
    optional_chars = ['ؤ', 'ء', 'ئ', 'ة']
    for char in optional_chars:
        if char in arabic_text and not key_mapping.get(MAPPING_FIELDS[char]):
            non_convertible_found.append(char)

    # Convert the Arabic text to code
    code_sequence = [f'({key_mapping.get(MAPPING_FIELDS[char], "")})' if char in MAPPING_FIELDS else ' ' for char in arabic_text]
    converted_code = ', '.join(code_sequence)

    # Ensure non_convertible_found is unique
    non_convertible_found = list(set(non_convertible_found))

    return jsonify({
        'result': converted_code,
        'non_convertible': non_convertible_found  # Return the unique non-convertible characters
    })

@app.route('/api/load_code', methods=['GET'])
def load_code():
    code_name = request.args.get('code')
    codes = {
        'numbering': NUMBERING_CODE,
        'opposite_numbering': OPPOSITE_NUMBERING_CODE,
        'jesus': JESUS_CODE,
        'arabic_morse': ARABIC_MORSE_CODE,
        'xbox': XBOX_CODE,
        'semaphore_squares': SEMAPHORE_SQUARES_CODE,
        'semaphore_power': SEMAPHORE_POWER_CODE,
        'braille': BRAILE_CODE,
        'arabic_char': ARABIC_CHAR_CODE,
        'number_addition': NUMBER_ADDITION_CODE,
        'clock': CLOCK_CODE,
        'arabic_english': ARABIC_ENGLISH_CODE,
        'coordinate': COORDINATE_CODE,
        'binary_morse': BINARY_MORSE_CODE
    }
    
    if code_name in codes:
        return jsonify(codes[code_name])
    else:
        return jsonify({'error': 'Code not found'}), 404

@app.route('/api/save_mapping', methods=['POST'])
def save_mapping():
    mapping = request.json
    # In a real application, you might want to save this to a database or file
    # For now, we'll just return it
    return jsonify(mapping)

@app.route('/api/load_mapping', methods=['GET'])
def load_mapping():
    # In a real application, you would load this from a database or file
    # For now, we'll just return a sample mapping
    sample_mapping = {
        'T_1': 'A', 'T_2': 'B', 'T_3': 'C', 'T_4': 'D',
        'T_5': 'E', 'T_6': 'F', 'T_7': 'G', 'T_8': 'H',
        'T_9': 'I', 'T_10': 'J', 'T_11': 'K', 'T_12': 'L',
        'T_13': 'M', 'T_14': 'N', 'T_15': 'O', 'T_16': 'P',
        'T_17': 'Q', 'T_18': 'R', 'T_19': 'S', 'T_20': 'T',
        'T_21': 'U', 'T_22': 'V', 'T_23': 'W', 'T_24': 'X',
        'T_25': 'Y', 'T_26': 'Z', 'T_27': '1', 'T_28': '2',
        'T_33': '3', 'T_34': '4', 'T_31': '5', 'T_0': '6',
        'T_32': '7'
    }
    return jsonify(sample_mapping)

if __name__ == '__main__':
    app.run(debug=True)