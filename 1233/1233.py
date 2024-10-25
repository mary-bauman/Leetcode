class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=len)
        arr = []
        for f in folder:
            if not any(len(f) >= len(a) and f.startswith(a + "/") for a in arr):
                arr.append(f)

        return arr
