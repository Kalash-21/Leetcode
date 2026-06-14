class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records =[]
        result=0
        for o in operations :
            try:
                records.append(int(o))
            except:
                if o == "+":
                    records.append(records[-1]+records[-2])
                elif o =="D":
                    records.append(2*records[-1])
                elif o == "C":
                    records=records[:len(records)-1]

        for record in records:
            result += record
        return result 