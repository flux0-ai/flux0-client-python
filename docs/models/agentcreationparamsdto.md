# AgentCreationParamsDTO


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `name`                                                            | *str*                                                             | :heavy_check_mark:                                                | The display name of the agent, mainly for representation purposes | Drizzle                                                           |
| `type`                                                            | *str*                                                             | :heavy_check_mark:                                                | The type of the agent                                             | weather                                                           |
| `description`                                                     | *OptionalNullable[str]*                                           | :heavy_minus_sign:                                                | N/A                                                               | An agent that checks the weather                                  |