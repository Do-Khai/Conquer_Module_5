import numpy as np
from sklearn.model_selection import train_test_split

def load_and_prepare_data(path):
    data = np.genfromtxt(path, delimiter=',', skip_header=1)
    X = data[:, :3]
    y = data[:, 3:]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Tìm x min và x max để dùng MinMaxScaling
    X_min = X_train.min(axis=0)
    X_max = X_train.max(axis=0)

    #Min max scaling 
    X_train_scaled = (X_train - X_min) / (X_max - X_min)
    X_test_scaled = (X_test - X_min) / (X_max - X_min)

    X_train_b = np.hstack((np.ones((X_train_scaled.shape[0], 1)), X_train_scaled))
    X_test_b = np.hstack((np.ones((X_test_scaled.shape[0], 1)), X_test_scaled))

    np.save('data/x_train_v1.npy', X_train_b)
    np.save('data/x_test_v1.npy', X_test_b)
    np.save('data/y_train_v1.npy', y_train)
    np.save('data/y_test_v1.npy', y_test)

if __name__ == "__main__":
    load_and_prepare_data("data/advertising.csv")