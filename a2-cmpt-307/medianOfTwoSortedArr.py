    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        X, Y = nums1, nums2
        total = len(X) + len(Y)
        half = total // 2

        if len(X) < len(Y): # so that X is always the shorter array
            X, Y = Y, X
        
        l, r = 0, len(X) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2 # - 2 for both arrays

            XleftPtr = X[i] if i >= 0 else float("-infinity")
            XrightPtr = X[i + 1] if i + 1 < len(X) else float("infinity")

            YleftPtr = Y[j] if j >= 0 else float("-infinity")
            YrightPtr = Y[j + 1] if j + 1 < len(Y) else float("infinity")

            if XleftPtr < YrightPtr and YleftPtr <= XrightPtr:
                if total % 2:
                    return min(XrightPtr, YrightPtr)
                return ((max(XleftPtr, YleftPtr) + min(XrightPtr, YrightPtr)) / 2)
            elif XleftPtr > YrightPtr:
                r = i - 1
            else:
                l = i + 1