class Solution:
    def defangIPaddr(self, address: str) -> str:
        output = ""
        for i in range(len(address)):
            if address[i] == ".":
                output += '[.]'
            else:
                output+= address[i]
        return output
        