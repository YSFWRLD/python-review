# Function Verification

## Intended Purpose

The `find_max` function is intended to examine a list of numbers and return the largest number in that list.

## Hand Trace with `[3, 1, 9]`

The function starts by setting `biggest` to the first number, so `biggest = 3`.

The loop uses `range(len(numbers) - 1)`. Since the list contains three numbers, the loop processes indexes `0` and `1` only.

* At index `0`, the value is `3`. Since `3` is not greater than `biggest`, `biggest` remains `3`.
* At index `1`, the value is `1`. Since `1` is not greater than `biggest`, `biggest` remains `3`.

The loop never checks index `2`, where the value `9` is stored. The function therefore returns `3` instead of `9`.

## Bug Found

The bug is an off-by-one error in the loop range. Using `range(len(numbers) - 1)` causes the function to skip the final item in the list. Because the last number is never checked, the function can return an incorrect result when the largest number appears at the end.
