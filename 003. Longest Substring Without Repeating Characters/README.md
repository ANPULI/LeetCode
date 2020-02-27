# Problem

Given a string, find the length of the longest substring without repeating characters.

Example 1:

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
```

Example 2:

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Solution (Python)

| `variable` | definition |
| - | - |
| `i` | head index of the substring |
| `j` | tail index of the substring |
| `res` | length of largest substring |
| `lookup` | store `(c: idx)` where `s[idx] = c` |

We loop through the string. Every iteration, we check if `s[j]` is in the `lookup`. If so, we move `i` to `max(i, lookup[j] + 1)`. We take the max here because if `lookup[j] + 1 < i`, it is not in the current substring. We then update `lookup`.