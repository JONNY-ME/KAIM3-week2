import pandas as pd


def aggregate_user_metrics(data, group_col, metrics):
    """
    Generalized function to aggregate user metrics.

    Parameters:
        data (pd.DataFrame): The input dataset.
        group_col (str): The column to group by (e.g., 'MSISDN/Number').
        metrics (dict): Dictionary where keys are the new column names 
                        and values are the columns to aggregate.
                        For sums, use a single column; for totals, pass a tuple.

    Returns:
        pd.DataFrame: Aggregated metrics per user.
    """
    agg_dict = {}
    agg_dict[group_col] = data[group_col].nunique()
    for metric_name, cols in metrics.items():
        if metric_name == "xDR_sessions":
            # Count unique session identifiers
            agg_dict[metric_name] = data.groupby(group_col)[cols].nunique()
        elif isinstance(cols, tuple):
            dl_col, ul_col = cols
            agg_dict[metric_name] = data.groupby(group_col)[[dl_col, ul_col]].sum().sum(axis=1)
        else:
            agg_dict[metric_name] = data.groupby(group_col)[cols].sum()

    # Combine all metrics into a DataFrame
    aggregated_data = pd.DataFrame(agg_dict)
    aggregated_data[group_col] = aggregated_data.index

    return aggregated_data.reset_index(drop=True)