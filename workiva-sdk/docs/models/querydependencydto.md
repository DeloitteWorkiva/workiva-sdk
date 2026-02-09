# QueryDependencyDto

The query text associated with any persisted query contains references to tables upon which that query relies. This model represents those dependencies. Every dependency contains a database and table identifier as in a traditional SQL database.


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `database_id`                                   | *str*                                           | :heavy_check_mark:                              | The database in which this dependency exists.   |
| `system`                                        | [models.System](../models/system.md)            | :heavy_check_mark:                              | The name of the system holding this reference.  |
| `table_id`                                      | *str*                                           | :heavy_check_mark:                              | The id of the table this dependency represents. |