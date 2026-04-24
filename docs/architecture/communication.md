# 📡 Communication Protocol & Bridge Logic

## JSON-RPC 2.0 Interface

All communication between the Frontend and Backend occurs via JSON-RPC 2.0 over a standard IPC channel or WebSocket.

### Standard Request Format:
```json
{
  "jsonrpc": "2.0",
  "method": "METHOD_NAME",
  "params": { ... },
  "id": "UNIQUE_ID"
}
```

### Registered Methods:
[To be populated]
