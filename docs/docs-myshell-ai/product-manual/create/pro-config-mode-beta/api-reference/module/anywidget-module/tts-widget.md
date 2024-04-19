# TTS Widget

Widget in Workshop

Config

Fields besides `widget_id` and `output_name`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
content

 | 

string (Required)

 | 

User input message processed by language models.

 | 

‘Hello.’

 |

Example

Copy

```
{
  "id": "test",
  "initial": "home_state",
  "states": {
    "home_state": {
      "inputs": {
        "read_text": {
          "type": "text",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "any_module_test_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743159010695057408",
            "content": "{{read_text}}",
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "{{read_text}}",
        "audio": "{{result}}",
        "buttons": [
          {
            "content":"Listen Again",
            "description":"",
            "on_click":"listen"
          }
        ]
      },
      "transitions": {
        "listen": "home_state"
      }
    }
  }
}
```