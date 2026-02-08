# EditsResult

A response from the POST edits endpoint


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  | Example                                                                      |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `record_id_map`                                                              | [Optional[models.RecordIDMap]](../models/recordidmap.md)                     | :heavy_minus_sign:                                                           | A mapping between temporary and actual record IDs                            | {<br/>"recordIdMap": {<br/>"myTempId123": "3f9d4e19-6281-4efb-8821-709d299809e7"<br/>}<br/>} |