class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # FIXED
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_name = {}

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]  # FIXED

            if first_email not in parent:  # ADDED
                parent[first_email] = first_email

            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email

                union(first_email, email)
                email_to_name[email] = name

        from collections import defaultdict
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        res = []
        for root in groups:
            res.append([email_to_name[root]] + sorted(groups[root]))

        return res