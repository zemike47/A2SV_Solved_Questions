class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_map = {}

        for cpdomain in cpdomains:
            domain = cpdomain.split()

            rep = int(domain[0])

            parts = domain[1].split(".")

            subDomains = [".".join(parts[i:]) for i in range(len(parts))]

            for sd in subDomains:
                domains_map[sd] = domains_map.get(sd,0) + rep
        
        output = []
        for rep, domian in domains_map.items():
            cpdomains = f"{domian} {rep}"
            output.append(cpdomains)

        return output





