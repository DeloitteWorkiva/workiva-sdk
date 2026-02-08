# InsertCellDestinationLink

Inserts a destination link at the provided cell. Creates a source link at the source anchor if one doesn't already exist. The destination link will reference the latest published revision of the source link.



## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `insert_at`                                                              | [models.Cell](../models/cell.md)                                         | :heavy_check_mark:                                                       | A cell indicates a single cell in a table. All indexes are zero based.<br/> | {<br/>"column": 9,<br/>"row": 5<br/>}                                    |
| `source_anchor`                                                          | *str*                                                                    | :heavy_check_mark:                                                       | The unique identifier for the source anchor.                             | WAxsaHxoYvTB4D0twUm6YtiF99TNO0gBkSOhgYBed9AMB99EUxqELDQychBaGR9SkZucm5sK |