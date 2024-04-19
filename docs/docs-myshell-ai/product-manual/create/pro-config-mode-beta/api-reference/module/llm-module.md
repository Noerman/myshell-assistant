# LLM Module

Most fields are compatible with [OpenAI API](https://platform.openai.com/docs/api-reference/chat/create).

`LLMConfig`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
model

 | 

"gpt-35-turbo-16k"

 | 

"gpt-4-1116-preview" (Required)

 | 

Determines the OpenAI language model to be used in LLMConfig.

 |
| 

temperature

 | 

number (Optional)

 | 

Controls randomness in the LLMConfig model's responses.

 | 

0.6

 |
| 

top\_p

 | 

number (Optional)

 | 

Controls diversity via nucleus sampling in LLMConfig.

 | 

0.8

 |
| 

max\_tokens

 | 

number (Optional)

 | 

Determines the maximum length of the model’s response in LLMConfig.

 | 

150

 |
| 

presence\_penalty

 | 

number (Optional)

 | 

Influences the likelihood of the model to talk about new topics in LLMConfig.

 | 

0.6

 |
| 

frequency\_penalty

 | 

number (Optional)

 | 

Controls how often the model makes use of infrequent words in LLMConfig.

 | 

0.5

 |
| 

memory

 | 

MemoryItem\[\] (Optional)

 | 

Stores information acquired across multiple rounds of dialog in LLMConfig.

 | 

\[{ role: 'user', content: 'Hello World' }\]

 |
| 

need\_memory

 | 

boolean (Optional)

 | 

Determines if memory usage is required in LLMConfig.

 | 

true

 |
| 

system\_prompt

 | 

string

 | 

Expression (Required)

 | 

Provides system prompt for the user in LLMConfig.

 |
| 

user\_prompt

 | 

string

 | 

Expression (Required)

 | 

Provides user prompt for the system in LLMConfig.

 |
| 

output\_name

 | 

string (Required)

 | 

Determines the name of the module output in LLMConfig, defaults to 'reply'.

 | 

"reply"

 |

`MemoryItem`

| Field's Name | JSON Type (Required/Optional) | Description | Example |
| --- | --- | --- | --- |
| 
role

 | 

user

 | 

assistant (Required)

 | 

Specifies the source of the memory item in MemoryItem.

 |
| 

content

 | 

string

 | 

Expression (Required)

 | 

Specifies the actual value of the memory item in MemoryItem.

 |

#### 