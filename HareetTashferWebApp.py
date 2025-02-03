from flask import Flask, request, jsonify, render_template
from predefined_codes import (
    NUMBERING_CODE, OPPOSITE_NUMBERING_CODE, JESUS_CODE, ARABIC_MORSE_CODE,
    XBOX_CODE, SEMAPHORE_SQUARES_CODE, SEMAPHORE_POWER_CODE, BRAILE_CODE,
    ARABIC_CHAR_CODE, NUMBER_ADDITION_CODE, CLOCK_CODE, ARABIC_ENGLISH_CODE,
    COORDINATE_CODE, BINARY_MORSE_CODE
)
import json

app = Flask(__name__)

# Mapping of Arabic characters to their respective keys
MAPPING_FIELDS = {
    'ا': 'T_1', 'آ': 'T_1', 'أ': 'T_1', 'إ': 'T_1',
    'ب': 'T_2', 'ت': 'T_3', 'ث': 'T_4', 'ج': 'T_5',
    'ح': 'T_6', 'خ': 'T_7', 'د': 'T_8', 'ذ': 'T_9',
    'ر': 'T_10', 'ز': 'T_11', 'س': 'T_12', 'ش': 'T_13',
    'ص': 'T_14', 'ض': 'T_15', 'ط': 'T_16', 'ظ': 'T_17',
    'ع': 'T_18', 'غ': 'T_19', 'ف': 'T_20', 'ق': 'T_21',
    'ك': 'T_22', 'ل': 'T_23', 'م': 'T_24', 'ن': 'T_25',
    'ه': 'T_26', 'و': 'T_27', 'ي': 'T_28', 'ى': 'T_28',
    ' ': 'T_33', 'ؤ': 'T_34', 'ء': 'T_31', 'ئ': 'T_0',
    'ة': 'T_32'
}

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

    return jsonify({
        'result': converted_code,
        'non_convertible': list(set(non_convertible_found))
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
        # Convert the code dictionary to the format expected by the frontend
        converted_code = {MAPPING_FIELDS[k]: v for k, v in codes[code_name].items() if k in MAPPING_FIELDS}
        return jsonify(converted_code)
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