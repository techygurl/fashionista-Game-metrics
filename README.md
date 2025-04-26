# Fashionista Game Metrics Dashboard 🎮👗

Welcome to the **Fashionista Game Metrics Dashboard**!  
This interactive Streamlit app analyzes key game metrics like churn rate, return rate, user acquisition cost (UAC), and conversion rates based on real player event data.

![Fashionista Banner](Leonardo_Kino_XL_create_am_image_for_a_dress_up_game_for_girls_2.jpg)

---

## 📊 Features

- **Data Preview**: Quickly view the uploaded data table.
- **Churn Analysis**: Compare 7-day vs 30-day churn rates.
- **Return Rate After Churn**: See how many users returned after churning.
- **Conversion Metrics**: Visualize conversion rates among players.
- **User Acquisition Cost (UAC)**: Monthly UAC calculation and visualization.
- **Quarterly UAC Filter**: Select and focus on quarterly UAC trends.

---

## 📂 Project Structure

```bash
fashionista-Game-metrics/
│
├── fashionista_metrics.py           # Main Streamlit app
├── fashionista data.csv              # Dataset (CSV format)
├── Leonardo_Kino_XL_create...jpg     # Dashboard header image
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fashionista-Game-metrics.git
cd fashionista-Game-metrics
```

### 2. Install dependencies

Make sure you have Python 3.8+ installed. Then run:

```bash
pip install -r requirements.txt
```

### 3. Launch the app

```bash
streamlit run fashionista_metrics.py
```

The app will open in your browser at `http://localhost:8501`.

---

## ⚙️ Requirements

The app depends on the following Python packages:

```
streamlit
pandas
Pillow
plotly
```

(Already listed in `requirements.txt`)

---

## 📈 Metrics Calculated

- **7-Day and 30-Day Churn Rates**
- **Return Rate after Churn**
- **User Conversion Rate**
- **Monthly and Quarterly User Acquisition Costs (UAC)**

Each metric is visualized using clean, modern Plotly charts embedded inside the Streamlit dashboard.

---

## 🛠️ Customization

- **Data Source**: Replace `fashionista data.csv` with your own data if needed.
- **Marketing Spend**: Adjust the hardcoded `$3000` marketing spend inside the script to match your real campaigns.
- **Date Ranges**: Modify the filtering dates for other months or years.

---

## 📸 Screenshots

_Example screenshots can be added here once the app is running._  
You can use Streamlit's `st.screenshot()` or your operating system to capture them.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) 

---

## ✨ Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [Pandas](https://pandas.pydata.org/)
- [Pillow](https://python-pillow.org/)
