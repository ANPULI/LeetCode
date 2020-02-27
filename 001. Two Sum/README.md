# Problem

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Solution (Python)

Every iteration, we look up the `value <- nums[i]` in a `dict`. If this value is not in the `dict`, we store the difference -> `target - nums[i]` as the key and the index `i` as the value in the dict. If this value is in the dict, we simply return `[dict[value], i]`

## Solution (Js)

Same as python.