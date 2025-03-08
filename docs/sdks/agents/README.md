# Agents
(*agents*)

## Overview

### Available Operations

* [list](#list) - List Agents
* [create](#create) - Create Agent
* [retrieve](#retrieve) - Retrieve Agent

## list

Retrieves a list of all agents in the system.

Returns an empty list if no agents exist.
Agents are returned in no guaranteed order.

### Example Usage

```python
from openapi import SDK


with SDK() as sdk:

    res = sdk.agents.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentsDTO](../../models/agentsdto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## create

Creates a new agent with the specified parameters.

### Example Usage

```python
from openapi import SDK


with SDK() as sdk:

    res = sdk.agents.create(name="Drizzle", type_="weather", description="An agent that checks the weather")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The display name of the agent, mainly for representation purposes   | Drizzle                                                             |
| `type`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The type of the agent                                               | weather                                                             |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 | An agent that checks the weather                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AgentDTO](../../models/agentdto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves details of a specific agent by ID.

### Example Usage

```python
from openapi import SDK


with SDK() as sdk:

    res = sdk.agents.retrieve(agent_id="vUfk4PgjTm")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | Unique identifier for the agent                                     | vUfk4PgjTm                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AgentDTO](../../models/agentdto.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |