# Integration with Any Widget

MyShell currently supports over a thousand widgets with diverse functionalities, including prompt widgets, voice widgets, image generation widgets, and many more, in which all you could find on our widget center.

The AnyWidget Module for Pro Config is designed to be versatile. For instance, constructing a video generation bot that combines ASR, TTS, LipSync, and AutoCaption widgets is within the realm of possibilities.

As introduced beforehand, after you get into MyShell's Widget center, there a numerous widgets where you could play with and insert that into your Pro Config. We suggest to follow these steps before you implement it in Pro Config.

### 1\. Try it, Hands-on

### 2\. Adjust the parameters

### 3\. Copy the widget Pro Config template (it's an independent automata that includes that widget as a task)

Copy

```
{
  "id": "prompt_widget_template",
  "initial": "home_state",
  "states": {
    "home_state": {
      "inputs": {
        "prompt_a": {
          "type": "text",
	  "description":"The prompt for your audio",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "any_module_example_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743838636299784192",            
            "prompt_a":"{{prompt_a}}", // this field will received value from user input
            "denoising":0.75, // How much to transform input spectrogram
            "prompt_b":"90's rap", // The second prompt to interpolate with the first, leave blank if no interpolation
            "alpha":0.5, // Interpolation alpha if using two prompts. A value of 0 uses prompt_a fully, a value of 1 uses prompt_b fully
            "num_inference_steps":50, // Number of steps to run the diffusion model
            "seed_image_id":"vibes", // Seed spectrogram to use
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "{{JSON.stringify(result)}}", // this widget will output a map, you can first run it and know what its type is.
        "buttons": [
          {
            "content":"Generate Again",
            "description":"",
            "on_click":"generate"
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

### 4\. Modify Pro Config according to the copied config

For example, the original Pro Config is the  in the previous chapter. We may replace TtsModule with the music generation widget.

The following JSON is invalid since we just copy the template without changing anything.

Copy

```
{
  "type": "automata",
  "id": "chat_demo",
  "initial": "chat_page_state",
  "inputs": {},
  "outputs": {},
  "transitions": {},
  "states": {
    "chat_page_state": {
      "inputs": {
        "user_message": {
          "type": "IM",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "generate_reply",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1744214024104448000",
            "system_prompt": "You are a teacher teaching Pro Config.",
            "user_prompt": "{{user_message}}",
            "output_name": "reply"
          }
        },
        {
          "name": "any_module_example_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743838636299784192",            
            "prompt_a":"{{prompt_a}}", // this field will received value from user input
            "denoising":0.75, // How much to transform input spectrogram
            "prompt_b":"90's rap", // The second prompt to interpolate with the first, leave blank if no interpolation
            "alpha":0.5, // Interpolation alpha if using two prompts. A value of 0 uses prompt_a fully, a value of 1 uses prompt_b fully
            "num_inference_steps":50, // Number of steps to run the diffusion model
            "seed_image_id":"vibes", // Seed spectrogram to use
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "{{reply}}",
        "audio": "{{reply_voice}}"
      },
      "transitions": {
        "CHAT": "chat_page_state"
      }
    }
  }
}
```

Then the variables' names may be changed to fit the original config. `"prompt_a":"{{prompt_a}}"` needs to be changed to `"prompt_a":"{{reply}}"`. `render` also needs to be changed.

You may find it necessary to add more inputs or outputs to use the widget, because widgets often require parameters you don't anticipate.

Copy

```
{
  "type": "automata",
  "id": "chat_demo",
  "initial": "chat_page_state",
  "inputs": {},
  "outputs": {},
  "transitions": {},
  "states": {
    "chat_page_state": {
      "inputs": {
        "user_message": {
          "type": "IM",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "generate_reply",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1744214024104448000",
            "system_prompt": "You are a teacher teaching Pro Config.",
            "user_prompt": "{{user_message}}",
            "output_name": "reply"
          }
        },
        {
          "name": "any_module_example_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1743838636299784192",            
            "prompt_a":"{{reply}}", // this field will received value from user input
            "denoising":0.75, // How much to transform input spectrogram
            "prompt_b":"90's rap", // The second prompt to interpolate with the first, leave blank if no interpolation
            "alpha":0.5, // Interpolation alpha if using two prompts. A value of 0 uses prompt_a fully, a value of 1 uses prompt_b fully
            "num_inference_steps":50, // Number of steps to run the diffusion model
            "seed_image_id":"vibes", // Seed spectrogram to use
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "{{JSON.stringify(result)}}", // this widget will output a map, you can first run it and know what its type is.
      },
      "transitions": {
        "CHAT": "chat_page_state"
      }
    }
  }
}
```

Finally, adjust the `module_config` according to the parameters you have tried and decided in the step 2.