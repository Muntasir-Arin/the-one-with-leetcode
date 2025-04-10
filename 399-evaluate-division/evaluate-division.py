class Solution:
  def calcEquation(
      self,
      equations: list[list[str]],
      values: list[float],
      queries: list[list[str]],
  ) -> list[float]:
    ans = []
    graph = collections.defaultdict(dict)

    for (A, B), value in zip(equations, values):
      graph[A][B] = value
      graph[B][A] = 1 / value

    def devide(A: str, C: str, seen: set[str]) -> float:
      """Returns A / C."""
      if A == C:
        return 1.0

      seen.add(A)

      for B, value in graph[A].items():
        if B in seen:
          continue
        res = devide(B, C, seen)  
        if res > 0: 
          return value * res  

      return -1.0  
    for A, C in queries:
      if A not in graph or C not in graph:
        ans.append(-1.0)
      else:
        ans.append(devide(A, C, set()))

    return ans