class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left = 0
        Right = len(people) - 1
        no_boats = 0

        while left <= Right:
            if people[left] + people[Right] > limit:
                no_boats += 1
            else:
                no_boats += 1
                left += 1
            Right -= 1
    
        return no_boats
