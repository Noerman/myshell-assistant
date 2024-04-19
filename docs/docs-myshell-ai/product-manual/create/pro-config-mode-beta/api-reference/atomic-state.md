# Atomic State

## AtomicState

An atomic state is a state executing real tasks, which usually are small functional modules, such as LLM module and TTS module.

In MyShell bot, an entered atomic state usually means a sent message with buttons if specified.

`AtomicState`

| Field's Name | Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
id

 | 

string (Optional)

 | 

Globally unique identifier.

 | 

"1234\_5678\_9101"

 |
| 

type

 | 

"state" (Optional)

 | 

Specifies that this is an atomic state.

 | 

"state"

 |
| 

properties

 | 

Object (Optional)

 | 

Static config. Similar to metadata.

 | 

 |
| 

properties.is\_final

 | 

boolean (Optional)

 | 

Flag to check if the current state is final. Default to false.

 | 

true

 |
| 

inputs

 | 

Object (Optional)

 | 

Expected inputs, including user inputs and other states' outputs.

 | 

 |
| 

inputs.\[input\_name\]

 | 

Input or Expression (Required)

 | 

Specification about each input.

 | 

{"type" : "IM", "user\_input": true}

 |
| 

tasks

 | 

SupportModule\[\] (Optional)

 | 

Tasks executed in written order, involving no control ability such as if/else and loop. Each element is configuration for supported modules, including LLMModule, LLMFunctionModule and TtsModule for now.

 | 

 |
| 

outputs

 | 

Object (Optional)

 | 

Output values, including state's outputs and modification to parent automata's context, if it has a parent automata.

 | 

 |
| 

outputs.\[output\_name\]

 | 

Variable or Expression (Required)

 | 

Usually its an expression evaluating an intermediate variable.

 | 

{"context.prompt" : "{{reply}}"}

 |
| 

render

 | 

RenderConfig (Optional)

 | 

Controls how to display the result to the user.

 | 

{"text": "{{reply}}", "buttons": \["context": "Chat", "on\_click": "start\_chat"\]}

 |
| 

transitions

 | 

Object (Optional)

 | 

Indicates how state flows responding to user action. transitions's keys are events which the state will handle, including events triggered by itself or its children states if its children states don't handle this event. We treat both actual happened events and user intents as events.

AtomicState can trigger special events, including CHAT, ALWAYS

 | 

 |
| 

transitions\[event\]

 | 

Transition (Required)

 | 

It could simply a target state name, or a TransitionCase object.

 | 

{"start\_chat" : {"target": "chat\_page"}}

 |

Example:

Copy

```
{
  "inputs": {
    "user_input": {
      "type": "IM",
      "user_input": true
    }
  },
  "tasks": [
    {
      "module_type": "LLMFunctionModule",
      "module_config": {
        "model": "gpt-35-turbo-16k",
        "system_prompt": "{{context.system_prompt}}",
        "user_prompt": "{{context.prefix_prompt}}\n{{user_input}}\n{{context.suffix_prompt}}",
        "function_name": "reply_to_user",
        "function_description": "Generate reply to user.Always use this function.",
        "function_parameters": [
          {
            "name": "reply",
            "type": "string",
            "description": "This is your reply to user. AWAYS IN ENGLISH"
          }
        ]
      }
    },
    {
      "module_type": "TtsModule",
      "module_config": {
        "content": "{{reply}}",
        "tts_id": "2",
        "output_name": "reply_voice"
      }
    }
  ],
  "render": {
    "text": "{{reply}}",
    "audio": "{{reply_voice}}",
    "buttons": [
      {
        "content": "Return",
        "description": "",
        "on_click": "return"
      }
    ]
  },
  "transitions": {
    "CHAT": {},
    "create_scenario": "new_scenario"
  }
}
```

## Inputs

Each `Input` signifies that a variable is required for the state to function, and it is typically provided by user input. If there is user input whose type is not `"IM"`, then a transition to this state would prompt the opening of a modal, allowing the user to complete the input form.

The primary distinction between `Input` and `Output` in this context is that `Input` generally includes additional fields that govern how the user should complete the input form. These fields could include things like data validation rules, default values, or specific instructions for the user, which provide guidance on the expected form and content of the input. `Output`, in contrast, typically refers to the information that is conveyed back to the user after processing their input or completing a particular state transition.

`Input`

| Field's Name | Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
type

 | 

"text" | "image" | "audio" | ”IM" (Required)

 | 

The type of a given variable. "IM" refers to input that originates from the user's bot Instant Messaging interface.

 | 

"text"

 |
| 

value

 | 

string (Optional)

 | 

The value of a given variable. The type of the value depends on the type field. For text, value could be any string. For image, audio, value is string of URL. ForIM, value is usually undefined. If the transition to the state specifies target\_inputs, value won’t be overridden.

 | 

"Hello, World!" or "[https://example.com/audio.mp3](https://example.com/audio.mp3)"

 |
| 

default\_value

 | 

string (Optional)

 | 

The default value of an input variable, which is used when no value is given. The type is same as value. If the transition to the state specifies target\_inputs, default\_value will be overridden.

 | 

"{{prompt}}"

 |
| 

user\_input

 | 

Boolean (Optional)

 | 

An optional flag that indicates whether the input should come from the user. Defaults to false.

 | 

true

 |
| 

name

 | 

string (Optional)

 | 

An optional string that serves as a label for the form input.

 | 

"username"

 |
| 

description

 | 

string (Optional)

 | 

An optional string that serves as a description for the form input.

 | 

"Input your username here."

 |
| 

choices

 | 

string\[\] (Optional)

 | 

Allow users to select the value from given choices.

 | 

\["GPT", "Gemini"\]

 |

## Tasks

We support LLM module, LLM Function module and TTS module for now. More kinds of modules and customized modules are coming very soon.

To fully understand the configuration of these modules, you should refer to the  section where detailed information about each module, including their inputs, outputs, and functionality, is provided.

**Important Update**: In previous versions, we supported the `Object` type for defining `tasks`. Please be aware that the execution order cannot be guaranteed for the `Object` type and it will become deprecated in a future release. It is recommended to transition to using the `Array` type to ensure the execution order of `tasks`.

## Outputs

Currently, the use of context is necessary to store any output variables, as they are fundamentally kept within the parent automata's scope. However, in a few days, we will introduce support for isolated output variables that can be accessed through a prefix tied to the state name.

`Variable` is a subset of `Input`, only including `type` and `value` fields.

`Variable`

| Field's Name | Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
type

 | 

"text"

 | 

"image"

 | 

"audio"

 |
| 

value

 | 

string (Optional)

 | 

The value of a given variable. The type of the value depends on the type field. For text, value could be any string. For image, audio, value is string of URL. ForIM, value is usually undefined. For expression, value is Expression.

 | 

"Hello, World!" or "[https://example.com/audio.mp3](https://example.com/audio.mp3)"

 |

## Render

`RenderConfig` is responsible for defining how a bot presents the results executed by a state to the user. It can specify content of the result, whether it's a text message, an audio message, or interactive buttons that facilitate transitions to different states or prompt further user interaction.

`RenderConfig`

| Field's Name | Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
text

 | 

string (Optional)

 | 

The text that would be displayed on the render.

 | 

"This is the render text."

 |
| 

image

 | 

string (Optional)

 | 

A URL string to an image that would be displayed on the render.

 | 

"[https://example.com/image.jpg](https://example.com/image.jpg)"

 |
| 

audio

 | 

string (Optional)

 | 

A URL string to an audio file that would be played on the render.

 | 

"[https://example.com/audio.mp3](https://example.com/audio.mp3)"

 |
| 

buttons

 | 

Button\[\] (Optional)

 | 

An array of Button objects that may appear on the render for interactive purposes.

 | 

 |

`Button`

| Field's Name | Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
content

 | 

string (Required)

 | 

The visible text displayed on the button.

 | 

"Click Me"

 |
| 

description

 | 

String (Optional)

 | 

A tooltip that appears when you hover over the button.

 | 

"This button triggers the next part of the process"

 |
| 

on\_click

 | 

string | Event (Required)

 | 

Defines the event that should be triggered when the button is clicked. You can pass data to Transition if needed.

 | 

"start\_chat"

 |
| 

UNSTABLE\_button\_id

 | 

string (Optional)

 | 

When triggering the `on_click` event, you may pass data to the subsequent state by setting this field, provided that a `button_id` is specified within the `inputs` of the next state.

 | 

 |

`Event`

| Field's Name | Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
event

 | 

string (Required)

 | 

The event name.

 | 

"create\_page"

 |
| 

payload

 | 

Object (Optional)

 | 

When triggering an event, you may pass data to the TransitionCase by setting values in payload. In TransitionCase , passed data can be accessed by the prefix `payload.` .

 | 

 |