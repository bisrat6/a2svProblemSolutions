class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = Counter()
        for domain in cpdomains:
            space = domain.index(' ')
            visits = int(domain[:space])
            for i in range(space, len(domain)):
                if domain[i] in ' .':
                    sub = domain[i + 1:]
                    count[sub] += visits
        return [f"{v} {d}" for d, v in count.items()]
