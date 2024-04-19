# Music Generation

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
        "prompt_a": {
          "type": "text",
          "user_input": true
        },
        "prompt_b": {
          "type": "text",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "any_module_test_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743838636299784192",
            "output_name": "result",
            "prompt_a": "{{prompt_a}}",
            "denoising": 0.75,
            "prompt_b": "{{prompt_b}}",
            "alpha": 0.5,
            "num_inference_steps": 50,
            "seed_image_id": "vibes"
          }
        }
      ],
      "render": {
        "text": "Result",
        "audio": "{{result.audio}}",
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