# Google Search Module

`GoogleSearchModule` provides creators with the ability to access google search and retrieve search result within Pro Config.

`GoogleSearchConfig`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
query

 | 

string (Required)

 | 

The search query in Google.

 | 

'What is the weather?'

 |
| 

num\_results

 | 

number (Optional. Default:3)

 | 

The number of search results. Keep in mind that more results may increase the module's response time.

 | 

3

 |
| 

length\_per\_result

 | 

number (Optional. Default:500)

 | 

The maximum character length for each retrieved search result. Any text exceeding this limit will be truncated.

 | 

500

 |
| 

output\_name

 | 

string (Required)

 | 

Specifies the name of the output in GoogleSearchModule.

 | 

'output'

 |

**Example**

Copy

```
{
  "id": "test",
  "initial": "home_state",
  "states": {
    "home_state": {
      "inputs": {
        "text_to_be_search": {
          "type": "text",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "google_search_module_test_task",
          "module_type": "GoogleSearchModule",
          "module_config": {
            "query": "{{text_to_be_search}}",
            "num_results": 3,
            "length_per_result":500,
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "{{result}}",
        "buttons": [
          {
            "content":"Search Again",
            "description":"",
            "on_click":"search"
          }
        ]
      },
      "transitions": {
        "search": "home_state"
      }
    }
  }
}
```