class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        Result = []

        domains = {}
        for domain in cpdomains:
            Dom = domain.split()
            visit = int(Dom[0])
            dmns = Dom[1].split(".")
            for i in range(len(dmns)):
                d = ".".join(dmns[i:])
                if d in domains:
                    domains[d] += visit
                else:
                    domains[d] = visit
        
        Answer = []
        for D in domains:
            s = str(domains[D]) + " " + D
            Answer.append(s)
        return Answer
