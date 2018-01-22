# Writing a function that can find the position of first substring of a string
# find_substring('hello, trinity', 'tri') == 6

def find_substring(string, sub):
        """
        :type string: str
        :type sub: str
        :rtype: int
        """
        # use flag to identify the substring position
        flag = 0
        for i in range(0,len(string)):
            if string[i] == sub[0]:
                for j in range(0,len(sub)):
                    if j <= i and string[i+j] == sub[j]:
                        flag = 1
                    else:
                        flag = 0
                if flag == 1:
                    # if find the result, return the position
                    return i
                # else, return none
        return None


