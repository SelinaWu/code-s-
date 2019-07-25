def maxProduct(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      # initialize
      product_min =  product_max = largest = nums[0]

      for i in range(1, len(nums)):

          product_max, product_min = max(product_max*nums[i], product_min*nums[i], nums[i]), min(product_max*nums[i], product_min*nums[i], nums[i])
          
          largest = product_max if product_max>largest else largest

      return largest
