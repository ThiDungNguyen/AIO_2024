
# ##########################
# Train Naive Bayes Model
# ##########################
from conditional_probability import compute_prior_probablity, create_train_data, get_index_from_value, compute_conditional_probability


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name

# ###################
# Prediction
# ###################


def prediction_play_tennis(x, list_x_name, prior_probability, conditional_probability):

    x1 = get_index_from_value(x[0], list_x_name[0])
    x2 = get_index_from_value(x[1], list_x_name[1])
    x3 = get_index_from_value(x[2], list_x_name[2])
    x4 = get_index_from_value(x[3], list_x_name[3])
    print("x1 = ", x1)
    print("x2 = ", x2)
    print("x3 = ", x3)
    print("x4 = ", x4)

    p0 = prior_probability[0] \
        * conditional_probability[0][x1][0]\
        * conditional_probability[0][x2][0]\
        * conditional_probability[0][x3][0]\
        * conditional_probability[0][x4][0]
    p1 = prior_probability[1] \
        * conditional_probability[1][x1][1]\
        * conditional_probability[1][x2][1]\
        * conditional_probability[1][x3][1]\
        * conditional_probability[1][x3][1]

    # your code here ***********************

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    data)
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)

if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
