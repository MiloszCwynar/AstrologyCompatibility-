#!/usr/bin/env python3
"""
Astrology Compatibility Calculator

Based on the theory that the pineal gland is magnetic and becomes "set" 
on the day of birth when light first enters the eyes. This application 
calculates compatibility between people based on their birth dates.
"""

from datetime import datetime
from typing import Tuple
import math


# Constants for magnetic signature calculations
LUNAR_CYCLE_DAYS = 29.53  # Average lunar cycle length in days
SOLAR_YEAR_DAYS = 365.25  # Average solar year length in days
SOLAR_WEIGHT = 0.6  # Weight of solar influence in magnetic signature
LUNAR_WEIGHT = 0.4  # Weight of lunar influence in magnetic signature

# Constants for compatibility calculations
MAX_YEAR_DIFF_FOR_RESONANCE = 10  # Maximum year difference to consider for resonance
RESONANCE_BOOST_FACTOR = 100  # Divisor for resonance factor calculation


class Person:
    """Represents a person with their birth date information."""
    
    def __init__(self, name: str, birth_date: datetime):
        """
        Initialize a Person with name and birth date.
        
        Args:
            name: The person's name
            birth_date: The person's birth date as a datetime object
        """
        self.name = name
        self.birth_date = birth_date
        self.magnetic_signature = self._calculate_magnetic_signature()
    
    def _calculate_magnetic_signature(self) -> float:
        """
        Calculate the magnetic signature based on the birth date.
        
        The theory states that the pineal gland becomes "set" on the day of birth
        when light first enters the eyes. This method calculates a unique magnetic
        signature based on the birth date's position in various cycles.
        
        Returns:
            A float representing the person's magnetic signature (0-360 degrees)
        """
        # Day of year (1-366)
        day_of_year = self.birth_date.timetuple().tm_yday
        
        # Lunar position based on cycle
        lunar_position = (day_of_year % LUNAR_CYCLE_DAYS) / LUNAR_CYCLE_DAYS * 360
        
        # Solar position in year
        solar_position = (day_of_year / SOLAR_YEAR_DAYS) * 360
        
        # Combine influences - weighted average
        # The pineal gland's magnetic particles align based on these cosmic influences
        magnetic_signature = (solar_position * SOLAR_WEIGHT + lunar_position * LUNAR_WEIGHT) % 360
        
        return magnetic_signature
    
    def __str__(self) -> str:
        return f"{self.name} (born {self.birth_date.strftime('%Y-%m-%d')})"


class CompatibilityCalculator:
    """Calculates astrological compatibility between two people."""
    
    @staticmethod
    def calculate_compatibility(person1: Person, person2: Person) -> Tuple[float, str]:
        """
        Calculate compatibility between two people based on their magnetic signatures.
        
        The theory suggests that the pineal gland's magnetic particles create a
        unique signature at birth. Compatibility is determined by the alignment
        of these magnetic signatures.
        
        Args:
            person1: First person
            person2: Second person
            
        Returns:
            A tuple of (compatibility_score, interpretation)
            - compatibility_score: A percentage from 0-100
            - interpretation: A text description of the compatibility
        """
        # Get magnetic signatures
        sig1 = person1.magnetic_signature
        sig2 = person2.magnetic_signature
        
        # Calculate angular difference (0-180 degrees)
        angular_diff = abs(sig1 - sig2)
        if angular_diff > 180:
            angular_diff = 360 - angular_diff
        
        # Convert to compatibility percentage
        # Maximum compatibility when signatures are aligned (0 or 180 degrees apart)
        # Minimum compatibility at 90 degrees (perpendicular magnetic fields)
        if angular_diff <= 90:
            # Compatibility decreases from 100% at 0° to minimum at 90°
            base_compatibility = 100 - (angular_diff / 90 * 50)
        else:
            # Compatibility increases from minimum at 90° to high at 180°
            base_compatibility = 50 + ((angular_diff - 90) / 90 * 45)
        
        # Apply resonance factor based on birth year proximity
        year_diff = abs(person1.birth_date.year - person2.birth_date.year)
        resonance_factor = 1.0 + (min(year_diff, MAX_YEAR_DIFF_FOR_RESONANCE) / RESONANCE_BOOST_FACTOR)  # Small boost for similar ages
        
        compatibility_score = min(100, base_compatibility * resonance_factor)
        
        # Generate interpretation
        interpretation = CompatibilityCalculator._get_interpretation(
            compatibility_score, angular_diff
        )
        
        return round(compatibility_score, 1), interpretation
    
    @staticmethod
    def _get_interpretation(score: float, angular_diff: float) -> str:
        """
        Generate a text interpretation of the compatibility score.
        
        Args:
            score: The compatibility score (0-100)
            angular_diff: The angular difference in magnetic signatures
            
        Returns:
            A descriptive interpretation string
        """
        if score >= 90:
            return (
                "Exceptional Harmony - Your magnetic signatures are in near-perfect "
                "alignment. The pineal glands resonate strongly, suggesting natural "
                "understanding and deep connection."
            )
        elif score >= 75:
            return (
                "Strong Compatibility - Your magnetic fields complement each other well. "
                "The pineal gland resonance indicates good mutual understanding and "
                "harmonious energy exchange."
            )
        elif score >= 60:
            return (
                "Moderate Compatibility - Your magnetic signatures show reasonable "
                "alignment. Some effort may be needed to synchronize your energies, "
                "but the foundation is positive."
            )
        elif score >= 40:
            return (
                "Challenging Compatibility - Your magnetic fields show significant "
                "differences. The pineal glands operate at different frequencies, "
                "which may require conscious effort to bridge."
            )
        else:
            return (
                "Low Compatibility - Your magnetic signatures are quite misaligned. "
                "The pineal gland frequencies differ substantially, suggesting "
                "fundamentally different energy patterns."
            )
    
    @staticmethod
    def get_detailed_analysis(person1: Person, person2: Person) -> str:
        """
        Generate a detailed compatibility analysis.
        
        Args:
            person1: First person
            person2: Second person
            
        Returns:
            A detailed analysis string
        """
        score, interpretation = CompatibilityCalculator.calculate_compatibility(
            person1, person2
        )
        
        angular_diff = abs(person1.magnetic_signature - person2.magnetic_signature)
        if angular_diff > 180:
            angular_diff = 360 - angular_diff
        
        analysis = f"""
╔══════════════════════════════════════════════════════════════════════╗
║           ASTROLOGICAL COMPATIBILITY ANALYSIS                        ║
╚══════════════════════════════════════════════════════════════════════╝

Person 1: {person1}
  Magnetic Signature: {person1.magnetic_signature:.1f}°

Person 2: {person2}
  Magnetic Signature: {person2.magnetic_signature:.1f}°

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPATIBILITY SCORE: {score}%

Magnetic Field Alignment: {angular_diff:.1f}° separation

{interpretation}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THEORY BASIS:
The pineal gland contains magnetic particles that become functionally
"set" at birth when light first enters the eyes. This creates a unique
magnetic signature influenced by cosmic positions. Compatibility is
determined by how well these magnetic signatures align and resonate.
"""
        return analysis


def parse_date(date_string: str) -> datetime:
    """
    Parse a date string in YYYY-MM-DD format.
    
    Args:
        date_string: Date in YYYY-MM-DD format
        
    Returns:
        A datetime object
        
    Raises:
        ValueError: If date format is invalid
    """
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError(
            f"Invalid date format: {date_string}. Please use YYYY-MM-DD format."
        )


def main():
    """Main function to run the compatibility calculator."""
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║        ASTROLOGY COMPATIBILITY CALCULATOR                            ║")
    print("║        Based on Pineal Gland Magnetic Theory                         ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print()
    
    try:
        # Get first person's information
        print("Enter details for Person 1:")
        name1 = input("  Name: ").strip()
        birth_date1_str = input("  Birth Date (YYYY-MM-DD): ").strip()
        birth_date1 = parse_date(birth_date1_str)
        person1 = Person(name1, birth_date1)
        
        print()
        
        # Get second person's information
        print("Enter details for Person 2:")
        name2 = input("  Name: ").strip()
        birth_date2_str = input("  Birth Date (YYYY-MM-DD): ").strip()
        birth_date2 = parse_date(birth_date2_str)
        person2 = Person(name2, birth_date2)
        
        print()
        
        # Calculate and display compatibility
        analysis = CompatibilityCalculator.get_detailed_analysis(person1, person2)
        print(analysis)
        
    except ValueError as e:
        print(f"\nError: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n\nCalculation cancelled.")
        return 0
    
    return 0


if __name__ == "__main__":
    exit(main())
