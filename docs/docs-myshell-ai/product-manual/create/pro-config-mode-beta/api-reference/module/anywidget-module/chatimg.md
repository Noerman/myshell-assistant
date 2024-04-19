# ChatImg

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
        "your_image_url": {
          "type": "image",
          "user_input": true
        },
        "your_question": {
          "type": "text",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "any_module_test_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743838640687026176",
            "output_name": "result",
            "image": "{{your_image_url}}",
            "prompt": "{{your_question}}",
            "top_p": 1,
            "temperature": 0.2,
            "max_tokens": 1024
          }
        }
      ],
      "render": {
        "text": "{{result.content}}",
        "buttons": [
          {
            "content": "Generate Again",
            "description": "",
            "on_click": "generate"
          }
        ]
      },
      "transitions": {
        "generate": "home_state"
      }
    }
  }
}
```