# LLM Widget

### Widgets in Workshop

### Config

Most fields are compatible with [OpenAI API](https://platform.openai.com/docs/api-reference/chat/create).

Fields besides `widget_id` and `output_name`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
temperature

 | 

number (Optional)

 | 

Controls randomness in the LLMConfig model's responses.

 | 

0.6

 |
| 

top\_p

 | 

number (Optional)

 | 

Controls diversity via nucleus sampling in LLMConfig.

 | 

0.8

 |
| 

max\_tokens

 | 

number (Optional)

 | 

Determines the maximum length of the model’s response in LLMConfig.

 | 

150

 |
| 

presence\_penalty

 | 

number (Optional)

 | 

Influences the likelihood of the model to talk about new topics in LLMConfig.

 | 

0.6

 |
| 

frequency\_penalty

 | 

number (Optional)

 | 

Controls how often the model makes use of infrequent words in LLMConfig.

 | 

0.5

 |
| 

memory

 | 

MemoryItem\[\] (Optional)

 | 

Stores information acquired across multiple rounds of dialog in LLMConfig.

 | 

\[{ role: 'user', content: 'Hello World' }\]

 |
| 

need\_memory

 | 

boolean (Optional)

 | 

Determines if memory usage is required in LLMConfig.

 | 

true

 |
| 

system\_prompt

 | 

string

 | 

Expression (Required)

 | 

Provides system prompt for the user in LLMConfig.

 |
| 

user\_prompt

 | 

string

 | 

Expression (Required)

 | 

Provides user prompt for the system in LLMConfig.

 |
| 

function\_name

 | 

string (Optional)

 | 

Specifies the name of the function in LLMFunctionConfig.

 | 

'get\_current\_weather'

 |
| 

function\_description

 | 

string (Optional)

 | 

Provides a description of the function in LLMFunctionConfig.

 | 

'Get the current weather in a given location'

 |
| 

function\_parameters

 | 

FunctionParameter\[\] (Optional)

 | 

Specifies the parameters of the function in LLMFunctionConfig.

 | 

\[{name: 'city', type: 'string', description: 'The city, e.g. San Francisco, CA'}\]

 |
| 

output\_name

 | 

string (Required)

 | 

Determines the name of the module output in LLMConfig, defaults to 'reply'.

 | 

"reply"

 |

`FunctionParameter`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
name

 | 

string (Required)

 | 

Specifies the name of the function parameter in FunctionParameter.

 | 

'city'

 |
| 

type

 | 

string (Required)

 | 

Specifies the type of the function parameter in FunctionParameter.

 | 

'list', 'string' or 'number'

 |
| 

description

 | 

string (Required)

 | 

Provides a description of the function parameter in FunctionParameter.

 | 

'The city, e.g. San Francisco, CA'

 |

### Function Call

If you want to execute LLM function calls, you may specify `function_name`, `function_description` and `function_parameters` fields.

Function calls can be seen as a formatting wrapper provided by LLM (currently only supports OpenAI series models), allowing parameters to be input via JSON, and outputting a serial JSON.

Reference:

-   [https://www.promptingguide.ai/applications/function\_calling](https://www.promptingguide.ai/applications/function_calling)
    
-   [https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create)
    

For LLM function calls, the output of the widget is a JSON object, which includes the LLM returned results and will be automatically output to the state machine output in the form of key-value pairs.

### Example

Copy

```
{
  "id": "prompt_widget_template",
  "initial": "home_state",
  "states": {
    "home_state": {
      "inputs": {
        "input_message": {
          "type": "IM",
          "user_input": true
        }
      },
      "tasks": [
        {
          "name": "llm_widget_example_task",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "widget_id": "1744214047475109888",
            "user_prompt": "{{input_message}}", // the text inputted into prompt widget, you can get it from user input or upper state
            "system_prompt": "Act as ...", // Optional field. You can input system prompt of bot.
            "top_p": 0.5, // Optional field. Default value is 0.5
            "temperature": 0.5, // Optional field. Default value is 0.5
            "frequency_penalty": 0, // Optional field. Default value is 0
            "presence_penalty": 0, // Optional field. Default value is 0
            "output_name": "result"
          }
        }
      ],
      "render": {
        "text": "{{result}}", // it's a string produced by prompt widget.
        "buttons": [
          {
            "content": "Chat Again",
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