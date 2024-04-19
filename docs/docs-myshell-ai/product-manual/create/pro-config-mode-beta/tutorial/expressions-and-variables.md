# Expressions and Variables

Key Concepts In This Chapter: - Variables to store and retain data - Expressions to perform conditions inside variables

### Variables: Concepts and Basic Use Cases

In this chapter, we will demonstrate how variables are defined, updated, and passed. As mentioned before, variables can be created within `inputs` of a state. For example:

Copy

```
{
  "type": "automata",
  "id": "hello_demo",
  "initial": "home_page_state",
  "inputs": {},
  "outputs": {},
  "transitions": {},
  "states": {
    "home_page_state": {
      "inputs": {
        "intro_message": {
          "type": "text",
          "user_input": true,
          "default_value": "Hi, this is your Pro Config Tutorial Bot"
        },
      },
      "render": {
        "text": "{{intro_message}}",
      },
    }
  }
}
```

The above simple example creates a variable called `intro_message` of type `text` with a default value and render it in the message. If `user_input` is `false`, user will not be prompted to input via a form, and a new variable with the value `default_value` will be automatically generated.

### Expressions

We can use expressions to take value of previously defined variables and perform basic calculations from it. In Pro Config, expressions are represented in a string wrapped by double curly braces like `{{expression}}`. Expressions uses the grammar of JavaScript, and supports most of the basic syntaxes.

Unlike defining a variable through `inputs`, the result type of an expression can be dynamically deduced during the execution of that expression. A more common use case is to use expressions inside a string (such as the prompts of LLM):

Copy

```
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
        ...
      ],
      "render": {
        "text": "{{reply}}",
        ...
      },
      ...
    }
```

In this case, Pro Config will replace the expression with the evaluated result of `user_message` (which is converted to string) and use that as the `user_prompt`.

### Scope of Variables

It is also important to understand the scope of variables. Currently, there are two ways to retrieve a variable:

1.  **Referring to a variable that's defined within an AutomicState**: we can directly use the variable name to refer to that variable (such as the `{{user_message}}` in the user\_prompt). Note that the execution of the AutomicState follows the order of `inputs->tasks->outputs->render`
    
2.  **Passing a variable across different AutomicStates**: we can use the `context` of the Automata to pass the variable. For example:
    

Copy

```
{
...
 "type": "automata",
 "context": {
    "var1": "",
  },
  "states": {
    "state1": {
      ...
      "outputs": {
        "context.var1": "{{some_variable}}",
      },
    },
    "state2": {
      "render": {
        "text": "{{context.var1}}",
      },
    }
  }
}
```

In the outputs of `state1`, we set `context.var1` as `some_variable` (which should be defined previously in `state1`), and we can display that variable in `state2` by `{{context.var1}}`. Note that the variable to be passed across states need to be declared in the `context` of the `Automata`

### Practice Example

In the following example, we will improve the chatbot built in previous chapters in two aspects:

-   Support customized `intro_message` and `tts_widget_id`
    
-   Implement memory in `LLMModule` to enable multiple rounds of chat.
    

Here is the config:

Copy

```
{
  "type": "automata",
  "id": "variable_expression_demo",
  "initial": "home_page_state",
  "inputs": {},
  "outputs": {},
  "context": {
    "intro_message": "",
    "tts_widget_id": "",
    "memory": ""
  },
  "transitions": {
    "go_home": "home_page_state"
  },
  "states": {
    "home_page_state": {
      "inputs": {
        "intro_message": {
          "type": "text",
          "user_input": true,
          "default_value": "Hi, this is your Pro Config Tutorial Bot, how can I assist you today"
        },
        "tts_widget_id": {
          "type": "text",
          "user_input": true,
          "default_value": "1743159010695057408"
        }
      },
      "outputs": {
        "context.intro_message": "{{intro_message}}",
        "context.tts_widget_id": "{{tts_widget_id}}"
      },
      "render": {
        "text": "Welcome to this demo. Click 'Start' to chat!",
        "buttons": [
          {
            "content": "Start Chat",
            "description": "Click to Start Chatting.",
            "on_click": "start_chat"
          }
        ]
      },
      "transitions": {
        "start_chat": "intro_message_state"
      }
    },
    "intro_message_state": {
      "render": {
        "text": "{{context.intro_message}}",
        "buttons": [
          {
            "content": "Home",
            "description": "Click to Go Back to Home.",
            "on_click": "go_home"
          }
        ]
      },
      "outputs": {
        "context.memory": "{{[]}}"
      },
      "transitions": {
        "CHAT": "chat_page_state"
      }
    },
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
            "memory": "{{context.memory}}",
            "output_name": "reply"
          }
        },
        {
          "name": "generate_voice",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "content": "{{reply}}",
            "widget_id": "{{context.tts_widget_id}}",
            "output_name": "reply_voice"
          }
        }
      ],
      "outputs": {
        "context.memory": "{{[...context.memory, {'user': user_message}, {'assistant': reply}]}}"
      },
      "render": {
        "text": "{{reply}}",
        "audio": "{{reply_voice}}",
        "buttons": [
          {
            "content": "Home",
            "description": "Click to Go Back to Home.",
            "on_click": "go_home"
          }
        ]
      },
      "transitions": {
        "CHAT": "chat_page_state"
      }
    }
  }
}
```

In the above example config, we prompt the user to input `intro_message` and `tts_widget_id`, which are written to `context` in the outputs. These two variables are reused later in `intro_message_state` and `chat_page_state` respectively. Besides, we leverage an array called `memory` to store the chat history and update the memory through an expression (for the grammar of this, follow the [Javascript syntax guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)) :

Copy

```
  "outputs": {
    "context.memory": "{{[...memory, {'user': user_message}, {'assistant': reply}]}}"
  },
```

which will append the latest chat messages to the memory. Then we pass the memory to the `memory` parameter of `LLMModule` so that the LLM can retain understand how to react based on previous interactions.

### Advanced Data Processing

If you want more powerful ability to process data, we recommend using  to execute code snippets in a free manner.

It requires knowledge about how to use a widget in Pro Config, which is just to be explained in the next chapter.