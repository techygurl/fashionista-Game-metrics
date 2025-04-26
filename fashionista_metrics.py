import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.graph_objects as go
print("Hello Learners")
# reading the data from excel file
df = pd.read_csv("fashionista data.csv")
st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
image = Image.open('Leonardo_Kino_XL_create_am_image_for_a_dress_up_game_for_girls_2.jpg')
col1, col2 = st.columns([0.1,0.9])
with col1:
    image = image.resize((120, 100))
st.image(image)

html_title = """
    <style>
    .title-test {
    font-weight:bold;
    padding:5px;
    border-radius:6px;
    }
    </style>
    <center><h1 class="title-test">Fashionista Game Metrics Dashboard</h1></center>"""
with col2:
    st.markdown(html_title, unsafe_allow_html=True)
df.head(5)
with st.expander("Data Preveiw"):
   st.dataframe(df)
col3, col4, col5,col6,col7, = st.columns([1.1,2.1,2.1,0.45,0.45])
with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last updated by:  \n {box_date}") 

    #looking through the data i have to convert the date and the event time stamp to a standard
df['event_date'] = pd.to_datetime(df['event_date'], format='%Y%m%d')

# print to verify
df.head(5)

# Convert 'event_timestamp' from Unix time to datetime
df['event_timestamp'] = pd.to_datetime(df['event_timestamp'], unit='s')




# we are looking to get the retention metric CHURN_RATE & RETURN_RATE of the game
# CHURN_RATE based on retention 
churn_7d = 1 - df['retained_7_days'].mean()
print(f"7-day churn rate: {churn_7d * 100:.2f}%")

churn_30d = 1 - df['retained_30_days'].mean()
print(f"30-day churn rate: {churn_30d * 100:.2f}%")


# Data for plotting
labels = ['7-Day Churn', '30-Day Churn']
churn_rates = [churn_7d * 100, churn_30d * 100]

with col4:
    # Create the Plotly figure
    fig = go.Figure(data=[
        go.Bar(
            x=labels,
            y=churn_rates,
            text=[f'{rate:.2f}%' for rate in churn_rates],  # Show value on bar
            textposition='auto',
            marker_color='black'  # Black color bars
        )
    ])

    # Customize the layout
    fig.update_layout(
        title='Churn Rates (7-day vs 30-day)',
        xaxis_title='Retention Period',
        yaxis_title='Churn Rate (%)',
        yaxis=dict(range=[0, max(churn_rates) + 10]),  # Make y-axis a bit higher
        template='plotly_white'
    )

    # Show the figure
    st.plotly_chart(fig, use_container_width=True)

    # Making sure event_date is in datetime format
df['event_date'] = pd.to_datetime(df['event_date'], format='%Y%m%d')

#  user and event date
df = df.sort_values(by=['user_id', 'event_date'])

# churned users (those with days_since_last_session > 30)
df['churned'] = df['days_since_last_session'] > 30

# Find users who ever churned & Check if those users returned
churned_users = df[df['churned']]['user_id'].unique()

returned_after_churn = df[(df['user_id'].isin(churned_users)) & (df['churned'] == False)]
returned_users = returned_after_churn['user_id'].unique()
# return rate after churn
return_rate_after_churn = len(returned_users) / len(churned_users) * 100

print(f"Return rate after churn: {return_rate_after_churn:.2f}%")



# --- Data Preparation ---
return_rate_after_churn = 100.0
no_return_rate = 100 - return_rate_after_churn

labels = ['Returned After Churn', 'Did Not Return']
values = [return_rate_after_churn, no_return_rate]

# --- Layout: Create 5 columns ---
#col1, col2, col3, col4, col5 = st.columns(5)

# --- Plot inside Column 5 ---
with col5:
    st.subheader('Return Rate After Churn (%)')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=labels,
        y=values,
        mode='lines+markers',
        line=dict(color='seagreen', width=3),
        marker=dict(size=10, color='lightpink'),
        name='Return Rate'
    ))

    fig.update_layout(
        title='',
        xaxis_title='User Status',
        yaxis_title='Percentage of Users',
        yaxis=dict(range=[0, 110]),
        template='plotly_white',
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        margin=dict(l=20, r=20, t=20, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)
# --- After your existing 6 columns and plots ---

st.divider()

# Create 3 columns (for example) and make the center one bigger
col1, col2, col3 = st.columns([1.1, 2.1, 2.1])

with col2:  # Put the plot inside the center column
    st.subheader('Conversion Rate')

    # --- Calculate Conversion Rate ---
    converters = df[df['total_purchases'] > 0]['user_id'].nunique()
    total_users = df['user_id'].nunique()
    conversion_rate = (converters / total_users) * 100

    # --- Data for Plot ---
    labels = ['Converted', 'Did Not Convert']
    values = [conversion_rate, 100 - conversion_rate]
    colors = ['black', 'seagreen']

    # --- Create Plot ---
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=labels,
        y=values,
        text=[f'{v:.1f}%' for v in values],
        textposition='auto',
        marker_color=colors
    ))

    fig.update_layout(
        title='',
        xaxis_title='',
        yaxis_title='Percentage',
        yaxis=dict(range=[0, 110]),
        template='plotly_white',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20)
    )

    # --- Show Plot ---
    st.plotly_chart(fig, use_container_width=True)

# Make sure event_date is in datetime format
df['event_date'] = pd.to_datetime(df['event_date'], format='%Y%m%d')

# MARCH
start_date = pd.to_datetime('2025-03-01')
end_date = pd.to_datetime('2025-04-01')

#  filter
new_users_df = df[(df['event_name'] == 'purchase_made') & 
                  (df['event_date'] >= start_date) & 
                  (df['event_date'] <= end_date)]

# unique new users
new_users_count = new_users_df['user_id'].nunique()

# marketing spend
marketing_spend = 3000

# UAC
uac = marketing_spend / new_users_count
print(f"User Acquisition Cost: ${uac:.2f}")

# Make sure event_date is in datetime format
df['event_date'] = pd.to_datetime(df['event_date'], format='%Y%m%d')

#FEBUARY
start_date = pd.to_datetime('2025-02-01')
end_date = pd.to_datetime('2025-03-01')

#  filter
new_users_df = df[(df['event_name'] == 'purchase_made') & 
                  (df['event_date'] >= start_date) & 
                  (df['event_date'] <= end_date)]

# unique new users
new_users_count = new_users_df['user_id'].nunique()

# marketing spend
marketing_spend = 3000

# UAC
uac = marketing_spend / new_users_count
print(f"User Acquisition Cost: ${uac:.2f}")

# Make sure event_date is in datetime format
df['event_date'] = pd.to_datetime(df['event_date'], format='%Y%m%d')

# APRIL
start_date = pd.to_datetime('2025-04-01')
end_date = pd.to_datetime('2025-05-01')

#  filter
new_users_df = df[(df['event_name'] == 'purchase_made') & 
                  (df['event_date'] >= start_date) & 
                  (df['event_date'] <= end_date)]

# unique new users
new_users_count = new_users_df['user_id'].nunique()

# marketing spend
marketing_spend = 3000

# UAC
uac = marketing_spend / new_users_count
print(f"User Acquisition Cost: ${uac:.2f}")

# Example data
uac_data = {
    'Month': ['Feb 2025', 'Mar 2025', 'Apr 2025'],
    'UAC': [21.13, uac, 35.71] 
}
uac_df = pd.DataFrame(uac_data)







# --- Load the CSV ---
df.columns = df.columns.str.strip()

# --- Make sure event_date is in datetime format ---
df['event_date'] = pd.to_datetime(df['event_date'], format='%Y%m%d', errors='coerce')

# --- Assume fixed marketing spend per month ---
monthly_marketing_spend = 3000  # Example, you can customize per month later

# --- Create 'YearMonth' column ---
df['YearMonth'] = df['event_date'].dt.to_period('M')

# --- Filter only 'purchase_made' events ---
purchase_df = df[df['event_name'] == 'purchase_made']

# --- Group by Month and calculate unique users ---
monthly_uac = (purchase_df
               .groupby('YearMonth')['user_id']
               .nunique()
               .reset_index()
               .rename(columns={'user_id': 'new_users'}))

# --- Calculate UAC per month ---
monthly_uac['UAC'] = monthly_marketing_spend / monthly_uac['new_users']

# --- Create 'MonthName' for better labeling ---
monthly_uac['MonthName'] = monthly_uac['YearMonth'].dt.strftime('%b %Y')

# --- Create a 'QuarterGroup' for 3-month periods ---
def quarter_label(period):
    month = period.month
    year = period.year
    if month in [1, 2, 3]:
        return f'Q1 {year}'
    elif month in [4, 5, 6]:
        return f'Q2 {year}'
    elif month in [7, 8, 9]:
        return f'Q3 {year}'
    else:
        return f'Q4 {year}'

monthly_uac['QuarterGroup'] = monthly_uac['YearMonth'].apply(quarter_label)

# --- Streamlit Layout ---
#col1, col2, col3 = st.columns([1, 1, 2])

# --- Dropdown for Quarter Selection ---
with col1:
    selected_quarter = st.selectbox(
        'Select Quaterly UAC',
        options=['All'] + sorted(monthly_uac['QuarterGroup'].unique())
    )

# --- Filter based on dropdown ---
if selected_quarter != 'All':
    filtered_df = monthly_uac[monthly_uac['QuarterGroup'] == selected_quarter]
else:
    filtered_df = monthly_uac

# --- Plot ---
with col3:
    st.subheader('User Acquisition Cost (UAC) by Month')

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=filtered_df['MonthName'],
        y=filtered_df['UAC'],
        text=[f"${uac:.2f}<br>{users} users" for uac, users in zip(filtered_df['UAC'], filtered_df['new_users'])],
        textposition='inside',
        marker_color='mediumseagreen'
    ))

    fig.update_layout(
        yaxis_title='UAC ($)',
        xaxis_title='Month',
        title='',
        template='plotly_white',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=20),
        yaxis=dict(range=[0, filtered_df['UAC'].max() + 10 if not filtered_df.empty else 10]),
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)
