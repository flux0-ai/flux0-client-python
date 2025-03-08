# ToolCallDTO


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `tool_call_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `tool_name`                                                          | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `args`                                                               | Dict[str, *Any*]                                                     | :heavy_check_mark:                                                   | N/A                                                                  |
| `result`                                                             | [OptionalNullable[models.ToolResultDTO]](../models/toolresultdto.md) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `error`                                                              | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |