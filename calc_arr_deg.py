from collections import Counter
class Sol:
    def calc_arr_deg(self,arr):
        l=[]
        c=Counter(arr)
        for i,count in enumerate(list(c.values())):
            if count==list(c.values())[0]:
                l.append(arr[i])
            else:
                break
        m=50000
        for num in l:
            arr.reverse()
            idx2=len(arr)-1-arr.index(num)
            arr.reverse()
            idx1=arr.index(num)
            dist=idx2-idx1+1
            m=min(m,dist)
        return m

if __name__ == '__main__':
    p=Sol()
    print(p.calc_arr_deg([1, 2, 2, 3, 1]))
