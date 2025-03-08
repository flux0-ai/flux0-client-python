# Sessions
(*sessions*)

## Overview

### Available Operations

* [create](#create) - Create a new session
* [retrieve](#retrieve) - Retrieve Session
* [create_event](#create_event) - Create and stream session events
* [list_events](#list_events) - List Events

## create

Create a new session bettween a user and an agent.

The session will be associated with the provided agent and optionally with a user.
If no user is provided, a guest user will be created.

### Example Usage

```python
from flux0_client import Flux0


with Flux0() as flux0:

    res = flux0.sessions.create(agent_id="vUfk4PgjTm", id="zv3h4j5Fjv", title="What's the weather in SF?")

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
from flux0_client import Flux0


with Flux0() as flux0:

    res = flux0.sessions.retrieve(session_id="zv3h4j5Fjv")

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
import flux0_client
from flux0_client import Flux0


with Flux0() as flux0:

    res = flux0.sessions.create_event(session_id="zv3h4j5Fjv", type_=flux0_client.EventTypeDTO.MESSAGE, source=flux0_client.EventSourceDTO.USER, content="What's the weather in SF?")

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

## list_events

List events for a session with optional filtering

Retrieves events that occurred within a session, optionally filtering by source, correlation ID, and types.

### Example Usage

```python
import flux0_client
from flux0_client import Flux0


with Flux0() as flux0:

    res = flux0.sessions.list_events(session_id="zv3h4j5Fjv", min_offset=0, correlation_id="RID(lyH-sVmwJO)::Y8oBzYT4CQ", types=[
        flux0_client.EventTypeDTO.MESSAGE,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `session_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | Unique identifier of the session                                                   | zv3h4j5Fjv                                                                         |
| `min_offset`                                                                       | *OptionalNullable[int]*                                                            | :heavy_minus_sign:                                                                 | N/A                                                                                | 0                                                                                  |
| `source`                                                                           | [OptionalNullable[models.EventSourceDTO]](../../models/eventsourcedto.md)          | :heavy_minus_sign:                                                                 | Source of the event within a session.<br/><br/>Identifies who or what generated the event. |                                                                                    |
| `correlation_id`                                                                   | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | N/A                                                                                | RID(lyH-sVmwJO)::Y8oBzYT4CQ                                                        |
| `types`                                                                            | List[[models.EventTypeDTO](../../models/eventtypedto.md)]                          | :heavy_minus_sign:                                                                 | N/A                                                                                | message,tool                                                                       |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |                                                                                    |

### Response

**[models.EventsDTO](../../models/eventsdto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |