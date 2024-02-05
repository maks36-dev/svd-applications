import numpy as np
import matplotlib.pyplot as plt

def generate_graph(n):
    adj = np.random.rand(n, n)
    adj[adj > 0.5] = 1
    adj[adj <= 0.5] = 0
    return adj

def plot_graph(pl, graph, points):
    pl.scatter(points[:, 0], points[:, 1])
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i,j]:
                pl.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]])
    pl.plot()

def kabsch_algorithm(molecule_a, molecule_b):
    # Вычисление центра масс каждой молекулы
    center_of_mass_a = np.mean(molecule_a, axis=0)
    center_of_mass_b = np.mean(molecule_b, axis=0)

    # Вычитание центра масс
    centered_molecule_a = molecule_a - center_of_mass_a
    centered_molecule_b = molecule_b - center_of_mass_b

    # Вычисление матрицы ковариации
    covariance_matrix = np.dot(centered_molecule_a.T, centered_molecule_b)

    # SVD разложение матрицы ковариации
    U, S, Vt = np.linalg.svd(covariance_matrix)

    # Определение оптимальной ориентации молекулы A относительно молекулы B
    rotation_matrix = np.dot(U, Vt)

    aligned_molecule_a = np.dot(centered_molecule_a, rotation_matrix) + center_of_mass_b

    return aligned_molecule_a

def main():
    A = np.array([
        [1, 0, 0],
        [0, 0, 0],
        [0, 1, 0]
    ])
    B = np.array([
        [-5, 0, 0],
        [-4, 0, 0],
        [-4, 1, 0]
    ])

    H = kabsch_algorithm(A, B)
    plt.plot(A[:, 0], A[:, 1], linewidth=2, c='b', label="1-ая молекула")
    plt.plot(B[:, 0], B[:, 1], linewidth=2, c='r', label="2-ая молекула")
    plt.plot(H[:, 0], H[:, 1], linewidth=2, linestyle=':', marker='o', c='g', label="Результат вращения")

    plt.legend()

    plt.xlabel('X-ось')
    plt.ylabel('Y-ось')
    plt.title('Алгоритм Кабша')
    plt.savefig("kabsch.jpg")


if __name__ == "__main__":
    generate_graph(5)