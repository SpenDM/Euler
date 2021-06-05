
class Solution:
    checked_indices = set()

    def jump(self, nums) -> int:
        return self.getMinJumps(nums, 0)

    def getMinJumps(self, nums, index):

        self.checked_indices.add(index)

        # Reached the end
        if index == len(nums) - 1:
            return 0

        # In progress
        else:
            max_jump = nums[index]
            max_jump_index = index + max_jump

            # If can jump to the end, return 1 jump
            if max_jump_index >= len(nums) - 1:
                return 1

            # Otherwise, recurse through options
            else:
                child_jump_counts = []

                for jump_distance in reversed(range(1, max_jump+1)):
                    child_index = index + jump_distance

                    # If no path forward, skip
                    if nums[child_index] == 0:
                        continue

                    # Check if worth analyzing
                    if self.isWorthChecking(nums, child_index, max_jump_index):

                        # Recursively get the min jumps for the child index
                        child_min_jumps = self.getMinJumps(nums, child_index)

                        # If child has a path to the end, add to list of min jumps
                        if child_min_jumps:
                            child_jump_counts.append(child_min_jumps)

                # Return the min jumps needed among all child indices
                if child_jump_counts:
                    return min(child_jump_counts) + 1

                # If no children have paths forward, provide nothing
                else:
                    return None

    def isWorthChecking(self, nums, child_index, max_jump_index):
        child_jump = nums[child_index]

        # If has already been checked, don't check again since it can't be faster
        if child_index in self.checked_indices:
            return False

        # Don't dive into a num's paths if you cannot jump further than one farther than it
        for i in range(child_index + 1, max_jump_index + 1):
            diff = i - child_index
            if child_jump <= nums[i] + diff:
                return False

        return True


soln = Solution()
print(soln.jump([1,2,1,1,1,4,4,1,5,2,3,4,1,4,2,5,2,6,4,4,2,2,5,6,2,3,4,5,4,4,2,3,1,4,1,6,2,3,5,3,6,6,1,2,5,3,3,4,6,1,1,5,3,3,4,5,1,4,2,6,6,4,1,4,1,2,1,4,4,2,1,2,2,5,6,5,4,4,3,6,5,2,5,6,1,4,3,4,3,3,1,2,6,5,3,6,1,2,6,4,2,3,3,4,6,3,5,3,2,3,3,1,3,2,4,1,3,5,1,1,5,2,4,2,2,5,3,4,2,1,3,3,1,2,4,5,4,6,2,5,6,4,6,5,2,2,1,4,6,4,2,4,1,6,3,3,6,1,4,5,4,5,1,2,3,6,1,4,3,2,5,1,5,2,5,1,2,3,3,6,6,3,5,2,6,1,6,4,3,4,1,2,5,1,5,6,5,3,1,5,6,3,6,3,5,6,2,2,6,3,4,1,4,1,1,3,4,1,5,6,5,4,2,5,3,6,4,1,2,3,5,6,5,2,3,6,1,3,4,6,3,2,5,5,1,6,6,6,2,3,5,5,4,5,2,1,6,6,2,5,1,3,2,5,1,2,3,4,1,1,5,1,4,1,2,2,6,1,4,3,2,1,6,5,1,6,2,3,5,3,6,6,5,2,1,4,4,5,3,5,5,1,3,2,6,1,6,6,4,6,5,3,3,1,6,2,6,4,2,4,1,2,2,2,2,1,5,4,3,6,3,2,5,5,4,6,4,1,5,2,4,6,2,4,5,5,3,4,6,6,1,6,6,5,3,1,4,6,5,3,5,3,5,2,3,4,6,2,5,6,6,2,5,6,1,1,5,4,5,6,6,5,5,3,3,4,4,5,2,6,5,1,3,2,3,1,3,1,2,3,5,2,5,3,2,2,3,4,4,2,6,5,1,3,4,6,1,6,4,4,2,4,5,2,5,6,6,1,3,1,1,4,6,5,6,4,1,3,1,1,6,2,6,4,5,5,3,5,3,6,6,2,1,3,2,5,5,3,5,3,3,5,3,2,1,2,2,6,1,6,4,2,2,2,6,2,4,2,5,5,2,3,1,1,5,6,6,3,4,6,2,1,2,1,4,2,5,6,5,5,3,2,1,5,1,3,2,2,5,1,6,1,6,5,6,2,6,3,6,5,1,4,6,3,3,6,6,4,1,4,6,3,4,1,4,2,5,5,5,4,2,5,6,6,3,1,5,4,2,3,6,1,6,4,1,5,5,6,4,5,4,4,6,5,2,5,1,4,3,2,6,1,5,2,6,2,6,1,2,3,5,5,4,4,5,4,2,1,4,1,4,6,1,1,2,6,2,3,6,4,4,5,6,6,4,1,6,3,2,4,1,4,5,5,2,6,6,4,2,5,4,6,6,5,2,4,1,1,4,1,1,4,6,1,5,2,4,6,5,1,6,6,6,2,1,6,1,5,5,4,5,2,3,2,2,2,6,4,6,2,4,6,4,5,1,3,2,4,2,6,6,4,3,3,1,1,4,4,5,5,4,1,6,5,1,3,3,6,5,5,3,6,3,5,2,4,3,4,6,5,2,6,6,1,2,3,4,6,1,5,6,4,6,6,1,1,2,4,6,4,1,1,6,6,2,1,1,2,3,6,5,3,1,6,1,3,6,2,4,5,3,2,5,3,5,5,2,1,3,4,4,6,2,4,3,3,1,5,3,3,1,2,5,2,5,2,2,4,2,2,4,6,3,1,4,2,3,4,2,2,6,3,2,6,3,3,5,5,5,2,3,1,6,5,4,5,2,6,5,2,1,2,2,2,2,2,3,2,6,3,1,5,6,1,4,6,5,3,3,5,5,6,5,1,4,3,5,5,3,4,6,4,6,3,2,1,1,6,2,2,5,5,3,1,3,5,6,3,6,2,5,6,2,1,4,4,2,2,6,2,1,5,6,1,1,3,3,5,5,3,2,5,2,1,3,2,4,3,5,2,5,5,4,1,1,3,4,3,1,3,5,5,4,5,5,1,3,5,4,6,5,4,2,1,2,6,6,4,4,5,6,6,6,3,4,3,5,2,5,6,5,2,1,4,5,3,1,6,4,1,5,4,5,2,5,1,4,2,6,3,3,5,1,3,4,3,3,6,6,5,5,5,4,5,3,6,6,6,4,2,4,4,1,2,2,2,3,2,2,5,6,5,6,3,3,1,1,4,1,6,6,5,3,2,6,5,2,1,6,1,4,6,4,1,2,1,2,5,1,1,6,3,2,5,4,5,2,6,5,6,2,2,1,5,5,1,6,2,1,3,4,5,4,3,1,5,6,5,4,1,2,3,4,2,2,6,2,4,3,2,5,3,2,2,5,6,3,3,2,1,4,5,2,3,2,5,3,1,3,6,3,6,4,2,5,3,6,1,6,5,2,1,5,2,1,1,4,3,3,1,1,2,2,1,1,4,1,6,5,5,6,4,6,6,2,2,2,6,1,1,1,1,5,2,2,1,6,5,6,1,3,1,6,4,1,2,1,5,1,1,3,6,4,5,4,2,3,4,1,5,2,2,1,6,2,3,2,3,3,1,1,4,5,5,3,5,3,6,4,5,4,4,4,2,2,1,4,6,0,0,0,0,0]))

