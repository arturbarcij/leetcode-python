    from typing import List
    from collections import defaultdict

    class Solution:
        def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
            parent = {}
            
            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])  # path compression
                return parent[x]

            def union(x, y):
                parent[find(x)] = find(y)        # merge groups

                
            for account in accounts:
                for email in account[1:]:
                    parent[email] = email
                    
            for account in accounts:
                first = account[1]
                for email in account[2:]:
                    union(first, email)
            
            groups = defaultdict(list)
            email_to_name = {}
            
            for account in accounts:
                name = account[0]
                for email in account[1:]:
                    groups[find(email)].append(email)
                    email_to_name[email] = name
            
            result = []
            for root, emails in groups.items():
                result.append([email_to_name[root]] + sorted(set(emails)))
            
            return result