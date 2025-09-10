#this program writes a letter to a group of people

def main():
    names = ["alice", "bob", "carol", "dave", "momo", "emilio", "frank", "grace", "heidi", "ivan"]
    for name in names:
        print(write_letter(name, "The Egg of Reason"))
        

def write_letter(receiver, sender):
    return f"""
        Dear {receiver},\n\n
        
        I hope this letter finds you well. I wanted to reach out and say hello!\n\n
        
        Best regards,\n
        
        {sender}\n

"""

main()