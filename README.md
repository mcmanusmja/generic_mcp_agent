# Generic MCP Agent
This project derives from the book: Building MCP Agents with Python (James Colton). \
Its purpose is to define a useful base for creating reliable compliant MCP Agents.
## Background
MCP - the 3 pillars:
* Context Models
* Structured Messaging Protocol
* Agent Roles and Responsibility Isolation
### Context Models
### Structure Message Protocol
MCP Agents communicate via structure messages. Such messages have a fixed format:
* Sender
* Receive
* Type
* Payload
### Agent Roles and Responsibility Isolation