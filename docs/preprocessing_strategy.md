# Data Cleaning Strategy

## TotalCharges

### Issue

The `TotalCharges` variable contained 11 hidden missing values represented as blank whitespace rather than standard `NaN` values.

### Resolution

The column was converted to a numeric data type using:

```python
pd.to_numeric(errors="coerce")
```

This converted blank whitespace into `NaN`.

The missing values were then replaced with **0** because the affected customers had zero months of tenure and had not accumulated any charges.

### Justification

Replacing these values with zero preserves all observations while accurately representing the underlying business process.