from functools import cmp_to_key

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def func(h1, h2):
            if h2[0]!=h1[0]:
                return h2[0] - h1[0]
            elif h2[1]!=h1[1]:
                return h1[1] - h2[1]
        
        people.sort(key = cmp_to_key(func))
        print(people)
        ans = []
        for person in people:
            ans.insert(person[1], person)
        return ans