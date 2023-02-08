class Solution:
    def interpret(self, command: str) -> str:
        re=""
        i=0
        while i<len(command):
            if command[i]=='('and command[i+1]==')':
                re+='o'
                i+=2
            elif command[i]=='(' or command[i]==')':
                i+=1
            else:
                re+=command[i]
                i+=1
        return re
            
