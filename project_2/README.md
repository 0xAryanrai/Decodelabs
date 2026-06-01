
# 🌸 Iris Flower Classification using K-Nearest Neighbors (KNN)

A machine learning project that classifies Iris flowers into three species using the K-Nearest Neighbors algorithm, achieving a final accuracy of **96.67%**.

---

## 📌 Objective

Classify Iris flowers into one of three species based on sepal and petal measurements:

- *Iris Setosa*
- *Iris Versicolor*
- *Iris Virginica*

---

## 📁 Project Structure

```
├── Data_classification.ipynb   # Main Jupyter Notebook
├── iris.csv                    # Dataset
└── README.md
```

---

## 🧰 Technologies Used

| Library | Purpose |
|---|---|
| `numpy` | Numerical computations |
| `pandas` | Data loading and manipulation |
| `matplotlib` | Data visualization |
| `seaborn` | Statistical plots |
| `scikit-learn` | ML model, preprocessing, and evaluation |

---

## 📊 Dataset

- **Source:** Iris dataset (`iris.csv`)
- **Samples:** 150 flower instances
- **Features:** Sepal length, sepal width, petal length, petal width
- **Target:** Species (Setosa, Versicolor, Virginica)

---

## 🔍 Workflow

1. **Exploratory Data Analysis (EDA)**
   - Pairplots to visualize class separation
   - Correlation heatmap
   - Feature histograms
   - Null value check

2. **Preprocessing**
   - Label encoding of target species
   - 80/20 train-test split with stratification
   - Feature scaling using `StandardScaler` (required for distance-based KNN)

3. **Model Training**
   - Initial model trained with `K=3`
   - K value tuned by testing K from 1 to 20 and comparing accuracy

4. **Evaluation**
   - Accuracy score
   - Confusion matrix
   - Full classification report (precision, recall, F1-score)

---

## 📈 Results

| Metric | Value |
|---|---|
| Best K | 1 |
| Final Accuracy | **96.67%** |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### Run the Notebook

```bash
jupyter notebook Data_classification.ipynb
```

---

## 🧠 Key Takeaways

- Feature scaling is essential for KNN since the algorithm relies on Euclidean distance.
- Iterating over multiple K values helps find the optimal hyperparameter.
- The Iris dataset is well-separated, allowing KNN to achieve high accuracy even at low K values.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
