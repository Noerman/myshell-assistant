# Transitions

Key Concepts In This Chapter: - **Types of Transitions, Transition Attributes, and Transition Scope**

In this chapter, we will show how to perform the transition between different states. Here is an example config:

Copy

```
{
  "type": "automata",
  "id": "transition_demo",
  "initial": "home_page_state",
  "inputs": {},
  "outputs": {},
  "transitions": {
    "go_home": "home_page_state"
  },
  "states": {
    "home_page_state": {
      "render": {
        "text": "Click 'Start' to chat!",
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
        "text": "Hi, welcome to the Pro Config tutorial. How can I assist you today?",
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
            "output_name": "reply"
          }
        },
        {
          "name": "generate_voice",
          "module_type": "AnyWidgetModule",
          "module_config": {
            "content": "{{reply}}",
            "widget_id": "1743159010695057408",
            "output_name": "reply_voice"
          }
        }
      ],
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

### State Transition Process In the Above Example

In the above bot, the user will start from a home page. In `home_page_state`, when the user clicks the `Start Chat` button, the state machine jumps to `intro_message_state` and display the intro message.

At `intro_message_state` , user can transit to `chat_page_state` by chatting with the bot.

We have included several concepts related to transitions in the above example. Let's explain them one by one.

### Transition & Its Attributes

A transition is usually defined as:

Copy

```
"transitions": {
   "<action_name>": "<target_state>"
}
```

Where `<action_name>` is the name of action, usually which you provide in the `on_click` property of button, and `<target_state>` is the state to transition when the action is run. This way, you can create a flow where the user gets to choose the path they want the workflow to go by clicking buttons. There are also some **reserved action names** that allow you to transition when a specific event happens in your bot.

We currently support three reserved action names:

-   **CHAT**: triggered when the user sends a message
    
-   **ALWAYS**: triggered when an AtomicState has finished. Usually used to connect two consecutive states.
    
-   **DONE:** triggered when an Automata is finished. This can be useful in nested automata (to determine the next state of a child automata).
    

### The Scope of Transitions

The `transitions` can be defined either in an `AtomicState` or in an `Automata`. If a transition is defined in an `AtomicState`, it will only handle the action triggered in that AtomicState (such as `start_chat` in the `home_page_state`). However, if a transition is defined in the `Automata`, it will handle the actions in all its states. For example, since `go_home` is handled in the `transitions` of the whole `transition_demo`, any button within `transition_demo` that can trigger the action `go_home` and make the automata jump to `home_page_state`.

### Conditional Transitioning

Pro Config also supports conditional transition, which means performing validation of some boolean expressions during the transition. The syntax is as follows:

Copy

```
"transitions": {
  "<action_name>": [
    {
      "target": "<target_name1>",
      "condition": "<condition1>",
    },
    {
      "target": "<target_name2>",
      "condition": "<condition2>",
    }
    ...
  ]
}
```

When `<action_name>` is triggered, Pro Config will check the conditions sequentially (first check `<condition1>`, and then `<condition2>`) to decide which state to jump to. If no condition is satisfied, the automata will stay in the original state. We will show how to leverage this advanced syntax in later examples.