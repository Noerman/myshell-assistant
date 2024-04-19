# Age Transformation

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
        "your_face_image_url": {
          "type": "image",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "any_module_test_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743838658173079552",
            "image": "{{your_face_image_url}}",
            "target_age": "default",
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "Result",
        "image": "{{result.file_url}}",
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