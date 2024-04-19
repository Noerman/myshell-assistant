# FAQ

## Bot configuration

### Intro Message and initial state

When you configure an Intro Message for your bot, the very first message from the bot will include the buttons set up for the initial state, eliminating the need for user input to activate the state machine.

## Running Pro Config

### Execution order of `AtomicState` and `Automata`

For `AtomicState`, the order is: `inputs` create variables, followed by `tasks`, then `outputs`, and finally, `render`, which does not create variables.

In `Automata`, variables are processed in this sequence: `inputs`, then `context`, followed by sequence of `states`, and lastly `outputs`.