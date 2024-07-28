import numpy as np


def create_train_data():

    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    prior_probability[0] = len(train_data[train_data[:, 4] == 'no'])/len(train_data[:, 4])
    prior_probability[1] = len(train_data[train_data[:, 4] == 'yes'])/len(train_data[:, 4])
    #print('prior_probability',prior_probability)
    return prior_probability


def compute_conditional_probability(train_data): # P(X1|C1)
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1] - 1):
        column_unique = np.unique(train_data[:, i])
        # print('column_unique', column_unique)
        list_x_name.append(column_unique)
        column_conditional_probability = []
        for item in column_unique:
            p_sunny_given_yes = len(train_data[((train_data[:, i] == item) & (train_data[:, 4] == 'yes'))])/len(train_data[train_data[:, 4] == 'yes'])
            p_sunny_given_no = len(train_data[((train_data[:, i] == item) & (train_data[:, 4] == 'no'))])/len(train_data[train_data[:, 4] == 'no'])
            column_conditional_probability.append([p_sunny_given_no, p_sunny_given_yes])

        conditional_probability.append(column_conditional_probability)

    print('conditional_probability', conditional_probability)
    print('conditional_probability[0]', conditional_probability[0])
    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    ''' This function is used to return the index of the feature name'''
    return np.where(list_features == feature_name)[0][0]


train_data = create_train_data()
print(train_data)

# Q14:
prior_probablity = compute_prior_probablity(train_data)
print("P(play tennis = No)", prior_probablity[0])
print("P(play tennis = Yes)", prior_probablity[1])

# Q15:
_, list_x_name = compute_conditional_probability(train_data)

print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])


# Q16:
outlook = list_x_name[0]

i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)

print(i1, i2, i3)

# Q17:
conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
# Compute P(" Outlook "=" Sunny "| Play Tennis "=" Yes ")
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'= 'Sunny'| Play Tennis = 'Yes') = ",
      np.round(conditional_probability[0][x1][1], 2))


# Q18:
conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
# Compute P(" Outlook "=" Sunny "| Play Tennis "=" No ")
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'= 'Sunny'| Play Tennis = 'No') = ",
      np.round(conditional_probability[0][x1][0], 2))
