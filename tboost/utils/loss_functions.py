import numpy as np


def loss_from_leaves(y_leaf, y_true, loss_func):
    """Calculate the gradients and hessian of the logloss functions

    Args:
        y_leaf (np.array or pd.Series): output of the leaves of the tre
        y_true (np.array or pd.Series): [description]
        loss_func ([type], optional): [description]. Defaults to logloss.

    Returns:
        [type]: [description]
    """
    # Apply the sigmoid transformation to the leaf values (transfrom it to probability)
    prob = _sigmoid(y_leaf)

    return loss_func(prob, y_true)


def logloss(y_pred, y_true):
    """Return the gradient and hessian of the log loss.

    Args:
        y_pred (np.array or pd.Series): predictions for the observations, in the range [0,1]
        y_true (np.array or pd.Series): true label for the observations

    Returns:
        tuple: (np.array, np.array), gradient and hessian for the observations
    """
    #     prob = 1.0 / (1.0 + np.exp(-y_pred))

    if isinstance(y_pred, pd.Series):
        y_pred = y_pred.values
    if isinstance(y_true, pd.Series):
        y_true = y_true.values
    grad = y_true - y_pred
    hess = y_pred * (1.0 - y_pred)
    return grad, hess


def _sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))