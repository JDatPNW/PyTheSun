import numpy as np

train_data = np.load('training_data.npy')
train_data_2 = np.load('training_data_2.npy')

print(train_data)
print(train_data_2)

final_data = np.concatenate((train_data, train_data_2))

print(final_data)

np.save('training_data_combined.npy', final_data)
