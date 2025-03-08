# CreateSessionRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `session_creation_params_dto`                                            | [models.SessionCreationParamsDTO](../models/sessioncreationparamsdto.md) | :heavy_check_mark:                                                       | N/A                                                                      | {<br/>"agent_id": "vUfk4PgjTm",<br/>"title": "What's the weather in SF?"<br/>} |
| `allow_greeting`                                                         | *Optional[bool]*                                                         | :heavy_minus_sign:                                                       | Indicates if the agent is permitted to send an initial greeting          |                                                                          |