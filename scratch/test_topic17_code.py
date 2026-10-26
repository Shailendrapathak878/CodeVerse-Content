"""Numerical verification and benchmark experiments for Topic 17: Dimensionality Reduction.
Tests:
1. Small 2D numerical PCA calculation (means, centered values, covariance matrix, eigenvalues, eigenvectors, projection).
2. Breast Cancer / Wine dataset PCA explained variance and cumulative variance curve.
3. 2D and 3D PCA projection coordinates.
4. Model performance comparison: Baseline Classifier vs PCA + Classifier pipeline (proving PCA is not always a magic bullet!).
5. 2D t-SNE projection on the dataset.
6. Linear Discriminant Analysis (LDA) 2D projection vs PCA 2D projection.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_wine, load_breast_cancer, load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score

def test_numerical_pca():
    print("=== 1. Small 2D Numerical PCA Calculation ===")
    # 5 samples, 2 features: Study Hours (x1) and Exam Score (x2)
    # Designed with positive correlation
    X = np.array([
        [2.0, 4.0],
        [4.0, 6.0],
        [6.0, 7.0],
        [8.0, 9.0],
        [10.0, 14.0]
    ])
    n = X.shape[0]
    
    # Means
    mu = np.mean(X, axis=0)
    print(f"Feature Means: mu_1 = {mu[0]:.2f}, mu_2 = {mu[1]:.2f}")
    assert np.allclose(mu, [6.0, 8.0])
    
    # Centered data
    X_cent = X - mu
    print("\nCentered Data Matrix X_centered:")
    print(X_cent)
    
    # Covariance matrix (sample covariance with ddof=1)
    cov_matrix = np.cov(X_cent, rowvar=False)
    print("\nCovariance Matrix (sample cov, ddof=1):")
    print(cov_matrix)
    
    # Eigen decomposition of covariance matrix
    # Note: np.linalg.eigh is symmetric/Hermitian, returns eigenvalues in ascending order
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    # Sort descending
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    print("\nEigenvalues (descending):", eigenvalues)
    print("Eigenvectors (principal directions as columns):")
    print(eigenvectors)
    
    total_var = np.sum(eigenvalues)
    exp_var_ratio = eigenvalues / total_var
    print(f"\nExplained Variance Ratio: PC1 = {exp_var_ratio[0]*100:.2f}%, PC2 = {exp_var_ratio[1]*100:.2f}%")
    
    # Projection onto PC1 and PC2: Z = X_cent @ W
    Z_manual = X_cent @ eigenvectors
    print("\nTransformed 2D Coordinates (Z = X_centered @ W):")
    print(Z_manual)
    
    # Compare with sklearn PCA
    pca_sk = PCA(n_components=2)
    Z_sk = pca_sk.fit_transform(X)
    print("\nscikit-learn PCA Explained Variance Ratio:", pca_sk.explained_variance_ratio_)
    print("scikit-learn Singular Values / Variances:", pca_sk.explained_variance_)
    
    # Check explained variance ratios match
    assert np.allclose(exp_var_ratio, pca_sk.explained_variance_ratio_), "Variance ratio mismatch"
    # Check absolute values of projections match (scikit-learn and eigh might flip sign of eigenvectors)
    assert np.allclose(np.abs(Z_manual), np.abs(Z_sk)), "Projection coordinates mismatch"
    print("\nPASS: Manual 2D PCA calculation matches scikit-learn!")

def test_wine_pca():
    print("\n=== 2. Wine Dataset PCA (13 Features -> 2D & 3D & Scree Plot) ===")
    wine = load_wine()
    X, y = wine.data, wine.target
    print(f"Wine Dataset Shape: {X.shape} (13 features, 3 classes, 178 samples)")
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    pca_full = PCA().fit(X_scaled)
    evr = pca_full.explained_variance_ratio_
    cum_evr = np.cumsum(evr)
    
    print("\nExplained Variance Ratio by Component (13 components):")
    for i, (r, c) in enumerate(zip(evr, cum_evr)):
        print(f"  PC{i+1:02d}: Individual = {r*100:5.2f}% | Cumulative = {c*100:6.2f}%")
        
    n_95 = np.argmax(cum_evr >= 0.95) + 1
    n_90 = np.argmax(cum_evr >= 0.90) + 1
    print(f"\nComponents needed for >= 90% variance: {n_90} components ({cum_evr[n_90-1]*100:.2f}%)")
    print(f"Components needed for >= 95% variance: {n_95} components ({cum_evr[n_95-1]*100:.2f}%)")
    
    # Fit 2D PCA
    pca_2d = PCA(n_components=2, random_state=42)
    X_pca2 = pca_2d.fit_transform(X_scaled)
    var_2d = np.sum(pca_2d.explained_variance_ratio_)
    print(f"2D PCA captures {var_2d*100:.2f}% of total variance (PC1: {pca_2d.explained_variance_ratio_[0]*100:.2f}%, PC2: {pca_2d.explained_variance_ratio_[1]*100:.2f}%)")

def test_pca_vs_baseline_performance():
    print("\n=== 3. Does PCA Improve Model Performance? Empirical Experiment ===")
    wine = load_wine()
    X, y = wine.data, wine.target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    
    # Baseline: StandardScaler + LogisticRegression
    pipe_baseline = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(random_state=42))
    ])
    pipe_baseline.fit(X_train, y_train)
    y_pred_base = pipe_baseline.predict(X_test)
    acc_base = accuracy_score(y_test, y_pred_base)
    f1_base = f1_score(y_test, y_pred_base, average='weighted')
    
    # PCA Pipeline (retaining only 2 components out of 13)
    pipe_pca2 = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=2, random_state=42)),
        ('clf', LogisticRegression(random_state=42))
    ])
    pipe_pca2.fit(X_train, y_train)
    y_pred_pca2 = pipe_pca2.predict(X_test)
    acc_pca2 = accuracy_score(y_test, y_pred_pca2)
    f1_pca2 = f1_score(y_test, y_pred_pca2, average='weighted')
    
    # PCA Pipeline (retaining 95% variance, e.g. 10 components)
    pipe_pca95 = Pipeline([
        ('scaler', StandardScaler()),
        ('pca', PCA(n_components=0.95, random_state=42)),
        ('clf', LogisticRegression(random_state=42))
    ])
    pipe_pca95.fit(X_train, y_train)
    y_pred_pca95 = pipe_pca95.predict(X_test)
    acc_pca95 = accuracy_score(y_test, y_pred_pca95)
    f1_pca95 = f1_score(y_test, y_pred_pca95, average='weighted')
    n_comp_95 = pipe_pca95.named_steps['pca'].n_components_
    
    print(f"Baseline (13 features):        Accuracy = {acc_base:.4f}, F1 = {f1_base:.4f}")
    print(f"PCA k=2 (severe reduction):    Accuracy = {acc_pca2:.4f}, F1 = {f1_pca2:.4f} (Information loss!)")
    print(f"PCA 95% variance (k={n_comp_95}):   Accuracy = {acc_pca95:.4f}, F1 = {f1_pca95:.4f}")
    
    # Also test on noisy synthetic dataset or high-dimensional dataset
    print("\nDemonstration note: Reducing to 2 features for visualization is great for plotting, but can discard discriminative information needed for maximum classification accuracy!")

def test_tsne_and_lda():
    print("\n=== 4. t-SNE & LDA Experiments ===")
    wine = load_wine()
    X, y = wine.data, wine.target
    X_scaled = StandardScaler().fit_transform(X)
    
    # t-SNE
    tsne = TSNE(n_components=2, perplexity=30, random_state=42, init='pca')
    X_tsne = tsne.fit_transform(X_scaled)
    print(f"t-SNE Output Shape: {X_tsne.shape}")
    
    # LDA (Supervised: max components = n_classes - 1 = 3 - 1 = 2)
    lda = LDA(n_components=2)
    X_lda = lda.fit_transform(X_scaled, y)
    print(f"LDA Output Shape: {X_lda.shape}")
    print(f"LDA Explained Variance Ratio: {lda.explained_variance_ratio_}")
    print(f"LDA Total Variance: {np.sum(lda.explained_variance_ratio_)*100:.2f}%")

if __name__ == '__main__':
    test_numerical_pca()
    test_wine_pca()
    test_pca_vs_baseline_performance()
    test_tsne_and_lda()
