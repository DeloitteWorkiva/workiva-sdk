# TestForms

## Overview

These endpoints are used to manage test forms, test phases, and matrices. They are also used to manage attachments on test phases, matrices, and samples.


### Available Operations

* [create_matrix](#create_matrix) - Create a new matrix
* [create_sample](#create_sample) - Create a new sample
* [get_matrices](#get_matrices) - Retrieve a list of matrices
* [get_matrix_attachment_by_id](#get_matrix_attachment_by_id) - Retrieve a single matrix attachment
* [get_matrix_attachments](#get_matrix_attachments) - Retrieve a list of matrix attachments
* [get_matrix_by_id](#get_matrix_by_id) - Retrieve a single matrix
* [get_sample_attachment_by_id](#get_sample_attachment_by_id) - Retrieve a single sample attachment
* [get_sample_attachments](#get_sample_attachments) - Retrieve a list of sample attachments
* [get_sample_by_id](#get_sample_by_id) - Retrieve a single sample
* [get_samples](#get_samples) - Retrieve a list of samples
* [get_test_form_by_id](#get_test_form_by_id) - Retrieve a single test form
* [get_test_forms](#get_test_forms) - Retrieve a list of test forms
* [get_test_phase_attachment_by_id](#get_test_phase_attachment_by_id) - Retrieve a single test phase attachment
* [get_test_phase_attachments](#get_test_phase_attachments) - Retrieve a list of test phase attachments
* [get_test_phase_by_id](#get_test_phase_by_id) - Retrive a single test phase
* [get_test_phases](#get_test_phases) - Retrieve a list of test phases
* [matrix_attachment_download_by_id](#matrix_attachment_download_by_id) - Initiate a matrix attachment download
* [matrix_attachment_export_by_id](#matrix_attachment_export_by_id) - Initiate an export of a matrix attachment
* [matrix_attachment_upload](#matrix_attachment_upload) - Initiate a matrix attachment upload
* [partially_update_sample_by_id](#partially_update_sample_by_id) - Partially update a single sample
* [sample_attachment_download_by_id](#sample_attachment_download_by_id) - Initiate a download of a sample attachment
* [sample_attachment_export_by_id](#sample_attachment_export_by_id) - Initiate an export of a sample attachment
* [sample_attachment_upload](#sample_attachment_upload) - Initiate an upload of a sample attachment
* [sample_insertion](#sample_insertion) - Insert samples
* [sample_update](#sample_update) - Update samples
* [test_form_export](#test_form_export) - Initiate a test form export
* [test_phase_attachment_download_by_id](#test_phase_attachment_download_by_id) - Initiate a test phase attachment download
* [test_phase_attachment_export_by_id](#test_phase_attachment_export_by_id) - Initiate a test phase attachment export
* [test_phase_attachment_upload](#test_phase_attachment_upload) - Initiate a test phase attachment upload

## create_matrix

Create a new empty [matrix](ref:testforms#matrix). The `id` field for the matrix and its columns should be left blank; this will be populated by the endpoint.


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="createMatrix" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.create_matrix(test_form_id="<id>", test_phase_id="<id>", matrix={
        "data_columns": [
            {
                "external_id": "TA05",
                "id": "d795d7a3-e7f7-4b3f-be6a-109653b2929b",
                "name": "PO Number",
            },
            {
                "external_id": "TA06",
                "id": "fbd818ec-4fd1-42ad-9112-3c80e71dc2dc",
                "name": "Amount",
            },
        ],
        "name": "Purchase Orders",
        "result_columns": [
            {
                "external_id": "TA07",
                "id": "d795d7a3-e7f7-4b3f-be6a-109653b2c34d",
                "name": "A",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="createMatrix" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.create_matrix(test_form_id="<id>", test_phase_id="<id>", matrix={
        "data_columns": [
            {
                "external_id": "TA05",
                "name": "PO Number",
            },
            {
                "external_id": "TA06",
                "name": "Amount",
            },
        ],
        "name": "Purchase Orders",
        "result_columns": [
            {
                "external_id": "TA07",
                "name": "A",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `test_form_id`                                                                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                | The unique identifier of the test form                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                   |
| `test_phase_id`                                                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                | The unique identifier of the test phase                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                   |
| `matrix`                                                                                                                                                                                                                                                                                                                                          | [models.MatrixInput](../../models/matrixinput.md)                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                | The properties of the matrix to create                                                                                                                                                                                                                                                                                                            | {<br/>"dataColumns": [<br/>{<br/>"externalId": "TA05",<br/>"id": "d795d7a3-e7f7-4b3f-be6a-109653b2929b",<br/>"name": "PO Number"<br/>},<br/>{<br/>"externalId": "TA06",<br/>"id": "fbd818ec-4fd1-42ad-9112-3c80e71dc2dc",<br/>"name": "Amount"<br/>}<br/>],<br/>"name": "Purchase Orders",<br/>"resultColumns": [<br/>{<br/>"externalId": "TA07",<br/>"id": "d795d7a3-e7f7-4b3f-be6a-109653b2c34d",<br/>"name": "A"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[models.Matrix](../../models/matrix.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## create_sample

Create a new [sample](ref:testforms#matrixsample) in a [matrix](ref:testforms#matrix). The new sample will be appended to the end of the matrix.


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="createSample" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.create_sample(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", matrix_sample={
        "data_values": [
            {
                "column": "6d870cd1-7bbe-4b14-b85d-f152913b068c",
                "value": "23897",
            },
            {
                "column": "6301bea4-30be-4c24-9f15-287396f41d2c",
                "value": "385.3",
            },
        ],
        "id": "3dd42da0-3543-4e03-ac4a-2ddefebe27d6",
        "result_values": [
            {
                "column": "674a9283-fd03-425d-bd62-0552263699e2",
                "value": "PASS",
            },
            {
                "column": "c7b812b4-70bb-47ed-a9bb-f56ca496c92f",
                "value": "FAIL",
            },
        ],
    })

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="createSample" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.create_sample(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", matrix_sample={
        "data_values": [
            {
                "column": "d795d7a3-e7f7-4b3f-be6a-109653b2929b",
                "value": "789",
            },
            {
                "column": "fbd818ec-4fd1-42ad-9112-3c80e71dc2dc",
                "value": "303.3",
            },
        ],
        "result_values": [
            {
                "column": "d795d7a3-e7f7-4b3f-be6a-109653b2c34d",
                "value": "PASS",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `matrix_id`                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                   | The unique identifier of the matrix                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                      |
| `test_form_id`                                                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                   | The unique identifier of the test form                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                      |
| `test_phase_id`                                                                                                                                                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                   | The unique identifier of the test phase                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                      |
| `matrix_sample`                                                                                                                                                                                                                                                                                                                                                                      | [models.MatrixSampleInput](../../models/matrixsampleinput.md)                                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                   | The properties of the sample to create                                                                                                                                                                                                                                                                                                                                               | {<br/>"dataValues": [<br/>{<br/>"column": "6d870cd1-7bbe-4b14-b85d-f152913b068c",<br/>"value": "23897"<br/>},<br/>{<br/>"column": "6301bea4-30be-4c24-9f15-287396f41d2c",<br/>"value": "385.3"<br/>}<br/>],<br/>"id": "3dd42da0-3543-4e03-ac4a-2ddefebe27d6",<br/>"resultValues": [<br/>{<br/>"column": "674a9283-fd03-425d-bd62-0552263699e2",<br/>"value": "PASS"<br/>},<br/>{<br/>"column": "c7b812b4-70bb-47ed-a9bb-f56ca496c92f",<br/>"value": "FAIL"<br/>}<br/>]<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                      |

### Response

**[models.MatrixSample](../../models/matrixsample.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_matrices

Returns a list of [matrices](ref:testforms#matrix).


### Example Usage

<!-- UsageSnippet language="python" operationID="getMatrices" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_matrices(test_form_id="<id>", test_phase_id="<id>", expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |                                                                     |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |                                                                     |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.MatricesListResult](../../models/matriceslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_matrix_attachment_by_id

Retrieve a single [attachment](ref:testforms#graphattachment) by its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getMatrixAttachmentById" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachments/{attachmentId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_matrix_attachment_by_id(attachment_id="<id>", matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attachment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the attachment                             |
| `matrix_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the matrix                                 |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GraphAttachment](../../models/graphattachment.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_matrix_attachments

Returns a list of [attachments](ref:testforms#graphattachment) for a matrix.


### Example Usage

<!-- UsageSnippet language="python" operationID="getMatrixAttachments" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachments" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_matrix_attachments(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `matrix_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the matrix                                 |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GraphAttachmentsListResult](../../models/graphattachmentslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_matrix_by_id

Retrieves a [matrix](ref:testforms#matrix) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getMatrixById" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_matrix_by_id(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `matrix_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the matrix                                 |                                                                     |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |                                                                     |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |                                                                     |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Matrix](../../models/matrix.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_sample_attachment_by_id

Retrieve a single [attachment](ref:testforms#graphattachment) by its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSampleAttachmentById" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachments/{attachmentId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_sample_attachment_by_id(request={
        "attachment_id": "<id>",
        "matrix_id": "<id>",
        "sample_id": "<id>",
        "test_form_id": "<id>",
        "test_phase_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.GetSampleAttachmentByIDRequest](../../models/getsampleattachmentbyidrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.GraphAttachment](../../models/graphattachment.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_sample_attachments

Returns a list of [attachments](ref:testforms#graphattachment) for a [sample](ref:testforms#matrixsample).


### Example Usage

<!-- UsageSnippet language="python" operationID="getSampleAttachments" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachments" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_sample_attachments(matrix_id="<id>", sample_id="<id>", test_form_id="<id>", test_phase_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `matrix_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the matrix                                 |
| `sample_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the sample                                 |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GraphAttachmentsListResult](../../models/graphattachmentslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_sample_by_id

Retrieves a [sample](ref:testforms#matrixsample) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSampleById" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_sample_by_id(request={
        "expand": "?$expand=relationships\n",
        "matrix_id": "<id>",
        "sample_id": "<id>",
        "test_form_id": "<id>",
        "test_phase_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetSampleByIDRequest](../../models/getsamplebyidrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MatrixSample](../../models/matrixsample.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_samples

Returns a list of [samples](ref:testforms#matrixsample).


### Example Usage

<!-- UsageSnippet language="python" operationID="getSamples" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_samples(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `matrix_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the matrix                                 |                                                                     |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |                                                                     |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |                                                                     |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.MatrixSamplesListResult](../../models/matrixsampleslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_test_form_by_id

Retrieves a [test form](ref:testforms#testform) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTestFormById" method="get" path="/testForms/{testFormId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_test_form_by_id(test_form_id="<id>", expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |                                                                     |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TestForm](../../models/testform.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_test_forms

Retrieves a list of [test forms](ref:testforms#testform).


### Example Usage

<!-- UsageSnippet language="python" operationID="getTestForms" method="get" path="/testForms" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_test_forms(expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TestFormsListResult](../../models/testformslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_test_phase_attachment_by_id

Retrieve a single [attachment](ref:testforms#graphattachment) by its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTestPhaseAttachmentById" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/attachments/{attachmentId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_test_phase_attachment_by_id(attachment_id="<id>", test_form_id="<id>", test_phase_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attachment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the attachment                             |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GraphAttachment](../../models/graphattachment.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_test_phase_attachments

Returns a list of [attachments](ref:testforms#graphattachment) for a [test phase](ref:testforms#testphase).


### Example Usage

<!-- UsageSnippet language="python" operationID="getTestPhaseAttachments" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}/attachments" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_test_phase_attachments(test_form_id="<id>", test_phase_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GraphAttachmentsListResult](../../models/graphattachmentslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_test_phase_by_id

Retrieves a [test phase](ref:testforms#testphase) given its ID.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTestPhaseById" method="get" path="/testForms/{testFormId}/testPhases/{testPhaseId}" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_test_phase_by_id(test_form_id="<id>", test_phase_id="<id>", expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |                                                                     |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |                                                                     |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TestPhase](../../models/testphase.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_test_phases

Returns a list of [test phases](ref:testforms#testphase).


### Example Usage

<!-- UsageSnippet language="python" operationID="getTestPhases" method="get" path="/testForms/{testFormId}/testPhases" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.get_test_phases(test_form_id="<id>", expand="?$expand=relationships\n")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |                                                                     |
| `expand`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Returns related resources inline with the main resource             | ?$expand=relationships<br/>                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TestPhasesListResult](../../models/testphaseslistresult.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## matrix_attachment_download_by_id

Asynchronously downloads an attachment from a [matrix](ref:testforms#matrix).

Responses include a `Location` header, which indicates where to poll for download results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the download is ready, its status will be `completed`, and the response body includes a `resourceURL`. To download the file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the download request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="matrixAttachmentDownloadById" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachments/{attachmentId}/download" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.matrix_attachment_download_by_id(attachment_id="<id>", matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attachment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the attachment                             |
| `matrix_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the matrix                                 |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MatrixAttachmentDownloadByIDResponse](../../models/matrixattachmentdownloadbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## matrix_attachment_export_by_id

Asynchronously exports an attachment for a [matrix](ref:testforms#matrix) to .PDF.

Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="matrixAttachmentExportById" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachments/{attachmentId}/export" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.matrix_attachment_export_by_id(request={
        "graph_attachment_export": {
            "format_": models.GraphAttachmentExportFormat.PDF,
        },
        "attachment_id": "<id>",
        "matrix_id": "<id>",
        "test_form_id": "<id>",
        "test_phase_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.MatrixAttachmentExportByIDRequest](../../models/matrixattachmentexportbyidrequest.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.MatrixAttachmentExportByIDResponse](../../models/matrixattachmentexportbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## matrix_attachment_upload

Starts the process to upload and attach a file to a [matrix](ref:testforms#matrix) using a [graph attachment upload](ref:testforms#graphattachmentupload) object. The response body will include an `uploadUrl`. To upload the file contents, perform a PUT on the `uploadUrl` with the same authentication credentials and flow as the attachmentUpload request. For more details, see [Authentication documentation](ref:overview#authentication).

The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="matrixAttachmentUpload" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachmentUpload" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.matrix_attachment_upload(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", graph_attachment_upload={
        "file_name": "signature.jpg",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `matrix_id`                                                           | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the matrix                                   |                                                                       |
| `test_form_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the test form                                |                                                                       |
| `test_phase_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the test phase                               |                                                                       |
| `graph_attachment_upload`                                             | [models.GraphAttachmentUpload](../../models/graphattachmentupload.md) | :heavy_check_mark:                                                    | Details about the attachment upload                                   | {<br/>"fileName": "signature.jpg"<br/>}                               |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.MatrixAttachmentUploadResponse](../../models/matrixattachmentuploadresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## partially_update_sample_by_id

Partially updates the properties of a [sample](ref:testforms#matrixsample). Note: Cell values must always be strings, even if they represent a number.
### Options
|Path|PATCH Operations Supported|
|---|---|
|`/dataValues/<index>/value`|`replace`|
|`/resultValues/<index>/value`|`replace`|


### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="partiallyUpdateSampleById" method="patch" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.partially_update_sample_by_id(request={
        "request_body": [
            {
                "op": models.Op.REPLACE,
                "path": "/name",
                "value": "New name",
            },
        ],
        "matrix_id": "<id>",
        "sample_id": "<id>",
        "test_form_id": "<id>",
        "test_phase_id": "<id>",
    })

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="partiallyUpdateSampleById" method="patch" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.partially_update_sample_by_id(request={
        "request_body": [
            {
                "op": models.Op.REPLACE,
                "path": "/dataValues/0/value",
                "value": "22.5",
            },
        ],
        "matrix_id": "<id>",
        "sample_id": "<id>",
        "test_form_id": "<id>",
        "test_phase_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.PartiallyUpdateSampleByIDRequest](../../models/partiallyupdatesamplebyidrequest.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.MatrixSample](../../models/matrixsample.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## sample_attachment_download_by_id

Asynchronously downloads an attachment from a [sample](ref:testforms#matrixsample).

Responses include a `Location` header, which indicates where to poll for download results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the download is ready, its status will be `completed`, and the response body includes a `resourceURL`. To download the file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the download request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="sampleAttachmentDownloadById" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachments/{attachmentId}/download" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.sample_attachment_download_by_id(request={
        "attachment_id": "<id>",
        "matrix_id": "<id>",
        "sample_id": "<id>",
        "test_form_id": "<id>",
        "test_phase_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.SampleAttachmentDownloadByIDRequest](../../models/sampleattachmentdownloadbyidrequest.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.SampleAttachmentDownloadByIDResponse](../../models/sampleattachmentdownloadbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## sample_attachment_export_by_id

Asynchronously exports an attachment for a [sample](ref:testforms#matrixsample) to .PDF.

Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="sampleAttachmentExportById" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachments/{attachmentId}/export" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.sample_attachment_export_by_id(request={
        "graph_attachment_export": {
            "format_": models.GraphAttachmentExportFormat.PDF,
        },
        "attachment_id": "<id>",
        "matrix_id": "<id>",
        "sample_id": "<id>",
        "test_form_id": "<id>",
        "test_phase_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.SampleAttachmentExportByIDRequest](../../models/sampleattachmentexportbyidrequest.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.SampleAttachmentExportByIDResponse](../../models/sampleattachmentexportbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## sample_attachment_upload

Starts the process to upload and attach a file to a [sample](ref:testforms#matrixsample) using a [graph attachment upload](ref:testforms#graphattachmentupload) object. The response body will include an `uploadUrl`. To upload the file contents, perform a PUT on the `uploadUrl` with the same authentication credentials and flow as the attachmentUpload request. For more details, see [Authentication documentation](ref:authentication).

The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).


### Example Usage

<!-- UsageSnippet language="python" operationID="sampleAttachmentUpload" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachmentUpload" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.sample_attachment_upload(request={
        "graph_attachment_upload": {
            "file_name": "signature.jpg",
        },
        "matrix_id": "<id>",
        "sample_id": "<id>",
        "test_form_id": "<id>",
        "test_phase_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.SampleAttachmentUploadRequest](../../models/sampleattachmentuploadrequest.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.SampleAttachmentUploadResponse](../../models/sampleattachmentuploadresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## sample_insertion

Inserts multiple [samples](ref:testforms#matrixsamples) into a [matrix](ref:testforms#matrix), and appends new samples to the end of the matrix. You can leave columns empty for later use. For new samples, provide no IDs; the endpoint generates them.

### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="sampleInsertion" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/insertion" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.sample_insertion(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", request_body=[
        {
            "data_values": [
                {
                    "column": "6d870cd1-7bbe-4b14-b85d-f152913b068c",
                    "value": "23897",
                },
                {
                    "column": "6301bea4-30be-4c24-9f15-287396f41d2c",
                    "value": "385.3",
                },
            ],
            "id": "3dd42da0-3543-4e03-ac4a-2ddefebe27d6",
            "result_values": [
                {
                    "column": "674a9283-fd03-425d-bd62-0552263699e2",
                    "value": "PASS",
                },
                {
                    "column": "c7b812b4-70bb-47ed-a9bb-f56ca496c92f",
                    "value": "FAIL",
                },
            ],
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="sampleInsertion" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/insertion" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.sample_insertion(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", request_body=[
        {
            "data_values": [
                {
                    "column": "d795d7a3-e7f7-4b3f-be6a-109653b2929b",
                    "value": "123",
                },
                {
                    "column": "fbd818ec-4fd1-42ad-9112-3c80e71dc2dc",
                    "value": "101.1",
                },
            ],
            "result_values": [
                {
                    "column": "d795d7a3-e7f7-4b3f-be6a-109653b2c34d",
                    "value": "PASS",
                },
            ],
        },
        {
            "data_values": [
                {
                    "column": "d795d7a3-e7f7-4b3f-be6a-109653b2929b",
                    "value": "456",
                },
                {
                    "column": "fbd818ec-4fd1-42ad-9112-3c80e71dc2dc",
                    "value": "202.2",
                },
            ],
            "result_values": [
                {
                    "column": "d795d7a3-e7f7-4b3f-be6a-109653b2c34d",
                    "value": "FAIL",
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `matrix_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the matrix                                 |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `request_body`                                                      | List[[models.MatrixSampleInput](../../models/matrixsampleinput.md)] | :heavy_check_mark:                                                  | Details about the samples to insert                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SampleInsertionResponse](../../models/sampleinsertionresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## sample_update

Updates multiple [samples](ref:testforms#matrixsamples), with the requestBody of each specifying columns to update by their IDs. Columns not included in the request remain as-is.

### Example Usage: BadRequest

<!-- UsageSnippet language="python" operationID="sampleUpdate" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/update" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.sample_update(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", request_body=[
        {
            "data_values": [
                {
                    "column": "6d870cd1-7bbe-4b14-b85d-f152913b068c",
                    "value": "23897",
                },
                {
                    "column": "6301bea4-30be-4c24-9f15-287396f41d2c",
                    "value": "385.3",
                },
            ],
            "id": "3dd42da0-3543-4e03-ac4a-2ddefebe27d6",
            "result_values": [
                {
                    "column": "674a9283-fd03-425d-bd62-0552263699e2",
                    "value": "PASS",
                },
                {
                    "column": "c7b812b4-70bb-47ed-a9bb-f56ca496c92f",
                    "value": "FAIL",
                },
            ],
        },
    ])

    # Handle response
    print(res)

```
### Example Usage: body

<!-- UsageSnippet language="python" operationID="sampleUpdate" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/update" example="body" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.sample_update(matrix_id="<id>", test_form_id="<id>", test_phase_id="<id>", request_body=[
        {
            "data_values": [
                {
                    "column": "6d870cd1-7bbe-4b14-b85d-f152913b068c",
                    "value": "23897",
                },
            ],
            "id": "3dd42da0-3543-4e03-ac4a-2ddefebe27d6",
            "result_values": [
                {
                    "column": "674a9283-fd03-425d-bd62-0552263699e2",
                    "value": "PASS",
                },
            ],
        },
        {
            "data_values": [
                {
                    "column": "6d870cd1-7bbe-4b14-b85d-f152913b068c",
                    "value": "9125",
                },
            ],
            "id": "4ee53eb1-3543-4e03-ac4a-3eef0fcf38e7",
            "result_values": [
                {
                    "column": "674a9283-fd03-425d-bd62-0552263699e2",
                    "value": "FAIL",
                },
            ],
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `matrix_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the matrix                                 |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `request_body`                                                      | List[[models.MatrixSampleInput](../../models/matrixsampleinput.md)] | :heavy_check_mark:                                                  | Details about the samples to update                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SampleUpdateResponse](../../models/sampleupdateresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## test_form_export

Asynchronously exports a [test form](ref:testforms#testform).

Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="testFormExport" method="post" path="/testForms/{testFormId}/export" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.test_form_export(test_form_id="<id>", test_form_export={
        "format_": models.TestFormExportFormat.XLSX,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |                                                                     |
| `test_form_export`                                                  | [models.TestFormExport](../../models/testformexport.md)             | :heavy_check_mark:                                                  | Details about the test form export                                  | {<br/>"format": "xlsx"<br/>}                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TestFormExportResponse](../../models/testformexportresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## test_phase_attachment_download_by_id

Asynchronously downloads an attachment from a [test phase](ref:testforms#testphase).

Responses include a `Location` header, which indicates where to poll for download results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the download is ready, its status will be `completed`, and the response body includes a `resourceURL`. To download the file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the download request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="testPhaseAttachmentDownloadById" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/attachments/{attachmentId}/download" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.test_phase_attachment_download_by_id(attachment_id="<id>", test_form_id="<id>", test_phase_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attachment_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the attachment                             |
| `test_form_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test form                              |
| `test_phase_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the test phase                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TestPhaseAttachmentDownloadByIDResponse](../../models/testphaseattachmentdownloadbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## test_phase_attachment_export_by_id

Asynchronously exports an attachment for a [test phase](ref:testforms#testphase) to .PDF.

Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:authentication).


### Example Usage

<!-- UsageSnippet language="python" operationID="testPhaseAttachmentExportById" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/attachments/{attachmentId}/export" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.test_phase_attachment_export_by_id(attachment_id="<id>", test_form_id="<id>", test_phase_id="<id>", graph_attachment_export={
        "format_": models.GraphAttachmentExportFormat.PDF,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `attachment_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the attachment                               |                                                                       |
| `test_form_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the test form                                |                                                                       |
| `test_phase_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the test phase                               |                                                                       |
| `graph_attachment_export`                                             | [models.GraphAttachmentExport](../../models/graphattachmentexport.md) | :heavy_check_mark:                                                    | Details about the attachment export                                   | {<br/>"format": "pdf"<br/>}                                           |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.TestPhaseAttachmentExportByIDResponse](../../models/testphaseattachmentexportbyidresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## test_phase_attachment_upload

Starts the process to upload and attach a file to a [test phase](ref:testforms#testphase) using a [graph attachment upload](ref:testforms#graphattachmentupload) object. The response body will include an `uploadUrl`. To upload the file contents, perform a PUT on the `uploadUrl` with the same authentication credentials and flow as the attachmentUpload request. For more details, see [Authentication documentation](ref:authentication).

The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:getoperationbyid).

### Example Usage

<!-- UsageSnippet language="python" operationID="testPhaseAttachmentUpload" method="post" path="/testForms/{testFormId}/testPhases/{testPhaseId}/attachmentUpload" example="BadRequest" -->
```python
from workiva import SDK, models


with SDK(
    security=models.Security(
        client_id="<YOUR_CLIENT_ID_HERE>",
        client_secret="<YOUR_CLIENT_SECRET_HERE>",
    ),
) as sdk:

    res = sdk.test_forms.test_phase_attachment_upload(test_form_id="<id>", test_phase_id="<id>", graph_attachment_upload={
        "file_name": "signature.jpg",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `test_form_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the test form                                |                                                                       |
| `test_phase_id`                                                       | *str*                                                                 | :heavy_check_mark:                                                    | The unique identifier of the test phase                               |                                                                       |
| `graph_attachment_upload`                                             | [models.GraphAttachmentUpload](../../models/graphattachmentupload.md) | :heavy_check_mark:                                                    | Details about the attachment                                          | {<br/>"fileName": "signature.jpg"<br/>}                               |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.TestPhaseAttachmentUploadResponse](../../models/testphaseattachmentuploadresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorResponse         | 400, 401, 403, 404, 409, 429 | application/json             |
| errors.ErrorResponse         | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |