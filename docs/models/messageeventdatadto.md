# MessageEventDataDTO


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `parts`                                  | List[[models.Parts](../models/parts.md)] | :heavy_check_mark:                       | N/A                                      |
| `type`                                   | *Literal["message"]*                     | :heavy_check_mark:                       | N/A                                      |
| `tags`                                   | List[*str*]                              | :heavy_minus_sign:                       | N/A                                      |
| `flagged`                                | *OptionalNullable[bool]*                 | :heavy_minus_sign:                       | N/A                                      |
| `participant`                            | Dict[str, *str*]                         | :heavy_minus_sign:                       | N/A                                      |