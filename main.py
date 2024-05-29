import asyncio
import os

from okta.client import Client as OktaClient

oktaDomain = os.environ['OKTADOMAIN']
apiToken = os.environ['APITOKEN']


# Instantiating with a Python dictionary in the constructor
config = {
    'orgUrl': oktaDomain,
    'token': apiToken
}

client = OktaClient(config)

async def ask(userInput):
    return await asyncio.get_event_loop().run_in_executor(None, input, userInput)

async def main():
    print('===================== Adding Users =====================')

    createOtherUser = True
    names = []

    while createOtherUser:
        try:
            # add new user to array of names
            fname = await ask("First Name: ")
            lname = await ask("Last Name: ")
            names.append({'fname': fname, 'lname': lname})

            addAnother = await ask("Add another user (Y to continue)?")

            # case-insensitive string comparison
            if addAnother.upper() != 'Y':
                createOtherUser = False

        except Exception as error:
            print(error)
            raise error

    # =========== Step 2 ================
    # Create users based on earlier input
    # Use firstname.lastname@atko.email as username (For example, john1.doe@atko.email)


    # =========== Step 3 ================
    # Create a group, get group name through console input
    

    # =========== Step 4 ================
    # Add all users to the group

    
    # =========== Step 5 (optional)================
    # Prompt for users to be deleted, and remove them from tenant

    print("=====================Activity Completed=====================")

if __name__ == "__main__":
    asyncio.run(main())

