# TestPhaseAttachmentUploadRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `graph_attachment_upload`                                          | [models.GraphAttachmentUpload](../models/graphattachmentupload.md) | :heavy_check_mark:                                                 | Details about the attachment                                       | {<br/>"fileName": "signature.jpg"<br/>}                            |
| `test_form_id`                                                     | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the test form                             |                                                                    |
| `test_phase_id`                                                    | *str*                                                              | :heavy_check_mark:                                                 | The unique identifier of the test phase                            |                                                                    |