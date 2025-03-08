# Sessions
(*sessions*)

## Overview

### Available Operations

* [create](#create) - Create a new session
* [retrieve](#retrieve) - Retrieve Session
* [create_event](#create_event) - Create and stream session events

## create

Create a new session bettween a user and an agent.

The session will be associated with the provided agent and optionally with a user.
If no user is provided, a guest user will be created.

### Example Usage

```python
from openapi import SDK


with SDK() as sdk:

    res = sdk.sessions.create(agent_id="vUfk4PgjTm", id="zv3h4j5Fjv", title="What's the weather in SF?")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the agent associated with the session.         | vUfk4PgjTm                                                          |
| `allow_greeting`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates if the agent is permitted to send an initial greeting     |                                                                     |
| `id`                                                                | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 | zv3h4j5Fjv                                                          |
| `title`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 | A tale about a friendly dragon and a lost princess                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SessionDTO](../../models/sessiondto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieve details of a session by its unique identifier

### Example Usage

```python
from openapi import SDK


with SDK() as sdk:

    res = sdk.sessions.retrieve(session_id="zv3h4j5Fjv")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier of the session                                    | zv3h4j5Fjv                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SessionDTO](../../models/sessiondto.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## create_event

Creates a new event in the specified session and streams upcoming events.

### Example Usage

```python
import openapi
from openapi import SDK


with SDK() as sdk:

    res = sdk.sessions.create_event(session_id="zv3h4j5Fjv", type_=openapi.EventTypeDTO.MESSAGE, source=openapi.EventSourceDTO.USER, content="What's the weather in SF?")

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     | Example                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `session_id`                                                                                                                    | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | Unique identifier of the session                                                                                                | zv3h4j5Fjv                                                                                                                      |
| `type`                                                                                                                          | [models.EventTypeDTO](../../models/eventtypedto.md)                                                                             | :heavy_check_mark:                                                                                                              | Type of event that occurred within a session.<br/><br/>Represents different types of interactions that can occur within a conversation. |                                                                                                                                 |
| `source`                                                                                                                        | [models.EventSourceDTO](../../models/eventsourcedto.md)                                                                         | :heavy_check_mark:                                                                                                              | Source of the event within a session.<br/><br/>Identifies who or what generated the event.                                      |                                                                                                                                 |
| `content`                                                                                                                       | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             | What's the weather in SF?                                                                                                       |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |                                                                                                                                 |

### Response

**[Union[eventstreaming.EventStream[models.SessionStream], eventstreaming.EventStreamAsync[models.SessionStream]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |