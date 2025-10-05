"""
Unit tests for the SimpleCalculator class.

This module contains comprehensive yet efficient tests for all arithmetic operations
in the SimpleCalculator class, balancing coverage with maintainability.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    Test case for the SimpleCalculator class.
    
    This class contains focused test methods that cover all critical scenarios
    while maintaining clean, readable, and maintainable code.
    """
    
    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test.
        
        Ensures each test starts with a fresh calculator instance
        for complete test isolation.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the addition method with comprehensive yet efficient test cases.
        
        Covers:
        - Basic positive numbers
        - Mixed positive/negative (cancellation)
        - Both negative numbers
        - Zero identity cases
        - Decimal numbers
        """
        # Core functionality
        self.assertEqual(self.calc.add(2, 3), 5)           # Basic positive
        self.assertEqual(self.calc.add(-1, 1), 0)          # Mixed signs (cancellation)
        self.assertEqual(self.calc.add(-2, -3), -5)        # Both negative
        
        # Edge cases
        self.assertEqual(self.calc.add(0, 0), 0)           # Zero identity
        self.assertEqual(self.calc.add(5, 0), 5)           # Zero as second operand
        self.assertEqual(self.calc.add(0, 5), 5)           # Zero as first operand
        
        # Decimal numbers
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)     # Decimal addition
        self.assertEqual(self.calc.add(-1.5, 1.5), 0.0)    # Decimal cancellation

    def test_subtraction(self):
        """
        Test the subtraction method with key scenarios.
        
        Covers:
        - Basic subtraction
        - Negative results
        - Zero operations
        - Mixed signs
        - Decimal numbers
        """
        # Core functionality
        self.assertEqual(self.calc.subtract(5, 3), 2)      # Basic positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)     # Negative result
        self.assertEqual(self.calc.subtract(-1, -1), 0)    # Both negative
        
        # Edge cases
        self.assertEqual(self.calc.subtract(0, 5), -5)     # Zero as minuend
        self.assertEqual(self.calc.subtract(5, 0), 5)      # Zero as subtrahend
        self.assertEqual(self.calc.subtract(0, 0), 0)      # Both zero
        
        # Mixed signs and decimals
        self.assertEqual(self.calc.subtract(-3, 2), -5)    # Mixed signs
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0) # Decimal subtraction

    def test_multiplication(self):
        """
        Test the multiplication method with critical test cases.
        
        Covers:
        - Basic multiplication
        - Negative number rules
        - Zero property
        - Identity property
        - Decimal numbers
        """
        # Core functionality
        self.assertEqual(self.calc.multiply(2, 3), 6)      # Basic positive
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Negative × positive
        self.assertEqual(self.calc.multiply(-2, -3), 6)    # Negative × negative
        
        # Mathematical properties
        self.assertEqual(self.calc.multiply(5, 0), 0)      # Zero property
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Zero property
        self.assertEqual(self.calc.multiply(5, 1), 5)      # Identity property
        
        # Decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)  # Decimal multiplication
        self.assertEqual(self.calc.multiply(-1.5, 2), -3.0) # Negative decimal

    def test_division(self):
        """
        Test the division method with comprehensive edge case coverage.
        
        Covers:
        - Basic division
        - Negative number division
        - Decimal results
        - Zero as numerator
        - Division by zero (critical edge case)
        """
        # Normal division cases
        self.assertEqual(self.calc.divide(6, 3), 2.0)      # Basic division
        self.assertEqual(self.calc.divide(-6, 3), -2.0)    # Negative numerator
        self.assertEqual(self.calc.divide(6, -3), -2.0)    # Negative denominator
        self.assertEqual(self.calc.divide(-6, -3), 2.0)    # Both negative
        
        # Decimal and fractional results
        self.assertEqual(self.calc.divide(5, 2), 2.5)      # Decimal result
        self.assertEqual(self.calc.divide(1, 3), 1/3)      # Fraction result
        
        # Zero cases
        self.assertEqual(self.calc.divide(0, 5), 0.0)      # Zero numerator
        self.assertEqual(self.calc.divide(0, -5), -0.0)    # Zero with negative
        
        # Critical edge case - division by zero
        self.assertIsNone(self.calc.divide(5, 0))          # Division by zero
        self.assertIsNone(self.calc.divide(-5, 0))         # Negative division by zero
        self.assertIsNone(self.calc.divide(0, 0))          # Zero by zero

    def test_operations_chain(self):
        """
        Test that the calculator can handle multiple operations sequentially.
        
        Ensures the calculator instance maintains state correctly
        and operations don't interfere with each other.
        """
        # Test a sequence of different operations
        self.assertEqual(self.calc.add(2, 3), 5)           # Start with addition
        self.assertEqual(self.calc.subtract(10, 4), 6)     # Then subtraction
        self.assertEqual(self.calc.multiply(3, 4), 12)     # Then multiplication
        self.assertEqual(self.calc.divide(15, 3), 5.0)     # Then division
        self.assertIsNone(self.calc.divide(5, 0))          # Finally edge case
        
        # Verify operations didn't affect each other
        self.assertEqual(self.calc.add(1, 1), 2)           # Addition still works


if __name__ == '__main__':
    # Run the tests with verbose output
    unittest.main(verbosity=2)