import requests
import os
def save_to_notion(current_date, content):
    title = str(current_date) + ' Diary' 
    Bearer = str(os.environ.get('Notion'))
    json = {
        "parent": { "type": "database_id", "database_id": "6f156fd64d634a3db44e8d5265953c87" },
        "properties": {
        "title": {
      "title": [{ "type": "text", "text": { "content": title } }]
        }
    },"children": [
            {
                "object": "block",
                "heading_2": {
                    "rich_text": [
                        {
                            "text": {
                                "content": str(current_date)
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "paragraph": {
                    "rich_text": [
                        {
                            "text": {
                                "content": content
                            
                            }
                        }
                    ],
                    "color": "default"
                }
            }
        ]
            }
    headers = {
    'Authorization': Bearer,
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}
    response = requests.post('https://api.notion.com/v1/pages', headers=headers, json=json)
    return "success to Notion"
