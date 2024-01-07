import os
from time import sleep
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Create a new OpenAI object
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# create an assistant
my_assistant = client.beta.assistants.create(
    instructions="You are my personal assistant. You remind me of things that I need to do. You will be invoked from time to time to ask me updates about my tasks and whether there are any new tasks. Our first message everyday will be about how the day looks like and what all i plan to do. You can make suggestsions to make my plan better as well.",
    name="my_assistant",
    model="gpt-3.5-turbo-1106",
)

# create a thread, which represents a conversation with the assistant
thread = client.beta.threads.create()

# add a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Hello, I need to do the following tasks today: \n 1. Go to the gym \n 2. Go to the office \n 3. Go to the bank \n 4. Go to the supermarket \n 5. Go to the park \n 6. Go to the library \n 7. Go to the restaurant \n 8. Go to the hospital \n 9. Go to the pharmacy \n 10. Go to the post office \n 11. Go to the airport \n 12. Go to the train station \n 13. Go to the bus station \n 14. Go to the school \n 15. Go to the university \n 16. Go to the cinema \n 17. Go to the museum \n 18. Go to the zoo \n 19. Go to the beach \n 20. Go to the swimming pool \n 21. Go to the stadium \n 22. Go to the concert \n 23. Go to the theatre \n 24. Go to the opera \n 25. Go to the church \n 26. Go to the mosque \n 27. Go to the temple \n 28. Go to the synagogue \n 29. Go to the hotel \n 30. Go to the bar \n 31. Go to the cafe \n 32. Go to the pub \n 33. Go to the nightclub \n 34. Go to the casino \n 35. Go to the amusement park \n 36. Go to the aquarium \n 37. Go to the bowling alley \n 38. Go to the golf course \n 39. Go to the stadium \n 40. Go to the library \n 41. Go to the park \n 42. Go to the museum \n 43. Go to the zoo \n 44. Go to the beach \n 45. Go to the swimming pool \n 46. Go to the stadium \n 47. Go to the concert \n 48. Go to the theatre \n 49. Go to the opera \n 50. Go to the church \n 51. Go to the mosque \n 52. Go to the temple \n 53. Go to the synagogue \n"
)

print("creating run")

# get the assistant's response to the message
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=my_assistant.id
)

CONCLUSIVE_RUN_STATUS = ["completed", "failed", "expired", "cancelled", "requires_action"]

# TODO: add a timeout
while run.status not in CONCLUSIVE_RUN_STATUS:
    sleep(5)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

match run.status:
    case "completed":
        print("Run completed successfully")
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )

        print("messages are - ", messages)
    case "failed":
        print("Run failed")
        print("last error in the run - ", run.last_error)
    case "expired":
        print("Run expired")
    case "cancelled":
        print("Run cancelled")
    case "requires_action":
        print("Run requires action")
        print(run)
    case _:
        print("Run status unknown")
        print(run)