import streamlit as st
import pandas as pd
import altair as alt

# Load the data
df = pd.read_csv('drug_clean.csv')

# Replace empty values in data set with "Unknown"
df.replace('\r\r\n', 'Unknown', inplace=True)

# Set the page title
st.set_page_config(page_title="Drug Data Visualization", page_icon=":bar_chart:")

# Display the data
st.header("Drug Performance Evaluation")
st.dataframe(df)

# Create session_state dictionary to keep track of added charts and their titles
if 'charts' not in st.session_state:
    st.session_state.charts = [] #This line executes only if the "charts" key is not found. It creates a new empty list named "charts" and assigns it to the "charts" key within st.session_state.

# Create "Add Chart" button in sidebar
add_chart = st.sidebar.button("Add Chart")

if add_chart: # Checks if the add_chart variable is True. The variable is likely set to True when the user clicks the "Add Chart" button (created using st.sidebar.button("Add Chart"))
    st.session_state.charts.append({ 
        'title': f"Chart {len(st.session_state.charts) + 1}", 
        'x_column': None, 
        'y_column': None,
        'chart_type': 'scatter' 
    })

# Create "Remove Charts" dropdown in sidebar, which allows the user to remove charts from the visualization
charts_to_remove = st.sidebar.multiselect(
    "Remove Charts",
    [f"Chart {i + 1} '{chart['title']}'" for i, chart in enumerate(st.session_state.charts)]
)

# This part deals with the removal of charts based on the user's selection in the multi-select widget.
if charts_to_remove: 
    charts_indices_to_remove = [int(chart.split()[1]) - 1 for chart in charts_to_remove] 
    
    st.session_state.charts = [chart for i, chart in enumerate(st.session_state.charts) if i not in charts_indices_to_remove] # Update the session state with the filtered list
    
# Define a list of available chart types with corresponding labels
chart_types = {
    'Scatter Plot': 'scatter',
    'Line Chart': 'line',
    'Area Chart': 'area',
    'Bar Chart': 'bar',
    'Histogram': 'histogram',
    'Box Plot': 'boxplot',
    'Pie Chart': 'pie',
    'Heatmap': 'heatmap'
}

for i, chart in enumerate(st.session_state.charts):
    chart_key = f"chart_{i + 1}"

    st.sidebar.markdown("")  # Add space for readability
    
    # Sidebar inputs for chart customization
    st.sidebar.markdown(f"### Chart {i + 1}")
    chart['title'] = st.sidebar.text_input("Chart Title", chart['title'], key=f"title_input_{chart_key}")
    chart['x_column'] = st.sidebar.selectbox(f'X-axis Column', df.columns, key=f"x_select_{chart_key}")
    chart['y_column'] = st.sidebar.selectbox(f'Y-axis Column', df.columns, key=f"y_select_{chart_key}")
    chart['chart_type'] = st.sidebar.selectbox(f'Chart Type', list(chart_types.keys()), index=0, format_func=lambda x: x, key=f"type_select_{chart_key}")

    if chart['x_column'] and chart['y_column']:  # Only render chart if both columns are selected
        st.subheader(chart['title'])
        st.write(f"X-axis: {chart['x_column']}, Y-axis: {chart['y_column']}, Type: {chart['chart_type']}")

        alt_chart_type = chart_types[chart['chart_type']]  # Map selected chart type to Altair chart type

        # Generate Altair chart based on selected chart type
        if alt_chart_type == 'scatter':
            chart_obj = alt.Chart(df).mark_circle().encode(
                x=chart['x_column'],
                y=chart['y_column']
            ).properties(height=400).interactive()
        elif alt_chart_type == 'line':
            chart_obj = alt.Chart(df).mark_line().encode(
                x=chart['x_column'],
                y=chart['y_column']
            ).properties(height=400).interactive()
        elif alt_chart_type == 'area':
            chart_obj = alt.Chart(df).mark_area().encode(
                x=chart['x_column'],
                y=chart['y_column']
            ).properties(height=400).interactive()
        elif alt_chart_type == 'bar':
            chart_obj = alt.Chart(df).mark_bar().encode(
                x=chart['x_column'],
                y=chart['y_column']
            ).properties(height=400).interactive()
        elif alt_chart_type == 'histogram':
            chart_obj = alt.Chart(df).mark_bar().encode(
                x=alt.X(chart['x_column'], bin=True),
                y='count()' # add function to set y-axis to none when histogram is selected
            ).properties(height=400).interactive()
        elif alt_chart_type == 'boxplot':
            chart_obj = alt.Chart(df).mark_boxplot().encode(
                x=chart['x_column'],
                y=chart['y_column']
            ).properties(height=400).interactive()
        elif alt_chart_type == 'pie':
            chart_obj = alt.Chart(df).mark_arc().encode(
                theta=chart['x_column'],
                color=chart['y_column']
            ).properties(height=400).interactive()
        elif alt_chart_type == 'heatmap':
            chart_obj = alt.Chart(df).mark_rect().encode(
                x=alt.X(chart['x_column'], bin=True),
                y=alt.Y(chart['y_column'], bin=True),
                color='count()'
            ).properties(height=400).interactive()

        st.altair_chart(chart_obj, use_container_width=True)
