# Melo TTS

### Widget

### Config

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
            "widget_id": "1745097608856756779",
            "language": "en_us",
            "speed": 1,
            "text": "{{input_message}}",
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "My Voice",
        "audio": "{{result.file_url}}",
        "buttons": [
          {
            "content": "Listen Again",
            "description": "",
            "on_click": "listen"
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