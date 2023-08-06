class Solution:
    def samesign(self, x, y):
        if x < 0 and y < 0:
            return True
        elif x > 0 and y > 0:
            return True
        return False

    def asteroidCollision(self, a):
        n = len(a)
        st = []
        for i in range(n):
            if len(st) == 0 or (st[-1] < 0 and a[i] > 0) or self.samesign(st[-1], a[i]):
                st.append(a[i])
            else:
                while len(st) > 0 and st[-1] > 0 and st[-1] < abs(a[i]):
                    st.pop()

                if len(st) == 0 or st[-1] < 0:
                    st.append(a[i])
                elif st[-1] == abs(a[i]):
                    st.pop()

       
        return st