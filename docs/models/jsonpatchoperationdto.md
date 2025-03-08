# JSONPatchOperationDTO


## Fields

| Field                        | Type                         | Required                     | Description                  | Example                      |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `op`                         | [models.Op](../models/op.md) | :heavy_check_mark:           | The operation to perform     | add                          |
| `path`                       | *str*                        | :heavy_check_mark:           | The path to the target       | /-                           |
| `value`                      | *Any*                        | :heavy_check_mark:           | Any valid JSON               | "foo"                        |