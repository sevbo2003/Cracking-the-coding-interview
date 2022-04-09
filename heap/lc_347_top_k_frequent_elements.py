""" 
LeetCode: 347. Top K Frequent Elements

Problem: Given an integer array nums and an integer k, return the k most frequent elements. 

Solution: 
1. Counter
2. Use the heap to get the K largests elements

Time: O(K*logN), where K is the top k elements and N is the length of the set(nums)
Space: O(N)
"""

from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        counts = Counter(nums)
        top_k = heapq.nlargest(k, counts.items(), key=lambda x: x[1])
        return [i[0] for i in top_k]
        
