# An Advanced Example

In this chapter, we will implement a more advanced app. This app will start by testing the user's understanding of Pro Config, and then redirect to different pages based on the user's score. If the user's score is low, they will be redirected to a Pro Config tutorial chatbot. This advanced example includes concepts of Pro Config we have learned in previous chapters and serves as a great starting point for developers who would prefer building an app with more complicated logic. Here is the config:

Copy

```
{
  "type": "automata",
  "id": "advanced_example_demo",
  "initial": "home_page_state",
  "inputs": {},
  "outputs": {},
  "context": {
    "questions_string": "[{\"question\": \"Which of the following statements is not correct? \\n A. The execution of an Automata starts from the `initial` state. \\n B. An Automata can contain multiple AtomicStates. \\n C. Each AtomicState must define both inputs and outputs. \\n D. We can define transitions in either Automata or AtomicState.\", \"answer\": \"C\", \"explanation\": \"Both inputs and outputs in an AtomicState are optional.\"}, {\"question\": \"You are building an AutomicState, please choose the correct order of execution: \\n A. inputs -> tasks -> outputs -> render \\n B. render -> inputs -> tasks -> outputs. \\n C. tasks -> inputs -> outputs -> render.  \\n D. render -> tasks -> inputs -> outputs\", \"answer\": \"A\", \"explanation\": \"The correct order is `inputs -> tasks -> outputs -> render`. Please refer to `Expressions and Variables`\"}, {\"question\": \"Which of the following expressions is not correct (assume all the variables exist)? \\n A. context.variable \\n B. variable \\n C. variable1 + variable2 \\n D. np.array(variable)\", \"answer\": \"D\", \"explanation\": \"Our expression supports JavaScript grammar.\"}]",
    "questions": "",
    "question_idx": "",
    "chosen_answer": "",
    "correct_answer": "",
    "correct_count": "",
    "memory": "{{[]}}",
    "is_correct": "{{false}}",
    "intro_message": "",
    "tts_widget_id": ""
  },
  "transitions": {
    "go_home": "home_page_state",
    "get_quiz": "quiz_page_state",
    "continue": "continue_state"
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
        "context.tts_widget_id": "{{tts_widget_id}}",
        "context.questions": "{{JSON.parse(context.questions_string)}}",
        "context.question_idx": "{{0}}",
        "context.correct_count": "{{0}}"
      },
      "render": {
        "text": "Welcome to this Pro Config tutorial bot. Let's start a quiz!",
        "buttons": [
          {
            "content": "Quiz",
            "description": "get_quiz",
            "on_click": "get_quiz"
          }
        ]
      }
    },
    "quiz_page_state": {
      "outputs": {
        "context.correct_answer": "{{context.questions[context.question_idx]['answer']}}"
      },
      "render": {
        "text": "{{context.question_idx + 1}}. {{context.questions[context.question_idx]['question']}}",
        "buttons": [
          {
            "content": "A.",
            "description": "Choose A.",
            "on_click": "check_answer",
            "UNSTABLE_button_id": "A"
          },
          {
            "content": "B.",
            "description": "Choose B.",
            "on_click": "check_answer",
            "UNSTABLE_button_id": "B"
          },
          {
            "content": "C.",
            "description": "Choose C.",
            "on_click": "check_answer",
            "UNSTABLE_button_id": "C"
          },
          {
            "content": "D.",
            "description": "Choose D.",
            "on_click": "check_answer",
            "UNSTABLE_button_id": "D"
          }
        ]
      },
      "transitions": {
        "check_answer": "analyze_answer_state"
      }
    },
    "analyze_answer_state": {
      "inputs": {
        "button_id": {
          "type": "text",
          "user_input": false,
          "value": "UNSTABLE_button_id"
        }
      },
      "outputs": {
        "context.chosen_answer": "{{button_id}}",
        "context.is_correct": "{{button_id == context.correct_answer}}"
      },
      "render": {
        "text": "Check answer state."
      },
      "transitions": {
        "ALWAYS": [
          {
            "target": "correct_answer_state",
            "condition": "{{context.is_correct}}"
          },
          {
            "target": "wrong_answer_state",
            "condition": "{{true}}"
          }
        ]
      }
    },
    "correct_answer_state": {
      "outputs": {
        "context.question_idx": "{{(context.question_idx + 1) % context.questions.length}}",
        "context.correct_count": "{{context.correct_count + 1}}"
      },
      "render": {
        "text": "Congratulations! You have chosen the correct answer {{context.correct_answer}}",
        "buttons": [
          {
            "content": "Continue",
            "description": "continue",
            "on_click": "continue"
          }
        ]
      }
    },
    "wrong_answer_state": {
      "outputs": {
        "context.question_idx": "{{(context.question_idx + 1) % context.questions.length}}"
      },
      "render": {
        "text": "Oh No! The chosen answer is {{context.chosen_answer}}, while the correct one is {{context.correct_answer}}.",
        "buttons": [
          {
            "content": "Continue",
            "description": "continue",
            "on_click": "continue"
          }
        ]
      }
    },
    "continue_state": {
      "render": {
        "text": "Click to Next Question"
      },
      "transitions": {
        "ALWAYS": [
          {
            "target": "quiz_page_state",
            "condition": "{{context.question_idx > 0}}"
          },
          {
            "target": "finish_state",
            "condition": "{{context.correct_count == context.questions.length}}"
          },
          {
            "target": "review_state",
            "condition": "{{true}}"
          }
        ]
      }
    },
    "finish_state": {
      "render": {
        "text": "Congratulations! You are now a master of Pro Config!",
        "buttons": [
          {
            "content": "Home",
            "description": "Back to Home",
            "on_click": "go_home"
          }
        ]
      }
    },
    "review_state": {
      "outputs": {
        "context.memory": "{{[]}}"
      },
      "render": {
        "text": "{{context.intro_message}}"
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

We now elaborate on the above example by first reviewing some learned concepts, and then introducing some advanced features.

### Overview of the Entire Pipeline

Here is the pipeline of the application defined by the above config:

-   When the app starts, user will be prompted to input the `intro_message` and `tts_widget_id`, which will be passed through the automata and reused later in the chat page.
    
-   The user is then directed into a quiz page, where they will be answering several questions about the basic concepts of Pro Config.
    
    -   If the user gets all questions correct, the app will end, and a congratulation message will pop up.
        
    -   If the user gets some question wrong, the app will redirect to a chatbot that can interact and answer questions about Pro Config.
        
    

### Review of Basic Concepts

#### Inputs, Outputs, and Render

In the above example, we have used two types of inputs `text` and `IM` . `text` inputs prompts the user to input the `intro_message` and `tts_widget_id`. `IM` input is used in the chatbot where user directly send text messages.

The outputs used in the example are mainly for writing some variables to the context and do some basic calculation (such as increasing the question index). For rendering, we have used text, buttons, and audio in this example.

#### Workflow

We simply use LLM + TTS as the workflow in the `chat_page_state` ,which has been already discussed in previous chapter. We have fed some basic knowledge of Pro Config to the system\_prompt of the LLM, so that the chatbot has it's internal knowledge base to answer questions.

#### Transitions

The above example includes transitions through buttons (controlled by the `on_click` properties) and some reserved action names such as `CHAT` and `ALWAYS` . It also demonstrates how to perform conditional transitions, which we will discuss later.

#### Expressions and Variables

We can find some basic use cases of expressions (JavaScript grammar) to initialize some variables and do some basic calculation. We have also demonstrated how to use context to pass variables across different states.

### Advanced Features

#### Conditional Transitions

Please refer to `continue_state` which determines the state transition based on user's quiz score.

Copy

```
      "transitions": {
        "ALWAYS": [
          {
            "target": "quiz_page_state",
            "condition": "{{context.question_idx > 0}}"
          },
          {
            "target": "finish_state",
            "condition": "{{context.correct_count == context.questions.length}}"
          },
          {
            "target": "review_state",
            "condition": "{{true}}"
          }
        ]
      }
```

In this example, it will redirect to the `quiz_page_state` if the `question_idx` is valid. Otherwise, if the user has answered all the questions correctly, it will jump to the `finish_state`. If the user get any question wrong, it will jump to the `review_state` the let the user chat with a Pro Config tutorial bot. The conditions of the transition cases are evaluated sequentially, and the condition in the last case `{{true}}` is similar to the `default` keyword in C++ `case` .

#### Obtaining Button ID

To decide whether the user has chosen the correct answer, we need to know which button is clicked. This can be achieved by the `UNSTABLE_utton_id` variable:

Copy

```
    "quiz_page_state": {
    ...
      "render": {
        ...
        "buttons": [
          {
            "content": "A.",
            "description": "Choose A.",
            "on_click": "check_answer",
            "UNSTABLE_button_id": "A"
          },
          ...
        ]
    },
    "analyze_answer_state": {
      "inputs": {
        "button_id": {
          "type": "text",
          "user_input": false,
          "value": "UNSTABLE_button_id"
        }
      },
      "outputs": {
        "context.chosen_answer": "{{button_id}}",
        "context.is_correct": "{{button_id == context.correct_answer}}"
      },
    },
```

As the name of UNSTABLE\_button\_id suggests, this feature will no longer be supported in future versions. We will use better methods that can pass parameters through transitions to achieve the same function.

#### More Complicated Expressions

In the above example, we have also shown more complicated expressions such as parse a JSON string to the `context.questions`, which is useful to initialize structured data. Our expression also supports slicing of a list or a dict, such as

Copy

```
"text": "{{context.question_idx + 1}}. {{context.questions[context.question_idx]['question']}}",
```