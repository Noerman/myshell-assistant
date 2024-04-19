# Code Runner Widget

### Widgets in Workshop

Currently we only provide JavaScript code runner. The supported syntax remains consistent with , including ECMAScript 5.1 and certain 6+ features. We don't support third-party libraries or host-environment-specific API like `fetch.`

### Config

Fields besides `widget_id` and `output_name`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
code

 | 

string (Required)

 | 

A stringified code snippet. It should contain one or more function definitions.

 | 

"function main(params) {\\n const { a, b } = params;\\n const sum = a + b;\\n return sum;\\n}"

 |
| 

function

 | 

string (Optional)

 | 

The name of the function you want to call in the code snippet. Defaults to `main`.

 | 

'main'

 |
| 

params

 | 

Object (Optional)

 | 

The parameters you pass to the calling function.

 | 

‘Hello.’

 |

You can use the widget's 'Copy' button to get a stringified code snippet for `code` field.

### Example

Copy

```
{
  "id": "code_widget_template",
  "initial": "home_state",
  "states": {
    "home_state": {
      "tasks": [
        {
          "name": "code_widget_example_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1751859390353202447",
            "params": {
              "a": "{{1}}",
              "b": "{{2}}"
            },
            "code": "function main(params) {\n const { a, b } = params;\n const sum = a + b;\n return sum;\n}",  // the text inputted into prompt widget, you can get it from user input or upper state
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "{{result}}", // it's a string produced by prompt widget.
        "buttons": [
          {
            "content": "Run Again",
            "description": "",
            "on_click": "rerun"
          }
        ]
      },
      "transitions": {
        "rerun": "home_state",
        "CHAT": "home_state"
      }
    }
  }
}
```