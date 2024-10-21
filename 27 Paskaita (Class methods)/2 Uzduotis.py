class Reversed:
    string = str(input("Enter string: "))
    @classmethod
    def stringreversed(cls):

        user = cls.string[::-1]

        return f"Reversed string: {user}"
print(Reversed.stringreversed())