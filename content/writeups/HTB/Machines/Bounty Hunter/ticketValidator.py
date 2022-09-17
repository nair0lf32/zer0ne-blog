#Skytrain Inc Ticket Validation System 0.1
#Do not distribute this file.

def load_file(loc):
    if loc.endswith(".md"):                                                   #script must end in md
        return open(loc, 'r')
    else:
        print("Wrong file type.")
        exit()

def evaluate(ticketFile):
    #Evaluates a ticket to check for ireggularities.
    code_line = None
    for i,x in enumerate(ticketFile.readlines()):
        if i == 0:
            if not x.startswith("# Skytrain Inc"):                            #script must hae this
                return False
            continue
        if i == 1:
            if not x.startswith("## Ticket to "):                            #and this
                return False
            print(f"Destination: {' '.join(x.strip().split(' ')[3:])}")
            continue

        if x.startswith("__Ticket Code:__"):                                  #necessary too
            code_line = i+1
            continue

        if code_line and i == code_line:                                  #ticket code modulo by 7 must be 4? wtf is that rule? lol
            if not x.startswith("**"):
                return False                                               
            ticketCode = x.replace("**", "").split("+")[0]
            if int(ticketCode) % 7 == 4:
                validationNumber = eval(x.replace("**", ""))
                if validationNumber > 100:                                #and validationNumber must be > 100...geez what does skytrain do?
                    return True
                else:
                    return False                                   #so a valid ticket code must be a number (>100 and %7==4) + 10 == total and ...commands to execute
    return False

def main():
    fileName = input("Please enter the path to the ticket file.\n")
    ticket = load_file(fileName)
    #DEBUG print(ticket)
    result = evaluate(ticket)
    if (result):
        print("Valid ticket.")
    else:
        print("Invalid ticket.")
    ticket.close

main()
 
