class HIndex(object):
    def hIndex(self, citations):
        if (len(citations) == 1 and citations[0] >= 1):
            return 1
        min_citations = min(citations)
        max_citations = max(citations)
        h_index = 0
        for i in range (0, max_citations + 1):
            number_of_papers_with_atleast_i_citations = 0
            for x in citations:
                if (x >= i):
                    number_of_papers_with_atleast_i_citations += 1
            if (number_of_papers_with_atleast_i_citations >= i):
                h_index = i
        return h_index
    
    #More optimized solution
    def hIndex2(self, citations):
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))