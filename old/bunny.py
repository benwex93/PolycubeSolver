def get_permutations(nums):
	#for empty list return 0
	if len(nums) == 1:
		return [nums]
	permutations = []
	for i in range(len(nums)):
		sub_perms = get_permutations(nums[:i] + nums[i+1:])
		for s in sub_perms:
			permutations.append([nums[i]] + s)
	return permutations

def solution(nums):

	#get max divisible by 3 combination
	permutations = get_permutations(nums)
	max_div_combo = 0
	for p in permutations:
		#convert to int
		perm_string = [str(i) for i in p]
		perm_int  = int("".join(perm_string))
		#compare if div by 3
		if perm_int % 3 == 0:
			max_div_combo = max(max_div_combo, perm_int)
	for i in range(len(nums)):
		#test all subsets
		max_div_combo = max(max_div_combo, solution(nums[:i] + nums[i+1:]))
	return max_div_combo