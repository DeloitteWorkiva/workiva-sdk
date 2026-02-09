# TestFormExportRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `test_form_id`                                       | *str*                                                | :heavy_check_mark:                                   | The unique identifier of the test form               |                                                      |
| `test_form_export`                                   | [models.TestFormExport](../models/testformexport.md) | :heavy_check_mark:                                   | Details about the test form export                   | {<br/>"format": "xlsx"<br/>}                         |