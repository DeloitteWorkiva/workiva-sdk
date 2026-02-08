# NumbersAsWordsOptions

Options relevant when showing numbers as words. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT. In order for these options to
take effect showNumbersAsWords must be set to true.



## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `capitalize_first_word`                                                                    | *OptionalNullable[bool]*                                                                   | :heavy_minus_sign:                                                                         | Capitalize the first word. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.            |
| `display_zero_as`                                                                          | [OptionalNullable[models.ValueFormatDisplayZeroAs]](../models/valueformatdisplayzeroas.md) | :heavy_minus_sign:                                                                         | The word to use for zero. Valid for ACCOUNTING, CURRENCY, NUMBER, and PERCENT.             |