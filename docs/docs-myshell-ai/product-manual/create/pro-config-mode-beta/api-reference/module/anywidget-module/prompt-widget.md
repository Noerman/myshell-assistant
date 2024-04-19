# Prompt Widget

### Widgets in Workshop

### Config

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

### Example

Copy

```
{
  "id": "test",
  "initial": "home_state",
  "states": {
    "home_state": {
      "inputs": {
        "input_message": {
          "type": "text",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "any_module_test_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743157315558707200",
            "content": "{{input_message}}",
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "{{result}}",
        "buttons": [
          {
            "content":"Chat Again",
            "description":"",
            "on_click":"chat"
          }
          ]
      },
      "transitions": {
        "chat": "home_state"
      }
    }
  }
}
```