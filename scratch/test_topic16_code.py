"""
Topic 16: Clustering - Mathematical & Code Verification Harness
Validates all formulas, distances, K-Means inertia, silhouette scores,
hierarchical linkage, and DBSCAN executions with scikit-learn and SciPy.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs, make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score, adjusted_rand_score
from scipy.cluster.hierarchy import linkage, dendrogram

print("=" * 70)
print("TOPIC 16: CLUSTERING - MATHEMATICAL & PIPELINE VERIFICATION")
print("=" * 70)

# -------------------------------------------------------------
# 1. Distance Metric Verification
# -------------------------------------------------------------
print("\n--- 1. Distance Metric Verification ---")
# Two customer profiles: Customer A (Income: $40k, Frequency: 12)
# Customer B (Income: $70k, Frequency: 4)
# Let normalized features be: x = [4.0, 12.0], y = [7.0, 4.0]
x = np.array([4.0, 12.0])
y = np.array([7.0, 4.0])

diff = x - y  # [-3.0, 8.0]
euclidean_dist = np.sqrt(np.sum(diff ** 2))  # sqrt(9 + 64) = sqrt(73) ≈ 8.5440
manhattan_dist = np.sum(np.abs(diff))        # 3 + 8 = 11.0000

print(f"Point X: {x}, Point Y: {y}")
print(f"Euclidean Distance: sqrt((-3)^2 + 8^2) = sqrt(73) = {euclidean_dist:.4f}")
print(f"Manhattan Distance: |-3| + |8| = {manhattan_dist:.4f}")
assert np.isclose(euclidean_dist, np.sqrt(73)), "Euclidean distance math error!"
assert np.isclose(manhattan_dist, 11.0), "Manhattan distance math error!"

# -------------------------------------------------------------
# 2. Feature Scaling (Standardization) Verification
# -------------------------------------------------------------
print("\n--- 2. Standardization Verification ---")
raw_feature = np.array([20.0, 40.0, 60.0, 80.0, 100.0])
mu = np.mean(raw_feature)  # 60.0
sigma = np.std(raw_feature)  # sqrt(800) = 28.28427
z_manual = (raw_feature - mu) / sigma

scaler = StandardScaler()
z_sklearn = scaler.fit_transform(raw_feature.reshape(-1, 1)).flatten()

print(f"Raw: {raw_feature}")
print(f"Mean (mu): {mu:.2f}, Std Dev (sigma): {sigma:.4f}")
print(f"Manual Z-scores:  {np.round(z_manual, 4)}")
print(f"Sklearn Z-scores: {np.round(z_sklearn, 4)}")
assert np.allclose(z_manual, z_sklearn), "StandardScaler verification failed!"

# -------------------------------------------------------------
# 3. K-Means Inertia & Objective Verification
# -------------------------------------------------------------
print("\n--- 3. K-Means Small Dataset Manual Inertia Check ---")
# 4 points, 2 clusters:
# C1: [1, 1], [1, 3] -> centroid mu1 = [1, 2]
# C2: [5, 5], [5, 7] -> centroid mu2 = [5, 6]
pts = np.array([[1.0, 1.0], [1.0, 3.0], [5.0, 5.0], [5.0, 7.0]])
mu1 = np.array([1.0, 2.0])
mu2 = np.array([5.0, 6.0])

# Within cluster 1 sum of squared distances:
# ||[1, 1] - [1, 2]||^2 = 0^2 + (-1)^2 = 1.0
# ||[1, 3] - [1, 2]||^2 = 0^2 + 1^2 = 1.0 -> Sum C1 = 2.0
# Within cluster 2:
# ||[5, 5] - [5, 6]||^2 = 1.0
# ||[5, 7] - [5, 6]||^2 = 1.0 -> Sum C2 = 2.0
manual_inertia = 2.0 + 2.0  # 4.0

km_small = KMeans(n_clusters=2, init=np.array([mu1, mu2]), n_init=1, random_state=42)
km_small.fit(pts)
print(f"Manual Inertia:  {manual_inertia:.4f}")
print(f"Sklearn Inertia: {km_small.inertia_:.4f}")
assert np.isclose(km_small.inertia_, manual_inertia), "K-Means inertia verification failed!"

# -------------------------------------------------------------
# 4. End-to-End K-Means Pipeline & Elbow / Silhouette Benchmark
# -------------------------------------------------------------
print("\n--- 4. End-to-End K-Means Benchmark ---")
# Create synthetic blobs: 300 samples, 2 features, 3 true centers, fixed seed 42
X_blobs, y_true_blobs = make_blobs(
    n_samples=300,
    centers=[[-3, -2], [2, 3], [4, -3]],
    cluster_std=0.85,
    random_state=42
)

# Scale data
scaler_blobs = StandardScaler()
X_blobs_scaled = scaler_blobs.fit_transform(X_blobs)

inertia_dict = {}
silhouette_dict = {}
davies_bouldin_dict = {}
calinski_harabasz_dict = {}

for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_blobs_scaled)
    inertia_dict[k] = km.inertia_
    silhouette_dict[k] = silhouette_score(X_blobs_scaled, labels)
    davies_bouldin_dict[k] = davies_bouldin_score(X_blobs_scaled, labels)
    calinski_harabasz_dict[k] = calinski_harabasz_score(X_blobs_scaled, labels)
    print(f"K={k}: Inertia={km.inertia_:.2f} | Silhouette={silhouette_dict[k]:.4f} | "
          f"Davies-Bouldin={davies_bouldin_dict[k]:.4f} | Calinski-Harabasz={calinski_harabasz_dict[k]:.2f}")

# Verify K=3 is the clear winner for Silhouette and Calinski-Harabasz
best_k_sil = max(silhouette_dict, key=silhouette_dict.get)
print(f"\nOptimal K by Silhouette Score: {best_k_sil} (Score: {silhouette_dict[best_k_sil]:.4f})")
assert best_k_sil == 3, "Optimal K should be 3 for this dataset!"

# Final K=3 model
km_final = KMeans(n_clusters=3, random_state=42, n_init=10)
km_final.fit(X_blobs_scaled)
print(f"K=3 Centroids (Scaled space):\n{km_final.cluster_centers_}")
print(f"Adjusted Rand Index (ARI vs ground truth): {adjusted_rand_score(y_true_blobs, km_final.labels_):.4f}")

# -------------------------------------------------------------
# 5. Hierarchical / Agglomerative Clustering Verification
# -------------------------------------------------------------
print("\n--- 5. Hierarchical Clustering Verification ---")
# Fit Agglomerative with Ward linkage
agg_ward = AgglomerativeClustering(n_clusters=3, linkage='ward')
agg_labels = agg_ward.fit_predict(X_blobs_scaled)
agg_sil = silhouette_score(X_blobs_scaled, agg_labels)
print(f"Agglomerative (Ward, K=3) Silhouette Score: {agg_sil:.4f}")
print(f"Agglomerative ARI vs ground truth: {adjusted_rand_score(y_true_blobs, agg_labels):.4f}")

# Test SciPy linkage matrix
Z = linkage(X_blobs_scaled[:15], method='ward')
print(f"SciPy Linkage Matrix Shape for 15 samples: {Z.shape} (Must be (14, 4))")
assert Z.shape == (14, 4), "Linkage matrix shape mismatch!"

# -------------------------------------------------------------
# 6. DBSCAN Verification (Nonlinear Density Clustering)
# -------------------------------------------------------------
print("\n--- 6. DBSCAN Verification ---")
# Create non-convex two moons dataset + Gaussian noise points
np.random.seed(42)
X_moons, y_true_moons = make_moons(n_samples=260, noise=0.08, random_state=42)
noise_points = np.random.uniform(low=-1.5, high=2.5, size=(20, 2))
X_dbscan_raw = np.vstack([X_moons, noise_points])

scaler_db = StandardScaler()
X_dbscan = scaler_db.fit_transform(X_dbscan_raw)

# Fit DBSCAN
dbscan = DBSCAN(eps=0.28, min_samples=6)
db_labels = dbscan.fit_predict(X_dbscan)

unique_labels = set(db_labels)
n_clusters_db = len(unique_labels - {-1})
n_noise_db = list(db_labels).count(-1)

print(f"DBSCAN Unique Labels: {sorted(list(unique_labels))}")
print(f"Discovered Clusters (excluding noise): {n_clusters_db}")
print(f"Identified Noise Points: {n_noise_db} out of {len(X_dbscan)} ({n_noise_db/len(X_dbscan)*100:.1f}%)")

# Compare with K-Means on the same non-convex moons
km_moons = KMeans(n_clusters=2, random_state=42, n_init=10)
km_moons_labels = km_moons.fit_predict(X_dbscan[:260])

ari_dbscan = adjusted_rand_score(y_true_moons, db_labels[:260])
ari_kmeans = adjusted_rand_score(y_true_moons, km_moons_labels)

print(f"Moons ARI - DBSCAN:  {ari_dbscan:.4f} (Understands non-convex geometry)")
print(f"Moons ARI - K-Means: {ari_kmeans:.4f} (Struggles with non-convex geometry)")
assert ari_dbscan > 0.90, "DBSCAN should achieve > 0.90 ARI on moons!"
assert ari_kmeans < 0.60, "K-Means should fail on crescent moons!"

print("\nALL PYTHON & MATHEMATICAL VERIFICATIONS PASSED 100%!")
