#!/usr/bin/env python3
"""
Tests for the Astrology Compatibility Calculator
"""

import unittest
from datetime import datetime
from astrology_compatibility import Person, CompatibilityCalculator, parse_date


class TestPerson(unittest.TestCase):
    """Test cases for the Person class."""
    
    def test_person_creation(self):
        """Test that a Person can be created with valid data."""
        birth_date = datetime(1990, 5, 15)
        person = Person("John Doe", birth_date)
        
        self.assertEqual(person.name, "John Doe")
        self.assertEqual(person.birth_date, birth_date)
        self.assertIsInstance(person.magnetic_signature, float)
        self.assertGreaterEqual(person.magnetic_signature, 0)
        self.assertLess(person.magnetic_signature, 360)
    
    def test_magnetic_signature_consistency(self):
        """Test that the same birth date always produces the same signature."""
        birth_date = datetime(1985, 12, 25)
        person1 = Person("Person 1", birth_date)
        person2 = Person("Person 2", birth_date)
        
        self.assertEqual(person1.magnetic_signature, person2.magnetic_signature)
    
    def test_magnetic_signature_different_dates(self):
        """Test that different birth dates produce different signatures."""
        person1 = Person("Person 1", datetime(1990, 1, 1))
        person2 = Person("Person 2", datetime(1990, 7, 1))
        
        self.assertNotEqual(person1.magnetic_signature, person2.magnetic_signature)
    
    def test_person_string_representation(self):
        """Test the string representation of a Person."""
        person = Person("Jane Smith", datetime(1995, 3, 20))
        self.assertIn("Jane Smith", str(person))
        self.assertIn("1995-03-20", str(person))


class TestCompatibilityCalculator(unittest.TestCase):
    """Test cases for the CompatibilityCalculator class."""
    
    def test_same_person_high_compatibility(self):
        """Test that the same birth date gives high compatibility."""
        birth_date = datetime(1990, 6, 15)
        person1 = Person("Person 1", birth_date)
        person2 = Person("Person 2", birth_date)
        
        score, interpretation = CompatibilityCalculator.calculate_compatibility(
            person1, person2
        )
        
        self.assertGreaterEqual(score, 90)
        self.assertIsInstance(interpretation, str)
        self.assertGreater(len(interpretation), 0)
    
    def test_compatibility_score_range(self):
        """Test that compatibility scores are within valid range."""
        person1 = Person("Person 1", datetime(1990, 1, 1))
        person2 = Person("Person 2", datetime(1990, 7, 1))
        
        score, _ = CompatibilityCalculator.calculate_compatibility(person1, person2)
        
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)
    
    def test_compatibility_symmetry(self):
        """Test that compatibility is symmetric (A->B == B->A)."""
        person1 = Person("Person 1", datetime(1985, 3, 15))
        person2 = Person("Person 2", datetime(1990, 9, 22))
        
        score1, _ = CompatibilityCalculator.calculate_compatibility(person1, person2)
        score2, _ = CompatibilityCalculator.calculate_compatibility(person2, person1)
        
        self.assertEqual(score1, score2)
    
    def test_detailed_analysis_format(self):
        """Test that detailed analysis is generated correctly."""
        person1 = Person("Alice", datetime(1992, 4, 10))
        person2 = Person("Bob", datetime(1993, 8, 25))
        
        analysis = CompatibilityCalculator.get_detailed_analysis(person1, person2)
        
        self.assertIsInstance(analysis, str)
        self.assertIn("Alice", analysis)
        self.assertIn("Bob", analysis)
        self.assertIn("COMPATIBILITY SCORE", analysis)
        self.assertIn("Magnetic Signature", analysis)
    
    def test_different_interpretations(self):
        """Test that different compatibility levels produce different interpretations."""
        # Create people with same birth date (high compatibility)
        person1a = Person("High1", datetime(1990, 1, 1))
        person1b = Person("High2", datetime(1990, 1, 1))
        
        # Create people with different birth dates
        person2a = Person("Diff1", datetime(1990, 1, 1))
        person2b = Person("Diff2", datetime(1990, 4, 1))
        
        score_high, interp_high = CompatibilityCalculator.calculate_compatibility(
            person1a, person1b
        )
        score_diff, interp_diff = CompatibilityCalculator.calculate_compatibility(
            person2a, person2b
        )
        
        # High compatibility should have different interpretation
        if score_high != score_diff:
            self.assertNotEqual(interp_high, interp_diff)


class TestParsers(unittest.TestCase):
    """Test cases for date parsing functions."""
    
    def test_parse_date_valid(self):
        """Test parsing of valid date strings."""
        date = parse_date("1990-05-15")
        
        self.assertEqual(date.year, 1990)
        self.assertEqual(date.month, 5)
        self.assertEqual(date.day, 15)
    
    def test_parse_date_invalid_format(self):
        """Test that invalid date formats raise ValueError."""
        with self.assertRaises(ValueError):
            parse_date("15-05-1990")  # Wrong format
        
        with self.assertRaises(ValueError):
            parse_date("1990/05/15")  # Wrong separator
        
        with self.assertRaises(ValueError):
            parse_date("not-a-date")  # Invalid date
    
    def test_parse_date_invalid_date(self):
        """Test that invalid dates raise ValueError."""
        with self.assertRaises(ValueError):
            parse_date("1990-13-01")  # Invalid month
        
        with self.assertRaises(ValueError):
            parse_date("1990-02-30")  # Invalid day


class TestMagneticSignatureCalculation(unittest.TestCase):
    """Test cases for magnetic signature calculations."""
    
    def test_signature_range(self):
        """Test that signatures are always within 0-360 degrees."""
        test_dates = [
            datetime(1990, 1, 1),
            datetime(1990, 6, 15),
            datetime(1990, 12, 31),
            datetime(2000, 2, 29),  # Leap year
            datetime(1985, 7, 4),
        ]
        
        for birth_date in test_dates:
            person = Person("Test", birth_date)
            self.assertGreaterEqual(person.magnetic_signature, 0)
            self.assertLess(person.magnetic_signature, 360)
    
    def test_signature_deterministic(self):
        """Test that the same date always gives the same signature."""
        birth_date = datetime(1995, 8, 20)
        
        signatures = []
        for i in range(5):
            person = Person(f"Person{i}", birth_date)
            signatures.append(person.magnetic_signature)
        
        # All signatures should be identical
        self.assertEqual(len(set(signatures)), 1)


if __name__ == "__main__":
    unittest.main()
