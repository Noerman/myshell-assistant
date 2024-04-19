# Core Concepts

## **Understanding State Machines**

### **What is a State Machine?**

A state machine is a conceptual model used to design software. It describes a system that can be in one of a finite number of states at any given time. The machine transitions from one state to another in response to external inputs or events, and these transitions are defined by a set of rules or conditions.

In essence, a state machine models the behavior of an entity by specifying the sequence of events it goes through during its lifecycle, the conditions under which it transitions from one state to another, and the actions that occur as a result of those transitions.

**Terminology Clarification:**

**Automata" and "State Machine":** In our documentation and system design, we will use the term "**automata**" interchangeably with "**state** **machine**." They both refer to our engine that handles various states, each conducting tasks or sequences of tasks. Whether we call it an automata or a state machine, the functionality remains the same—executing tasks, managing transitions, and potentially operating as a recursive element within our application's architecture. This linguistic choice enables us to maintain consistent terminology while honoring the traditional and theoretical roots of “automata” within computer science.

### **Common Uses of State Machines in Software Development Modeling**

In software development, state machines are often used to model complex logic that requires a system to behave differently based on its history or context. They are particularly valuable in scenarios where it's essential to keep track of an object's state and ensure the system handles transitions and actions predictably. Some of the common applications include:

-   User Interface (UI) Control: Managing states of buttons, forms, and other UI elements.
    
-   Network Protocol Design: Handling connections, messages, and errors in networking code.
    
-   Business Process Management: Modeling workflow processes, approvals, and decision points.
    
-   Game Development: Managing character states, game levels, and object interactions.
    

### **The Relevance of State Machines to AI Native** **App**

In the context of a AI Native App development, a state machine is used to manage the flow of conversation. Since AI App must react to user inputs, which can be unpredictable, a state machine helps in defining how the bot should respond based on various conversational contexts or user inputs. Here's how it relates to chatbot apps:

-   Conversation States: The bot may have different states like greeting, awaiting response, processing information, and ending conversation.
    
-   Transition Triggers: User inputs, such as questions, commands, or button clicks, trigger the bot to transition between states.
    
-   Contextual Responses: Based on the current state, the bot can give contextually relevant responses, ask for further input, or perform actions.
    
-   Handling Complexity: As conversations progress, they may become complex. State machines help manage this complexity by breaking down the conversation into manageable chunks.
    

By integrating a state machine approach, developers can create a more structured and logical flow for the bot's conversation, leading to a more natural and efficient user experience. It simplifies the tracking of conversation progress, ensures consistency in responses, and allows for scaling the conversation logic as the bot's functionality grows.

## **Understanding Workflows**

### **What is a Workflow?**

A workflow represents the sequence of processes through which a piece of work passes from initiation to completion. In software terms, a workflow can be viewed as an automation of business processes during which documents, information, or tasks are passed from one participant to another in the correct order and to the proper standard.

### **Comparing State Machines and Workflows**

While state machines and workflows both manage sequences of operations or activities, they focus on different aspects of these sequences:

-   **State Machines**: They emphasize the states of a system and the transitions between those states. They deal with what the system is (its state) and how it reacts to events (transitions).
    
-   **Workflows**: They focus on the order of operations, specifically the tasks and the procedural steps required. They deal with when actions are taken and who performs them.
    

State machines are typically used in cases where an application has to manage complex, event-driven behavior that depends on context, such as user inputs in interactive applications or games, whereas workflows are commonly applied to business process management where tasks need to be performed in a specific order.

In short, state machines are about reacting to events, while workflows are about executing a series of tasks.

## Pro Config

### **Combining State Machine and Workflow**

Our product is designed to merge the reactive system capabilities of a state machine with the structured task execution of workflows.

1.  **Task-Oriented State:** Our states are designed to be task-oriented, empowering them to execute tasks autonomously. This means a state can perform its functions and transition to the next state without the need for user interaction. This ability essentially harnesses the full potential of workflows within the state machine's architecture, allowing for greater autonomy and efficiency.
    
2.  \*\*Recursive State Machine:\*\*To further streamline our system, we have engineered states to not only run sequences of tasks but also to operate as independent state machines when necessary. This recursive nature simplifies setup and management by reducing complexity in state configurations. A state acting as a state machine brings the flexibility of handling a more complex flow of tasks while maintaining the clear structure and reactivity of the overall state machine system.
    

By imbuing states with the ability to carry out tasks independently and allowing states to function recursively as state machines themselves, we create a dynamic and highly capable system. This approach enhances workflow execution without sacrificing the responsiveness and structure that is characteristic of state machines.

### **Modular AI Model as Tasks within States**

Now, let's talk about the integration of AI models within our product.

We treat AI models like the language model (LLM) or text-to-speech (TTS) as modular units that perform specific functions. They are analogous to running a function in programming, where inputs are provided, and outputs are generated accordingly.

Within the context of a state, these AI model functions act as tasks. When a state is activated, it may call upon an AI module with the relevant inputs, and the AI module processes these inputs to produce an output.

The output from the AI module is then either used to determine the next state transition or passed on to subsequent tasks within the same workflow for further action.