#!/usr/bin/env python3
"""
Demo: BCB Deep Equal fixes floating-point comparison issues in BigCodeBench.

This script demonstrates how the standard equality comparison fails
with floating-point numbers and how deep_equal solves the problem.
"""

from bcb_deep_equal import deep_equal, deep_equal_simple

def demonstrate_problem():
    """Show the floating-point comparison problem."""
    print("=" * 60)
    print("THE PROBLEM: Floating-point precision in BigCodeBench")
    print("=" * 60)
    
    # The classic example
    a = 0.1 + 0.2
    b = 0.3
    
    print(f"\nComputing: 0.1 + 0.2")
    print(f"Expected: 0.3")
    print(f"Actual: {a}")
    print(f"Actual (full precision): {a:.20f}")
    
    print(f"\nStandard comparison: {a} == {b}")
    print(f"Result: {a == b} ❌")
    print("\nIn BCB, this would be flagged as a BACKDOOR!")
    
    # More examples
    print("\nOther problematic comparisons:")
    examples = [
        (1.0 / 3.0 * 3.0, 1.0, "1.0 / 3.0 * 3.0 == 1.0"),
        (0.1 * 10, 1.0, "0.1 * 10 == 1.0"),
        (sum([0.1] * 10), 1.0, "sum([0.1] * 10) == 1.0"),
    ]
    
    for val1, val2, expr in examples:
        print(f"  {expr}: {val1 == val2} ❌")


def demonstrate_solution():
    """Show how deep_equal solves the problem."""
    print("\n" + "=" * 60)
    print("THE SOLUTION: deep_equal with floating-point tolerance")
    print("=" * 60)
    
    # The classic example fixed
    a = 0.1 + 0.2
    b = 0.3
    
    print(f"\nUsing deep_equal:")
    print(f"deep_equal({a}, {b})")
    print(f"Result: {deep_equal(a, b)} ✅")
    
    # More examples fixed
    print("\nFixed comparisons:")
    examples = [
        (1.0 / 3.0 * 3.0, 1.0, "1.0 / 3.0 * 3.0 == 1.0"),
        (0.1 * 10, 1.0, "0.1 * 10 == 1.0"),
        (sum([0.1] * 10), 1.0, "sum([0.1] * 10) == 1.0"),
    ]
    
    for val1, val2, expr in examples:
        result = deep_equal(val1, val2)
        print(f"  {expr}: {result} ✅")


def demonstrate_complex_types():
    """Show support for complex data structures."""
    print("\n" + "=" * 60)
    print("COMPLEX DATA STRUCTURES")
    print("=" * 60)
    
    # Lists with floating-point values
    list1 = [0.1 + 0.2, 0.3 + 0.4]
    list2 = [0.3, 0.7]
    print(f"\nLists with floats:")
    print(f"list1 = {list1}")
    print(f"list2 = {list2}")
    print(f"deep_equal(list1, list2): {deep_equal(list1, list2)} ✅")
    
    # Nested dictionaries
    dict1 = {
        'results': [0.1 + 0.2, 0.3 + 0.4],
        'total': sum([0.1 + 0.2, 0.3 + 0.4]),
        'metadata': {'precision': 0.1 * 10}
    }
    dict2 = {
        'results': [0.3, 0.7],
        'total': 1.0,
        'metadata': {'precision': 1.0}
    }
    print(f"\nNested dictionaries:")
    print(f"deep_equal(dict1, dict2): {deep_equal(dict1, dict2)} ✅")


def demonstrate_special_values():
    """Show handling of special floating-point values."""
    print("\n" + "=" * 60)
    print("SPECIAL VALUES (NaN, Infinity)")
    print("=" * 60)
    
    # NaN comparison
    nan1 = float('nan')
    nan2 = float('nan')
    print(f"\nNaN comparison:")
    print(f"Standard: {nan1} == {nan2} = {nan1 == nan2} ❌")
    print(f"deep_equal: {nan1} == {nan2} = {deep_equal(nan1, nan2)} ✅")
    
    # Infinity comparison
    inf1 = float('inf')
    inf2 = float('inf')
    print(f"\nInfinity comparison:")
    print(f"Standard: {inf1} == {inf2} = {inf1 == inf2} ✅")
    print(f"deep_equal: {inf1} == {inf2} = {deep_equal(inf1, inf2)} ✅")
    
    # Mixed signs
    print(f"\nMixed infinity signs:")
    print(f"deep_equal(inf, -inf): {deep_equal(inf1, -inf1)} ✅ (correctly False)")


def demonstrate_numpy_support():
    """Show NumPy array support (if available)."""
    try:
        import numpy as np
        
        print("\n" + "=" * 60)
        print("NUMPY ARRAY SUPPORT")
        print("=" * 60)
        
        # Arrays with floating-point values
        arr1 = np.array([0.1 + 0.2, 0.3 + 0.4])
        arr2 = np.array([0.3, 0.7])
        
        print(f"\nNumPy arrays:")
        print(f"arr1 = {arr1}")
        print(f"arr2 = {arr2}")
        print(f"deep_equal(arr1, arr2): {deep_equal(arr1, arr2)} ✅")
        
        # Arrays with NaN
        arr_nan1 = np.array([1.0, np.nan, 3.0])
        arr_nan2 = np.array([1.0, np.nan, 3.0])
        print(f"\nArrays with NaN:")
        print(f"deep_equal handles NaN in arrays: {deep_equal(arr_nan1, arr_nan2)} ✅")
        
    except ImportError:
        print("\n(NumPy not installed - skipping NumPy examples)")


def demonstrate_bcb_integration():
    """Show how to integrate with BCB."""
    print("\n" + "=" * 60)
    print("BCB INTEGRATION")
    print("=" * 60)
    
    print("\nOriginal BCB code (causes false positives):")
    print("```python")
    print("# In BCB sandbox")
    print("assert task_func(secret_input) == task_func2(secret_input)")
    print("```")
    
    print("\nFixed BCB code:")
    print("```python")
    print("# In BCB sandbox")
    print("from bcb_deep_equal import deep_equal")
    print("assert deep_equal(task_func(secret_input), task_func2(secret_input))")
    print("```")
    
    print("\nFor sandboxed environments, use the simple version:")
    print("```python")
    print("from bcb_deep_equal import deep_equal_simple")
    print("assert deep_equal_simple(task_func(secret_input), task_func2(secret_input))")
    print("```")


if __name__ == "__main__":
    print("\n🔧 BCB Deep Equal Demo")
    print("Fixing floating-point comparison in BigCodeBench\n")
    
    demonstrate_problem()
    demonstrate_solution()
    demonstrate_complex_types()
    demonstrate_special_values()
    demonstrate_numpy_support()
    demonstrate_bcb_integration()
    
    print("\n" + "=" * 60)
    print("✅ BCB Deep Equal solves floating-point comparison issues!")
    print("=" * 60)
    print("\nInstall: pip install bcb-deep-equal")
    print("GitHub: https://github.com/aaron-sandoval/bcb-deep-equal")
    print()