class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        table = {}

        def calculate(A, B, visited):
            if A == B:
                return 1.0
            visited.add(A)
            for C in table[A]:
                if C in visited:
                    continue
                cal = calculate(C, B, visited)
                if cal > 0:
                    return cal * table[A][C]
            return -1.0

        for (A, B), val in zip(equations, values):
            table[A] = table.get(A, {})
            table[B] = table.get(B, {})
            table[A][B] = val
            table[B][A] = 1/val

        result = []
        for A, B in queries:
            if not A in table or not B in table:
                result.append(-1.0)
                continue
            result.append(calculate(A, B, set()))

        return result
