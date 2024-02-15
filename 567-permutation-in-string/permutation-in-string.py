class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # fixed size sliding window

        s2_size, s1_size = len(s2),len(s1)
        
        s1_count = [0]*26
        window_count = [0]*26

        # get counts
        for c in s1:
            s1_count[ord(c)-97] += 1 #Unicode value - Unicode value of A
        
        # build window
        for c in s2[:s1_size]:
            window_count[ord(c)-97] += 1
            
        #
        for i in range(s2_size-s1_size):
            if s1_count == window_count:
                return True
            window_count[ord(s2[i])-97] -= 1 # shift window, remove left char
            window_count[ord(s2[i+s1_size])-97] += 1 # add right char

        return s1_count == window_count
           
        