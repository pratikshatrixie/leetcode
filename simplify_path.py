class Solution(object):
    def simplifyPath(self, path):
        output = []

        if len(path) == 0:
            return

        output1 = []

        for j in range(0,len(path)):
            if path[j] == "/" and j == len(path)-1:
                break
            elif path[j] == ".":
                continue
            else:
                output.append(path[j])
                
        for i in range(0,len(output)):
            if output[i] == "/":
                if i == len(output) - 1:
                    output1.append(output[i])
                elif output[i+1] == "/":
                    continue
                else:
                    output1.append(output[i])
            else:
                output1.append(output[i])
            

        return "".join(output1)