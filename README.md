# Astrology Compatibility Calculator

An application to check astrological compatibility between people based on the magnetic pineal gland theory.

## Theory Background

This application is based on the astrological compatibility theories of an astrology researcher/author, which proposes:

1. **Magnetic Pineal Gland**: The pineal gland of humans contains magnetic particles
2. **Blood Re-magnetization**: Human lifeblood is re-magnetized every time it passes through the pineal gland
3. **Birth Imprinting**: The pineal gland only becomes functional and "set" on the day of birth when light first enters the eyes

The application calculates compatibility by determining the magnetic signatures of individuals based on their birth dates and analyzing how well these signatures align.

## Features

- Calculate compatibility between two people based on their birth dates
- Generate detailed compatibility reports with interpretations
- Displays magnetic signature alignment and compatibility percentage
- Beautiful command-line interface with formatted output

## Requirements

- Python 3.6 or higher (uses type hints and f-strings)

## Installation

No installation required! Just clone the repository:

```bash
git clone https://github.com/MiloszCwynar/AstrologyCompatibility-.git
cd AstrologyCompatibility-
```

## Usage

### Interactive Mode

Run the application in interactive mode to calculate compatibility:

```bash
python3 astrology_compatibility.py
```

You will be prompted to enter:
1. Name and birth date for Person 1
2. Name and birth date for Person 2

The application will then display a detailed compatibility analysis.

### Example Session

```
╔══════════════════════════════════════════════════════════════════════╗
║        ASTROLOGY COMPATIBILITY CALCULATOR                            ║
║        Based on Pineal Gland Magnetic Theory                         ║
╚══════════════════════════════════════════════════════════════════════╝

Enter details for Person 1:
  Name: Alice
  Birth Date (YYYY-MM-DD): 1990-05-15

Enter details for Person 2:
  Name: Bob
  Birth Date (YYYY-MM-DD): 1992-08-22

╔══════════════════════════════════════════════════════════════════════╗
║           ASTROLOGICAL COMPATIBILITY ANALYSIS                        ║
╚══════════════════════════════════════════════════════════════════════╝

Person 1: Alice (born 1990-05-15)
  Magnetic Signature: 123.4°

Person 2: Bob (born 1992-08-22)
  Magnetic Signature: 234.5°

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPATIBILITY SCORE: 75.2%

Magnetic Field Alignment: 111.1° separation

Strong Compatibility - Your magnetic fields complement each other well.
The pineal gland resonance indicates good mutual understanding and
harmonious energy exchange.
```

### Programmatic Usage

You can also use the module in your own Python code:

```python
from datetime import datetime
from astrology_compatibility import Person, CompatibilityCalculator

# Create two people
person1 = Person("Alice", datetime(1990, 5, 15))
person2 = Person("Bob", datetime(1992, 8, 22))

# Calculate compatibility
score, interpretation = CompatibilityCalculator.calculate_compatibility(
    person1, person2
)

print(f"Compatibility: {score}%")
print(interpretation)

# Get detailed analysis
analysis = CompatibilityCalculator.get_detailed_analysis(person1, person2)
print(analysis)
```

## Testing

Run the test suite to verify the application:

```bash
python3 -m unittest test_astrology_compatibility.py
```

Or run with verbose output:

```bash
python3 -m unittest test_astrology_compatibility.py -v
```

## How It Works

### Magnetic Signature Calculation

Each person's magnetic signature is calculated based on their birth date:

1. **Day of Year**: The position in the annual cycle (1-366)
2. **Lunar Influence**: Position within the ~29.53 day lunar cycle
3. **Solar Position**: Position within the 365.25 day solar year

These cosmic influences are combined to create a unique magnetic signature (0-360 degrees) representing the state of the pineal gland at birth.

### Compatibility Calculation

Compatibility is determined by:

1. **Angular Alignment**: The difference between two magnetic signatures
   - Maximum compatibility: Signatures aligned (0°) or opposite (180°)
   - Minimum compatibility: Perpendicular signatures (90°)

2. **Resonance Factor**: A small adjustment based on birth year proximity

3. **Interpretation**: Text descriptions ranging from "Exceptional Harmony" to "Low Compatibility"

## Date Format

All dates must be entered in **YYYY-MM-DD** format:
- ✅ Valid: `1990-05-15`, `2000-12-31`, `1985-01-01`
- ❌ Invalid: `15-05-1990`, `05/15/1990`, `15.05.1990`

## License

This project is provided as-is for educational and entertainment purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This application is based on astrological theories and is intended for entertainment purposes. The magnetic pineal gland theory is not scientifically validated.