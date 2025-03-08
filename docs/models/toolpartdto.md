# ToolPartDTO


## Fields

| Field                  | Type                   | Required               | Description            | Example                |
| ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- |
| `tool_call_id`         | *str*                  | :heavy_check_mark:     | N/A                    |                        |
| `tool_name`            | *str*                  | :heavy_check_mark:     | N/A                    |                        |
| `args`                 | *Any*                  | :heavy_check_mark:     | Any valid JSON         | "foo"                  |
| `type`                 | *Literal["tool_call"]* | :heavy_check_mark:     | N/A                    |                        |