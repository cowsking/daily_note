from datetime import datetime
import openai
from src.database.database import db 
from datetime import datetime
def get_daily_report():
    notes = []
    with db:
        with db.cursor() as cursor:
            insert_query = "SELECT note from notes where date = %s"

            values = (str(datetime.now().date()))

            cursor.execute(insert_query, (values,))
            results = cursor.fetchall()
            for row in results:
                notes.append(row[0])
    print(notes,'test!')
    current_date = datetime.now().date()
    tempate = '''
    Dear ChatGPT, today is {}. I want you to be my daily journal co-pilot. I will write down my random thoughts, notes ideas etc during the day. At the end of the day I will ask you to:
1. Write a version of my journal that is better formatted, logically structured/organized, with improved writing without altering the meaning of my journal.
2.Summarize the key take-aways from my journal
3. Discover important insights into my life
4. Base on my journal, create an actionable to-do lists of the tasks/plans mentioned in my journal. Write the list in first-person voice, also in notion format


    Here is my Note:
    {}

    Thanks!


    '''.format(str(current_date), '\n'.join(notes))
    print(tempate)
    message=[{"role": "user", "content": tempate}]
    response = openai.ChatCompletion.create(
            model="gpt-4",
            messages = message,
            temperature=0.3,
            max_tokens=5000,
            frequency_penalty=0.0
        )
    print(response)
    return response