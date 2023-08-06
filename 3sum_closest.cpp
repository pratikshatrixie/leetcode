class Solution
{
	public: int ans = 0;
	int mx = INT_MAX;
	void Solve(vector<int> &nums, int x, int i, int T)
	{
		int n = nums.size();
		int L = i;
		int R = n - 1;
		while (L < R)
		{
			int val = (nums[x] + nums[L] + nums[R]);
			if (abs(T - val) < mx)
			{
				ans = val;
				mx = abs(T - val);
			}
			else if (val > T) R--;
			else L++;
		}
	}

	int threeSumClosest(vector<int> &nums, int target)
	{
		int n = nums.size();
		sort(nums.begin(), nums.end());
		for (int i = 0; i < n - 2; i++)
		{
			if (i == 0 || nums[i - 1] != nums[i])
			{
				Solve(nums, i, i + 1, target);
			}
		}

		return ans;
	}
};