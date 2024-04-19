# Building Workflow

Key Concepts In This Chapter: - **Module and its Configuration**

### A Simple Chatbot Example

In Pro Config, a workflow is a cascade of multiple Modules that can perform a series of tasks. In this chapter, we will build a simple chatbot that involves the cascade of two Modules.

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
        "audio": "{{reply_voice}}"
      },
      "transitions": {
        "CHAT": "chat_page_state"
      }
    }
  }
}
```

In the above config, we have created a chatbot that generates a reply to the user's input. Please note that this is a very simple chatbot without any memory (we will implement a chatbot with memory in Variables and Expressions). Now let's delve into the details of the above example:

In the chatbot above, we define the variable `user_message` of type `IM` (Instant Messaging). This allows the bot to take input in the form of messages sent to the bot. In the above example, we have set a transition on event `CHAT` to point to `chat_page_state`. So, whenever a user sends a message in the chat, the state is reloaded and the message is taken as in `IM` input.

This `user_message` is then passed into the tasks.

### Configuration of Each Module

Tasks contain multiple modules that execute sequentially. For each module, we need to specify the `module_type` and `module_config`. Rather, `name` is optional (for readability). In the example above, we include a GPT-3.5 LLM widget and a TTS widget provided on MyShell.

For demonstration purposes, we only used a simple system prompt `"You are a teacher teaching Pro Config."` In real-world applications, it is required to put some effort into prompt engineering and optimizing this system prompt for better performance. As for the TTS Widgets, you can choose any of your favorite voices from [https://app.myshell.ai/robot-workshop](https://app.myshell.ai/robot-workshop) and paste the widget ID into the config.

Specifically, after clicking the "workshop" button on the left menu bar, you will see this widget center. On the very top selection bar, select "TTS". Then pick your favorite voice model, use the "more" button to copy the widget ID, and paste into the config file.

If you would like to add more modules or widgets, please refer to  and 

### Render and Transitions

After the execution of the tasks, two variables called `reply` and `reply_voice` are obtained and ready to be rendered in a message that would appear in the User Interface. We have also handled a special event called `CHAT` in the transitions, which means when a user sends a message, the automata will jump into `chat_page_state` and execute that state. In the next section, we will describe how to handle and use different types of transitions.