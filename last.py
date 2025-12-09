from random import sample

class Recursion:
    def __init__(self):
        self.data = []
        self.max_size = 100

    def initialise(self):
        self.data = sample(range(1,3*self.max_size),self.max_size)

    def print_all(self):
        print(f"the size of the array is {str(len(self.data))}")
        print(f"b4 sorting the data is{self.data}")

    def fib_iter(self,n):
        if n < 1:
            raise ValueError("n must be positive")
        f1 = f2 =1 
        out = -1
        if n == 1 or n == 2:
            return f1
        for i in range(3,n+1):
            out = f1 + f2
            f1 = f2
            f2 = out
            print("the "+ str(i)+ "th fib number is "+ str(out))

    def fib_rec(self,n):
        if n < 1:
            raise ValueError("n must be positive")
        if n == 1 or n == 2:
            return 1
        else:
            return self.fib_rec(n-1) + self.fib_rec(n-2)

    def gcd(self,n,m):
        if n == m:
            return n 
        elif n < m:
            return self.gcd(m-n,n)
        else:
            return self.gcd(n-m,m)
    
    def merge_sort(self):
        self._merge_sort(self.data,0,len(self.data)-1)
        print("after merge is "+ str(self.data))

    def _merge_sort(self,arr,start,end):
        if start >= end:
            return
        mid = (end - start) // 2 + start
        self._merge_sort(arr,start,mid)
        self._merge_sort(arr,mid+1,end)
        self._merge(arr,start,mid,end)

    def _merge(self,arr,start,mid,end):
        temp = []
        p1 = start
        p2 = mid + 1
        while p1 <= mid and p2 <= end:
            if arr[p1] < arr [p2]:
                temp.append(arr[p1])
                p1+= 1
            else:
                temp.append(arr[p2])
                p2 += 1
        while p1 <= mid:
            temp.append(arr[p1])
            p1+= 1
        while p2 <= end:
            temp.append(arr[p2])
            p2+= 1
        for i in range(len(temp)):
            arr[start+i] = temp[i]

    def quick_sort(self):
        self._quick_sort(self.data,0,len(self.data)-1)
        print("after the quick sort the array is "+ str(self.data))

    def _quick_sort(self,arr,start,end):
        if start < end:
            pivot = self._partition(arr,start,end)
            self._quick_sort(arr,start,pivot-1)
            self._quick_sort(arr,pivot + 1, end)

    def _partition(self,arr,start,end):
        pivot = arr[end]
        i = start
        for j in range(start,end):
            if arr[j] < pivot:
                arr[j],arr[i] = arr[i],arr[j]
                i+=1
        arr[end],arr[i] = arr[i],arr[end]
        return i

    def palindrome(self,s):
        if len(s) == 0 or len(s) == 1:
            return True
        elif s[0] != s[len(s)- 1]:
            print("the first is "+ s[0])
            print("the last is "+ s[len(s)-1])
            return False
        else:
            return self.palindrome(s[1: len(s)- 1])

    def binary_combinations(self, n):
        if n < 0:
            raise ValueError("length must be non-negative")

        return self._binary_combinations(n)

    def _binary_combinations(self, n):
        if n == 0:
            return [""]      # base case: empty string
        if n == 1:
            return ["0", "1"]

        prev_list = self._binary_combinations(n - 1)

        combos = []
        for s in prev_list:
            combos.append("0" + s)
            combos.append("1" + s)

        return combos

            


def main():
    test = Recursion()
    test.initialise()
    test.print_all()
    test.fib_iter(5)
    print(test.fib_rec(5))
    print(test.gcd(27,18))
    merge = Recursion()
    merge.initialise()
    merge.print_all()
    merge.merge_sort()
    print("-------------")
    quick = Recursion()
    quick.initialise()
    quick.print_all()
    quick.quick_sort()
    print("-------------")
    str1 = "!_abba_!"
    str2 = "!_ab_!"
    print(quick.palindrome(str2))
    print(quick.binary_combinations(3))



if __name__ == "__main__":
    main()


