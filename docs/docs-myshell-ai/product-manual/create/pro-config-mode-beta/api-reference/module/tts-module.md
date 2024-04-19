# TTS Module

TTSModule provides creators with the ability to freely assemble TTS (Text-to-Speech) configurations within MyShell.

`TTSConfig`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
tts\_widget\_url

 | 

string (Required)

 | 

Specifies the URL for the TTS widget. Creators can select their desired voices in the Workshop, and use the share function to obtain a shared widget link, which is used here.

 | 

'[https://app.myshell.ai/widget/yi2aIf](https://app.myshell.ai/widget/yi2aIf)'

 |
| 

content

 | 

string

 | 

Expression (Required)

 | 

Specifies the text that needs to be read aloud.

 |
| 

output\_name

 | 

string (Required)

 | 

Specifies the name of the output in TtsConfig.

 | 

'output'

 |

## 