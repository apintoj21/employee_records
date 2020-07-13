import psycopg2
from bokeh.plotting import figure, show
from bokeh.palettes import Paired
from bokeh.transform import cumsum
from bokeh.models import HoverTool
from math import pi
import pandas as pd


def get_figure(wd, ht, title, tooltips):
    pd_default = figure(plot_width=wd, plot_height=ht, tools="", title=title, tooltips=tooltips)
    pd_default.border_fill_color = None
    pd_default.background_fill_color = None
    pd_default.background_fill_alpha = 0.5
    pd_default.outline_line_color = None
    pd_default.toolbar.autohide = True
    pd_default.axis.major_label_text_color = None
    pd_default.axis.axis_line_color = None
    pd_default.axis.minor_tick_line_color = None
    pd_default.grid.visible = False
    pd_default.axis.major_tick_line_color = None
    pd_default.title.text_color = "black"
    return pd_default

try:
    connection = psycopg2.connect("host=localhost dbname=emp_db user=postgres password=ajp-21")

    cursor = connection.cursor()
    postgreSQL_select_Query = "select count(*) from emp_rec where gender='F'"

    cursor.execute(postgreSQL_select_Query)
    female_count = cursor.fetchall()
    postgreSQL_select_Query = "select count(*) from emp_rec where gender='M'"

    cursor.execute(postgreSQL_select_Query)
    male_count = cursor.fetchall()
    f_c = female_count[0][0]
    m_c = male_count[0][0]

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

colours = Paired[3]
x = {'Male': m_c, 'Female': f_c}
data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'Gender_Ratio'})
data['color'] = colours[1:]
data['angle'] = data['value'] / data['value'].sum() * 2 * pi
TOOLTIPS = []
p = get_figure(350, 350, "Gender Ratio", TOOLTIPS)
p.annular_wedge(x=0, y=1, inner_radius=0.15, outer_radius=0.35,
                start_angle=cumsum('angle', include_zero=True),
                end_angle=cumsum('angle'), fill_color='color',
                legend_field='Gender_Ratio', source=data)

p.add_tools(HoverTool(tooltips="@Gender_Ratio: @value"))
show(p)