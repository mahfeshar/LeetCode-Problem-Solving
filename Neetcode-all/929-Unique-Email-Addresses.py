class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        from collections import defaultdict
        # emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
        myDic = defaultdict(set)
        for email in emails:
            domain = ""
            local = ""
            i = 0
            while i < len(email):
                if email[i] == '.':
                    i += 1
                    continue
                if email[i] == '+':
                    i = email.index('@')
                    continue
                if email[i] == '@':
                    domain = email[i + 1 :]
                    break
                local += email[i]
                i += 1
            myDic[local].add(domain)

        # print(myDic)
        count = 0
        for value in myDic.values():
            # print(value)
            # print(type(value))
            count += len(value)
        return(count)