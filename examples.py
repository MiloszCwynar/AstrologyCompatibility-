#!/usr/bin/env python3
"""
Example usage of the Astrology Compatibility Calculator
"""

from datetime import datetime
from astrology_compatibility import Person, CompatibilityCalculator


def example_usage():
    """Demonstrate various ways to use the compatibility calculator."""
    
    print("=" * 70)
    print("EXAMPLE 1: Basic Compatibility Check")
    print("=" * 70)
    
    # Create two people
    alice = Person("Alice", datetime(1990, 5, 15))
    bob = Person("Bob", datetime(1992, 8, 22))
    
    # Calculate compatibility
    score, interpretation = CompatibilityCalculator.calculate_compatibility(
        alice, bob
    )
    
    print(f"\n{alice} and {bob}")
    print(f"Compatibility Score: {score}%")
    print(f"\n{interpretation}")
    
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Detailed Analysis")
    print("=" * 70)
    
    # Get detailed analysis
    analysis = CompatibilityCalculator.get_detailed_analysis(alice, bob)
    print(analysis)
    
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Multiple Comparisons")
    print("=" * 70)
    
    # Create multiple people
    people = [
        Person("Charlie", datetime(1988, 1, 10)),
        Person("Diana", datetime(1991, 6, 20)),
        Person("Eve", datetime(1993, 11, 5)),
    ]
    
    print(f"\nComparing {alice.name} with others:\n")
    
    for person in people:
        score, _ = CompatibilityCalculator.calculate_compatibility(alice, person)
        print(f"  {alice.name} & {person.name}: {score}% compatible")
    
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Same Birthday (High Compatibility)")
    print("=" * 70)
    
    # Same birthday test
    person1 = Person("Twin 1", datetime(1995, 7, 4))
    person2 = Person("Twin 2", datetime(1995, 7, 4))
    
    score, interpretation = CompatibilityCalculator.calculate_compatibility(
        person1, person2
    )
    
    print(f"\n{person1} and {person2}")
    print(f"Compatibility Score: {score}%")
    print(f"\n{interpretation}")
    
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Magnetic Signatures")
    print("=" * 70)
    
    print(f"\nMagnetic Signatures:")
    for person in [alice, bob, person1]:
        print(f"  {person.name}: {person.magnetic_signature:.1f}°")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    example_usage()
