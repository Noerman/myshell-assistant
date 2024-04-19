# Atomic State

## AtomicState

An atomic state is a state executing real tasks, which usually are small functional modules, such as LLM module and TTS module.

In MyShell bot, an entered atomic state usually means a sent message with buttons if specified.

## Inputs

Each  signifies that a variable is required for the state to function, and it is typically provided by user input. If there is user input whose type is not `"IM"`, then a transition to this state would prompt the opening of a modal, allowing the user to complete the input form.

The primary distinction between `Input` and `Output` in this context is that `Input` generally includes additional fields that govern how the user should complete the input form. These fields could include things like data validation rules, default values, or specific instructions for the user, which provide guidance on the expected form and content of the input. `Output`, in contrast, typically refers to the information that is conveyed back to the user after processing their input or completing a particular state transition.

## Tasks

We support LLM module, LLM Function module and TTS module for now. More kinds of modules and customized modules are coming very soon.

To fully understand the configuration of these modules, you should refer to the  section where detailed information about each module, including their inputs, outputs, and functionality, is provided.

**Important Update**: In previous versions, we supported the `Object` type for defining `tasks`. Please be aware that the execution order cannot be guaranteed for the `Object` type and it will become deprecated in a future release. It is recommended to transition to using the `Array` type to ensure the execution order of `tasks`.

## Outputs

Currently, the use of context is necessary to store any output variables, as they are fundamentally kept within the parent automata's scope. However, in a few days, we will introduce support for isolated output variables that can be accessed through a prefix tied to the state name.

 is a subset of `Input`, only including `type` and `value` fields.

## Render

 is responsible for defining how a bot presents the results executed by a state to the user. It can specify content of the result, whether it's a text message, an audio message, or interactive buttons that facilitate transitions to different states or prompt further user interaction.