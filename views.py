from django.shortcuts import render
import plotly.graph_objects as go
import plotly.io as pio


def home(request):
    return render(request,'home.html')

def graph(request):
    if request.method == 'POST':
        # Extract x and y values from the POST data
        x_values_str = request.POST.get('x')
        y_values_str = request.POST.get('y')

        # Remove commas from the strings and convert them to integers
        x_values = int(x_values_str.replace(',', ''))
        y_values = int(y_values_str.replace(',', ''))

        # Create the Plotly figure
        fig = go.Figure(go.Scatter(x=[x_values], y=[y_values]))
        fig.update_layout(
            title='User Input Line Chart',
            title_font=dict(size=24, color='darkslategray', family='Arial'),
            font=dict(size=16, color='crimson'),
            legend=dict(title='Legend', orientation='h', y=1.25, x=0.5, xanchor='center')
        )

        # Customize axes
        fig.update_xaxes(
            title='X-Axis Title',
            tickangle=-45,
            tickfont_size=14,
            zeroline=False
        )
        fig.update_yaxes(
            title='Y-Axis Title',
            showgrid=True,
            gridwidth=1,
            gridcolor='LightSteelBlue'
        )

        # Add a shape (e.g., a vertical line) for emphasis
        fig.add_shape(
            type='line',
            y0=300, y1=300,
            line=dict(color='DarkSlateGrey', width=2, dash='dashdot')
        )

        # Add an annotation
        fig.add_annotation(
            text='Key Point',
            x=0.5, y=0.8,
            showarrow=False,
            font=dict(size=16, color='DeepSkyBlue'),
            align='center',
            ax=0, ay=-30
        )
        # Define the path where the image will be saved
        img_path = 'static/generated_chart.png'  # Adjust the path as needed

        # Save the figure as an image file using Kaleido
        pio.write_image(fig, img_path)

        # Pass the image path to the template
        return render(request, 'graph.html', {'img_path': img_path})
    else:
        # Render the initial page if the request method is not POST
        return render(request, 'graph.html')
