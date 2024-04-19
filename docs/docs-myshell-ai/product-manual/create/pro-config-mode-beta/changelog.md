# Changelog

### v0.8.1

#### Features

-   `AnyWidgetModule` supports Code Runner widgets.
    

### v0.8.0

#### Features

-   `AnyWidgetModule` supports LLM widgets.
    

`Module` will be deprecated in future and replaced by `Widget`.

#### Documentation

-   `LLMModule` and `TtsModule` in examples are replaced by `AnyWidgetModule` with LLM widgets and TTS widgets correspondingly.
    

### v0.7.0

#### Features

-   `Transition` supports `target_inputs` that specifies the value for the inputs of target state.
    
-   `Button` supports passing data through `on_click.payload` field.
    
-   MyShell supports copying any widget’s configuration JSON for Pro Config mode, containing necessary information about the inputs and outputs of that widget.
    

`UNSTABLE_button_id` will be deprecated in v1.0.0. Use `on_click.payload` and `target_inputs` instead.

### v0.6.1

#### Features

-   Modules now support `AnyWidgetModule` that allows using any widget in MyShell Workshop.
    
-   Modules now support GoogleSearchModule for google search.
    

### v0.6.0

#### Breaking Changes

-   The `tasks` within `AtomicState` have been changed to an array format. The object syntax is no longer supported, which means the execution order cannot be guaranteed if the object syntax is used.
    

#### Features

-   Transition now support conditional transitions.
    
-   Expressions now support ECMAScript 5.1 syntax and certain ECMAScript 6+ features.
    
-   The Button now supports passing parameters using the `UNSTABLE_button_id` property.
    

#### Documentation

-   Corrected the PepeTalk Example.
    
-   Included a link to a more comprehensive tutorial.
    