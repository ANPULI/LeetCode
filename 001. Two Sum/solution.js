/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  lookup = new Map();
  for (let i = 0; i < nums.length; i++) {
      if (lookup.has(nums[i])) {
          return [lookup.get(nums[i]), i];
      }
      lookup.set(target - nums[i], i);
  }
};