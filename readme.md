<details>
<summary>

# V1 Browser automation

Browser is required on startup to fetch cookies. Breaks terms of service.

> ## Working version

</summary>

## Installation

`pip3 install revChatGPT`

## Configuration

1. Create account on [OpenAI's ChatGPT](https://chat.openai.com/)
2. Save your email and password

Required configuration:

```json
{
  "email": "<your email>",
  "password": "your password"
}
```

Optional configuration:

```json
{
  "conversation_id": "UUID...",
  "parent_id": "UUID...",
  "proxy": "..."
}
```

3. Save this as `$HOME/.config/revChatGPT/config.json`

## Usage

### Command line

`python3 -m revChatGPT.Unofficial`

```
!help - Show this message
!reset - Forget the current conversation
!refresh - Refresh the session authentication
!config - Show the current configuration
!rollback x - Rollback the conversation (x being the number of messages to rollback)
!exit - Exit this program
```

### Developer

```python
from revChatGPT.Unofficial import Chatbot

chatbot = Chatbot({
    "email": "<your email>",
    "password": "your password"
}, conversation_id=None, parent_id=None)  # You can start a custom conversation

response = chatbot.ask("Prompt", conversation_id=None,
                       parent_id=None)  # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

print(response)
# {
#   "message": message,
#   "conversation_id": self.conversation_id,
#   "parent_id": self.parent_id,
# }
```

Refer to [wiki](https://github.com/acheong08/ChatGPT/wiki/V1---Outdated-version) for advanced developer usage

<details>

<summary>

### API

`python3 -m revChatGPT.GPTserver`

</summary>

HTTP POST request:

```json
{
  "session_token": "eyJhbGciOiJkaXIiL...",
  "prompt": "Your prompt here"
}
```

Optional:

```json
{
  "session_token": "eyJhbGciOiJkaXIiL...",
  "prompt": "Your prompt here",
  "conversation_id": "UUID...",
  "parent_id": "UUID..."
}
```

- Rate limiting is enabled by default to prevent simultaneous requests

</details>

</details>



