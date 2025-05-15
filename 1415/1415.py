class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        options = {"a","b","c"}
        for i in range(1,n):
            newOp = set()
            for o in options:
                prev = o[-1]
                match prev:
                    case "a":
                        newOp.add(o+"b")
                        newOp.add(o+"c")
                    case "b":
                        newOp.add(o+"a")
                        newOp.add(o+"c")
                    case _:
                        newOp.add(o+"a")
                        newOp.add(o+"b")
            options = newOp
        options = sorted(list(options))
        for o in options: print(o)


        return options[k-1] if len(options)>=k else ""
