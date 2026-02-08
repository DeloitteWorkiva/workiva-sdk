# CurrencySymbol

The currency symbol to display. Valid for ACCOUNTING and CURRENCY. Either generic or currency should be set, but not both.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `currency`                                                 | [OptionalNullable[models.Currency]](../models/currency.md) | :heavy_minus_sign:                                         | An ISO currency format                                     |
| `generic`                                                  | [OptionalNullable[models.Generic]](../models/generic.md)   | :heavy_minus_sign:                                         | Generic currency options                                   |