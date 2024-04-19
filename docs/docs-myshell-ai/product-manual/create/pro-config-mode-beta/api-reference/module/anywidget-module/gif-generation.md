# GIF Generation

### GIF Generation

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
        "prompt": {
          "type": "text",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "any_module_test_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743838648844947456",
            "output_name": "result",
            "prompt": "{{prompt}}",
            "negative_prompt": "blurry",
            "width": 672,
            "height": 384,
            "scheduler": "EulerAncestralDiscreteScheduler",
            "steps": 30,
            "mp4": false,
            "seed": 6226
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